public class neg_no_store {
    public static void main(String[] args) {
        // float f = 8.125f;
        // System.err.printf("%.20f%n",f);

        //implicit conversion
        //byte to int
        // byte b =10;
        // int i;
        // i=b;
        // System.err.println(i);

        //explicit conversion
        // int i = 300;
        // byte b ;
        // b=(byte)i; //when we write b=i it give error , we have to write using casting (b=(byte)i)
        // System.out.println(b);  //or 300 % 256 = 44

        //truncating conversion
        // float f = 15.765f;
        // int i ;
        // i=(int)f;   ///error when write i=f , have to do casting
        // System.out.println(i);

        byte b = 50;;
        b = (byte) (b*2);
        System.out.println(b);
    }
}
