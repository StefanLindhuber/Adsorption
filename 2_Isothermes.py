import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Isothermes",
    page_icon=":bar_chart:",
    layout="wide")


#Start: Auslesen aus Excel
df = pd.read_excel(
    io="C:/Users\lise693\PycharmProjects\Plotly1\Überblick Eigenschaften Adsorbentien.xlsx",
    sheet_name="Übersicht",
    engine="openpyxl",
    skiprows=1,
)
#Ende: Auslesen aus Excel


#start sidebar
st.sidebar.header("Please filter here:")

group = st.sidebar.selectbox(
    "Select the group:",
    options=df["group"].unique(),
)

sorbent= st.sidebar.selectbox(
    "Select the sorbent:",
    options=df["sorbent"].unique(),
)

#end sidebar

df_selection = df.query(
    "sorbent == @sorbent & group == @group"
)

fig =px.scatter(
    data_frame=df_selection,
    x="partial pressure [bar]",
    y="Capacity [mmol/g]",
    color="sorbent"
)
#Start: plot
st.title("Isothermes :bar_chart:")
st.markdown("---")
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df_selection, x="partial pressure [bar]", y="Capacity [mmol/g]", title='Isotherm', color="Temp [K]",markers=True, range_y=[0, 8],range_x=[0, 1],hover_data=["Temp [K]"])
st.plotly_chart(fig)

st.dataframe(df_selection)
#End: plot

