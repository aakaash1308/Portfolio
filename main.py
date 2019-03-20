from flask import Flask 
app = Flask(__name__)

# Pointing to the first page
@app.route("/")
def main():
	return "<h1>Started an empty flask project</h1>"


# Allows us to run and refresh on debug mode
if __name__ == '__main__':
	app.run(debug=True)