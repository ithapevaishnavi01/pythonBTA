def main():
    try:
        a= int (input("enter a no :"))
        print(a)
        return


    except Exception as e:
        print(e)    
        return                   

    finally:                                        #execute without return in funation and everywhere
        print("i am inside finally")

main()