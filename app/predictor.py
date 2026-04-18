import joblib
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model_xgb = joblib.load( f'{BASE_DIR}/model/xgboost_model.joblib' )

le_make = joblib.load( f'{BASE_DIR}/model/label_encoder_make.joblib' )
le_model = joblib.load( f'{BASE_DIR}/model/label_encoder_model.joblib' )


def predict_price( year : int,
                miles : int,
                make : str,
                model :str )-> float:
    make_enc = le_make.transform( [make] )[0]
    model_enc = le_model.transform( [model] )[0]

    # Feature vector
    features = np.array([[ year, miles, make_enc, model_enc ]])
    return float( model_xgb.predict( features )[ 0 ])