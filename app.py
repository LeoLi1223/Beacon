import pandas as pd
import numpy as np
import streamlit as st

dataset_url = "https://raw.githubusercontent.com/LeoLi1223/Beacon/main/datasets/github_dataset.csv"

@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    df.drop_duplicates(inplace=True)
    return df

# repo of {language} sorted by {stars/forks/issues/pull/contributors} in ascending/descending
def search_by_lang(df, lang, sorted_key, ascending=True):
    result = df.sort_values(sorted_key, ascending=ascending)
    result = result[['repositories', sorted_key, 'language']]
    result = result[result['language']==lang]
    if result.shape[0] < 10:
        return result
    else:
        return result.head(10)

df = load_dataset(dataset_url)

lang = st.selectbox(
    "language of interest",
    df['language'].unique()
)

sort_by = st.selectbox(
    "sorted by",
    df.select_dtypes(include='int').columns
)

is_ascending = st.checkbox(
    'ascending'
)

result_df = search_by_lang(df, lang, sort_by, is_ascending)
result_df.reset_index(drop=True, inplace=True)
st.dataframe(data=result_df)

# search system
# search option: 
#   - keyword (text input)
#   - language (selectbox)
# sort option: stars, forks, issues, pull_requests, contributors (selectbox)
# if sorting, enable ascending checkbox