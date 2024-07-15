months = ['January','February','March','April','May','June','July','August','September','October','November','December']
total_rain = 0
total_months = 0

years = int(input("How many years?\n"))
for year in range(1,years+1):#years is offset by 1 to output the correct year number in the print statement
    for month in months:
        rain = int(input("How many inches of rain in {} of year {}?\n".format(month, year)))
        total_rain += rain 
        total_months += 1
    year += year
avg = total_rain / total_months
print("Number of months:",total_months,"months")
print("Total rainfall:", total_rain,"inches")
print("Average Rainfall:",avg,"inches")

input("Press Enter to exit.")