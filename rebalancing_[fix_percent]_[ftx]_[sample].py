# -*- coding: utf-8 -*-
"""Rebalancing [Fix Percent] [FTX] [Sample]

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hunbOQsxBePEUCxKpD_u_78eNXat_B7T
"""

!pip install ccxt
!pip install pandas
# cr:
# พี่ต้าน Mudley
# กลุ่ม กองทุนความมั่งคั่งแห่งชาติ
# B2 Spetsnaz Club

## Login 

import ccxt
# เปลี่ยน API เปลียน ข้อมูลกันด้วยนะครับ
apiKey    = "QCRmk7hfi_WGcn4_K9_TG2OlMtu87x2dLQBBvDWE" 
secret    = "KhdBMjLE_MHY1_YcNaYxaEwBM72xWE9Zfb3H7O1e" 
password  = "" 
Account_name  = "FTT" 


exchange = ccxt.ftx  ({'apiKey' : apiKey ,'secret' : secret ,'password' : password ,'enableRateLimit': True})
# Sub Account Check
if Account_name == "" :
  print("\n""Account Name - This is Main Account",': Broker - ',exchange)     
else:
  print( "\n"'Account Name - ',Account_name,': Broker - ',exchange)
  exchange.headers = {'ftx-SUBACCOUNT': Account_name,}

# ดูในพอร์ท ว่ามีเงินเท่าไร
import pandas as pd
Get_balance = exchange.fetch_balance()
print(pd.DataFrame(Get_balance))

# ดูในพอร์ท ว่ามีเงินเท่าไร
Asset_01 = Get_balance ['FTT'] ['total']
Asset_02 = Get_balance ['USD'] ['total']
print("Asset 01 = " , Asset_01,"FTT")
print("Asset 02 = " , Asset_02,"USD")

# เรียกดูราคา สินทรัพย์ ที่เราเทรด เพื่อหา มูลค่า
get_price     = exchange.fetch_ticker('FTT/USD') 
print(get_price)
Average_price = (get_price ['bid'] + get_price ['ask'] ) / 2
print("Average_price = " ,Average_price)

# มูลค่า ของ Asset
Asset_01_Value = Asset_01 * Average_price
print("Asset_01_Value = " ,Asset_01_Value)

# เปรียบเทียบ และ ตัดสินใจเทรด

Rebalance_mark = 2000
Rebalance_percent = 1

#    Asset_01_Value > (2000           + (2000          *   1             /100) ) :      
if   Asset_01_Value > (Rebalance_mark + (Rebalance_mark*Rebalance_percent/100) ) :
  print("Asset_01_Value ",Asset_01_Value ,">", (Rebalance_mark + (Rebalance_mark*Rebalance_percent/100) ))
  print("SELL")
  diff_sell  = Asset_01_Value - Rebalance_mark
  print(diff_sell)
  #exchange.create_order('FTT/USD' ,'market','sell',(diff_sell/Average_price)) ## กำหนดเป็น Unit USD/Price

elif Asset_01_Value < (Rebalance_mark - (Rebalance_mark*Rebalance_percent/100) ) :
  print("Asset_01_Value ",Asset_01_Value ,"<", (Rebalance_mark - (Rebalance_mark*Rebalance_percent/100) ))
  print("Buy")
  diff_buy  = Rebalance_mark - Asset_01_Value
  print(diff_buy)
  #exchange.create_order('FTT/USD' ,'market','buy',(diff_buy/Average_price))
  
else :
  print("None Trade")

import ccxt

while True:
  # เปลี่ยน API เปลียน ข้อมูลกันด้วยนะครับ
  apiKey = "QCRmk7hfi_WGcn4_K9_TG2OlMtu87x2dLQBBvDWE" #@param {type:"string"}
  secret = "KhdBMjLE_MHY1_YcNaYxaEwBM72xWE9Zfb3H7O1e" #@param {type:"string"}
  password = ""                   #@param {type:"string"}
  Account_name  = "FTT"           #@param {type:"string"}

  pair_trade = 'FTT/USD'          #@param {type:"string"}
  Asset_RB   = 'FTT'              #@param {type:"string"}

  Rebalance_mark = 2000           #@param 
  Rebalance_percent = 1           #@param 

####################################################
  exchange = ccxt.ftx  ({
    'apiKey' : apiKey ,'secret' : secret ,'password' : password ,'enableRateLimit': True
  })
  # Sub Account Check
  if Account_name == "" :
    print("\n""Account Name - This is Main Account",': Broker - ',exchange)     
  else:
    print( "\n"'Account Name - ',Account_name,': Broker - ',exchange)
    exchange.headers = {
      'ftx-SUBACCOUNT': Account_name,
    }

  Get_balance = exchange.fetch_balance()
  Asset_01 = Get_balance [Asset_RB] ['total']
  print("Asset 01 = " , Asset_01,Asset_RB)

  get_price     = exchange.fetch_ticker(pair_trade) 
  Average_price = (get_price ['bid'] + get_price ['ask'] )/2
  print("Asset 01 = " , Asset_01*Average_price)
  print("Asset Rebalance_mark = " , Rebalance_mark)

  # มูลค่า ของ Asset
  Asset_01_Value = Asset_01 * Average_price
  print("Asset_01_Value = " ,Asset_01_Value)

  if   Asset_01_Value > (Rebalance_mark + (Rebalance_mark*Rebalance_percent/100) ) :
    print("Asset_01_Value ",Asset_01_Value ,">", (Rebalance_mark + (Rebalance_mark*Rebalance_percent/100) ))
    print("SELL")
    diff_sell  = Asset_01_Value - Rebalance_mark
    print(diff_sell)
    #exchange.create_order(pair_trade ,'market','sell',(diff_sell/Average_price))

  elif Asset_01_Value < (Rebalance_mark - (Rebalance_mark*Rebalance_percent/100) ) :
    print("Asset_01_Value ",Asset_01_Value ,"<", (Rebalance_mark - (Rebalance_mark*Rebalance_percent/100) ))
    print("Buy")
    diff_buy  = Rebalance_mark - Asset_01_Value
    print(diff_buy)
    #exchange.create_order(pair_trade ,'market','buy',(diff_buy/Average_price))
    
  else :
    print("None Trade")

  import time
  sleep = 10 
  print("Sleep",sleep,"sec.")
  time.sleep(sleep) # Delay for 1 minute (60 seconds).