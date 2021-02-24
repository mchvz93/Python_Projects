#This is HW4PS1
#Marco Chavez
#student id 913519
#CS 10

def main():
    indexEntries = {}

    infile = open("icecream.txt", "r")
    fields = extractRecord(infile)
    column1 = column2 = column3 = 0
    while len(fields) != 0:
        entries, column1, column2, column3 = Calc(indexEntries, fields[0], fields[1], fields[2], fields[3],column1,column2,column3)                                     
        fields = extractRecord(infile)

    infile.close()

    printIndex(indexEntries,column1,column2,column3)


def extractRecord(infile):
    line = infile.readline()
    if line != "":
        fields = line.split(":")
        term = fields[0].rstrip()
        page = float(fields[1])
        page2 = float(fields[2])
        page3 = (fields[3].rstrip())
        page3 = float(fields[3])
        
        return [term,page,page2,page3]
    else:
        return[]


def Calc(dic, term, page, page2, page3, column1, column2, column3):
    tup = tuple([page, page2, page3,page+page2+page3])
    dic[term] = tup
    column1 += tup[0]
    column2 += tup[1]
    column3 += tup[2]

    return dic, column1, column2, column3


def printIndex(entries,column1,column2,column3):
    for key in sorted(entries):
        print(key,"\t", end= " ")
        pageSet = entries[key]
        first = True
        for page in pageSet:
            if first:
                print(page, end=" ")
                first = False
            else:
                print("\t", page, end=" ")
        print()
    print("\t\t", column1,"\t", column2, "\t", column3)

main()



'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
chocolate 	 10225.25 	 9025.0 	 9505.0 	 28755.25 
cookie dough 	 7901.25 	 4267.0 	 7056.5 	 19224.75 
rocky road 	 6700.1 	 5012.45 	 6011.0 	 17723.55 
strawberry 	 9285.15 	 8276.1 	 8705.0 	 26266.25 
vanilla 	 8580.0 	 7201.25 	 8900.0 	 24681.25 
		 42691.75 	 33781.8 	 40177.5
>>> '''
