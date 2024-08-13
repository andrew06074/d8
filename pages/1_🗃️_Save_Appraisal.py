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

form = st.form("my_form")
form.write('Complete this form is you would like to save this appraisal.')
address = form.text_input('Address:')
quote = form.text_input('Quote: ')
cus_name = form.text_input('Customer Name:')
cus_sid = form.text_input('Customer SID:')
cus_phone = form.text_input('Customer Phone#:')
realtor = form.text_input('Realtor:')
date = form.date_input('Quoted Date:')
submitted = form.form_submit_button("Submit")

if submitted:
    if address is None or quote is None or cus_name is None or cus_sid is None or realtor is None or date is None:
        st.write("Field Missing")
    else:
        all_appraisals = conn.read(worksheet="Appraisals",ttl=0)
        appraisal = pd.DataFrame({"Address":[address],"Price":[quote],"Customer":[cus_name],"SID":[cus_sid],"Phone":[cus_phone],"Realtor":[realtor],"Date of appraisal":[date]})
        new_appraisals = pd.concat([all_appraisals,appraisal])
        conn.update(worksheet="Appraisals", data=new_appraisals)
        st.write("Submitted!")