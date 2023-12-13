import pandas as pd
import numpy as np
import streamlit as st

large_dataset_path = "./datasets/repository_data.csv"

@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

# df1 = load_dataset(small_dataset_path)
df = load_dataset(large_dataset_path)

langs = st.selectbox(
    "language of interest",
    df['primary_language'].unique()
)

st.write(langs)

# 1. distributions of # stars, # forks, # language used
# 2. proportion of each language used
# 3. contributors
# 4. fetch top repo by # stars, # forks