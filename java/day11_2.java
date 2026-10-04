public class day11_2 {

    public static void main(String[] args) {

        //function overloading
        int x=add(10,20);
        System.out.println(x);

        int y=add(10,20,30);
        System.out.println(y);

        greet(20,"Vaishnavi");
        greet("Vaishnavi",20);

}

         static int add(int a, int b){
             return a+b;
        }   

        static int add(int a, int b, int c){ //dif no on paramethers
            return a+b+c;    
        }

        static int add(double a, double b){. //diff type of parameters
            return (int)(a+b);
        }

        static void greet(int age,String name){ //diff type of parameters
            System.out.println("Hello " + name + " your age is " + age);
        }

        static void greet(String name, int age){ //diff type of parameters
            System.out.println("Hello " + name + " your age is " + age);
        }
}
