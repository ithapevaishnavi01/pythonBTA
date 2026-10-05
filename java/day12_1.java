public class day12_1 {
    
    public static void main(String[] args){
        Student s1 = new Student();
        s1.name = "John";
        s1.age = 20;
        s1.rollno = 101;
        s1.markAttendance();
        s1.print();
}
}

class Student{
    String name;
    int age;
    int rollno;

    void markAttendance(){
        System.out.println("Attendance marked for " + name);
    }
    
    void print(){
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Roll No: " + rollno);   
    }
}

