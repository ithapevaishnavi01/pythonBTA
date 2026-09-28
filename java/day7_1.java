public class day7_1 {
    public static void main(String[] args) {


        // infinite loop in while
        
        // int i = 5;
        // while(i < 10){
        // }
        // System.out.println(i);

        //infinite loop in for
        //comma sepration int  i=1 , j; i<10 ;i ++),j++V)

        // for (int  i=1 ; i<10 ;i ++){        //remove i it will. become infinite loop
        //     System.out.println("hello");
        // }



        for (int  i=1 ; i<=5;i ++){        
            for(int j=1;j<=i;j++){
                System.out.print("*");
            }
            System.err.println();
    }
}
}