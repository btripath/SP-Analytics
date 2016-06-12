from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector


cnx = mysql.connector.connect(user='root', password='ranikhet1',
                              host='127.0.0.1',
                              database='stock')


cursor = cnx.cursor()

today_dt = datetime.now().date()

add_quote = ("insert into stk_data "
  " (quote_date, symbol, name, open_price, close_price, high_52_wk, low_52_wk, ma_200_day, revenue, market_cap, PEG, yield, beta) "
   "values (%s, %s, %s,    %s, %s, %s,    %s, %s, %s,   %s, %s, %s, %s)" )




add_quote_data =  (today_dt, "ABBV","AbbVie Inc. Common Stock",59.99,60.75,71.60,45.45,-58.05,23000,98000,0.78,3.69,1.46627)


cursor.execute (add_quote, add_quote_data)

cnx.commit()

cnx.close()
    

