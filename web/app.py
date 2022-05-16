from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/agg')
def agg():  # put application's code here
    return render_template('agg_templates.html')

@app.route('/railways')
def railways():  # put application's code here
    return render_template('railways.html')

@app.route('/streets')
def streets():  # put application's code here
    return render_template('streets.html')

if __name__ == '__main__':
    app.config.update(
        DEBUG=True,
    )
    app.run()
