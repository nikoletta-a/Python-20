products = {'milk': 0.8, 'cookies': 2.0, 'pasta': 0.9, 'water': 0.5, 'tomatoes': 1.2, 'orange juice': 2.5, 'cheese': 1.7}
shoppinglist = []
sum = 0
print("List of Products:", products)
i = input("Enter number of products:")

while i.isnumeric()==False:
     print("Please enter a valid number.")
     i = input("Enter number of products:")

finali=int(i)

for finali in range(0, finali):
    prod = input("Enter product name:")
    while prod not in products:
        print("Product doesn't exist.")
        prod = input("Enter product name:")
    if prod in products:
        shoppinglist.append(prod)

for elem in shoppinglist:
    if elem in products:
        sum = sum + products[elem]+products[elem]*13/100

print("Total sum with VAT:", sum)
print("Products bought:", shoppinglist)