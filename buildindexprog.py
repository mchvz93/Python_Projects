#this program builds the index of a book from terms and page numbers

def main():
    # Create an empty dictionary
    indexEntries = {}

    # Extract the data from text file
    infile = open("indexdata.txt", "r")
    fields = extractRecord(infile)
    while len(fields) > 0:
        addWord(indexEntries, fields[1], fields[0])
        fields = extractRecord(infile)
    infile.close()

    #print the index listing
    printIndex(indexEntries)

# Extract a single record from the input file
# @param infile the input file object
# @return a list containing the page number and term or an empty list if
# the end of the file was reached

def extractRecord(infile):
    line = infile.readline()
    if line != "" :
        fields = line.split(":")
        page = int(fields[0])
        term = fields[1].rstrip()
        return [page, term]
    else:
        return[]

# add a word and it page number to the index
# @param entries the dictionary of index entries
# @param term the term to be added to the index
# @param page the page number for this occurrence of the term

def addWord(entries, term, page):
    #if the term is already in the dictionary, add the page to the set
    if term in entries:
        pageSet = entries[term]
        pageSet.add(page)

    #otherwise, create a new set that contains the page and add an entry.
    else:
        pageSet = set([page])
        entries[term] = pageSet

# print the index listing
# @param entries a dictionary containing the entries of the index

def printIndex(entries):
    for key in sorted(entries):
        print(key, end= " ")
        pageSet = entries[key]
        first = True
        for page in sorted(pageSet):
            if first :
                print(page, end="")
                first = False
            else:
                print(",", page, end="")

        print()

# start the program
main()

'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
example 7, 10
index 7
program 7, 11
set 20
type 6, 8
>>> '''
                
