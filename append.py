
with open('test.txt', "w") as f:
    for i in range(3):
        print("This is line " + str(i), file=f)
