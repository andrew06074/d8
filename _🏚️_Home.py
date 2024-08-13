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

df = conn.read(
    worksheet="Houses",
    ttl=0
)

#start page render
#st.image("images/All/dolf_racing_banner.png")
st.title("D8 House Pricing Calculator")

try:
    for index, row in df.iterrows():
        if st.checkbox(row['Location']):
            bot_price = int(row['Bot Price'])
            top_price = int(row['Top Price'])

    bot_value = bot_price 
    top_value = top_price

    st.title("Price Range:")
    st.header("Bottom Price: " + '${:,.0f}'.format(bot_value))
    st.header("Top Price: " + '${:,.0f}'.format(top_value))
    baseprice = st.slider("Narrow the price",bot_value,top_value,(bot_value,top_value))

    if st.button("Generate random price: "):
        price = random.randint(baseprice[0],baseprice[1])
        st.header('${:,.0f}'.format(price))               

except:
    st.header("")






