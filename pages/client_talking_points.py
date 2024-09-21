import sys
import streamlit as st
from menu import menu
import time 
menu()
if 'authentication_status' not in st.session_state:
    st.info('Please Login from the Home page and try again.')
    st.stop()

from talking_points_text import *







def main():
    # st.set_page_config(page_title="Client talking Points",layout='wide')
    st.markdown(
    """#### This demo illustrates how LLM can summarise client MI data and generate client specific insights using various data sources"""
)
    # upload file
    # pdf = st.file_uploader("Upload your PDF", type="pdf")
    with st.form("my_form"):
        st.text_input('Enter Client name to generate talking points','EasyJet PLC')
        submitted = st.form_submit_button("Submit")
    if submitted:
        test_name = 'EasyJet'
        if test_name is not None:
            with st.spinner('Generating Report'):
                with st.expander('Annual Report Insights',expanded=False):
                    st.markdown("### Annual Report Insights")
                    with st.spinner("Generating insights from EasyJet Annual Report"):
                        time.sleep(5)
                        st.markdown("#### Summarisation of Report")   
                        st.markdown(summarisation_text)
                    with st.spinner("Summarising Performance"):
                        time.sleep(5)
                        st.markdown("#### Performance Summary")     
                        st.markdown(performance_text_AR)
                    with st.spinner("Identifying Key Future Risk from Report"):
                        time.sleep(5)
                        st.markdown("#### Key Future Risk")     
                        st.markdown(key_risk_AR)
                    
                    with st.spinner("Identifying Company's growth plan and banking product opportunties"):
                        time.sleep(5)
                        st.markdown("####  Company's Growth Plan and Banking Product Opportunties")   
                        st.markdown(growth_opportunities_AR) 
    
    
                with st.expander('Client Income Performance Insights',expanded=False):
                    st.markdown("### Client Income Performance Insights")
                    # with st.spinner("Generating insights from Client's monthly income by Product"):
                    #     time.sleep(5)
                    #     st.markdown("#### Product Income Summary")   
                    #     st.markdown(product_insights_income_text)
                    with st.spinner("Significant product income trend?"):
                        time.sleep(5)
                        st.markdown("#### Latest Month Income Insight and Trend by Product")     
                        st.markdown(product_income_insight_trends)
                    with st.spinner("Comparison with Industry avg Income"):
                        time.sleep(5)
                        st.markdown("#### Comparison with Industry avg Income")     
                        st.markdown(industry_comparison)

                with st.expander('Client Product Balance Insights',expanded=False):
                    st.markdown("### Client Balance Performance Insights")
                    with st.spinner("Latest Month Income Insight and Trend by Product"):
                        time.sleep(5)
                        st.markdown("#### Latest Month Significant Decrease in Balance")     
                        st.markdown(product_balance_insight_trends)

if __name__ == '__main__':
    main()