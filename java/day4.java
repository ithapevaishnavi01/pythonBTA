public class day4 {
    public static void main(String[] args) {
        //bitwise op
        int a = 2;  // 00000000 00000000 00000000 00000010
        int b =3;  // 00000000 00000000 00000000 00000011
        int c = a & b;  // 10  // 2
        int d = a | b ;  //  11 //3
        int e = ~a;  // 11111111 11111111 11111111 11111101  //-3
        int f = a ^ b;  //01 //1


        System.out.println(+c + "," +d +"," +e +"," +f);


        //shift op  

        //left shift << , <<<
        int g =1;
        g = g << 30; //g << 33 == g << 1
        System.out.println(g);

        //right shift (>>) and (>>>)
        byte h = 12;
        h= (byte)(h >> 3);
        System.out.println(h);
    }
}
