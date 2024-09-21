import streamlit as st

def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    st.sidebar.page_link("multipage_app.py", label="Home",icon='🏠')
    st.sidebar.page_link("pages/1_text_to_sql.py", label="Text to SQL",icon='📃')
    st.sidebar.page_link("pages/1_text_to_sql-Templates.py", label="Text to SQL (Templates)",icon='📃')
    st.sidebar.page_link("pages/text_summarisation.py", label="PDF Q&A",icon='💬')
    st.sidebar.page_link("pages/csv_helper.py", label="CSV Data Analyst (Soon)",icon='💹')
    st.sidebar.page_link("pages/document_extraction.py", label="Knowledge Base/Q&A (Soon)",icon='🔍')
def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("multipage_app.py")
    menu()