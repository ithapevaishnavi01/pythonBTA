public class day9_2 {
    
    public static void main(String[] args) {

        int [] [] marks = new int [3][];
        marks[0] = new int[3];
        marks[1] = new int[2];
        marks[2] = new int[4];

        marks[0][0] = 10;
        marks[0][1] = 20;
        marks[0][2] = 30;  

        marks[1][0] = 40;
        marks[1][1] = 50;

        marks[2][0] = 60;
        marks[2][1] = 70;
        marks[2][2] = 80;
        marks[2][3] = 90;   

        for(int row=0;row<marks.length;row++){
            for(int col=0;col < marks[row].length;col++){
                System.out.print(marks[row][col]+ " ");
            }
            System.out.println();
        }
}
}
