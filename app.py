from flask import Flask, request, render_template
from src.pipeline.prediction_pipeline import Predictpipeline,CustomData

application = Flask(__name__)

app = application


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('form.html')

    try:

        data = CustomData(

            # Basic Details
            hectares=float(request.form.get('hectares', 0)),
            agriblock=request.form.get('agriblock', ''),
            variety=request.form.get('variety', ''),
            soil_types=request.form.get('soil_types', ''),

            # Nursery & Seed
            seedrate_in_kg=float(request.form.get('seedrate_in_kg', 0)),
            lp_mainfield_in_tonnes=float(request.form.get('lp_mainfield_in_tonnes', 0)),
            nursery=request.form.get('nursery', ''),
            nursery_area_cents=float(request.form.get('nursery_area_cents', 0)),
            lp_nurseryarea_in_tonnes=float(request.form.get('lp_nurseryarea_in_tonnes', 0)),

            # Fertilizers
            dap_20days=float(request.form.get('dap_20days', 0)),
            weed28d_thiobencarb=float(request.form.get('weed28d_thiobencarb', 0)),
            urea_40days=float(request.form.get('urea_40days', 0)),
            potassh_50days=float(request.form.get('potassh_50days', 0)),
            micronutrients_70days=float(request.form.get('micronutrients_70days', 0)),
            pest_60day_in_ml=float(request.form.get('pest_60day_in_ml', 0)),

            # Rainfall & Irrigation
            rain_30d_mm=float(request.form.get('rain_30d_mm', 0)),
            ai_30d_mm=float(request.form.get('ai_30d_mm', 0)),
            rain_30_50d_mm=float(request.form.get('rain_30_50d_mm', 0)),
            ai_30_50d_mm=float(request.form.get('ai_30_50d_mm', 0)),
            rain_51_70d_mm=float(request.form.get('rain_51_70d_mm', 0)),
            ai_51_70d_mm=float(request.form.get('ai_51_70d_mm', 0)),
            rain_71_105d_mm=float(request.form.get('rain_71_105d_mm', 0)),
            ai_71_105d_mm=float(request.form.get('ai_71_105d_mm', 0)),

            # Temperature
            min_temp_d1_d30=float(request.form.get('min_temp_d1_d30', 0)),
            max_temp_d1_d30=float(request.form.get('max_temp_d1_d30', 0)),
            min_temp_d31_d60=float(request.form.get('min_temp_d31_d60', 0)),
            max_temp_d31_d60=float(request.form.get('max_temp_d31_d60', 0)),
            min_temp_d61_d90=float(request.form.get('min_temp_d61_d90', 0)),
            max_temp_d61_d90=float(request.form.get('max_temp_d61_d90', 0)),
            min_temp_d91_d120=float(request.form.get('min_temp_d91_d120', 0)),
            max_temp_d91_d120=float(request.form.get('max_temp_d91_d120', 0)),

            # Wind Speed
            wind_speed_d1_d30=float(request.form.get('wind_speed_d1_d30', 0)),
            wind_speed_d31_d60=float(request.form.get('wind_speed_d31_d60', 0)),
            wind_speed_d61_d90=float(request.form.get('wind_speed_d61_d90', 0)),
            wind_speed_d91_d120=float(request.form.get('wind_speed_d91_d120', 0)),

            # Wind Direction
            wind_direction_d1_d30=request.form.get('wind_direction_d1_d30', ''),
            wind_direction_d31_d60=request.form.get('wind_direction_d31_d60', ''),
            wind_direction_d61_d90=request.form.get('wind_direction_d61_d90', ''),
            wind_direction_d91_d120=request.form.get('wind_direction_d91_d120', ''),

            # Humidity
            humidity_d1_d30=float(request.form.get('humidity_d1_d30', 0)),
            humidity_d31_d60=float(request.form.get('humidity_d31_d60', 0)),
            humidity_d61_d90=float(request.form.get('humidity_d61_d90', 0)),
            humidity_d91_d120=float(request.form.get('humidity_d91_d120', 0)),

            # Others
            trash_in_bundles=float(request.form.get('trash_in_bundles', 0))
        )

        # Convert to DataFrame
        final_new_data = data.get_data_as_dataframe()

        # Prediction Pipeline
        predict_pipeline = Predictpipeline()

        # Prediction
        pred = predict_pipeline.predict(final_new_data)

        # Regression Output
        results = round(pred[0], 2)

        return render_template(
            'results.html',
            final_result=f'{results} Kg'
        )

    except Exception as e:

        return render_template(
            'results.html',
            final_result=f'Error Occurred: {str(e)}'
        )


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)