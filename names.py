file = open("Names.txt","w")
file.write("James\n")
file.write("Susan\n")
file.write("Job\n")
file.write("Steve\n")
file.write("Jota\n")

file = open("Names.txt","a")
newname = input("Enter new name: ")
file.write(newname + "\n")

file = open("Names.txt","r")
print(file.read())
file.close