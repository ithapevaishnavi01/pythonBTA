public class day5 {
    public static void main(String[] args) {
   
    int i =12;

    //selection statemnet
            //normal if
            // if(i == 4) {
            //     System.out.println("its ture");
            
            // }
            // System.out.println("done");
            // }



             //if-else 
            //  if(i == 4) {
            //     System.out.println("i is 5 ");
            
            // }
            // else
            //     {
            //         System.out.println("i is not 5");
            //     }
 


            //nested if
            if (i>5){
                if(i<10){
                    System.out.println("less than 10");
                }
                else{
                    System.out.println("greater than 10");
                }
            }else{  
                System.out.println("less than 5");

            }

            // if (i > 5 && i <10){} .... doing this is better than  nasted .. there are lots of confusion in nasted
            
            
            //if-elseif ladder
            if(i == 5){
                System.out.println("i is 5");
            }
            else if (i == 4) {
                System.out.println("i is 4");
            }
             else if (i == 3) {
                System.out.println("i is 3");
            }
              else if (i == 12) {
                System.out.println("i is 12");
            }

         }
}
