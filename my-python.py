import csv
file = open("Books.csv","w")
newRecord = "To kill a mockingbird,Haper Lee,1960\n"
file.write(str(newRecord))
newRecord = "A Brief History of Time,Stephen Hawkings,1968\n"
file.write(str(newRecord))
file.close()