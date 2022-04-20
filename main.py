from flask import Flask, request
import pandas as pd
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    if request.method == 'GET':
        df = pd.read_csv("SpotifyAudioFeaturesApril2019.csv")
        df = df.sort_values(by=['popularity'], ascending=True)
        df['track_name'] = df['track_name'].str.replace('[^\x00-\x7F]+', 'chinese')
        df=df.head(10)
        df = df['track_name']
        print(df)

    return df.to_json()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
