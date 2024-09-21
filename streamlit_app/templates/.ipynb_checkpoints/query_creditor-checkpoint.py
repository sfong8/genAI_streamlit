def query_creditor(creditor_name:str='',date_from:str='',date_end:str='',groupby:str=''):
    if date_from!='' and date_end!='':
        date_str = f'with start date (inclusive) {date_from} and end date (inclusive) {date_end}'
    elif date_from=='' and date_end!='':
        date_str = f'with end date (inclusive) {date_end}'
    elif date_from!='' and date_end=='':
        date_str = f'with start date (inclusive) {date_from}'
    else: 
        date_str=''

    if groupby != '':
        groupby_str = f'grouped by {groupby}'
    prompt = f'''show me the total value where the creditor name is like {creditor_name} {date_str} {groupby_str}'''
    return prompt

_title = "Query Creditor Name (Party receiving Payments)"
_description = "Provide the company name of the creditor you want to search. Outputs the total value. Optional: provide start date, end date and columns to group by"