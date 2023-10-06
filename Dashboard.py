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

group = st.sidebar.multiselect(
    "Select the group:",
    options=df["group"].unique(),
    default=df["group"].unique(),
)

sorbent= st.sidebar.multiselect(
    "Select the sorbent:",
    options=df["sorbent"].unique(),
    default=df["sorbent"].unique(),
)

fgroup= st.sidebar.multiselect(
    "Select the functional group:",
    options=df["functional group"].unique(),
    default=df["functional group"].unique(),
)

#end sidebar

df_selection = df.query(
    "sorbent == @sorbent & group == @group"
)

st.title("Dashboard :house:")
st.markdown("---")
st.title("CO2-Adsorbents")
#dataframe: This function displays the data of your table in a nice format.
st.dataframe(df_selection)



#mainpage
st.title("CO2-Adsorbents")
st.markdown("---")

#wichtige Infos

total = int(df_selection["sorbent"].count())
average= round(df_selection["Capacity [mmol/g]"].mean(),2)
median = round(df_selection["Capacity [mmol/g]"].median(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Selected sorbents:")
    st.markdown(total)
with middle_column:
    st.subheader("Mean capacity:")
    st.markdown(str(average) + " mmol/g")
with right_column:
    st.subheader("Median capacity:")
    st.markdown(str(median) + " mmol/g")

st.markdown("---")

# pyplot

fig =px.scatter(
    hover_data=["sorbent","Temp [K]","Capacity [mmol/g]","partial pressure [bar]"],
    data_frame=df_selection,
    x="Temp [K]",
    y="Capacity [mmol/g]",
    color="sorbent"
)

st.plotly_chart(fig)
