public class day15 {
    public static void main(String[] args) {
        bankaccount ba = new bankaccount();
        ba.balance = 150000.2;

        System.out.println(ba.balance); 
    }
}

class bankaccount{
    private double balance;

    public void depsite(int amount){
        balance += amount ;
    }
     public void withdrow(int amount){
        balance -= amount ;
    }

    //geters and setters
    public void getbalance(){
        System.out.println(balance);
    } 
}

class student{
    private String name;
    private int age;    


    student(String name, int age){
        this.name = name;
        this.age = age;
    }

    public String getname(){
        return name;    
    }
    public void setname(String name){
        this.name = name;
    }
}
 