import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="CO2-Adsorbents",
    page_icon=":bar_chart:",
    layout="wide")

#emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

df = pd.read_excel(
    io="C:/Users\lise693\PycharmProjects\Plotly1\Überblick Eigenschaften Adsorbentien.xlsx",
    sheet_name="Übersicht",
    engine="openpyxl",
    skiprows=1,
)

st.table(df)

