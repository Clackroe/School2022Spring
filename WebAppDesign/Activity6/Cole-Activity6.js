


window.onload = pressed()

function pressed(){
        let gradeNum = -100
        let letterGrade;
    
        while(gradeNum != -1){
            gradeNum = prompt("What is your grade? (Enter a number 0-120 | or enter -1 to end)");

            if(gradeNum == -1 || gradeNum == null || gradeNum == "")
                break;

            if (gradeNum > 120 || gradeNum < 0){
                pressed();
                break;
            }
            
            letterGrade = findLetterGrade(gradeNum);

            alert("With a number grade of: " + gradeNum + "\nYour Letter Grade is: " + letterGrade)
           
            
            
        }


    }

function findLetterGrade(num){
    let letterGrade;
    if (num < 60)
        letterGrade = "F";
    else if (num <= 69)
        letterGrade = "D";
    else if (num <= 79)
        letterGrade = "C";
    else if (num <= 99)
        letterGrade = "B";
    else if (num <= 120)
        letterGrade = "A";
    else
        letterGrade = "N/A"
    
    return letterGrade
}
