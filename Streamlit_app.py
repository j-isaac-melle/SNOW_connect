#dont run anything past while troubleshooting:
import streamlit
import snowflake.connector
import pandas

streamlit.title('Air Canada Webpage')

streamlit.header('Current Privileges: /n/n/n/n/n')
streamlit.header('Roles with correct Privileges:/n/n/n/n/n')
streamlit.header('Roles with invalid Naming:/n/n/n/n/n')
streamlit.header('Roles with missing Privileges:/n/n/n/n/n')
streamlit.hearder('Roles with wrong Privileges:/n/n/n/n/n')

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
