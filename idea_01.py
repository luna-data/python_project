#난이도 하: 학생(Student) 클래스를 작성하고 객체를 생성해보기
class Student {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

const student1 = new Student("Alice", 20);
console.log(student1);

# 난이도 중: 사각형(Rectangle) 클래스를 만들어 넓이를 구하는 메서드 추가하기
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    getArea() {
        return this.width * this.height;
    }
}

const rect = new Rectangle(4, 5);
console.log(rect.getArea());

# 난이도 상: 동물(Animal)을 상속받는 강아지(Dog) 클래스를 만들고, 메서드 오버라이딩하기
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a sound.`);
    }
}

class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks.`);
    }
}

const dog1 = new Dog("Buddy");
dog1.speak();

# 난이도 최상: 추상 클래스 개념을 활용한 도형(Shape) 클래스와 다형성 구현하기
# 여러 도형 클래스(Circle, Rectangle)를 만들고, 공통 인터페이스를 통해 다형성 구현
class Shape {
    constructor(name) {
        this.name = name;
    }

    // 추상 메서드 개념 (자식 클래스에서 반드시 구현해야 함)
    getArea() {
        throw new Error("getArea() must be implemented by subclass");
    }

    getPerimeter() {
        throw new Error("getPerimeter() must be implemented by subclass");
    }

    displayInfo() {
        console.log(`${this.name} - Area: ${this.getArea()}, Perimeter: ${this.getPerimeter()}`);
    }
}

class Circle extends Shape {
    constructor(radius) {
        super("Circle");
        this.radius = radius;
    }

    getArea() {
        return Math.PI * this.radius * this.radius;
    }

    getPerimeter() {
        return 2 * Math.PI * this.radius;
    }
}

class Rectangle extends Shape {
    constructor(width, height) {
        super("Rectangle");
        this.width = width;
        this.height = height;
    }

    getArea() {
        return this.width * this.height;
    }

    getPerimeter() {
        return 2 * (this.width + this.height);
    }
}

# 다형성 활용: 다양한 도형 객체를 배열에 담아서 처리
const shapes = [
    new Circle(5),
    new Rectangle(4, 6),
    new Circle(3)
];

# 모든 도형의 정보를 출력
shapes.forEach(shape => shape.displayInfo());