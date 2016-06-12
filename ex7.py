from __future__ import print_function
from datetime import date, datetime, timedelta
import urllib
import urllib.request
import time
import string
import mysql.connector
import csv


def getbeta (sym):

    url = "http://finance.yahoo.com/q?s=" + sym


    betaresponse = str(urllib.request.urlopen(url).read())


    beginning = betaresponse.find ('Beta:</th><td class="yfnc_tabledata1">') +38

    end1 = betaresponse.find ('</td></tr><tr><th scope="row" width="54%">Next Earnings Date:')
    end2 = betaresponse.find ('</td></tr><tr><th scope="row" width="54%">Earnings Date:')


    beta = betaresponse[beginning: max(end1, end2) ]

    

    if len(beta)  > 20:
        beta = "999"

    if beta == "N/A":
        beta = '999'

    
    return beta

def get_stock_data(inputfile):

    f = open(inputfile, 'r')
    
    tkr_list = []

    for line in f:
        symbol = line.rstrip('\n')
        tkr_list.append(symbol)
# call the yahoo service to get the beta, append to beta file
        getbeta(symbol)

    
    arg = tkr_list[0]

    i=0
    for tkr in tkr_list:
    
        if i != 0: 
            arg = arg + '+' + tkr 
        i += 1    

    print ("arg is " + arg)
    url = ("url call")
    url = "http://finance.yahoo.com/d/quotes.csv?s=" + arg + "&f=sopkjm4s6j1r5yn"

    print (url)
    

    response = urllib.request.urlopen(url).read()

#    print (response))

    f.close
    return response

###  Begin of main program

output_file = 'stock_quotes' + time.strftime('%Y%m%d') + '.csv'


fout = open(output_file, 'a')


cnx = mysql.connector.connect(user='root', password='ranikhet1',
                              host='127.0.0.1',
                              database='stock')


cursor = cnx.cursor()

today_dt = datetime.now().date()

add_quote = ("insert into stk_data "
  " ( quote_date, symbol, name, open_price, close_price, high_52_wk, low_52_wk, ma_200_day, revenue, market_cap, PEG, yield, beta) "
   "values ( %s, %s, %s,    %s, %s, %s,    %s, %s, %s,   %s, %s, %s, %s)" )


header =  'symbol, open, close, 52wk High, 52 wk low, 200 mvg avg, rev, Mkt cap, PEG, yield, name, beta \n'
print (header)
fout.write(header)

# change 1 to 12

for i in range (1, 12):
    input_file = "ti"
    input_file = input_file + str(i)
    input_file += ".txt"
    print ("now processing " + input_file)

    stock_recs = str(get_stock_data(input_file))
#    stock_recs = str(get_stock_data("ti2test.txt"))



    for row in  (stock_recs.split('\\n')):
        row1 = row.lstrip("b'")
        if row1:
            print (row1)

            field_list = row1.split(",")
            
            
            beta =  getbeta(field_list[0])

            fout.write(row1 + ','+ beta + '\n')

            if str.isnumeric(field_list[1][0]):
                  
                cur_arg =  (today_dt, field_list[0], field_list[10], field_list[1], field_list[2], field_list[3], field_list[4], field_list[5], field_list[6], field_list[7], field_list[8], field_list[9], beta)
                print (add_quote)
                print (cur_arg)
                cursor.execute (add_quote, cur_arg)
            
                
                  
                

    print ("going to sleep now")    
#   time.sleep(60)
    print ("waking up")

cnx.commit()

cnx.close()

fout.close

print ("end of program")


 
fout.close

print ("end of processing")

