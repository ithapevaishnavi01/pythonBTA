class emp:
   
    language="python"  
    salary=100000

harry = emp()
harry.language = "js"           #instance attribute takes preferance over class attribute dusring assignmant or retrieval
print(harry.language,harry.salary)



