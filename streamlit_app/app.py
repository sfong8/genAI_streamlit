import streamlit as st
from query_creditor import query_creditor
import time
from text_to_sql_script import text_to_sql_func,text_to_sql_func_test
from sql_formatter.core import format_sql
import sys
sys.path.append('/home/sagemaker-user/text-to-sql-for-athena/')
from dataframe_agent import dataframe_agent


st.set_page_config(layout="wide")    
st.title("Test GenAI Chatbot")
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'show_chart_reset' not in st.session_state:
    st.session_state.show_chart_reset = None
if 'queryDataFrame' not in st.session_state:
    st.session_state.queryDataFrame = False
def click_queryDF():
    st.session_state.queryDataFrame = True
def click_button():
    st.session_state.clicked = True
def click_button_reverse():
    st.session_state.clicked = False

with st.chat_message("user"):
    st.write("Hello! ")
    st.markdown(
        """
    <style>
        div[role=radiogroup] label:first-of-type {
            visibility: hidden;
            height: 0px;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    st.radio('What would you like to do today?',
             key = "task",
        options= ['Dummy','Query Internal Data','Query External Data (soon)','Text Summarisation/Insights (soon)','Document Retrival/Similarity Match (Soon)']
    )
    if st.session_state.task!='Query Internal Data':
        st.write("This functionality is coming soon please choose another option")

    if st.session_state.task=='Query Internal Data':
        st.write("You have selected: Query Internal Data")
        st.markdown(
            """
        <style>
            div[role=radiogroup] label:first-of-type {
                visibility: hidden;
                height: 0px;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.radio('Choose from common query templates or type in your question?',
             key = "query_internal_choice",
        options= ['Dummy','Templates','Ask Bot']
                )


        if st.session_state.query_internal_choice == 'Templates':
            st.selectbox('Main Theme?',
             key = "query_internal_template",
        options= ['Query Payments Data','Query MI Data (soon)','Query Financial Data (soon)','Query Complaints (soon)','Query Salesforce Data (soon)']
                )
            if st.session_state.query_internal_template in(['Query MI Data (soon)','Query Financial Data (soon)','Query Complaints (soon)','Query Salesforce Data (soon)']):
                st.write("This functionality is coming soon please choose another option")

            if st.session_state.query_internal_template=='Query Payments Data':
                st.selectbox('Choose query payments template',
             key = "query_payments_template",
        options= ['Query Creditor Name','Query your Client Payments']
                )

            if st.session_state.query_payments_template=='Query Creditor Name':
                with st.form("my_form"):
                    st.selectbox('Level of Aggregation',
                 key = "payment_level",
            options= ['Total Value','Top 50 Individual Payments']
                    )
                    st.text_input('(Required) Enter Credit company name',key='creditor_name')
                    st.text_input('(Optional) Enter Payment Start date (inclusive). Format: yyyy-mm-dd',value='',key= 'start_date' )
                    st.text_input('(Optional) Enter Payment End date (inclusive). Format: yyyy-mm-dd',value='',key= 'end_date')
                    st.text_input('(Optional) Group by conditions',value='',key='groupbys')
                    # st.button('Fetch Data',key='fetch')
                    submitted = st.form_submit_button("Submit")
                    # if st.session_state.fetch:
                    if submitted or st.session_state.queryDataFrame:
                        user_prompt = query_creditor(payment_level=st.session_state.payment_level,creditor_name=st.session_state.creditor_name
                                                     ,   date_from=st.session_state.start_date,date_end=st.session_state.end_date,groupby=st.session_state.groupbys)
                        st.write('User Prompt: ' + user_prompt)

                        with st.spinner('Generating SQL and Fetching Results'):
                            sql_query,result,explanation = text_to_sql_func(user_query=user_prompt)

                            if result.shape[0]==0:
                                st.success('Error!')
                                st.text(sql_query + ', Please try again')
                            else:
                                st.success('Done!')
                                st.text('Generated SQL:')
                                st.code(format_sql(sql_query),language='sql')
                                st.text('Explanation:')
                                st.text(explanation)
                                st.text('Returned Result:')
                                st.table(result)
        if st.session_state.query_internal_choice=='Ask Bot':
            with st.form("my_form"):
                st.text_input('(Required) Enter your query',key='free_text')
                submitted = st.form_submit_button("Submit")
                
                if submitted or  st.session_state.queryDataFrame::
                    user_prompt = st.session_state.free_text
                    st.write('User Prompt: ' + user_prompt)
    
                    with st.spinner('Generating SQL and Fetching Results'):
                        sql_query,result,explanation  = text_to_sql_func_test(user_query=user_prompt)
                        if result.shape[0]==0:
                                st.error('Error!')
                                st.text(sql_query + ', Please try again')
                        else:
                                st.success('Done!')
                                st.text('Generated SQL:')
                                st.code(format_sql(sql_query),language='sql')
                                st.text('Explanation:')
                                st.text(explanation)
                                st.text('Returned Result:')
                                st.table(result)
                        st.session_state.show_chart_reset=True

            if st.session_state.show_chart_reset:
                col1, col2 = st.columns(2)
                with col1:
                    button1 = st.button('Query Result',key='queryDataFrame',on_click=click_queryDF)
    
                with col1:
                    button2 = st.button('Clear Form',key='clear',on_click=click_button_reverse)
                print(submitted,st.session_state.show_chart_reset)
    
            if st.session_state.queryDataFrame:
                st.text_input('Enter your query for the returned Result',key= 'dataframe_query')
                # agent = dataframe_agent(result)
                # output = agent.invoke(st.session_state.dataframe_query,verbose=False).get('output')
                

        if st.session_state.show_chart_reset and st.session_state.queryDataFrame:
            st.text('test')