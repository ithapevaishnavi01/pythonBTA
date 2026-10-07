public class day13_1 {
    public static void main(String[] args){
      
        Student s1 = new Student();
        
        System.out.println(s1.name);
        System.out.println(s1.age);
        System.out.println(s1.rollno);
        System.out.println(s1.clg); 


        /*
        int = 0
        String = null
        float = 0.0
        boolean = false
        */


    }


}


class Student{          //--> instance variables --> state of the object
    String name;
    int age;
    int rollno;
    String clg;

    void markAttendance(){      //bevaior --> funcations ----> instance methods
        System.out.println("Attendance marked for " + name);
    }
    
}
