public class type_promotion {
    public static void main(String[] args) {
        byte b = 47;
        char c = 'a';
        short s = 1211;
        int i = 2355;
        float f = 23.536f;
        double d = .124;

        double result = (f*b) + (i/c) - (d*s);

        System.err.println(result);
    }
}
