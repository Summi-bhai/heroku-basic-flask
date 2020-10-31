from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>TRILOK TEA COMPANY</h1>
    <p>Coming Soon in Vidisha</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

