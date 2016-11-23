import random

def GetType():
    return random.randrange(0, 3)

TH = random.randrange(1, 500)
N = random.randrange(1, 20)
TP = random.randrange(1, 300)

with open("input.txt", "w") as f:
    # print first two lines 
    f.write("{0}    {1}    {2}\n".format(TH, N, TP))

    for i in range(3):
        c = random.random() * 10
        f.write("{0} ".format(c))
    f.write("\n")

    # print enemies
    n = input("Number of enemies: ")
    includeSpeed = input("Include Enemies Speeds in File? [bonus] 0/1?")

    for i in range(n):
        TY = random.randrange(0, 3)
        T = int(random.random() * 10) 
        H = random.randrange(1, TH)
        Pow = random.randrange(1, TP)
        Prd = random.randrange(1, 10)
        f.write("{0}    {1}     {2}     {3}     {4}     {5}     ".format(i, TY, T, H, Pow, Prd))

        if (includeSpeed == 1):
            Speed = random.randrange(1, 30)
            f.write("{0}    ".format(Speed))

        R = random.choice(['A', 'B', 'C', 'D'])
        f.write("{0}\n".format(R))

    f.write("-1")
        

    
