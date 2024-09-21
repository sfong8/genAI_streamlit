import sys
import streamlit as st
from menu import menu
summarisation_text= "Here is a summary of the key points from the easyJet half-year financial report:\n\n- easyJet reported a headline loss before tax of £350 million for the six months ended 31 March 2024, an improvement from a £411 million loss in the same period last year.\n\n- Total revenue increased 22% to £3,268 million, driven by a 12% increase in capacity and strong yields.\n\n- Passenger numbers increased 11% to 36.7 million.\n\n- Load factor was 86.7%, slightly down from 87.5% last year.\n\n- easyJet holidays continued strong growth, with customer numbers up 42% and profit up 210% to £31 million.\n\n- The company had a net cash position of £146 million as of 31 March 2024.\n\n- easyJet expects strong summer demand to deliver earnings growth for full year 2024.\n\n- New bases were opened in Birmingham and Alicante, performing well.\n\n- The company announced a 10th UK base to open at London Southend in summer 2025.\n\n- easyJet agreed to purchase a heavy maintenance facility in Malta to provide supply certainty and cost benefits.\n\n- The company remains on track to deliver its medium-term target of over £1 billion profit before tax.\n\nThe report provides detailed financial statements and notes covering easyJet's performance and financial position for the half-year period."

performance_text_AR = "Here are the key points about easyJet's performance and contributing factors for the six months ended 31 March 2024:\n\n1. Headline loss before tax of £350 million, an improvement of £61 million compared to the same period last year.\n\n2. Total revenue increased by 22% to £3,268 million, driven by:\n   - 11% increase in passenger numbers to 36.7 million\n   - 12% increase in capacity to 42.3 million seats\n   - 5% increase in airline revenue per seat to £69.87\n\n3. Factors contributing to performance:\n   - Strong demand, especially for leisure travel\n   - Growth in easyJet holidays business, with 42% customer growth and 210% profit growth\n   - Cost discipline, with headline airline cost per seat excluding fuel remaining flat\n   - Network optimization, including new bases in Birmingham and Alicante\n   - Ancillary revenue growth of 30%\n\n4. Challenges faced:\n   - Impact from the conflict in the Middle East\n   - Continued inflationary pressures across the industry\n   - Increase in fuel costs by 18% to £914 million\n\n5. Positive outlook:\n   - Expecting strong FY24 earnings growth\n   - Summer demand looks positive\n   - On track to achieve medium-term profit target of over £1 billion\n\nThe company appears to be recovering well from previous challenges, with growth in revenue and passenger numbers, though still reporting a loss for this typically weaker half of the year. The holidays business and ancillary revenues are providing significant growth opportunities."


key_risk_AR =  'Some of the key risks for easyJet\'s future include:\n\n1. Environmental sustainability - The report mentions easyJet\'s pathway to net zero and efforts to reduce carbon emissions, indicating this is a key focus area and risk.\n\n2. Macroeconomic and geopolitical factors - The report notes these as one of easyJet\'s risk themes.\n\n3. Legislative/regulatory landscape - This is listed as one of easyJet\'s risk themes.\n\n4. Safety, security and operations - Another risk theme mentioned in the report.\n\n5. Technology risks - Listed as one of easyJet\'s risk themes.\n\n6. Asset performance - Noted as a risk theme for easyJet.\n\n7. People-related risks - "Our People" is listed as one of the key risk themes.\n\n8. Fuel price volatility - The report discusses fuel hedging, indicating this remains a key risk area.\n\n9. Foreign exchange rate fluctuations - Currency hedging is discussed, suggesting this is an ongoing risk.\n\n10. Demand fluctuations - The report mentions modeling demand suppression scenarios, indicating this is a key risk area.\n\nThe report states that easyJet\'s principal risks and uncertainties have not materially changed from those set out in the 2023 Annual Report. However, it does not provide extensive details on specific future risks beyond the themes mentioned above.'

growth_opportunities_AR =  "Here are some key points about easyJet's growth plan and potential banking product needs:\n\nGrowth plan:\n- Expect FY24 capacity of around 100 million seats, an 8% increase year-over-year\n- Targeting growth through new bases and routes:\n  - Recently launched new bases in Birmingham and Alicante \n  - Announced 10th UK base at London Southend to open summer 2025\n  - Launched over 158 new routes for FY24\n- Continuing fleet renewal and growth:\n  - Expect 16 A320neo family aircraft deliveries in FY24\n  - Have orders for 306 more A320neo family aircraft through FY34\n- Growing easyJet holidays business:\n  - Expecting >35% customer growth in FY24\n  - Aiming to increase UK market share from 5% to 7%\n\nPotential banking product needs:\n- Financing for aircraft purchases and deliveries\n- Working capital facilities to manage seasonality (winter losses, summer profits)\n- Foreign exchange hedging products (exposed to EUR, USD, CHF)\n- Fuel hedging products \n\nThe company already has some banking facilities in place:\n- $400 million Revolving Credit Facility maturing in September 2025\n- $1,750 million UKEF backed facility maturing in June 2028\n\nHowever, given the significant growth plans and capital expenditures outlined, they may require additional financing or banking products to support this expansion. The report does not provide enough detail to determine specific new banking needs with certainty."

