def inch_to_centi(inch):
    return   inch*2.54

n = int (input("enter value in inch: "))

print(f"the value in cms is {inch_to_centi(n)}")