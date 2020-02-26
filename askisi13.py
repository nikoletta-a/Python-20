card=input("Enter Card number")
while len(card)<16 or len(card)>16:
    print("Card length must be 16 digits long.")
    card = input("Enter Card number")
b = True
list= [int(x) for x in str(card)]

# lastdig= list[len(list)-1]
# print(lastdig)
# list.pop()
print(list)
for i in range(len(list)-1,-1,-1):
    if b==True:
        list[i]=list[i]*2
        b=False
    elif b==False:
        b=True

sum=0
for i in range(0,len(list)):

    sum=sum+list[i]

if sum%10==0:
    print("Card valid")
else:
    print("Card Invalid")