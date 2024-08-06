import streamlit as st
import random
import pandas as pd


#page config
st.set_page_config(
    page_title="Dynasty 8",
    page_icon="8️⃣"
)


#start page render
#st.image("images/All/dolf_racing_banner.png")
st.title("D8 House Pricing Calculator")

bot_value = 450000
top_value = 4000000

if st.checkbox("Enable big dick mode"):
    bot_value = 0
    top_value = 100000000

baseprice = st.slider("Select a price range",bot_value,top_value,(bot_value,top_value))

price = random.randint(baseprice[0],baseprice[1])


st.write()

price_list = {'Price':["Base","With pool","+5%"],'Amount':['${:,.0f}'.format(price),'${:,.0f}'.format(price+100000),'${:,.0f}'.format(price*1.05)]}

price_df = pd.DataFrame(data=price_list)

st.dataframe(price_df,hide_index=True)


