def query_creditor(payment_level:str,creditor_name:str,date_from:str='',date_end:str='',groupby:str=''):
    if date_from!='' and date_end!='':
        date_str = f'with payment date (inclusive) between {date_from} and {date_end}'
    elif date_from=='' and date_end!='':
        date_str = f'with payment date (inclusive) to {date_end}'
    elif date_from!='' and date_end=='':
        date_str = f'with payment date (inclusive) from {date_from}'
    else:
        date_str=''

    if groupby != '':
        groupby_str = f'grouped by {groupby}'
    else:
        groupby_str=''

    prompt = f'''Show me the {payment_level} where the creditor name is like {creditor_name.lower()} {date_str} {groupby_str}'''
    return prompt
