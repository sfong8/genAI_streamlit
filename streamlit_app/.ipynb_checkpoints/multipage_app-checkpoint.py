import streamlit as st
import pandas as pd
import numpy as np
from menu import menu
import streamlit as st
st.set_page_config(layout="wide")    
st.write("# Demo GenAI Application")
st.markdown(
    """
**Disclaimer**: This app was created for demo purposes only and any datasets used in this app is either **synthetic** data or **publicly available** datasets. 

## To Begin, Select a task on the side panel.
- **Data Querying Assistant** : Ability to self-serve - Query databases and extract data through natural language. 

- **PDF Q&A** : Upload PDF and ask questions about document.

- **Client Talking Points** : Summarises Clients data and Generate client specific insights using internal and external data sources. 
"""
)
# - **CSV Data Analyst** : Upload CSV File and perform analysis.

# - **Documents Search/Q&A** : Perform Q&A on a collection of documents and retrieve similar documents. 

# - **Data Servicing Assistant** : Retrieve similar requests and generate SQL code suggestion to help with request.
menu()
