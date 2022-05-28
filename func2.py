import streamlit as st
import pandas as pd
import pickle


def user_input_features(): 
    
    YearBuilt = st.sidebar.number_input('Année de construction (obligatoire)', step=1)
    reno = st.sidebar.checkbox('Cochez si vous avez fait des rénovations')
    if reno:
        YearRemodAdd= st.sidebar.number_input('Date de rénovation', step=1) 
    else:
        YearRemodAdd=YearBuilt

    LotArea = st.sidebar.number_input('Surface totale en pi² (obligatoire)')
    GrLivArea = st.sidebar.number_input('Surface au sol en pi²')
    TotalBsmtSF= st.sidebar.number_input('Surface du sous-sol en pi²')
    FstFlrSF= st.sidebar.number_input('Surface du rez-de-chaussée en pi²')
    SndFlrSF= st.sidebar.number_input('Surface du premier étage en pi²')    
    LotFrontage = st.sidebar.number_input('Taille de la façade en pi²')
    
    TotRmsAbvGrd= st.sidebar.number_input('Nombre de pièces hors sous-sol et hors salles de bain (obligatoire)', step=1)
    FullBath = st.sidebar.number_input('Nombre de salles de bains (obligatoire)', step=1)
    BedroomAbvGr = st.sidebar.number_input('Nombre de chambres', step=1)
    KitchenAbvGr = st.sidebar.number_input('Nombre de cuisines', step=1)
    Fireplaces = st.sidebar.number_input('Nombre de cheminées', step=1)

    garage = st.sidebar.checkbox('Cochez si vous avez un garage')
    if garage:
        GarageArea = st.sidebar.number_input('Taille du garage en pi²')
        GarageCars = st.sidebar.number_input('Capacité du garage', step=1)
    else:
        GarageArea = 0
        GarageCars = 0

    veranda = st.sidebar.checkbox('Cochez si vous avez une veranda')
    if veranda:
        ScreenPorch = st.sidebar.number_input('Taille de la veranda en pi²')
    else:
        ScreenPorch = 0
   
    Porch = st.sidebar.checkbox("Cochez si vous avez un porche d'entrée")
    if Porch:
        state = st.sidebar.radio("Est-il couvert",("oui","non"))
        if state == "oui":
            OpenPorchSF = st.sidebar.number_input("Taille du porche d'entrée en pi²")
            EnclosedPorch = 0
        else:
            EnclosedPorch = st.sidebar.number_input("Taille du porche d'entrée en pi²")
            OpenPorchSF = 0
    else:
        OpenPorchSF = 0
        EnclosedPorch = 0
   

    terrasse = st.sidebar.checkbox('Cochez si vous avez une terrasse en bois')
    if terrasse:
        WoodDeckSF = st.sidebar.number_input('Taille de la terrasse en pi²')
    else:
        WoodDeckSF = 0

    Fence = st.sidebar.checkbox('Cochez cette case si votre terrain est cloturé')
    Pool = st.sidebar.checkbox('Cochez cette case si vous possédez une piscine')

    features_dict = {
        'ScreenPorch':ScreenPorch,
        'OpenPorchSF':OpenPorchSF,
        'WoodDeckSF':WoodDeckSF,
        'EnclosedPorch':EnclosedPorch,
        'GarageCars':GarageCars,
        'Fireplaces':Fireplaces,
        'YearBuilt': YearBuilt,
        'YearRemodAdd': YearRemodAdd,
        'LotArea': LotArea,
        'GrLivArea': GrLivArea,
        'TotalBsmtSF':TotalBsmtSF,
        'FstFlrSF':FstFlrSF,
        'SndFlrSF':SndFlrSF,
        'LotFrontage': LotFrontage,
        'GarageArea': GarageArea,
        'TotRmsAbvGrd':TotRmsAbvGrd,
        'FullBath':FullBath,
        'BedroomAbvGr':BedroomAbvGr,
        'KitchenAbvGr':KitchenAbvGr,
        'Fence': Fence,
        'Pool' : Pool
    }
    return features_dict
   

def create_dataset(features_dict):
    dataset = pd.DataFrame(features_dict, index=[0])
    return dataset

def get_prediction(dataset):
    loaded_model = pickle.load(open("last_model.sav", 'rb'))
    prediction = loaded_model.predict(dataset)
    return prediction
