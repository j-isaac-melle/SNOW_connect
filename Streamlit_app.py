#dont run anything past while troubleshooting:
import streamlit
import snowflake.connector
import pandas

streamlit.title('Air Canada Webpage')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#sets the index to Fruit column NOT NUMBERS
my_fruit_list = my_fruit_list.set_index('Roles')
#pick select list here for smothie creation: (list from index index declared)
#manually adds avo and bana to list 
fruits_selected = streamlit.multiselect("Select a role", list(my_fruit_list.index),['',''])
#hides the giant table 
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display table on page (was my fruit list) now just fruits to show 
streamlit.dataframe(fruits_to_show)
#create the repeatable code block (called a function) function starts with def: and returns:


streamlit.header('Current Privileges: ' )
streamlit.header('Roles with correct Privileges: ')
streamlit.header('Roles with invalid Naming: ')
streamlit.header('Roles with missing Privileges: ')
streamlit.hearder('Roles with wrong Privileges: ')

#streamlit.header('Check out our users:')

#streamlit.multiselect(

#streamlit.dataframe()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake001"])

#my_cur = my_cnx.cursor()

#my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.USERS")
#myresult = my_cur.fetchall()


#streamlit.dataframe(myresult)


#streamlit.header('Check out our Roles:')
#my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.OUR_ROLES")
#myresult = my_cur.fetchall()
#streamlit.multiselect("Pick a user: ", list(my_cur.index))
#streamlit.dataframe(myresult)
