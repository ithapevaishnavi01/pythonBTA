public class day13_3 {

    public static void main(String[] args) {

        student s1 = new student();

        System.out.println(s1.name);
        System.out.println(s1.age);
        System.out.println(s1.rollno);
    }
}

class student {

    String name;
    int age;
    int rollno;

    student() {
        this("null");
        
        System.out.println("1st");
    }

    student(String name) {
        this(name, 0);
        System.out.println("2nd");
    }

    student(String name, int age) {
        this(name, age, 0);
        System.out.println("3rd");  
    }

    student(String name, int age, int rollno) {
        this.name = name;
        this.age = age;
        this.rollno = rollno;
        System.out.println("4th");
    }
}