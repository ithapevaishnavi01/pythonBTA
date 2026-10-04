public class day11_1 {
    public static void main(String[] args) {
        
        //function in java

        greet();

        sayhello("Vaishnavi");

        int x =getno();
        System.out.println(x);

        int y = mul(10,20);
        System.out.println(y);

    }

    //no inout and no output
    static void greet() {
        System.out.println("Hello");
        return;
    }
    //iput and no output
    static void sayhello(String name){
        System.out.println("Hello " + name);
        return;
    }

    //no input and output
    static int getno(){
        return 10;
    }
       
    //input and output
    static int mul(int a, int b){
        return a*b;
    }

}
