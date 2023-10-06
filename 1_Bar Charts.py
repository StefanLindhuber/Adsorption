import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Bar Charts",
    page_icon=":bar_chart:",
    layout="wide")


df = pd.read_excel(
    io="C:/Users\lise693\PycharmProjects\Plotly1\Überblick Eigenschaften Adsorbentien.xlsx",
    sheet_name="Übersicht",
    engine="openpyxl",
    skiprows=1,
)


st.sidebar.header("Please filter here:")


ordinate = st.sidebar.selectbox(
    "Select the ordinate:",
    options=(("Capacity [mmol/g]"),("Temp [K]"), ("partial pressure [bar]"),
             ("Heat of adsorption [kJ/mol]"),("pore size [nm]"), ("pore volume [cm3/g]"),
             ("specific surface [m2/g]"), ("particle size [μm]"), ("breaking strength [N/bead]"),("funct. Content wt-%"))
)

group= st.sidebar.multiselect(
    "Select the sorbent:",
    options=df["group"].unique(),
    default=df["group"].unique(),
)
sorbent= st.sidebar.multiselect(
    "Select the sorbent:",
    options=df["sorbent"].unique(),
    default=df["sorbent"].unique(),
)

df_selection = df.query(
    "sorbent == @sorbent & group == @group"
)

#Start: plot

st.title("Bar Charts :bar_chart:")
st.markdown("---")
print(df)
fig = px.scatter(
    data_frame=df_selection,
    x= "sorbent",
    y=ordinate,
    color="group"
)
st.plotly_chart(fig)

#End: plot