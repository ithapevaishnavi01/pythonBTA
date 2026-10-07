public class day13_2 {

    public static void main(String[] args) {

        student s1 = new student("vaishnavi", 20);

        System.out.println(s1.name);
        System.out.println(s1.age);

        student s2 = new student();
    }
}

class student {

    String name;
    int age;

    student(String n, int a) {

        this.name = n;
        age = a;
    }

    student() {
        System.out.println("Default constructor called");
    }
}