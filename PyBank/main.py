import csv
import os

csvpath=os.path.join("", "budget_data.csv")
outputfile=os.path.join("analysis","budget_analysis.txt")
print(csvpath)

#variables
totalmonths= 0
totalprofitlosses=0
averageprofitlosses=0
greateastincrease=["",0]
greateastdecrease=["",0]
lastmonthprofit=0
netprofitlosseslist=[]

#code to read the data in the file

with open(csvpath)as budget_data:
    #create a csv reader object
    csvreader = csv.reader(budget_data)

    # read the head row
    header = next(csvreader)
    #read the first row
    firstdatarow= next(csvreader)

    totalmonths += 1
    lastmonthprofit = int(firstdatarow[1])
    totalprofitlosses += int(firstdatarow[1])

    for row in csvreader:
        # add the count of the total months
        totalmonths += 1
        totalprofitlosses+=int(row[1])

        netprofitlosses= int(row[1])-lastmonthprofit
        lastmonthprofit=int (row[1])
        netprofitlosseslist+=[netprofitlosses]

        if netprofitlosses> greateastincrease[1]:
           greateastincrease[1]=netprofitlosses
           greateastincrease[0]=row[0]

        elif netprofitlosses < greateastdecrease[1]:
           greateastdecrease[1] = netprofitlosses
           greateastdecrease[0] = row[0]

    averageprofitlosses= sum(netprofitlosseslist)/len(netprofitlosseslist)
    # output
    output =(
    f"Financial analysis\n"
    f"--------------------------\n"
    f"total months= {totalmonths }\n"
    f"--------------------------\n"
    f"totalprofitlosses= ${totalprofitlosses}\n"
    f"--------------------------\n"
    f"averageprofitlosses= ${ averageprofitlosses:.2f}\n"
    f"--------------------------\n"
    f"greatestprofitincrease= {greateastincrease[0]}, ${greateastincrease[1]}\n"
    f"--------------------------\n"
    f"greatestprofitdecrease= {greateastdecrease[0]},${greateastdecrease[1]}\n")

    print(output)

    with open(outputfile,"w") as txt:
        txt.write(output)




