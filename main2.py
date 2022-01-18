import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from func2 import user_input_features, create_dataset, get_prediction
# config
st.set_page_config(layout="wide")

# css
st.markdown("""
<style>
.big-font {
    font-size:200px !important;
}
</style>
""", unsafe_allow_html=True)


# download dataset
X = pd.read_csv("clean_X.csv")

# implement sidebar
st.sidebar.header('Description du bien')

#init variables
prediction=0


# creation du dataset du bien à évaluer, seulement si critères remplis
Age,GrLivArea,LotFrontage,LotArea,GarageArea,Fence,Pool=user_input_features()


if Age!=0 and GrLivArea!=0 and LotFrontage!=0 and LotArea!=0 and GarageArea!=0:
    df = create_dataset(Age,GrLivArea,LotFrontage,LotArea,GarageArea,Fence,Pool)
    features_ok = True
    # Apply Model to Make Prediction
    loaded_model = pickle.load(open("last_model.sav", 'rb'))
    prediction = loaded_model.predict(df)
    formated_prediction = '{:,}$'.format(int(prediction))
else: 
    error='veuillez remplir tous les critères'
    features_ok = False



#affichage de l'evaluation
cols = st.columns(5)
if cols[2].button('Evaluez votre bien'):
    if features_ok :
        cols[1].balloons()
        cols[1].markdown('<p class="big-font">{}</p>'.format(formated_prediction), unsafe_allow_html=True)
    else: cols[2].write(error)
    
    col = st.columns(2)
    if not Fence and features_ok:
        df_with_fence = create_dataset(Age,GrLivArea,LotFrontage,LotArea,GarageArea,True,Pool)
        prediction_with_fence = get_prediction(df_with_fence)
        evol =int(prediction_with_fence)-int(prediction)
        col[0].metric('Si votre terrain était cloturé votre bien vaudrait:',int(prediction_with_fence),evol)

    if not Pool and features_ok:
        df_with_pool = create_dataset(Age,GrLivArea,LotFrontage,LotArea,GarageArea,Fence,True)
        prediction_with_pool = get_prediction(df_with_pool)
        evol =int(prediction_with_pool)-int(prediction)
        col[1].metric('Si vous possédiez une piscine votre bien vaudrait:',int(prediction_with_pool),evol)