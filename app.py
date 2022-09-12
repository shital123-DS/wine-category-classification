from flask import Flask, request, render_template
from Artifacts.utils import wine

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('wine.html')

@app.route('/prediction', methods = ['POST'])
def prediction():
    data = request.form
    wine_obj = wine(data)
    result = wine_obj.predict()
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=8080)

