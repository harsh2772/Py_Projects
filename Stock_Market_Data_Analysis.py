import datetime
import time
from plyer import notification
import yfinance as yf


company_symbols=["RELIANCE.NS","TCS.NS","HDFCBANK.NS","HINDUNILVR.NS","INFY.NS","ICICIBANK.NS","BHARTIARTL.NS","KOTAKBANK.NS","ITC.NS","MSFT"]

company_list=["Reliance Industries Ltd.","Tata Consultancy Services Ltd.","HDFC Bank Ltd.","Hindustan Unilever Ltd.","Infosys Ltd.","ICICI Bank Ltd.","Bharti Airtel Ltd.","Kotak Mahindra Bank Ltd.","ITC Ltd.","Microsoft Pvt. Ltd."]

print("The Company Name Which Stock You Want To Analyse:")

for i,z in enumerate(company_list,start=1):
    print(f"for press {i} to know details of {z}")

index=int(input("Enter the stock you want to analyse: "))

company_name=company_list[index-1]
company_symbol=company_symbols[index-1]

stock_analysis=yf.Ticker(f"{company_symbol}")
stock=stock_analysis.info
# print(stock)                                      # To see all data of that company.


if(index==4 or index==7 or index==8):

    while True:
        notification.notify(
            title=f"Stock Market Data of {company_name}".format(datetime.date.today()),
            message=f"""The Current Price is {stock['currentPrice']}""",
            app_icon="C:/Users/harsh/Desktop/Python_Projects/Source Files/Notify.ico",
            timeout=5
        )
        time.sleep(10)

else:
    while True:
        notification.notify(
            title=f"Stock Market Data of {company_name}".format(datetime.date.today()),
            message=f"""The Current Price is {stock['currentPrice']}\nThe Target High Price is {stock["targetHighPrice"]}\nThe Target Low Price is {stock['targetLowPrice']}\nThe Target Mean Price is {stock['targetMeanPrice']}\nThe Target Median Price is {stock['targetMedianPrice']}""",
            app_icon="C:/Users/harsh/Desktop/Python_Projects/Source Files/Notify.ico",
            timeout=5
        )
        time.sleep(10)