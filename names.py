file = open("Names.txt","w")
file.write("James\n")
file.write("Susan\n")
file.write("Job\n")
file.write("Steve\n")
file.write("Jota\n")

file = open("Names.txt","r")
print(file.read())