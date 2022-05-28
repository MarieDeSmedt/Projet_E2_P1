import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from func2 import user_input_features, create_dataset, get_prediction

# config
st.set_page_config(layout="wide")

# css
st.markdown("""<style>.big-font { font-size:200px !important;}</style>""", unsafe_allow_html=True)


# implement sidebar
st.sidebar.header('Description du bien')

#init variables
prediction=0
features_dict = {
    'ScreenPorch':0,'OpenPorchSF':0,'WoodDeckSF':0,'EnclosedPorch':0,'GarageCars':0,'Fireplaces':0,'YearBuilt': 0,
    'YearRemodAdd': 0,'LotArea': 0,'GrLivArea': 0,'TotalBsmtSF':0,'FstFlrSF':0,'SndFlrSF':0,'LotFrontage': 0,'GarageArea': 0,
    'TotRmsAbvGrd':0,'FullBath':0,'BedroomAbvGr':0,'KitchenAbvGr':0,'Fence': False,'Pool' : False
}


# creation du dataset du bien à évaluer, seulement si critères remplis
features_dict = user_input_features()


if ('YearBuilt',0) and ('LotArea',0) and ('TotRmsAbvGrd',0) and ('FullBath',0) not in features_dict.items():
    df = create_dataset(features_dict)
    features_ok = True
    # Apply Model to Make Prediction
    loaded_model = pickle.load(open("last_model.sav", 'rb'))
    prediction = loaded_model.predict(df)
    formated_prediction = '{:,}$'.format(int(prediction))
else: 
    if  ('YearBuilt',0) in features_dict.items():
        error="Veuillez indiquer l'année de construction"
    elif ('LotArea',0) in features_dict.items():
        error="Veuillez indiquer la surface totale du bien"
    elif ('TotRmsAbvGrd',0) in features_dict.items():
        error="Veuillez indiquer le nombre de pièces"
    elif ('FullBath',0) in features_dict.items():
        error="Veuillez indiquer le nombre de salles de bain"
    else:
        error="error fatale"
    features_ok = False



#affichage de l'evaluation
cols = st.columns(5)
if cols[2].button('Evaluez votre bien'):

    if features_ok :
        cols[1].balloons()
        cols[1].markdown('<p class="big-font">{}</p>'.format(formated_prediction), unsafe_allow_html=True)
    else: cols[2].warning(error)
    
    # affichage des propositions d'améliorations
    row1 = st.columns(2)
    if features_ok and ('Fence',False) in features_dict.items():
        features_dict["Fence"] = True
        df_with_fence = create_dataset(features_dict)
        prediction_with_fence = get_prediction(df_with_fence)
        evol =int(prediction_with_fence)-int(prediction)
        row1[0].metric('Si votre terrain était cloturé votre bien vaudrait:',int(prediction_with_fence),evol)

    if features_ok and ('Pool',False) in features_dict.items():
        features_dict["Pool"] = True
        df_with_pool = create_dataset(features_dict)
        prediction_with_pool = get_prediction(df_with_pool)
        evol =int(prediction_with_pool)-int(prediction)
        row1[1].metric('Si vous possédiez une piscine votre bien vaudrait:',int(prediction_with_pool),evol)
    
    row2 = st.columns(3)
    if features_ok and ('GarageArea',False) in features_dict.items():
        features_dict["GarageArea"] = 50
        df_with_garage = create_dataset(features_dict)
        prediction_with_garage = get_prediction(df_with_garage)
        evol =int(prediction_with_garage)-int(prediction)
        row2[0].metric('Si vous possédiez un garage de 50pi² votre bien vaudrait:',int(prediction_with_garage),evol)

    if features_ok and ('ScreenPorch',False) in features_dict.items():
        features_dict["ScreenPorch"] = 50
        df_with_veranda = create_dataset(features_dict)
        prediction_with_veranda = get_prediction(df_with_veranda)
        evol =int(prediction_with_veranda)-int(prediction)
        row2[1].metric('Si vous possédiez une veranda de 50pi² votre bien vaudrait:',int(prediction_with_veranda),evol)
    
    if features_ok and ('WoodDeckSF',False) in features_dict.items():
        features_dict["WoodDeckSF"] = 20
        df_with_terrase = create_dataset(features_dict)
        prediction_with_terrase = get_prediction(df_with_terrase)
        evol =int(prediction_with_terrase)-int(prediction)
        row2[2].metric('Si vous possédiez une terrase en bois de 20pi² votre bien vaudrait:',int(prediction_with_terrase),evol)