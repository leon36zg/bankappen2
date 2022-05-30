import math
import sys 

print("Hejjj och väkommna till Leon BANKING SYSTEM!!\n")
print("provided by LEON BANKING SYSTEM.\n")                       #böjan av koden 

def addStartingBalance():
    print("ÅTERSTÄLLA STARTSALDO?")
    addStart = str(input())
    addStart = addStart.lower()
    if addStart == "j" or addStart == "ja":
        file = open("bankdatan.txt", "w")        #startbeloppet som är 200kr (står i bankdatan.txt)
        file.write(str(100))
    print("ÅTERSTÄLLA GAMLA LOGGAR?")
    erase = str(input())
    erase = erase.lower()
    if erase == "j" or erase == "ja":
        file = open("Transaction Log.txt", "w")         #det står alla trasaktioner man har gjort  
        file.write("Starta")
    prompt()

def prompt():
    print("Vill du göra en transaktion?")       #frågan om du vill göra transaktiionen 
    transact = str(input())
    transact = transact.lower()
    startup(transact)

def startup(confirm):
    run = True
    while run:
      if confirm == "ja" or confirm == "j":
        transaction_option()
      elif confirm == "nej" or confirm == "n" or confirm == "lämna" or confirm == "l":   #om du ska inte göra transaktionen då avslutas programmet 
        print("Avslutar programmet.....")
        sys.exit()
      elif confirm == "klar" or confirm == "k":
          addStartingBalance()
      else:
        print("Input invalid")
        prompt()

def transaction_option():
    print("\nVill du göra en insättning eller ett uttag")     # vill du göra insättning eller uttag 
    change = str(input(""))
    change = change.lower()
    if change == "insättning" or change == "i":
        deposit_money()
    elif change == "uttag" or change == "u":              
        withdrawMoney()
    elif change == "sluta" or change == "klar":
        print("Avslutar programmet.....")
        sys.exit() 
    else:
        print("Invalid input")
        
def checkBalance():
    file = open("bankdatan.txt", "r") 
    print("Aktuellt saldo")
    print(file.read())
    current = open("bankdatan.txt", "r").read()
    floatCurrent = float(current) 
    file.close()
    
def deposit_money():
    checkBalance()
    depositAction()

def depositAction():
    try:
        file = open("bankdatan.txt", "r")
        current = open("bankdatan.txt", "r").read()
        floatCurrent = float(current)
        file.close()
    
        print("Hur mycket vill du sätta in?")         #hur mycket vill du sätta in 
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("bankdatan.txt", "w") 
        newAmount = floatCurrent + floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("bankdatan.txt", "r")
        print("Nytt belopp är: ")
        print(file.read())
        file.close()
        transactionOccured = "+"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("Du angav en ogiltig input...")


def withdrawMoney():
    checkBalance()
    withdrawalAction()

def withdrawalAction():
    try:
        file = open("bankdatan.txt", "r")
        current = open("bankdatan.txt", "r").read()
        floatCurrent = float(current) 
        file.close()
    
        print("Hur mycket skulle du vilja ta ut?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("bankdatan.txt", "w")
        newAmount = floatCurrent - floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("bankdatan.txt", "r")
        print("Nytt belopp är: ")                           #balansen 
        print(file.read())
        file.close()
        transactionOccured = "-"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("Du angav en ogiltig input...")

    

def transactionLogs(floatCurrent, transactionOccured, floatAddedAmount,newAmount):
    LOG = open("Transaction Log.txt", "a")
    oldAmount = floatCurrent
    oldAmount = str(floatCurrent)
    transactionType = transactionOccured
    transactionAmount = floatAddedAmount
    transactionAmount = str(transactionAmount)
    updatedAmount = newAmount
    updatedAmount = str(newAmount)
    LOG.write("\n\nGammalt saldo: " + oldAmount)
    LOG.write("\nTransaktion inträffade: " + transactionType + transactionAmount)    
    LOG.write("\nNy balans: " + updatedAmount)            # nytt balans 
    

def main():
    prompt()
    

main()      
 
