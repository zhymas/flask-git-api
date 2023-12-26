from flask import Flask, request, render_template, url_for
from request import git_api

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        username = request.form['username']
        repos = git_api(username)
        if repos:
            return render_template('repos.html', username=username, repos=repos)
        else:
            return render_template('error.html', username=username)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
