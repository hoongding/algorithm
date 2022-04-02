hour, minute = map(int, input().split())

cal_minute = int(minute - 45)

if cal_minute >= 0 :
    print("%d %d" %(hour,cal_minute))
else:
    cal_hour = hour-1
    if cal_hour<0:
        cal_hour = 23
    cal_minute = 60 + cal_minute
    print("%d %d" %(cal_hour,cal_minute) ) 
    