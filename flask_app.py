from flask import Flask, render_template
import modelSet

app = Flask(import_name=__name__)


@app.route('/')
def index():
    # return render_template('/templates/index.html', )
    return render_template('index.html', photos=modelSet.db)


if __name__ == '__main__':
    app.run(debug=True)