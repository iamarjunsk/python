import csv

def year_check(yr):
    with open('rainfall.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for y in reader:
            if y["Year"] == yr:
                return y
        print("Data Not available")

def total_rainfall(yr):
    y = year_check(yr)
    if y:
        a=[]
        for i in y:
            a.append(y[i])
        sum=0
        for i in range(1,13):
            sum=sum+float(a[i])
        print("Annual rainfall for the year " +str(yr)+" = "+str(round(sum,1)))

def winter_rain(yr):
    # jan and feb
    y = year_check(yr)
    if y:
        sum = float(y["Jan"])+float(y["Feb"])
        print("Annual winter rain for the year " +str(yr)+" = "+str(round(sum,1)))

def pre_mansoon_rain(yr):
    # March, April and May.
    y = year_check(yr)
    if y:
        sum = float(y["Mar"])+float(y["Apr"])+float(y["May"])
        print("Annual pre-mansoon rain for the year " +str(yr)+" = "+str(round(sum,1)))

def south_west_monsoon(yr):
    # June, July, August and September
    y = year_check(yr)
    if y:
        sum = float(y["Jun"])+float(y["Jul"])+float(y["Aug"])+float(y["Sep"])
        print("Annual south west mansoon rain for the year " +str(yr)+" = "+str(round(sum,1)))

def north_east_monsoon(yr):
    # October, November and December.
    y = year_check(yr)
    if y:
        sum = float(y["Oct"])+float(y["Nov"])+float(y["Dec"])
        print("Annual north west mansoon rain for the year " +str(yr)+" = "+str(round(sum,1)))

def monthly_rain(yr):
    y=year_check(yr)
    if y:
        a=[]
        months = ['Year','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for i in y:
            a.append(y[i])
        for i in range(13):
            print(months[i]+" : "+a[i])

yr = input("Enter year for total rainfall")
total_rainfall(yr)
winter_rain(yr)
pre_mansoon_rain(yr)
south_west_monsoon(yr)
north_east_monsoon(yr)
monthly_rain(yr)


