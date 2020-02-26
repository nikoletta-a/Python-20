with open("askisi2.txt", 'r') as file:
    for line in file:
        for word in line.split():
            if 'f' in word or 'r' in word or 'c' in word or 'k' in word:
                print(word+" Κακή Λέξη")
                continue
            if word==".":
                continue
            else:
                print(word + " Καλή Λέξη")