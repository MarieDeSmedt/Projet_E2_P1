import streamlit as st
import pandas as pd
import pickle


def user_input_features(): 
    
    year = st.sidebar.number_input('Année de construction', step=1)
    Age = round(2022-year,0)
    
    LotArea = st.sidebar.number_input('Surface totale en m²')

    GrLivArea = st.sidebar.number_input('Surface au sol en m²')
    
    LotFrontage = st.sidebar.number_input('Taille de la façade en m²')
    
    GarageArea = st.sidebar.number_input('Taille du garage en m²')
    
    Fence = st.sidebar.checkbox('Cochez cette case si votre terrain est cloturé')

    Pool = st.sidebar.checkbox('Cochez cette case si vous possédez une piscine')

    return Age,GrLivArea,LotFrontage,LotArea,GarageArea,Fence,Pool

def create_dataset(Age,GrLivArea,LotFrontage,LotArea,GarageArea,Fence,Pool):
    data = {'Age': Age,
        'GrLivArea': GrLivArea,
        'LotFrontage': LotFrontage,
        'LotArea': LotArea,
        'GarageArea': GarageArea,
        'Fence': Fence,
        'Pool' : Pool
        }
    dataset = pd.DataFrame(data, index=[0])
    return dataset

def get_prediction(dataset):
    loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
    prediction = loaded_model.predict(dataset)
    return prediction
