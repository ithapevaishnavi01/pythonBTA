public class datatype {
    public static void main(String[] args) {
        // byte b = 5;
        //byte b = 0b101;      //for  binary no we put 0b and then the binary number of that number
                                // menas 5=101 for printing 5 we write 0b101    
        
        //byte b = 05;            //octal no representation
        byte b = 0x5;            //hexadecimal representation
                                
        short s = 20;
        int i = 2000;
        long l = 300__000;

        float f = 15.0f;
        //double d=56.659;
        double d =6.022e23;  //6.022 * 10^23


        char c = 'A';

        boolean bul = true ;


        System.out.println(+b +"," +s +"," +i +"," +l +"," +f +"," +d +"," +c +"," +bul);
    }
}
