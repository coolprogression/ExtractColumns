import sys
import csv
import os


#check if -l used
pos = 1
if sys.argv[pos] == '-l':
  pos = pos + 1


if os.path.exists(sys.argv[pos]):
  
  with open(sys.argv[pos], newline='') as myFile:  
    reader = csv.DictReader(myFile, delimiter=':')

    #checks if given case insensitive arguments(field) are valid, appends for our header 

    # taking intersection between the user's input and the offical header was another idea I want to consider
 
    Heading = []
    for i in range(pos+1,len(sys.argv)):

      if sys.argv[i].upper() in reader.fieldnames:
       
       Heading.append(sys.argv[i].upper())
    
         
    
  
  
  #prints out header only if user uses -l shortcut
    if sys.argv[1] == '-l':
     print(' '.join(map(str, Heading)))

  #prints out columns that user wa
    for row in reader:
      print(' '.join([row[i] for i in Heading]))
    

else:
  print("Invalid File")