product_insights_income_text = "Here are the insights into the Client Income by product for EasyJet PLC:\n\n1. Cash:\n   - Highest average income (mean: £35,351)\n   - Most consistent income stream (small range between min: £34,420 and max: £36,522)\n   - Likely the primary product for EasyJet PLC\n   - Performs best compared to industry average, with only £1,816 below average\n\n2. Cheques:\n   - Lowest average income (mean: £15,734)\n   - Most consistent low-level usage (small range between min: £14,561 and max: £16,451)\n   - Second-best performer compared to industry average, £6,582 below average\n\n3. BACS:\n   - Third highest average income (mean: £22,966)\n   - Moderate variability in income (range from £19,781 to £35,253)\n   - Significantly underperforming compared to industry average, £21,346 below average\n\n4. Overdraft:\n   - Second highest average income (mean: £25,868)\n   - Highest variability (min: £0, max: £35,700)\n   - Worst performer compared to industry average, £23,963 below average\n   - Inconsistent usage suggests potential issues or opportunities\n\nKey Insights:\n1. EasyJet PLC relies heavily on Cash transactions, which provide the highest and most consistent income.\n2. The company underperforms the industry average across all products, but Cash and Cheques are closest to industry standards.\n3. BACS and Overdraft products show significant underperformance compared to industry averages, indicating potential areas for improvement.\n4. The high variability in Overdraft usage (including periods with £0 income) suggests inconsistent cash flow management or potential issues with this product.\n5. There may be opportunities to increase usage and income from BACS and Overdraft products to bring them closer to industry averages.\n6. The company might benefit from strategies to shift more transactions to Cash and Cheques, where they perform better relative to industry standards.\n\nThese insights suggest that EasyJet PLC should focus on improving its BACS and Overdraft offerings while maintaining its strong performance in Cash transactions. Additionally, investigating the reasons for the inconsistent Overdraft usage could reveal opportunities for more stable income from this product."

industry_comparison ="The client's income compared to the industry average income varies significantly across different products:\n\n1. Cash: The client's performance is closest to the industry average in this category, with income only 4.89% below the industry average.\n\n2. Cheques: The client's income is significantly lower, at 29.49% below the industry average.\n\n3. BACS and Overdraft: These two categories show the largest gaps, with the client's income approximately 48% below the industry average for both.\n\nIn summary, the client's income is below the industry average across all product categories, but the gap is smallest for Cash products and largest for BACS and Overdraft products. This suggests that while the client is underperforming compared to the industry in all areas, there's particular room for improvement in BACS and Overdraft products, followed by Cheques. The Cash product category is where the client is most competitive relative to the industry average."

product_trend_text = "Yes, there are significant product income trends observable in the data:\n\n1. BACS shows a significant upward trend in the last three months of the data.\n2. Cash remains stable throughout the period with no significant trend.\n3. Cheques also remain relatively stable with no significant trend.\n4. Overdraft displays the most dramatic trend, with a sharp decline in the last five months of the data, going from being the highest-income product to zero.\n\nThese trends suggest changes in the company's financial products or customer behavior, particularly for BACS (increasing in popularity) and Overdraft (sharply decreasing in usage or being phased out). The stability of Cash and Cheques indicates consistent use of these traditional banking methods."

product_income_insight_trends = 'Latest Month Insights and Trends of Income by Product (June 2024):\n\n1. Product Ranking:\n   - Cash is the top income generator with £36,522.\n   - BACS is a close second with £35,253.\n   - Cheques are third with £16,096.\n   - Overdraft shows no income (£0) for June 2024.\n\n2. Month-over-Month Trends:\n   - All products except Overdraft showed positive growth from May to June 2024.\n   - BACS had the highest absolute increase, growing by £4,361.\n   - Cash increased by £978.\n   - Cheques saw a modest increase of £245.\n   - Overdraft experienced a significant decline, dropping by £2,010 to £0.\n\n3. Key Insights:\n   - Cash and BACS continue to be the primary income sources, collectively accounting for about 81% of the total income in June 2024.\n   - The strong growth in BACS income (+14% month-over-month) suggests a possible shift towards electronic payments.\n   - The complete drop in Overdraft income to £0 is noteworthy and may indicate a change in policy, reduced customer reliance on overdrafts, or potential data anomaly that should be investigated.\n   - Despite being the third-largest income source, Cheques generate less than half the income of BACS or Cash, reflecting a possible long-term decline in check usage.\n\n4. Potential Areas for Further Investigation:\n   - The reason behind the sudden drop in Overdraft income to £0.\n   - The substantial growth in BACS income and whether this represents a sustainable trend.\n   - Strategies to maintain the strong performance of Cash transactions while potentially encouraging more BACS usage for its efficiency.\n   - The long-term viability of Cheques as an income source, given its relatively low contribution.\n\nThese insights provide a snapshot of the current income distribution across products and highlight recent trends, which can be valuable for strategic decision-making and resource allocation in the coming months.'

product_balance_insight_trends = "In June 2024, EasyJet PLC has two active overdraft accounts with significantly different balances. ACC000020 has a low balance of 261.0, showing a consistent decrease over the past year, potentially indicating improved financial management or reduced credit needs. ACC000044 has a much higher balance of 2,790,405.0, with more volatile usage patterns throughout the year, suggesting possible seasonal or irregular financial needs. Both accounts exclusively use the Overdraft product, which appears to be a key financial tool for EasyJet PLC. The stark difference in account balances might reflect different operational needs within the company or separate credit facilities for different business units. This disparity in overdraft usage could warrant further investigation into the company's financial structure and credit risk management strategies."

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