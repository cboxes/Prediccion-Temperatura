import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from link import *

import time
import keyboard
import os
import psutil



def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'

st.set_page_config(page_title="Dashboard",page_icon="🌦", layout="wide",initial_sidebar_state="expanded")
#st.subheader("🏂 Dashboard Predicciones de temperatura")

#st.markdown("##")


alt.themes.enable("dark")

#obtener datos
resultado = vista_todos_datos()
df=pd.DataFrame(resultado,columns=["id","Temperatura", "Valor_Prediccion", "RMSE", "MAPE", "Modelo", "DS", "VAR", "NVAR"])
df.rename(columns={'id': 'Observaciones', 'Valor_Prediccion': 'Prediccion'}, inplace = True)

#st.dataframe(df)

#barra lateral
with st.sidebar:
    st.title('📈 Dashboard Predicciones de Temperatura')
    
    #year_list = list(df_reshaped.year.unique())[::-1]
    #selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    #df_selected_year = df_reshaped[df_reshaped.year == selected_year]
    #df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

    # color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    # selected_color_theme = st.selectbox('Select a color theme', color_theme_list)



    st.sidebar.image("images/clima.jpg",caption="Predicciones climaticas")

    #filtrado
    st.sidebar.header("Seccion de Filtrado")

    dataset =st.sidebar.multiselect(
        "Seleccione Dataset",
        options=["1","2"],
        default=["1","2"]    
    )
    modelo =st.sidebar.multiselect(
        "Seleccione Modelo",
        options=["LSTM_U_U","LSTM_M_U"],
        default=["LSTM_U_U","LSTM_M_U"]    
    )
    variable =st.sidebar.multiselect(
        "Seleccione # de variables",
        options=[1,6],
        default=[1,6]    
    )

    df_seleccion =df.query(
        "DS==@dataset & Modelo==@modelo & NVAR==@variable"
    )
    #calcular indices
    total_predicciones = format_number((df_seleccion["Temperatura"]).count())
    min_rmse = (df_seleccion["RMSE"]).min()
    max_rmse = (df_seleccion["RMSE"]).max()
    min_mape = (df_seleccion["MAPE"]).min()
    max_mape = (df_seleccion["MAPE"]).max()


#st.dataframe(df_seleccion)
    # with st.expander("Tabular"):
    #     showData=st.multiselect('Filtro: ',df_seleccion.columns,default=[])
    #     st.write(df_seleccion[showData])

    

    

        

        # total1,total2,total3,total4,total5=st.columns(5,gap='large')
        # with total1:
        #     st.info('Total predicciones',icon="🧪")
        #     st.metric(label="Contador Total", value=f"{total_predicciones:,.0f}")

        # with total2:
        #     st.info('Minimo RMSE',icon="🧪")
        #     st.metric(label="Valor minimo RMSE", value=f"{min_rmse:,.3f}")    

        # with total3:
        #     st.info('Maximo RMSE',icon="🧪")
        #     st.metric(label="Valor maximo RMSE", value=f"{max_rmse:,.3f}")        

        # with total4:
        #     st.info('Minimo MAPE',icon="🧪")
        #     st.metric(label="% minimo MAPE", value=f"{min_mape:,.3f}")    

        # with total5:
        #     st.info('Maximo MAPE',icon="🧪")
        #     st.metric(label="% maximo MAPE", value=f"{max_mape:,.3f}")  

      
#graficos

    #min_rmse = (df_seleccion["RMSE"]).min()

    #grafico simple linea  predicciones
    # filtro data
    # filter = df_seleccion["DS"] == 1
    # #predicc_ds=df_seleccion[["id", "Temperatura"]].where(filter, inplace=True)
    # predicc_ds=df_seleccion[["id", "Temperatura","DS","Modelo"]].query("DS==1 & Modelo=='ARIMA'").iloc[:4]

    #graficar en pantalla
    #st.plotly_chart(fig_rmse)
    #st.plotly_chart(fig_mape)
    #st.plotly_chart(fig_predicc)

    # left,right=st.columns(2)
    # left.line_chart(chart_data, x="Orden", y=["Temperatura","Prediccion"], color=["#FF0000", "#0000FF"] ,use_container_width=True)
    # right.plotly_chart(fig_rmse,use_container_width=True)                

    
 
#Graficos()

#######################
# Dashboard Main Panel
col = st.columns((1.3, 6.5, 2.5))
#, gap='small'

