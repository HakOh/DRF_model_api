from api.settings import BASE_DIR
from django.apps import AppConfig
from joblib import load
import os
import pandas as pd


class PredictionConfig(AppConfig):
    name = 'Prediction'
    #CLASSIFIER_FOLDER = Path("classifier")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'prediction/classifier/')
    #CLASSIFIER_FILE = CLASSIFIER_FOLDER / "IRISRandomForestClassifier.joblib"
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "IRISRandomForestClassifier.joblib")
    classifier = load(CLASSIFIER_FILE)