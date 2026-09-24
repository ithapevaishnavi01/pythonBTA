public class operators {
    public static void main(String[] args) {
        //operators in java
        //arithmatic operators
        int a = 5;
        int b = 10;
        int c=a+b;    // - , * , / , % , += , -= , *= , /= , %= , ++ , --
        
        System.out.println(c);


        int d = 6;
        d ++;  //increment by 1
        System.out.println(d);

        //pre increment and post increment / decrement
        int e = 6;
        e++;   //postfix
        ++e;  //prefix
       

        int f = e++; //here e=9 and f=8
        // int f = ++e; //here e=9 and f=9
        System.out.println(e + "," + f);


    }
}
