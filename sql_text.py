defined_prompts = {
    'I would like to see the monthly income and month on month percentage difference by client name and product for RD John Smith': {
        'sql_query': """
WITH monthly_income as (SELECT lower(ci.client_name) as client_name,
                               pi.product_level2,
                               date_trunc('month', pi.summary_date) as month,
                               sum(pi.income) as monthly_income
                        FROM   client_product.client_info ci 
                        JOIN client_product.product_income pi
                                ON ci.client_id = pi.client_id
                        WHERE  lower(ci.rd_name) like lower('%john smith%')
                        GROUP BY lower(ci.client_name), pi.product_level2, date_trunc('month', pi.summary_date)
                        ),
income_with_previous as (SELECT client_name,
                              product_level2,
                              month,
                              monthly_income,
                              LAG(monthly_income) OVER (PARTITION BY client_name,
                                                                     product_level2
                                                        ORDER BY month) as previous_month_income
                       FROM   monthly_income
                       )
SELECT client_name,
       product_level2,
       month,
       monthly_income,
       CASE WHEN previous_month_income is not null AND
                 previous_month_income != 0 THEN ((monthly_income - previous_month_income) / previous_month_income) * 100
            ELSE null end as month_on_month_percentage_difference
FROM   income_with_previous
ORDER BY client_name, product_level2, month
""",
        'explanation': """This query does the following:

1. We start with a CTE called `monthly_income` that:
   - Joins the `client_info` and `product_income` tables
   - Filters for RD John Smith (using LOWER and LIKE for case-insensitive matching)
   - Groups the data by client name, product level 2, and month
   - Calculates the monthly income

2. We then use another CTE called `income_with_previous` that:
   - Uses the LAG function to get the previous month's income for each client and product

3. Finally, we select from `income_with_previous` to:
   - Show the client name, product level 2, month, and monthly income
   - Calculate the month-on-month percentage difference
   - Order the results by client name, product level 2, and month

This query complies with Athena syntax and follows the important notes you provided:
- It uses CAST for date comparisons where necessary
- It doesn't use aliases in the GROUP BY clause
- It respects column types (e.g., using quotes for string values)
- It converts relevant columns to lowercase for case-insensitive matching""",
        'results': './results/844526a2-dbb7-4dc1-abdc-6f7ac063ce8f.csv',
        'query_questions': {
            'Can you identify significant trends in the monthly income by product and client': """
    Given the information we have, here are some significant trends in the monthly income by product and client:

1. Client-specific trends:
   - Company abc1 shows the highest income for BACS products, with an average of 61,027 per month. This is significantly higher than other clients for the same product.
   - Company def1 has the highest income for Cash products, averaging 55,690 per month.

2. Product-specific trends:
   - BACS and Cash products generally show higher monthly incomes across most clients.
   - Current Accounts and FPS products tend to have lower monthly incomes for all clients.
   - Overdraft products show high variability between clients, with company abc1 having much higher averages than others.

3. Variability in income:
   - Company def3's Overdraft product shows the highest variability (standard deviation of 1008.77), indicating significant fluctuations in monthly income.
   - Current Accounts and FPS products generally show lower variability across clients, suggesting more stable income streams.

4. Potential seasonal patterns:
   - While we couldn't visualize the time series data, the presence of minimum and maximum values suggests there might be seasonal fluctuations or trends over time.
   - For example, company abc1's BACS product ranges from a minimum of 58,860 to a maximum of 62,987, which could indicate seasonal peaks and troughs.

5. Client portfolio differences:
   - Different clients seem to have varying strengths in different products. For instance, while company abc1 excels in BACS, company def1 shows strength in Cash products.

6. Product importance:
   - BACS, Cash, and Overdraft products seem to be the most significant income generators across clients.
   - Current Accounts and FPS, while present for most clients, contribute less to the overall monthly income.

To gain more detailed insights into specific trends over time, month-to-month changes, or to identify any clear upward or downward trends, we would need to visualize the time series data or perform more advanced time series analysis.
    """
            , "Plot a heatmap of the total income by client and product": 'total_income_heatmap_archived.png'
            , 'Generate me some insights into the income by product and client': """Based on this data, I can provide several insights into the income by product and client:

1. Top Earning Clients and Products:
   - Company abc1's BACS product is the highest income generator overall, with £732,332.
   - Company def1's Cash product is the second-highest, earning £668,281.

2. Client-specific insights:
   - Company abc1: Relies heavily on BACS, which generates significantly more income than its other products.
   - Company def1: Has a more balanced product mix, with Cash, Current Accounts, and BACS all generating substantial income.
   - Company def2: Also has a relatively balanced mix, with Cash, BACS, and Cheques as top earners.
   - Company def3: Overdraft is by far their biggest income generator, followed by BACS and Cash.

3. Product-specific insights:
   - BACS is a strong performer across multiple clients, appearing in the top 3 for several companies.
   - Cash is also a consistently high earner across different clients.
   - Overdraft services generate significant income for some clients (especially company def3) but not for others.
   - FPS (Faster Payments Service) is only a significant income source for company def2.

4. Diversity of income sources:
   - Some clients like company abc1 and company def3 have a more concentrated income source (BACS and Overdraft respectively).
   - Others like company def1 and company def2 have more diversified income across multiple products.

5. Potential areas for growth:
   - Clients with lower income from certain products might have room for growth. For example, company abc1 could potentially increase its income from Current Accounts or FPS.

To gain more detailed insights, especially regarding trends over time, we would need to analyze the data by summary_month as well. This would allow us to see if there are any seasonal patterns or growth trends for specific products or clients.""",
            "Plot a heatmap of the total income by client and product": 'total_income_heatmap_archived.png',

            'which client had a decrease in total income in the latest month?': """The clients that had a decrease in total income in the latest month (June 2024) compared to the previous month (May 2024) were company def1, company def2, and company def3."""

        }
    }, 'show me the monthly income and balance for parent "parent company abc"': {
        'sql_query': """
WITH parent_clients AS (
    SELECT client_id
    FROM client_product.client_info
    WHERE LOWER(parent_name) LIKE LOWER('%parent company abc%')
        ),
monthly_data AS (
    SELECT DATE_TRUNC('month', pi.summary_date) AS month,
        SUM(pi.income) AS total_income,
        SUM(pb.balance) AS total_balance
    FROM client_product.product_income pi
    JOIN parent_clients pc ON pi.client_id = pc.client_id
    LEFT JOIN client_product.product_balance pb 
        ON pi.account_id = pb.account_id 
        AND pi.product_id = pb.product_id
        AND pi.summary_date = pb.summary_date
    GROUP BY DATE_TRUNC('month', pi.summary_date)
        )
SELECT 
    CAST(month AS DATE) AS month,
    total_income,
    total_balance
FROM monthly_data
ORDER BY month""",
        'explanation': """ This query does the following:\n\n1. First, we create a CTE called `parent_clients` to get all the client IDs associated with the parent company "parent company abc". We use LOWER() function and LIKE operator for case-insensitive partial matching.\n\n2. Then, we create another CTE called `monthly_data` where we:\n   - Join the `product_income` table with the `parent_clients` CTE to filter only the relevant clients.\n   - Left join with the `product_balance` table to include balance information.\n   - Group the data by month using DATE_TRUNC function.\n   - Sum up the income and balance for each month.\n\n3. In the main query, we select from the `monthly_data` CTE, casting the month to DATE type for better readability.\n\n4. Finally, we order the results by month.\n\nThis query complies with Athena syntax and follows the important notes you provided:\n- It uses CAST for date comparisons.\n- It doesn\'t use aliases in the GROUP BY clause.\n- It respects column types (e.g., using quotes for string values).\n- It uses LOWER() for case-insensitive string comparisons.""",
        'results': './results/f85a54ac-fd08-4f94-ba7c-e3c042e0881b.csv',
        'query_questions': {
            'Plot a heatmap of the date with the monthly income': 'monthly_income_heatmap_archiveTotal.png'
        }

    },

    'I would like to see the total monthly income and balance by parent company': {
        'sql_query': """
WITH monthly_data AS (
    SELECT 
        ci.parent_name,
        pi.summary_date,
        SUM(pi.income) AS total_income,
        SUM(pb.balance) AS total_balance
    FROM client_product.client_info ci
    JOIN client_product.product_income pi 
            ON ci.client_id = pi.client_id
    JOIN client_product.product_balance pb 
            ON pi.account_id = pb.account_id 
            AND pi.summary_date = pb.summary_date
    GROUP BY 
        ci.parent_name,
        pi.summary_date
)
SELECT 
    parent_name,
    CAST(summary_date AS DATE) AS month,
    total_income,
    total_balance
FROM 
    monthly_data
ORDER BY 
    parent_name,
    month;""",
        'explanation': """This query does the following:\n\n1. We use a CTE (Common Table Expression) named `monthly_data` to join the three tables and perform the initial aggregation.\n\n2. We join `client_info` with `product_income` using `client_id`, and then join with `product_balance` using `account_id` and `summary_date`.\n\n3. We group by `parent_name` and `summary_date` to get monthly totals for each parent company.\n\n4. In the main query, we select from the CTE, casting the `summary_date` to DATE type for better readability.\n\n5. We order the results by `parent_name` and `month` for a clear presentation.\n\nThis query complies with Athena syntax and follows the important notes:\n- It doesn't use aliases in the GROUP BY clause.\n- It casts the `summary_date` to DATE in the final SELECT statement.\n- It includes all required columns in the CTE.\n- It doesn't use any string comparisons that would require special handling.""",
        'results': './results/f5f63e25-5249-44d7-b594-cbf5f9eb70a6.csv',
        'query_questions': {
            'Plot the total income by parent company': 'total_income_by_parent_company_archived1.png'
        }
    }

    ,

    'show me monthly income by client name and product for RD John Smith': {
        'sql_query': """
WITH client_rd AS (
    SELECT client_id, client_name
    FROM client_product.client_info
    WHERE LOWER(rd_name) LIKE LOWER('%John Smith%')
)

SELECT 
    ci.client_name,
    pi.product_level2,
    DATE_TRUNC('month', pi.summary_date) AS month,
    SUM(pi.income) AS monthly_income
FROM client_product.product_income pi
JOIN client_rd ci ON pi.client_id = ci.client_id
GROUP BY 
    ci.client_name,
    pi.product_level2,
    DATE_TRUNC('month', pi.summary_date)
ORDER BY 
    ci.client_name,
    pi.product_level2,
    month""",
        'explanation': """This query does the following:

1. We create a CTE named `client_rd` to filter clients with RD John Smith. We use LOWER() function to make the comparison case-insensitive.

2. In the main query, we join the `product_income` table with our `client_rd` CTE.

3. We select the client name, product level 2, and use DATE_TRUNC to get the month from the summary_date.

4. We sum the income to get the monthly income.

5. We group by client name, product level 2, and month.

6. Finally, we order the results by client name, product level 2, and month for a clear presentation.

This query complies with Athena syntax and follows the important notes you provided:
- It uses LIKE with LOWER() for string comparisons.
- It doesn't use aliases in the GROUP BY clause.
- It respects column types (no quotes around non-string columns).
- It includes all required columns in the CTE.""",
        'results': './results/a575d7b6-1b13-4d7b-ab57-0195477b1686.csv',
        'query_questions': {
            'Generate me some insights into the income by product and client': """Based on this data, I can provide several insights into the income by product and client:

1. Top Earning Clients and Products:
   - Company abc1's BACS product is the highest income generator overall, with £732,332.
   - Company def1's Cash product is the second-highest, earning £668,281.

2. Client-specific insights:
   - Company abc1: Relies heavily on BACS, which generates significantly more income than its other products.
   - Company def1: Has a more balanced product mix, with Cash, Current Accounts, and BACS all generating substantial income.
   - Company def2: Also has a relatively balanced mix, with Cash, BACS, and Cheques as top earners.
   - Company def3: Overdraft is by far their biggest income generator, followed by BACS and Cash.

3. Product-specific insights:
   - BACS is a strong performer across multiple clients, appearing in the top 3 for several companies.
   - Cash is also a consistently high earner across different clients.
   - Overdraft services generate significant income for some clients (especially company def3) but not for others.
   - FPS (Faster Payments Service) is only a significant income source for company def2.

4. Diversity of income sources:
   - Some clients like company abc1 and company def3 have a more concentrated income source (BACS and Overdraft respectively).
   - Others like company def1 and company def2 have more diversified income across multiple products.

5. Potential areas for growth:
   - Clients with lower income from certain products might have room for growth. For example, company abc1 could potentially increase its income from Current Accounts or FPS.

To gain more detailed insights, especially regarding trends over time, we would need to analyze the data by summary_month as well. This would allow us to see if there are any seasonal patterns or growth trends for specific products or clients.""",
            'which client had a decrease in total income in the latest month?': """The clients that had a decrease in total income in the latest month (June 2024) compared to the previous month (May 2024) were company def1, company def2, and company def3.""",

        }
    }

}