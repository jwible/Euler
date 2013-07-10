Cnt_Of_Mnths_Starting_W_Sun = 0
Days_Since_Last_Cnt = 2 
Month = 1
Year = 1901
while Year<2001:
    if Month in (1, 3, 5, 7, 8, 10):
        Days_Since_Last_Cnt=Days_Since_Last_Cnt+31
    if Month in (4,6,9,11):
        Days_Since_Last_Cnt=Days_Since_Last_Cnt+30
    if Month is 2:
        if Year % 400 == 0:
            Days_Since_Last_Cnt=Days_Since_Last_Cnt+29
        elif Year % 100 == 0:
            Days_Since_Last_Cnt=Days_Since_Last_Cnt+28
        elif Year % 4 == 0:
            Days_Since_Last_Cnt=Days_Since_Last_Cnt+29
        else:
            Days_Since_Last_Cnt=Days_Since_Last_Cnt+29
    if Month is 12:
        Days_Since_Last_Cnt=Days_Since_Last_Cnt+31
        Month = 0
        Year = Year + 1
    if Days_Since_Last_Cnt % 7 == 0:
        Cnt_Of_Mnths_Starting_W_Sun = Cnt_Of_Mnths_Starting_W_Sun+1
    Month = Month + 1


print (Cnt_Of_Mnths_Starting_W_Sun)

