smthing = input("Enter a sentence: ")


def parrot(smth):

    smth = smth.split(" ")

    for i in smth:
        count = smth.index(i)
        for j in i:
            if j == "," or j == ".":
                i = i.replace(j, "")
                smth[count] = i
            else:
                continue

    print(max(smth, key=len))


parrot(smthing)
