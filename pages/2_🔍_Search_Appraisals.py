import streamlit as st
import random
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from time import sleep

#page config
st.set_page_config(
    page_title="Dynasty 8",
    page_icon="8️⃣"
)

# Create a connection object to gsheets
conn = st.connection("gsheets", type=GSheetsConnection)

all_appraisals = conn.read(worksheet="Appraisals",ttl=0)


st.title('Search past appraisals')
st.dataframe(all_appraisals,hide_index=True)