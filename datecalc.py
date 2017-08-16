#This Code Calculates the number of possible date/Holy Day combinations in the Past/Future.
#This does not find the exact holy days for a specific year.

from array import *
import sys

Normal = [None]*366
Leap = [None]*367

MonthName = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
MonthLength = [31,28,31,30,31,30,31,31,30,31,30,31]
MonthLengthLeap = [31,29,31,30,31,30,31,31,30,31,30,31]
Count=1
CountLeap=1
for month in range(0,12):
    for day in range(1, MonthLength[month]+1): 
        Normal[Count] = MonthName[month] + "-" + str(day).zfill(2)
        Count = Count + 1

for month in range(0,12):
    for day in range(1, MonthLengthLeap[month]+1):
        Leap[CountLeap] = MonthName[month] + "-" + str(day).zfill(2)
        CountLeap = CountLeap+1


#KeyDays
#Sunday Before Dec 25th, 4th Advent
#Sunday After Dec 25th
#Baptism: 1st Sunday after Epiphany
#Easter: Between March 22 and Apr 25
Year = Normal
Results = []
IsLeap = False
#Fixed Days
#Results.append(["Every Year",""])
Results.append(["Christmas/Nativity",Year[Year.index("Dec-25")]])
Results.append(["Christmas Eve",Year[Year.index("Dec-24")]])
Results.append(["New Year's Day",Year[Year.index("Jan-01")]])
Results.append(["New Year's Eve",Year[Year.index("Dec-31")]])
Results.append(["Epiphany",Year[Year.index("Jan-07")]])
Results.append(["Presentation of the Lord",Year[Year.index("Feb-02")]])
Results.append(["Annunciation of the Lord",Year[Year.index("Mar-25")]])
Results.append(["Holy Cross",Year[Year.index("Sep-14")]])
Results.append(["All Saints",Year[Year.index("Nov-01")]])
for loop in range(0,1):
    for weekday in range(0, 6):
        #0 means Jan 1st is Sunday
        
        if loop == 1:
          IsLeap = True
        #Weekday Dependant
        FourthAdvent = Year[Year.index("Dec-25")-(weekday+1)]
        Results.append(["1st Sunday of Advent",Year[Year.index(FourthAdvent)-21]])
        Results.append(["2nd Sunday of Advent",Year[Year.index(FourthAdvent)-14]])
        Results.append(["3rd Sunday of Advent",Year[Year.index(FourthAdvent)-7]])
        Results.append(["4th Sunday of Advent/Sunday Before Christmas",Year[Year.index("Dec-25")-(weekday+1)]])
        
        Results.append(["Sunday After Christmas",Year[Year.index("Dec-25")+(weekday+1)]])
        
        #Thanksgivings
        USThanksSeed = Year.index("Nov-01")
        Results.append(["US Thanksgiving",Year[USThanksSeed+weekday+21]])
        CanThanksSeed = Year.index("Oct-01")
        Results.append(["Canada Thanksgiving",Year[CanThanksSeed+weekday+14]])
            
        # Epiphany Offset
        Baptism = Year[Year.index("Jan-07")+(weekday+1)]
        Results.append(["Baptism Sunday",Year[Year.index(Baptism)]])
        Results.append(["2nd Sunday after Epiphany",Year[Year.index(Baptism)+7]])
        Results.append(["3rd Sunday after Epiphany",Year[Year.index(Baptism)+14]])
        Results.append(["4th Sunday after Epiphany",Year[Year.index(Baptism)+21]])
        Results.append(["5th Sunday after Epiphany",Year[Year.index(Baptism)+28]])
        Results.append(["6th Sunday after Epiphany",Year[Year.index(Baptism)+35]])
        Results.append(["7th Sunday after Epiphany",Year[Year.index(Baptism)+42]])
        Results.append(["8th Sunday after Epiphany",Year[Year.index(Baptism)+49]])
        Results.append(["9th Sunday after Epiphany",Year[Year.index(Baptism)+56]])
        for EasterOffset in range(0,35):
            #Easter Dependent
            EasterSeed = Year.index("Mar-22")
            Easter = Year[EasterSeed + EasterOffset]
            #Results.append(["Leap = " + str(IsLeap) + ", Offset = " + str(weekday) + ", Easter = " + Easter,""])
            Results.append(["Transfiguration",Year[Year.index(Easter)-49]])
            Results.append(["Ash Wednesday",Year[Year.index(Easter)-46]])
            Results.append(["1st Sunday of Lent",Year[Year.index(Easter)-42]])
            Results.append(["2nd Sunday of Lent",Year[Year.index(Easter)-35]])
            Results.append(["3rd Sunday of Lent",Year[Year.index(Easter)-28]])
            Results.append(["4th Sunday of Lent",Year[Year.index(Easter)-21]])
            Results.append(["5th Sunday of Lent",Year[Year.index(Easter)-14]])
            Results.append(["Palm Sunday/6th Sunday of Lent",Year[Year.index(Easter)-7]])
            Results.append(["Holy Monday",Year[Year.index(Easter)-6]])
            Results.append(["Holy Tuesday",Year[Year.index(Easter)-5]])
            Results.append(["Holy Wednesday",Year[Year.index(Easter)-4]])
            Results.append(["Maundy Thursday",Year[Year.index(Easter)-3]])
            Results.append(["Good Friday",Year[Year.index(Easter)-2]])
            Results.append(["Holy Saturday",Year[Year.index(Easter)-1]])
            Results.append(["Easter",Year[Year.index(Easter)]])
            Results.append(["2nd Sunday of Easter",Year[Year.index(Easter)+7]])
            Results.append(["3rd Sunday of Easter",Year[Year.index(Easter)+14]])
            Results.append(["4th Sunday of Easter",Year[Year.index(Easter)+21]])
            Results.append(["5th Sunday of Easter",Year[Year.index(Easter)+28]])
            Results.append(["6th Sunday of Easter",Year[Year.index(Easter)+35]])
            Results.append(["Ascension Thursday",Year[Year.index(Easter)+40]])
            Results.append(["Ascension Sunday/7th Sunday of Easter",Year[Year.index(Easter)+42]])
            Results.append(["Pentecost",Year[Year.index(Easter)+49]])
            Results.append(["Holy Trinity",Year[Year.index(Easter)+56]])
            Results.append(["Proper 3",Year[Year.index(Easter)+63]])
            Results.append(["Proper 4",Year[Year.index(Easter)+70]])
            Results.append(["Proper 5",Year[Year.index(Easter)+77]])
            Results.append(["Proper 6",Year[Year.index(Easter)+84]])
            Results.append(["Proper 7",Year[Year.index(Easter)+91]])
            Results.append(["Proper 8",Year[Year.index(Easter)+98]])
            Results.append(["Proper 9",Year[Year.index(Easter)+105]])
            Results.append(["Proper 10",Year[Year.index(Easter)+112]])
            Results.append(["Proper 11",Year[Year.index(Easter)+119]])
            Results.append(["Proper 12",Year[Year.index(Easter)+126]])
            Results.append(["Proper 13",Year[Year.index(Easter)+133]])
            Results.append(["Proper 14",Year[Year.index(Easter)+140]])
            Results.append(["Proper 15",Year[Year.index(Easter)+147]])
            Results.append(["Proper 16",Year[Year.index(Easter)+154]])
            Results.append(["Proper 17",Year[Year.index(Easter)+161]])
            Results.append(["Proper 18",Year[Year.index(Easter)+168]])
            Results.append(["Proper 19",Year[Year.index(Easter)+175]])
            Results.append(["Proper 20",Year[Year.index(Easter)+182]])
            Results.append(["Proper 21",Year[Year.index(Easter)+189]])
            Results.append(["Proper 22",Year[Year.index(Easter)+196]])
            Results.append(["Proper 23",Year[Year.index(Easter)+203]])
            Results.append(["Proper 24",Year[Year.index(Easter)+210]])
            Results.append(["Proper 25",Year[Year.index(Easter)+217]])
            Results.append(["Proper 26",Year[Year.index(Easter)+224]])
            Results.append(["Proper 27",Year[Year.index(Easter)+231]])
            Results.append(["Proper 28",Year[Year.index(Easter)+238]])
            Results.append(["Christ the King",Year[Year.index(Easter)+245]])
            #print(str(offset)+ " Sunday After Christmas: " + Normal[SunAfterChristmas])
            #print(str(offset)+ " Sunday Before Christmas: " + Normal[SunBeforeChristmas])
    Year = Leap
#FilteredResults = list(set(Results))
print(len(Results))
#FilteredList = list(set(Results))
text_file = open("Full List.txt", "w")
text_file2 = open("Filtered List.txt", "w")
FilteredList = set([])

for Result in Results:
    print(str(Result[0])+"  "+str(Result[1]))
    FilteredList.add(str(Result[0])+"  "+str(Result[1]))
    text_file.write(str(Result[0])+"  "+str(Result[1]) + "\n")
for Result in sorted(FilteredList):
    text_file2.write(str(Result)+"\n")

text_file.close()
text_file2.close()