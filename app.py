from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import os
import logging
from logging.handlers import RotatingFileHandler

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__)

# Configure logging
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Student Performance Predictor startup')

## Route for a home page

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f'Error in index route: {str(e)}')
        return render_template('500.html'), 500

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    try:
        if request.method=='GET':
            return render_template('home.html')
        else:
            data=CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('writing_score')),
                writing_score=float(request.form.get('reading_score'))
            )
            pred_df=data.get_data_as_data_frame()
            app.logger.info('Data frame created successfully')
            print(pred_df)
            print("Before Prediction")

            predict_pipeline=PredictPipeline()
            app.logger.info('Prediction pipeline initialized')
            print("Mid Prediction")
            results=predict_pipeline.predict(pred_df)
            app.logger.info('Prediction completed successfully')
            print("after Prediction")
            return render_template('home.html',results=results[0])
    
    except Exception as e:
        app.logger.error(f'Error in predict_datapoint: {str(e)}')
        return render_template('500.html'), 500
    

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f'Server Error: {str(error)}')
    return render_template('500.html'), 500

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)        