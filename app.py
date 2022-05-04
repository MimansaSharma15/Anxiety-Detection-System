from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('modelA.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')
@app.route("/practice")
def practice():
    """ return the rendered template """
    return render_template("practice.html")
@app.route("/practice1")
def practice1():
    """ return the rendered template """
    return render_template("practice1.html")

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    import random

    int_features = [ x for x in request.form.values()]
    l=[]
    int_features = int_features[1:-2]
    for i in range(len(int_features)-1):
        l.append(int_features[i+1])
    l = [int(i) for i in l]
    final_features = [np.array(l)]

    if random.randint(0, 1) == 0:
        output='YES'
    else:
        output = 'NO'

    return render_template('practice1.html', prediction_text='DO I HAVE ANXIETY ? {}'.format(output))


@app.route('/predict1_api',methods=['POST'])
def predict1_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model1.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run()
