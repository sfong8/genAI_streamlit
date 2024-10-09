import streamlit as st

def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    st.sidebar.page_link("multipage_app.py", label="Home",icon='🏠')
    st.sidebar.divider()
    st.sidebar.write('**RD Assistant Tools**')
    st.sidebar.page_link("pages/1_text_to_sql.py", label="Data Querying Assistant",icon='📃')
    st.sidebar.page_link("pages/text_summarisationeasyJet.py", label="PDF Q&A",icon='❔')
    st.sidebar.page_link("pages/client_talking_points.py", label="Client Talking Points",icon='💬')

    st.sidebar.write('**GenBI Tools**')
    st.sidebar.page_link("pages/text-to-sql-tech.py", label="Data Querying Assistant (SQL Output)",icon='📃')

    # st.sidebar.page_link("pages/csv_helper.py", label="CSV Data Analyst",icon='💹')
    # st.sidebar.page_link("pages/rag_llm.py", label="Documents Search/Q&A",icon='🔍')
    # st.sidebar.divider()
    # st.sidebar.write('**Data Servicing Assistant**')
    # st.sidebar.page_link("pages/Data Servicing Assistant.py", label="Data Servicing Assistant",icon='🤖')
    
def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("multipage_app.py")
    menu()