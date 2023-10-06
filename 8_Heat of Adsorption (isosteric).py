import pandas as pd
import plotly.express as px
import os
import streamlit as st
import numpy as np
import plotly.graph_objects as go

#layout
st.set_page_config(
    page_title="Heat of adsorption",
    page_icon=":bar_chart:",
    layout="wide")
st.sidebar.header("Please filter here:")
#Ende layout
current_directory = __file__
current_directory = current_directory.split('\\')
current_directory="\\".join(current_directory[:-1])

#Dateien aus Ordner auslesen
dateien = os.listdir(f"{current_directory}/Database/dH")
nur_dH_dateien = []
print(dateien)
print(dateien[6].split("_")[-1].split(".txt")[0])
for datei in dateien:
    if datei.split("_")[-1].split(".txt")[0] == "dH":
            nur_dH_dateien.append(datei.split("_")[0])

print(nur_dH_dateien)

#layout
choice_name = st.sidebar.multiselect(
    "Select the sorbent:",
    options=nur_dH_dateien,
    default=nur_dH_dateien[0]
)


i=0
df_selection=pd.DataFrame()
for element in choice_name:
    txt_file= f"{current_directory}/Database/dH/{element}_dH.txt"
    df2 = pd.read_csv(txt_file, sep='\t')

    df_selection = pd.concat([df_selection,df2])
    i=i+1



# Start: plot
st.title("dH :bar_chart:")
st.markdown("---")


fig = px.scatter(
    data_frame=df_selection,
    x="adsorption",
    y="H_T1-T2",
    color=("adsorbent"),
    hover_data=("adsorbent","T1")
)

#fig.add_trace(go.Scatter(x="adsorption", y=df_selection["H_T2-T3"], mode='markers', name='H_T2-T3'))
st.plotly_chart(fig)


i=0
df_selection2=pd.DataFrame()
df3=pd.DataFrame()
for element in choice_name:
    dateien2 = os.listdir(f"{current_directory}/Database")
    print(dateien2)

    neue_liste = []
    for datei in dateien2:
        print(datei.split("_")[0])
        if datei.split("_")[0] == element:
            neue_liste.append(datei)
            txt_file = f"{current_directory}/Database/{datei}"
            df3 = pd.read_csv(txt_file, sep='\t')
            df_selection2 = pd.concat([df_selection2, df3])
    print(neue_liste)
    i=i+1
    print(df_selection2)


fig2 = px.line(
    data_frame=df_selection2,
    x="pressure",
    y=df_selection2.columns.values[3],
    color=("name"),
    hover_data=("adsorbent","Temp [K]","pressure",df_selection2.columns.values[3])
)
fig2.update_layout(
    width=800,  # Breite in Pixeln
    height=600  # Höhe in Pixeln
)
fig2.update_traces(mode="lines+markers")

st.plotly_chart(fig2)
st.dataframe(df_selection2)
