import sys
import streamlit as st
from menu import menu
from talking_points_text import *
import time
menu()
if 'authentication_status' not in st.session_state:
    st.info('Please Login from the Home page and try again.')
    st.stop()
def main():
    st.write(
    """This demo illustrates how to you can upload a PDF file and ask questions on the content"""
)
    # upload file
    # pdf = st.file_uploader("Upload your PDF", type="pdf")
    st.text('Placeholder for File upload')
    st.text('Demo Purpose: You have uploaded EasyJet Half-Year Annual Report')

    init_prompt = st.selectbox(
        'You might want to try these prompts...',
         ['Summarise the document',
         'What was their performance and the factors contributing to performance',
         'What is the growth plan and identify where they might need banking product',
          'What are the key risk facing company']
         )
    with st.form("my_form"):
        st.text_input('Enter your question',init_prompt,key='free_text')
        submitted = st.form_submit_button("Submit")
    if submitted and st.session_state.free_text == 'Summarise the document':
        with st.spinner("Generating Response"):
            time.sleep(5)
            st.markdown(summarisation_text)
    if submitted and st.session_state.free_text == 'What was their performance and the factors contributing to performance':
            with st.spinner("Generating Response"):
                time.sleep(5)
                st.markdown(performance_text_AR)
    if submitted and st.session_state.free_text ==  'What is the growth plan and identify where they might need banking product':
            with st.spinner("Generating Response"):
                time.sleep(5)
                st.markdown(growth_opportunities_AR)
    if submitted and st.session_state.free_text ==  'What are the key risk facing company':
            with st.spinner("Generating Response"):
                time.sleep(5)
                st.markdown(key_risk_AR)
        # st.markdown(performance_text_AR)
        # st.markdown(key_risk_AR)
    # if "messages2" not in st.session_state:
    #     st.session_state.messages2 = []
    # # Display chat messages from history on app rerun
    # for message in st.session_state.messages2:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])
    #
    #     # Accept user input
    # if prompt := st.chat_input("Ask a question about the PDF"):
    #     # Add user message to chat history
    #     st.session_state.messages2.append({"role": "user", "content": prompt})
    #     # Display user message in chat message container
    #     with st.chat_message("user"):
    #         st.markdown(prompt)
    #     output='test'
    #
    #     st.session_state.messages2.append({"role": "assistant", "content": output})
    # menu()
if __name__ == '__main__':
    main()