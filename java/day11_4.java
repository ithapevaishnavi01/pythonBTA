public class day11_4 {

    static int n = 10; //global scope variable
    public static void main(String[] args){
        //Scope of variables. 

        int x=4;
        int y=5;

       System.out.println(x);
       System.out.println(y);
       
       fun();


    }
    static void fun(){
        // system.out.println(x); //x is not accessible here as it is local variable of main function
        System.out.println(n); //n is accessible here as it is global variable

    }
}
