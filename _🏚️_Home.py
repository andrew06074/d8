import streamlit as st
import random
import pandas as pd
from streamlit_gsheets import GSheetsConnection

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

        with st.form("my_form"):   
            st.write('Complete this form is you would like to save this appraisal.')
            address = st.text_input('Address:')
            quote = st.text_input('Quote: ',placeholder=price)
            cus_name = st.text_input('Customer Name: ')
            cus_sid = st.text_input('Customer SID: ')
            cus_phone = st.text_input('Customer Phone#:')
            realtor = st.text_input('Realtor:')
            date = st.date_input('Quoted Date:')

            submitted = st.form_submit_button("Submit")
            if submitted:
                df = pd.DataFrame({"Home Address":address,"Price":quote,"Customer":cus_name,"Customer SID":cus_sid,"Customer Phone#":cus_phone,"Realtor":realtor,"Date of appraisal":date})
                appraisal = conn.update(worksheet="Appraisals", data=df)
                st.write("Submitted! ")


except:
    st.header("")






