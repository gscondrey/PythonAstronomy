#Julian and Gregorian date conversions
#using the Fliegel-Van Flandern algorithm
C=int(input ("Select the calendar you are converting to: Julian(1) or Gregorian(2): "))
if C == 1:
    Year = int(input ("Input the year (YYYY): "))
    Month = int(input ("Input the month (1-12): "))
    Day = int(input ("Input the day (1-31): "))
    M1 = (Month - 14)/12
    Y1 = Year + 4800
    Julian = int(1461*(Y1 + M1)/4 + 367*(Month-2-12*M1)/12 - (3*((Y1+M1+100)/100))/4+Day - 32075)
    print("The Julian date is", Julian)
else:
     J = int(input ("Input the Julian date to the nearest integer: "))
     p = J + 68569
     q = int(4*p/146097)
     r = int(p - (146097*q + 3)/4)
     s = int(4000 * (r + 1)/1461001)
     t = int(r - (1461*s)/4 + 31)
     u = int(80*t/2447)
     v = int(u/11)
     Y = int(100*(q-49)+s+v)
     M = int(u + 2 - (12*v))
     D = int(t - (2447*u)/80)
     print("The Gregorian date is 1200 UTC on", int(Y),"/",int(M),"/",int(D),".")
     
