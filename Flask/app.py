import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('index_demo.html')

@app.route('/predict_all_variables',methods=['POST'])
def predict_all_variables():
    #retrieve input
    inputs = [str(x) for x in request.form.values()]
    output = predict(inputs)
    
    # output = scaled_inputs
    return render_template('index.html', prediction_text=output)


@app.route('/demo_result',methods=['POST'])
def demo_predict():
    #retrieve input
    inputs = [str(x) for x in request.form.values()]
    output = predict(inputs)
    
    # output = scaled_inputs
    return render_template('index_demo.html', prediction_text=output)


def predict(inputs):
    timeframe = inputs[0]
    timeframe = timeframe.lower()
    date_time = datetime.datetime.fromisoformat(inputs[-1])
    inputs.pop(0)
    inputs.pop(-1)

    #scaling the inputs, using the same scaler that scaled the train set of the model
    model_type = ["RandomForestRegressor", "GradientBoostingRegressor"]
    scaler = pickle.load(open(f'../models/{timeframe}/{model_type[0]}/scaler.pkl', 'rb')) #we import the scaler
    inputs_df = pd.DataFrame(columns=scaler.feature_names_in_)
    inputs_series = pd.Series(inputs, index = inputs_df.columns)
    inputs_df = inputs_df.append(inputs_series, ignore_index=True)
    scaled_inputs = list(scaler.transform(inputs_df)[0])

    scaled_inputs.append(date_time.hour + date_time.minute/60)
    scaled_inputs.append(date_time.day)
    scaled_inputs.append(date_time.month)

    final_features = [np.array(scaled_inputs)]

    
    variable_to_predict = "Global_active_power"
    model = pickle.load(open(f'../models/{timeframe}/{model_type[0]}/{variable_to_predict}.pkl', 'rb'))
    prediction_scaled = model.predict(final_features)[0]

    #unscaling the resulting prediction
    pred_row_scaled = pd.DataFrame(columns=scaler.feature_names_in_)
    row = [0]*len(pred_row_scaled.columns)
    row[0] = prediction_scaled
    pred_row = pd.Series(row, index = pred_row_scaled.columns)
    pred_row_scaled = pred_row_scaled.append(pred_row, ignore_index=True)
    pred_row_unscaled = scaler.inverse_transform(pred_row_scaled)
    prediction = pred_row_unscaled[0,0]

    prediction = round(prediction, 3)
    output = f'Avg global active power in the next {timeframe} from {str(date_time)} should be {prediction} kiloWatt.'

    return output


# @app.route('/predict',methods=['POST'])
# def predict():
#     str_features = [str(x) for x in request.form.values()]
#     timeframe = str_features[0]
#     timeframe = timeframe.lower()
#     date_time = datetime.datetime.fromisoformat(str_features[-1])
#     str_features.pop(0)
#     str_features.pop(-1)
#     str_features.append(date_time.hour + date_time.minute/60)
#     str_features.append(date_time.day)
#     str_features.append(date_time.month)
#     final_features = [np.array(str_features)]

#     model_type = "RandomForestRegressor"
#     variable_to_predict = "Global_active_power"

#     model = pickle.load(open(f'../models/{timeframe}/{model_type}/{variable_to_predict}.pkl', 'rb'))
#     print("type of model : ", type(model))

#     prediction = model.predict(final_features)
#     output = round(prediction[0], 3)
    
#     return render_template('index.html', prediction_text=f'Avg global active power in the next {timeframe} from {str(date_time)} should be {output} kiloWatt.')

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)