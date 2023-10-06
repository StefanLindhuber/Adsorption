import pandas as pd
import plotly.express as px
import os
import streamlit as st
import numpy as np
import plotly.graph_objects as go

#layout
st.set_page_config(
    page_title="Isothermes",
    page_icon=":bar_chart:",
    layout="wide")

st.sidebar.header("Please filter here:")

#Ende layout
current_directory = __file__

current_directory = current_directory.split('\\')
current_directory="\\".join(current_directory[:-1])

txt_file= f"{current_directory}/Database/KIT-6-C_273.txt"
data_name = txt_file.split('/')[-1]
df= pd.read_csv(txt_file, sep='\t')

#Dateien aus Ordner auslesen
dateien = os.listdir(f"{current_directory}/Database")
nur_txt_dateien = [datei for datei in dateien if datei.endswith('.txt')]
nur_csv_dateien = [datei for datei in dateien if datei.endswith('.csv')]
nur_txt_dateien_ohne_txt= [datei.replace(".txt","") for datei in nur_txt_dateien]
nur_txt_dateien_ohne_text_adsorbent= [datei.split('_')[0] for datei in nur_txt_dateien_ohne_txt]
eindeutige_werte = list(set(nur_txt_dateien_ohne_text_adsorbent))
nur_txt_dateien_ohne_text_temperature= [datei.split('_')[1] for datei in nur_txt_dateien_ohne_txt]

#layout
choice_name = st.sidebar.multiselect(
    "Select the sorbent_temperature:",
    options=nur_txt_dateien_ohne_txt,
    default=nur_txt_dateien_ohne_txt[0],
)


i=0
df_selection=pd.DataFrame()
for element in choice_name:
    txt_file= f"{current_directory}/Database/{element}.txt"
    df2 = pd.read_csv(txt_file, sep='\t')

    df_selection = pd.concat([df_selection,df2])
    i=i+1



# Start: plot
st.title("Isothermes :bar_chart:")
st.markdown("---")


fig = px.line(
    data_frame=df_selection,
    x="pressure",
    y=df.columns.values[3],
    color=("name"),
    hover_data=("adsorbent","Temp [K]","pressure",df.columns.values[3])
)
fig.update_layout(
    width=800,  # Breite in Pixeln
    height=600  # Höhe in Pixeln
)
fig.update_traces(mode="lines+markers")

st.dataframe(df_selection)
st.plotly_chart(fig)

if len(choice_name) == 1:
    # Start: plot Langmuir
    pressure_list = df_selection.iloc[:, 1].tolist()
    capacity_list = df_selection.iloc[:, 3].tolist()

    max_pressure = max(pressure_list)
    max_capacity = max(capacity_list)

    K = df_selection.at[0, "K"]
    Q = df_selection.at[0, "Q"]

    x = np.linspace(0, max_pressure, 100)
    def f(x):
        return (K * x) / (1 + K * x) * Q

    y = f(x)

    df_plot = pd.DataFrame({'x': x, 'y': y})

    fig2 = px.line(
        data_frame=df_selection,
        x="pressure",
        y=df.columns.values[3],
        color=("name"),
        hover_data=("adsorbent", "Temp [K]", "pressure", df.columns.values[3])
    )
    fig2.update_layout(
        width=800,  # Breite in Pixeln
        height=600  # Höhe in Pixeln
    )
    fig2.update_traces(mode="lines+markers")
    fig2.add_trace(go.Scatter(x=df_plot['x'], y=df_plot['y'], mode='lines', name='Langmuir'))

    st.plotly_chart(fig2)
    # End: plot Langmuir



