#dont run anything past while troubleshooting:
import streamlit
import snowflake.connector
import pandas

streamlit.title('Air Canada Webpage')

streamlit.header('Current Privileges:')
streamlit.header('Roles with correct Privileges:')
streamlit.header('Roles with invalid Naming:')
streamlit.header('Roles with missing Privileges:')
streamlit.hearder('Roles with wrong Privileges:')

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
