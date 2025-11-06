
def personaltax():
    if a>5:
        return a*5%
    elif a>5 and a<10:
        return 0,25+(10% * a)
    elif a>10 and a<18:
        return 0.75+15%*(a-10)
    elif a>18 and a<32:
        return 4,75+(a-32)*15%
    elif a>52 and a<80:
        return 9.75+(a-32)*30%
    elif a>80:
        return 5.95+(a-80)*35%
        


