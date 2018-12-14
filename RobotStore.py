# Lab 9 - Working with Objects
# Angeli Pinol
# Prof. Johnson
# CMPT120L - 113
# Nov 29 2018
productNames = [ "Ultrasonic range finder"
               , "Servo motor"
               , "Servo controller"
               , "Microcontroller Board"
               , "Laser range finder"
               , "Lithium polymer battery"
               ]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]

def printStock():
     print()
     print("Available Products")
     print("------------------")
     for i in range(0,len(productNames)):
         if productQuantities[i] > 0:
             print(str(i)+")",productNames[i], "$", productPrices[i])
     print()
     
# First define product class using constructor

class Products:
    def __init__(self,name,price,quantities):
        self.name = name
        self.price = price
        self.quantities = quantities
    def __str__(self):
        ans= "Name:    "+self.name
        ans+="Price:   "+str(self.price)
        ans+="Quantity:"+str(self.quantities)
    def  getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getQuant(self):
        return self.quantities
    def setName(self, newname):
        self.name = newname
    def setPrice(self, newprice):
        self.price = newprice
    def setQuant(self, newquant):
        self.quantities = newquant
        
# First define product class using constructor
        product_instances = [Products("Ultrasonic range finder", 2.50,4),
                             Products("Servo motor",14.99, 10),
                             Products("Servo controller", 44.95, 5),
                             Products("Microcontroller Board", 34.95, 7),
                             Products("Laser range finder", 149.99, 2),
                             Products("Lithium polymer battery", 8.99,8)]
    
     
def main():
     cash = float(input("How much money do you have? $"))
     while cash > 0:
         printStock()
         vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
         if vals[0] == "quit": break
         
         prodId = int(vals[0])
         count = int(vals[1])
         
         if productQuantities[prodId] >= count:
             if cash >= productPrices[prodId] * count:
                 productQuantities[prodId] -= count
                 cash -= productPrices[prodId] * count
                 print("You purchased", count, productNames[prodId]+".")
                 print("You have $", "{0:.2f}".format(cash), "remaining.")
             else:
                 print("Sorry, you cannot afford that product.")
         else:
             print("Sorry, we are sold out of", productNames[prodId])

        
     main()

     