with col[0]:
        st.markdown('#### Metricas ####')

        st.metric(label="Total predicciones", value=total_predicciones)

        st.metric(label="RMSE", value=f"{min_rmse:,.3f}")  

        #st.metric(label="Maximo RMSE", value=f"{max_rmse:,.3f}") 

        st.metric(label="%MAPE", value=f"{min_mape:,.3f}")    

        #st.metric(label="% maximo MAPE", value=f"{max_mape:,.3f}")

        st.markdown("""---""")     

with col[1]:
    st.markdown('#### Predicciones ####')

    predicc_ds=df_seleccion[["Observaciones", "Temperatura","Prediccion"]]
    chart_data = pd.DataFrame(predicc_ds, columns=["Observaciones", "Temperatura","Prediccion"])
    st.line_chart(chart_data, x="Observaciones", y=["Temperatura","Prediccion"], color=["#FF0000", "#0000FF"] ,
                  use_container_width=True, height=540)

with col[2]:
    st.markdown('#### Comparacion metricas ####')

    #grafico de barras rmse
    # rmse_by_modelo = (
    # df_seleccion.groupby(by=["Modelo"]).min()[["RMSE"]].sort_values(by="RMSE",ascending=False)
    # ) 
    # fig_rmse=px.bar(
    #         rmse_by_modelo,
    #         x="RMSE",
    #         y=rmse_by_modelo.index,
    #         orientation="h",
    #         title="<b> RMSE Minimo por Modelos</b>",
    #         color_discrete_sequence=["#0083B8"]*len(rmse_by_modelo),
    #         template="plotly_white",

    #     )
    # fig_rmse.update_layout(
    #         plot_bgcolor="rgba(0,0,0,0)",
    #         font=dict(color="black"),
    #         yaxis=dict(showgrid=True, gridcolor='#cecdcd'),  # Show y-axis grid and set its color  
    #         paper_bgcolor="rgba(0, 0, 0, 0)",  # Set paper background color to transparent
    #         xaxis=dict(showgrid=True, gridcolor='#cecdcd'),  # Show x-axis grid and set its color
    #     )
    
    # st.dataframe(rmse_by_modelo,
    #              column_order=("Modelo","RMSE"),
    #              hide_index=True,
    #              width=None,
    #              column_config={
    #                 "Modelo": st.column_config.TextColumn(
    #                     "modelo",
    #                 ),
    #                 "RMSE": st.column_config.ProgressColumn(
    #                     "rmse",
    #                     format="%f",
    #                     min_value=0,
    #                     max_value=max(rmse_by_modelo.index),
    #                  )}
    #              )
    

    #grafico de barras mape
    # mape_by_modelo = (
    #      df_seleccion.groupby(by=["Modelo"]).min()[["MAPE"]].sort_values(by="MAPE",ascending=False)
    # ) 
    # fig_mape=px.bar(
    #      mape_by_modelo,
    #      x="MAPE",
    #      y=mape_by_modelo.index,
    #      orientation="h",
    #      title="<b> MAPE Minimo por Modelos</b>",
    #      color_discrete_sequence=["#0083B8"]*len(mape_by_modelo),
    #      template="plotly_white",

    # )
    # fig_mape.update_layout(
    #     plot_bgcolor="rgba(0,0,0,0)",
    #     font=dict(color="black"),
    #     yaxis=dict(showgrid=True, gridcolor='#cecdcd'),  # Show y-axis grid and set its color  
    #     paper_bgcolor="rgba(0, 0, 0, 0)",  # Set paper background color to transparent
    #     xaxis=dict(showgrid=True, gridcolor='#cecdcd'),  # Show x-axis grid and set its color
    # )

    with st.expander('Acerca de Metricas', expanded=True):
        # st.plotly_chart(fig_rmse)
        # st.plotly_chart(fig_mape)
        st.write('''
            - Datos: [JENA Max Planck Institute](https://www.bgc-jena.mpg.de/wetter/weather_data.html).
            - :orange[**Predicciones**]: comportamiento en base a 17 variables
            - :orange[**Metricas**]: valores y porcentajes 
            ''')
    # st.plotly_chart(fig_rmse)
    # st.plotly_chart(fig_mape)

exit_app = st.sidebar.button("Salir")
if exit_app:
    # Give a bit of delay for user experience
    time.sleep(5)
    # Close streamlit browser tab
    keyboard.press_and_release('ctrl+w')
    # Terminate streamlit python process
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()