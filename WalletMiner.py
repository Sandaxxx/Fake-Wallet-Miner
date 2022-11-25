#basic fake eth wallet miner by drak-o


import random
import os
from os import system, name
import time


def clear():
  
    if name == "nt":
        _ = system("cls")
  
    else:
        _ = system("clear")



website = "(Your website)" #put your website here
count1 = 0
count2 = 0
eth_ammount = str(round(random.uniform(0.5, 2), 4)) #generates fake eth ammount
random_id = ''
list_ = str('A''B''C''D''E''F''G''H''I''J''K''L''M''N''O''P''Q''R''S''T''U''V''W''X''Y''Z''a''b''c''d''e''f''g''h''i''j''k''l''m''n''o''p''q''r''s''t''u''v''w''x''y''z''1''2''3''4''5''6''7''8''9''0')

print("Miner de TRON (TRX)") #you can delete this and add your own tag/name
time.sleep(5)

user_adress=input('> ADDRESSE DE RECUPERATION  ---> ')
if (user_adress[:2]) == "0x" and len(user_adress) == 42:   #here it checks if the format of the adress is correct
    print ("> CHECK DE L'ADDRESSE...")
    time.sleep(2)
    
    print ("> ADDRESSE CORRECT ==>")
    time.sleep(1)
    
    print ("> CHECK DATABASE...")
    time.sleep(5)
    
    print ("> whitdrawal configuration complete")
    time.sleep(1)

else:
    print ("> checking adress...")
    time.sleep(2)
    
    print ("> error, adress format is wrong")
      


os.system('color 4')
while count1<random.randint(1000000,1500000): #number of tries until you get a fake win
    
    while count2<40:
        random_id = random_id + (random.choice(list_)) #makes random fake eth adress
        count2 = count2+1
    count2 = 0
    print("> ADDRESS:  0x" + random_id + "   | BALANCE:  TRON = 0.0")
    count1 = count1 + 1
    random_id2 = random_id
    random_id = ''
    

clear()    
os.system('color 2')
print("> ADDRESS:  0x"+random_id2 + "   | BALANCE:  TRON = " + eth_ammount) #the text that get's displayed when they "find a wallet"

print("> Attemptin withdrawal...")
time.sleep(5)
print("> Error number 4132, visit "+ website +" to complete withdrawal process") #fake error message that get's displayed

os.system('pause')