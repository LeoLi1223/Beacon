import pandas as pd
import numpy as np
import streamlit as st

dataset_path = "./datasets/repository_data.csv"
dataset_url = "https://raw.githubusercontent.com/LeoLi1223/Beacon/main/datasets/github_dataset.csv"


@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


df = load_dataset(dataset_url)

langs = st.selectbox(
    "language of interest",
    df['language'].unique()
)

st.write(langs)

# 1. distributions of # stars, # forks, # language used
# 2. proportion of each language used
# 3. contributors
# 4. fetch top repo by # stars, # forks