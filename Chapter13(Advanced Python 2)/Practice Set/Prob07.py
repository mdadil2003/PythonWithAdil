# 7. Explore the ‘Flask’ module and create a web server using Flask & Python. 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__ == "__main__":
    app.run()

# Install Flask using pip
# pip install flask
