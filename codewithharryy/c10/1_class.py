class emp:
   
    language="python"   #class atribute
    salary=100000

harry = emp()
harry.name = "harry"       #obj attribute or instance attribute
print(harry.language,harry.salary,harry.name)

rohan = emp()
rohan.name = "RR"             #obj attribute or instance attribute
print(rohan.name,rohan.salary,rohan.language)

# here name is obj attribute and ,sal and language are class atribute as it directly belong to the class 