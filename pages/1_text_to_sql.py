import sys
import streamlit as st
from menu import menu
import pandas as pd
import datetime
import time
menu()
if 'authentication_status' not in st.session_state:
    st.info('Please Login from the Home page and try again.')
    st.stop()

if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'show_chart_reset' not in st.session_state:
    st.session_state.show_chart_reset = None
if 'result' not in st.session_state:
    st.session_state.result = None
if 'dataframe_query' not in st.session_state:
    st.session_state.dataframe_query = ''



def click_queryDF():
    st.session_state.queryDataFrame = True
def click_button():
    st.session_state.clicked = True
def click_button_reverse():
    st.session_state.clicked = False
import os
st.title("Data Querying Assistant - Query data using Natural Language")
st.write(
    """This demo illustrates how to retrieve data from databases and analyse results using natural language"""
)



with st.chat_message("user"):
    with st.form("my_form"):
        st.text_input('Enter your query','show me monthly income by client name and product level 2 for RD John Smith',key='free_text')
        submitted = st.form_submit_button("Submit")

    
    if submitted or st.session_state.show_chart_reset:
        user_prompt = st.session_state.free_text
        st.write('User Prompt: ' + user_prompt)
        with st.spinner('Fetching Results'):
            if st.session_state.free_text == 'show me monthly income by client name and product level 2 for RD John Smith':
                if st.session_state.result is None:
                    time.sleep(5)
                st.session_state.sql_query= '' 
                st.session_state.explanation =''
                st.session_state.result = pd.read_csv(r'result_df_johnSmith.csv')
            if st.session_state.result is None:
                st.session_state.sql_query,st.session_state.explanation  = text_to_sql_func(user_query=user_prompt)
            if st.session_state.sql_query=='Cannot Generate Query':
                    st.error('Error!')
                    st.text(sql_query + ', Please try again')
            else:
                    # st.success('Done!')
                    # with st.expander("See SQL Code",expanded=False):
                    #     st.text('Generated SQL:')
                    #     st.code(format_sql(sql_query),language='sql')
                    #     st.text('Explanation:')
                    #     st.text(explanation.split('The key things I kept in mind:')[0])
                    # with st.spinner('Fetching Results'):
                    if st.session_state.result is None:
                        st.session_state.result= fetch_results(st.session_state.sql_query)
                        # test =  st.session_state.result
                        # test.to_csv(r'result_df_johnSmith.csv',index=None)
                    with st.expander("Returned Result:",expanded=True):
                    # st.text('')
                        st.dataframe(st.session_state.result)
                    init_prompt = st.selectbox(
                    'You might want to try these prompts...',
                    ['Generate me some insights into the income by product and client',
                    "which client had a decrease in total income in the latest month?",
                    "plot a barchart for the total income by client"]
                )
                    with st.form("my_form2"):
                      
                        st.text_input('Query returned result',init_prompt,key= 'dataframe_query')
                        submitted2 = st.form_submit_button("Submit")
                    # result.to_csv('test_result2.csv',index=None)
            st.session_state.show_chart_reset=True
        # with st.form("my_form2"):
        #     st.text_input('Ask question on returned result',key= 'dataframe_query')
        #     submitted2 = st.form_submit_button("Submit")
        # if submitted2  or st.session_state.clicked:
        #     st.text('test')
        #     # agent = dataframe_agent(result)
        #     # output = agent.invoke(st.session_state.dataframe_query,verbose=False).get('output')
        #     submitted=True
        #     st.session_state.clicked=True
        if submitted2:
            if len(st.session_state.dataframe_query)>0:
                with st.spinner('Generating response'):
                    if  st.session_state.free_text == 'show me monthly income by client name and product level 2 for RD John Smith' and st.session_state.dataframe_query=='Generate me some insights into the income by product and client':
                        time.sleep(5)
                        st.markdown("""Based on this data, I can provide several insights into the income by product and client:

1. Top Earning Clients and Products:
   - Company abc1's BACS product is the highest income generator overall, with £732,332.
   - Company def1's Cash product is the second-highest, earning £668,281.
   - EasyJet plc's top products are Cash and Overdraft, both earning over £400,000.

2. Client-specific insights:
   - Company abc1: Relies heavily on BACS, which generates significantly more income than its other products.
   - Company def1: Has a more balanced product mix, with Cash, Current Accounts, and BACS all generating substantial income.
   - Company def2: Also has a relatively balanced mix, with Cash, BACS, and Cheques as top earners.
   - Company def3: Overdraft is by far their biggest income generator, followed by BACS and Cash.
   - EasyJet plc: Has four main products (Cash, Overdraft, BACS, and Cheques) all generating significant income.

3. Product-specific insights:
   - BACS is a strong performer across multiple clients, appearing in the top 3 for several companies.
   - Cash is also a consistently high earner across different clients.
   - Overdraft services generate significant income for some clients (especially EasyJet and company def3) but not for others.
   - FPS (Faster Payments Service) is only a significant income source for company def2.

4. Diversity of income sources:
   - Some clients like company abc1 and company def3 have a more concentrated income source (BACS and Overdraft respectively).
   - Others like company def1, company def2, and EasyJet plc have more diversified income across multiple products.

5. Potential areas for growth:
   - Clients with lower income from certain products might have room for growth. For example, company abc1 could potentially increase its income from Current Accounts or FPS.

To gain more detailed insights, especially regarding trends over time, we would need to analyze the data by summary_month as well. This would allow us to see if there are any seasonal patterns or growth trends for specific products or clients.""")
                if st.session_state.free_text == 'show me monthly income by client name and product level 2 for RD John Smith' and st.session_state.dataframe_query=='which client had a decrease in total income in the latest month?':
                    time.sleep(5)
                    st.markdown("""The clients that had a decrease in total income in the latest month (June 2024) compared to the previous month (May 2024) were company def1, company def2, and company def3.""")
                if st.session_state.free_text == 'show me monthly income by client name and product level 2 for RD John Smith' and st.session_state.dataframe_query == 'plot a barchart for the total income by client':
                    time.sleep(7)
                    st.image('total_income_by_client.png')
                # else:
                #     agent = dataframe_agent(st.session_state.result)
                #     if 'plot' in st.session_state.dataframe_query:
                #         print('test')
                #         output = agent.invoke(st.session_state.dataframe_query+'. If any charts or graphs or plots were created save them localy and include the save file names in your response. You must use all rows of the dataframe.',verbose=False).get('output')
                        
                #         png_file = [x for x in output.split("'") if 'png' in x][0]
                        
                #         time.sleep(5)
                #         # st.text(get_image_file())
                #         st.image(get_image_file())
                #         st.text('Chat output: ' + output)
                #     else:
                #         try:
                #             output = agent.invoke(st.session_state.dataframe_query,verbose=False).get('output')
                #             st.markdown(output)
                #         except Exception as e:
                #             response = str(e)
                #             if response.startswith("Could not parse LLM output: `"):
                #                 response = response.removeprefix("Could not parse LLM output: `").removesuffix("`")
                #                 st.text(response)
                #             elif 'Could not parse LLM output' in response:
                #                 response = response.split('Could not parse LLM output: `')[1]
                #                 st.text(response)
                #             else:
                #                 st.text(response)



