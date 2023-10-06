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


#start sidebar
st.sidebar.header("Please filter here:")

ordinate = st.sidebar.selectbox(
    "Select the ordinate:",
    options=(("Capacity [mmol/g]"),("Temp [K]"), ("partial pressure [bar]"),
             ("Heat of adsorption [kJ/mol]"),("pore size [nm]"), ("pore volume [cm3/g]"),
             ("specific surface [m2/g]"), ("particle size [μm]"), ("breaking strength [N/bead]"),("funct. Content wt-%"))
)

abscissa= st.sidebar.selectbox(
    "Select the abscissa:",
    options=( ("Temp [K]"), ("Capacity [mmol/g]"),("partial pressure [bar]"),
             ("Heat of adsorption [kJ/mol]"), ("pore size [nm]"), ("pore volume [cm3/g]"),
             ("specific surface [m2/g]"), ("particle size [μm]"), ("breaking strength [N/bead]"),
             ("funct. Content wt-%"))
)

#df_selection = df.query(
    #"ordinate == @sorbent & group == @group"

#end sidebar


#Start: plot

st.title("Custom Plots :bar_chart:")
st.markdown("---")
print(df)
fig = px.scatter(
    data_frame=df,
    x=abscissa,
    y=ordinate,
    color="sorbent"
)
st.plotly_chart(fig)

#End: plot