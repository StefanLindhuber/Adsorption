import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

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


#Start: plot
st.title("Scatter Matrix :clipboard:")
st.markdown("---")
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df["sorbent"],df["group"],df["functional group"]
                       ,df["functional group"],df["funct. Content wt-%"],df["Temp [K]"]
                       ,df["partial pressure [bar]"],df["Capacity [mmol/g]"],df["Heat of adsorption [kJ/mol]"]
                       ,df["Source 1"],df["Source 2"],df["pore size [nm]"]
                       ,df["pore volume [cm3/g]"],df["specific surface [m2/g]"],df["particle size [μm]"]
                       ,df["breaking strength [N/bead]"],df["Source 3"]],  # transpose values from df.values
               fill_color='lavender',
               align='left')
    )])
st.plotly_chart(fig)

print(df)
fig = px.scatter_matrix(df,
    dimensions=["Capacity [mmol/g]", "partial pressure [bar]", "Temp [K]"],
    color="sorbent"
)


st.plotly_chart(fig)
#End: plot
