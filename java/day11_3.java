public class day11_3 {
    public static void main(String[] args){
        //Chaining of functions

        fun1();
        System.out.println("Bye");
    }

    static void fun1(){
        fun2();
        System.out.println("HI");
        
    }

    static void fun2(){
        fun3();
        System.out.println("Hello");
        
    }
    static void fun3(){
        System.out.println("HRU");
    }
}

