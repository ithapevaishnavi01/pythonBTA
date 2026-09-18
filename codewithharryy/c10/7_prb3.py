class Demo :
    a=4

k=Demo()
print(k.a)    #print classs attribute because instance attribute are not present
k.a=0        #insrtance atttrinute is set 

print(k.a)   # print instance attribute

print(Demo.a)   #prints the class attribute
