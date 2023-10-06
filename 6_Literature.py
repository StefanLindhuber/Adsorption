import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="CO2-Adsorbents",
    page_icon=":books:",
    layout="wide")

df = pd.read_excel(
    io="C:/Users\lise693\PycharmProjects\Plotly1\Überblick Eigenschaften Adsorbentien.xlsx",
    sheet_name="Sources",
    engine="openpyxl",
    skiprows=0,
)



fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df["Sources:"],df["Title"],df["authors"],df["DOI:"]],
               fill_color='lavender',
               align='left')
    )])

#Start: Plot

st.title("Literature :books:")
st.markdown("---")
st.plotly_chart(fig)
st.table(df)

#Ende: Plot