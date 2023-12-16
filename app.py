import pandas as pd
import numpy as np
import streamlit as st

dataset_url = "https://raw.githubusercontent.com/LeoLi1223/Beacon/main/datasets/github_dataset.csv"

@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    df.drop_duplicates(inplace=True)
    return df


def search(df, lang=None, keyword=None):
    if keyword is not None:
        df = search_by_keyword(df, keyword)
    if lang is not None:
        df = search_by_lang(df, lang)
    return df

def search_by_lang(df, lang):
    result = df[df['language']==lang]
    if result.shape[0] < 10:
        return result
    else:
        return result.head(10)

def search_by_keyword(df, keyword):
    def filter(name):
        if keyword.lower() in name.lower():
            return name
        else:
            return None
    
    df['repositories'] = df['repositories'].apply(filter)
    df.dropna(inplace=True)
    return df

df = load_dataset(dataset_url)

keyword = st.text_input(
    "Searching keyword",
    placeholder='python'
)

lang = st.selectbox(
    "language of interest",
    df['language'].unique()
)

result_df = search(df, lang=lang, keyword=keyword)
result_df.reset_index(drop=True, inplace=True)
st.dataframe(
    data=result_df,
    column_config={
        "repositories": st.column_config.TextColumn(
            "repo name",
            width='large',
        ),
        "stars_count": st.column_config.NumberColumn(
            "Stars",
            format="%d ⭐",
        ),
        "forks_count": "forks",
        "issues_count": "issues",
        "pull_requests": "pull requests",
        "contributors": "contributors",
        "language": "language",
    },
    hide_index=True,
)

# search system
# search option: 
#   - keyword (text input)
#   - language (selectbox)
# sort option: stars, forks, issues, pull_requests, contributors (selectbox)
# if sorting, enable ascending checkbox