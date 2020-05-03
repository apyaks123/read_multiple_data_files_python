import math
import string
import re
from collections import Counter 

str = []
global yyy
counts = 0
fours = 0
global lengt




def readFile():
    count = -1
    global file
    file = input('Please enter the file name along with the extension like .txt : ')
    print(file)
    with open(file) as fp: 
        Lines = fp.readlines() 
        for line in Lines: 
            count += 1
            
            x = {count,  line.strip()}
            str.append(line)
    return file      
            


# function Call

readFile()

# Split the value in list and Capitalize it
xxx = str[0].split()
qqq = [i.capitalize() for i in xxx]

# Then sort the list in ascending order
sorts = sorted(qqq)

# make it as a string now 
zzz = " ".join(sorts)

# print the value in the list
print("\n-----------------------------------\n")
print(zzz)
ppp = Counter(zzz)
print("\n-----------------------------------\n")


#print(len(xxx))
#print(len(xxx))

cnt = Counter()
for word in sorts:
     cnt[word] += 1
print("-----------------------------------")
print("word\t: \t\t\t\t\tOcurrences")
print("_______\t\t\t_||_____________________________________")
for x in cnt:
    print( "% s : \t\t\t\t\t\t% s" % (x, cnt[x]), end ="\n") 
    qqq = 0
   

print("\n-----------------------------------\n")
print("1.Total number of words in the report:",len(xxx))
lengt = len(xxx)


print("\n-----------------------------------\n")       
for x in cnt:
       if (cnt[x] == 1):
          counts += 1
print("2.Total number of unique words:", counts)
print("\n-----------------------------------\n")

for x in cnt:
    if (len(x) >= 4):
        fours += 1

print("3.Total number of unique words of more than four letters:", fours)
print("\n-----------------------------------\n")
        


#f = open('Output.txt', 'w')
with open('Output.txt', "w") as f:
    f.write("-------------------------------------------\n")
    f.write("-------------Summary--------------------------\n")
    f.write("-------------------------------------------\n")
    if file:
        f.write('Name of the file: '+ file)
    
    f.write("\n-----------------------------------\n")
    
    
    
    
    f.write("1.Total number of words in the report:" + format(len(xxx)))
    #print >> f.out, "x is", len(xxx)
    #f.write("1.Total number of words in the report:" + lengt)
    f.write("\n-----------------------------------\n") 
    f.write("\n-----------------------------------\n")   
    f.write("2.Total number of unique words:" + format(counts))
    f.write("\n-----------------------------------\n") 
    f.write("\n-----------------------------------\n")
    f.write("3.Total number of unique words of more than four letters:" + format(fours))   

    f.write("\n-----------------------------------\n")
    f.write("\n-----------------------------------\n")
    f.write("All the words in the list have been capitalized and sorted to be counted easily.")
    f.write("They are as follows:")
    f.write("\n-----------------------------------\n")
    f.write("\n-----------------------------------\n")
    f.write(zzz)
    f.write("\n-----------------------------------\n")

 


    
