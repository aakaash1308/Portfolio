from flask import Flask, render_template, url_for

app = Flask(__name__)

# Pointing to the loading page
@app.route("/loading")
def loading():
	return "<h1>Starting an empty flask project</h1>"

# Pointing to the main page
@app.route("/")
@app.route("/main")
def main():
	return render_template('main.html')


# Allows us to run and refresh on debug mode
if __name__ == '__main__':
	app.run(debug=True)



# REFRENCES
# https://www.youtube.com/watch?v=MwZwr5Tvyxo
# 17 17 17