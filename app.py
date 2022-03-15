import setproctitle

from application.init import app
from flask import render_template
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    setproctitle.setproctitle('Hassans_website')
    app.run(debug=True)