class Student {
    constructor({ first_name = '', last_name = '', major = '', gpa = 0, description = '' }) {
        this.first_name = first_name;
        this.last_name = last_name;
        this.major = major;
        this.gpa = gpa;
        this.description = description;
    }

    // Get methods for the Student class
    getFirstName() {
        return this.first_name;
    }

    getLastName() {
        return this.last_name;
    }

}

class StudentBuilder {
    // takes in no arguments, but creates a new Student object with default values
    constructor() {
        this.student = new Student({});
    }

    // Method to set the name of the student
    setFirstName(first_name) {
        this.student.first_name = first_name;
        return this;
    }

    // Method to set the last name of the student
    setLastName(last_name) {
        this.student.last_name = last_name;
        return this;
    }

    // Method to return the student object
    build() {
        return this.student;
    }
}

function writeStudentProfilePicture(fullName) {
    // create a new img element
    const img = document.createElement("img");
    // set the src attribute of the img element
    img.src = "./imgs/" + fullName + ".jpeg";
    // set the alt attribute of the img element
    img.alt = fullName;
    // set the class attribute of the img element
    img.className = "profile-picture";

    // return the img element to be appended to the DOM
    return img;
}

function writeStudentHeader(first_name, last_name) {
    // create a new h1 element
    const h1 = document.createElement("h1");
    // set the text content of the h1 element
    h1.textContent = first_name + " " + last_name;

    // return the h1 element to be appended to the DOM
    return h1;
}

function writeStudentProfile(description) {

    // create a new div element
    const div = document.createElement("div");
    // set the class attribute of the div element
    div.className = "student-profile";

    // create a new p element
    const p = document.createElement("p");
    // set the text content of the p element
    p.textContent = description;

    // append p elements to the div element
    div.appendChild(p);

    // return the div element
    return div;
}

function buildPage() {

    // create a new student builder object
    const studentBuilder = new StudentBuilder();

    // populate the student builder object with the student's information
    studentBuilder
        .setFirstName("Douglas")
        .setLastName("Thain")
        .setMajor("Computer Science")
        .setGPA(4.0)
        .setDescription("Douglas is a professor at Notre Dame, where he teaches courses in computer science. He loves writing stellar books on Compiler Construction.")

    // build the student object
    const student = studentBuilder.build();

    // write the student to the DOM
    document.body.appendChild(writeStudent(student));
}

window.onload = buildPage;