from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=8000,
    )
    app.run(**config)
