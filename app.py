from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Demo</title>
        <style>
            body {
                background: linear-gradient(to right, #1e3c72, #2a5298);
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                width: 60%;
                margin: auto;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
            }

            h1 {
                font-size: 45px;
            }

            p {
                font-size: 22px;
            }

            .heart {
                color: red;
                font-size: 30px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD Demo Successful</h1>
            <p>Deployment completed successfully using Flask.</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
