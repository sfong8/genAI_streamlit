import streamlit as st
import pandas as pd
import numpy as np
from menu import menu
import streamlit as st
st.set_page_config(layout="wide")    
st.write("# Demo GenAI Chatbot")
st.markdown(
    """
**Disclaimer**: This app was created for demo purposes only and any datasets used in this app is either **synthetic** data or **publicly available** datasets. 

## To Begin, Select a task on the side panel.
- **Text to SQL** : Ability to self-serve - Query databases and extract data through natural language. 

- **Text to SQL (Templates)** : Commonly asked queries for Text to SQL. 

- **PDF Q&A** : Upload PDF and ask questions about document.

- **CSV Data Analyst** : Upload CSV File and perform analysis.

- **Knowledge Base/Q&A (Soon)** : Perform Q&A on a corpus of data and retrieve similar documents. 
"""
)


menu()
