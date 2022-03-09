import pandas as pd  # pip install pandas openpyxl
import plotly.express as px # pip install plotly-express
import streamlit as st # pip install streamlit
from collections import Counter


st.set_page_config(
	page_title='Roles: Access to Programs',
	page_icon=':speedboat:',
	layout='wide'
)


df = pd.read_excel(
	io='2021_H1_LS5.1_APM436_System.xlsx',
	engine='openpyxl',
	sheet_name='CMP100',
	skiprows=0,
	usecols='A:G',
	nrows=49942,
)

#st.dataframe(df)

# SIDEBAR
st.sidebar.header('Please Filter Here:')
company = st.sidebar.multiselect(
	'Select the company:',
	options=df['COMPANY'].unique(),
)

program = st.sidebar.multiselect(
	'Select the programs:',
	options=sorted(df['PROGRAM'].unique())
)

role = st.sidebar.multiselect(
	'Select the role:',
	options=sorted(df['ROLE'].unique())
)

df_selection = df.query(
	'COMPANY == @company & PROGRAM == @program'
)

st.dataframe(df_selection)
# MAINPAGE
st.title(':speedboat: Roles Dashboard')
#new paragraph
st.markdown('##')
roles_count = int(df_selection['ROLE'].nunique())
st.subheader('Number of roles found: ')
st.subheader(f'{roles_count}')

st.markdown('---')
#st.subheader('List of roles with number of corresponding programs: ')
roles_found = df_selection['ROLE'].tolist()
dict = Counter(roles_found)


dict_sorted = sorted(dict, key=dict.get, reverse=True)
dict_sorted2 = sorted(dict.items(), key=lambda x: x[1])
#st.subheader(dict_sorted)
#st.bar_chart(df_selection['COMPANY'])
for r in sorted(dict):
	if int(dict[r])>1:
		st.subheader('Role: ')
		st.subheader(f'{r}')
		st.subheader('Number of corresponding programs: ')
		number_of_roles = int(dict[r])
		st.subheader(f'{number_of_roles}')

