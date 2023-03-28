from flask import Flask, render_template, request
from keras.models import Sequential, load_model

app = Flask(__name__)

def matrix_prediction(parameters):
    model = load_model({path_name})
    pred = model.predict([parameters])
    return pred

@app.route('/', methods=['POST', 'GET'])
def matrix_form():
    message = ''
    if request.method == 'POST':
        parameters_list = ('dens', 'elast', 'hard', 'epoxy', 'temp', 'surf', 'mod', 'tens', 'tar', 'angle', 'step', 'denn')
        parameters = []
        for i in parameters_list:
            entry = request.form.get(i)
            parameters.append(entry)
        parameters = [float(i.replace(',', '.')) for i in parameters]

        message = f'Рекомендуемое cоотношение: {matrix_prediction(parameters)}'
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
