import streamlit as st

st.set_page_config(page_icon="📊", page_title="Dashboard", layout="wide")
st.image("https://i.imgur.com/IWEpAbC.png", width=250)
st.title("Dashboard")
st.markdown('***')

st.markdown('##### En esta página se encuentra el dashboard interactivo con la información de los datos de banco y los créditos otorgados, como así también la información personal de los clientes y su estado financiero. ')

st.markdown('***') 

dashboard_url = 'https://app.powerbi.com/view?r=eyJrIjoiMGExYWRiNDQtYTNiNi00ZDJkLWE1ZWEtMTg3M2M5Mjc5ZDRmIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9'
st.write(f'<iframe src="{dashboard_url}" width="1000" height="600"></iframe>', unsafe_allow_html=True)
