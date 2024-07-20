import mysql.connector
#import streamlit as st
import requests

#funccion
def fetch_data(endpoint):
     response = requests.get(endpoint)
     data = response.json()
     return data


#coneccion
conn= mysql.connector.connect(
      host="localhost",
      port="3306",
      user="root",
      passwd="Mysql",
      db="clima"
  )
c=conn.cursor()

#seleccionar datos desde el API
def vista_todos_datos():
     # api_url = 'http://127.0.0.1:8000/api/predicciones/'
     # datos = fetch_data(api_url)
    
     # if datos:
     #     return datos

     c.execute('Select * from predicciones order by Modelo, DS, NVAR')
     datos=c.fetchall()
     return datos