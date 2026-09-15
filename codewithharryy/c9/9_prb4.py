word = "donkey "

with open("dfile.txt", "r") as f :
    content = f.read()

contentnew = content.replace(word , "######")

with open("dfile.txt", "w") as f :
    content = f.write(contentnew)  

f.close()