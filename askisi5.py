with open("askisi5.txt",'r') as file:
    for line in file:
        for word in line.split():
            if len(word)>3:
                word=word[1:]+ word[0] + "ay"
                print(word)
            else:
                print(word)