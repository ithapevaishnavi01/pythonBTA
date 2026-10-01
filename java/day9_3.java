public class day9_3 {
    
    public static void main(String[] args) {
  

        // 2D array in java
        
        int  [] [] marks= {
            {10,20,30},
            {40,50},
            {60,70,80,90}
        };

        for(int i =0 ; i < marks.length;i++){
           for(int j = 0 ; j < marks[i].length;j++){
            System.out.print(marks[i][j]+ " ");

           }System.out.println();
        }


}}
