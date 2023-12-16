import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

dataset_url = "https://raw.githubusercontent.com/LeoLi1223/Beacon/main/datasets/github_dataset.csv"

@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    df.drop_duplicates(inplace=True)
    return df

def search(df, lang=None, keyword=None):
    result = df.copy()
    if keyword is not None:
        result = search_by_keyword_(result, keyword)
    if lang is not None:
        result = search_by_lang_(result, lang)
    return df

def search_by_lang_(df, lang):
    result = df[df['language']==lang]
    if result.shape[0] < 10:
        return result
    else:
        return result.head(10)

def search_by_keyword_(df, keyword):
    def filter(name):
        if keyword.lower() in name.lower():
            return name
        else:
            return None
    
    df['repositories'] = df['repositories'].apply(filter)
    df.dropna(inplace=True)
    return df

# draw pie chart
def draw_piechart(df):
    lang_serires = df['language'].copy()
    cnts = lang_serires.where(lang_serires!='Unknown').dropna().value_counts()
    langs = np.array(cnts.index)
    cnts = np.array(cnts)
    other_cnts = np.sum(cnts[5:])
    cnts = np.array([cnts[0], cnts[1], cnts[2], cnts[3], cnts[4], other_cnts])
    cnts = cnts / np.sum(cnts) * 100
    langs = np.array([langs[0], langs[1], langs[2], langs[3], langs[4], "other"])
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(cnts, labels=langs, autopct="%1.1f%%")
    return fig_pie, ax_pie

df = load_dataset(dataset_url)

st.write("### Overview")
st.pyplot(draw_piechart(df)[0])

keyword = st.text_input(
    "Searching keyword",
    placeholder='python'
)

lang_list = df['language'].dropna().unique()
lang = st.selectbox(
    "language of interest",
    lang_list,
    placeholder='choose an option'
)

result_df = search(df, lang=lang, keyword=keyword)
result_df.reset_index(drop=True, inplace=True)
st.dataframe(
    data=result_df,
    column_config={
        "repositories": st.column_config.TextColumn(
            "repo name",
            width='medium',
        ),
        "stars_count": st.column_config.NumberColumn(
            "stars",
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

# Overview
# piechart for frequently used languages

# search system
# search option: 
#   - keyword (text input)
#   - language (selectbox)