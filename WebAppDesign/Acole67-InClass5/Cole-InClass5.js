
const $ = selector => document.querySelector(selector);

document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll('.btnn').forEach(item =>{
        item.addEventListener('click', dispatchEvent)})
    })
    document.querySelectorAll('#action').forEach(item =>{
        item.addEventListener('click', dispatchEvent)})


//Global variables
var prevCalc = 0;
var calc = "";
var calculated = false;


function dispatchEvent(event) {
    console.log("Test");
    let eid = event.target.value;
    
    if(eid == "+"){
        console.log("Test");
        add();
    }
    else if (eid == "-"){
        subtract();
    }
    else if (eid == "*"){
        multiply();
    }
    else if (eid == "/"){
        divide();
    }
    else if (eid == "^"){
        pow();

    }
    else if (eid == "^2"){
        pow2();
    }
    else if(eid == "--"){
        decrement();
    }
    else if(eid == "++"){
        increment();
    }
    else if(eid == "sqrt()"){
        sqroot();
    }
    else if(eid == "Floor"){
        floor();
    }
    else if(eid == "Round"){
        round();
    }
    else if(eid == "Clear"){
        clearText();
    }
    else if(eid == "Calculate"){
        calculate();
    }
    else if(parseInt(eid) >= 0 && parseInt(eid) <= 9){
        showNum(eid);
    }
}








//The following function displays a number in the textfield when a number is clicked.
//Note that it keeps concatenating numbers which are clicked. 
function showNum(value) {
    console.log("Test")
    if(calculated){
        clearText()
        calculated = false
     document.frmCalc.txtNumber.value += value;
    }
    else{
        document.frmCalc.txtNumber.value += value;
    }
}

//The following function decreases the value of displayed number by 1.
//isNaN method checks whether the value passed to the method is a number or not.     
function decrement() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            num--;
            document.frmCalc.txtNumber.value = num;
            calculated = true;
        }
}
function increment() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
    if (!(isNaN(num))) {
        num++;
        document.frmCalc.txtNumber.value = num;
        calculated = true;
    }
}

function pow2() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
    if (!(isNaN(num))) {
        num = num ** 2;
        document.frmCalc.txtNumber.value = num;
    }
}

function round() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
    if (!(isNaN(num))) {
        num = Math.round(num);
        document.frmCalc.txtNumber.value = num;
    }
}

function sqroot() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
    if (!(isNaN(num))) {
        num = Math.sqrt(num);
        document.frmCalc.txtNumber.value = num;
    }
}

function floor() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
    if (!(isNaN(num))) {
        num = Math.floor(num);
        document.frmCalc.txtNumber.value = num;
    }
}

//The following function is called when "Add" button is clicked. 
//Note that it also changes the values of the global variables.       
function add() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            prevCalc = num;
            calculated = false
            document.frmCalc.txtNumber.value = "";
            calc = "Add";
        }
}

function pow() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            prevCalc = num;
            calculated = false
            document.frmCalc.txtNumber.value = "";
            calc = "Pow";
        }
}

function subtract() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            prevCalc = num;
            calculated = false
            document.frmCalc.txtNumber.value = "";
            calc = "Sub";
        }
}
function multiply(){
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            prevCalc = num;
            calculated = false
            document.frmCalc.txtNumber.value = "";
            calc = "Mult";
        }
}

function divide(){
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            prevCalc = num;
            calculated = false
            document.frmCalc.txtNumber.value = "";
            calc = "Div";
        }
}



function sqrt() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            num = Math.sqrt(num);
            document.frmCalc.txtNumber.value = num;
        }
}

//The following function is called when "Calculate" button is clicked.
//Note that this function is dependent on the value of global variable.        
function calculate() {
    var num = parseFloat(document.frmCalc.txtNumber.value);
        if (!(isNaN(num))) {
            if (calc == "Add"){
                var total = prevCalc + num;
                document.frmCalc.txtNumber.value = total;
            }
            else if (calc == "Sub"){
                var total = prevCalc - num;
                document.frmCalc.txtNumber.value = total;
            }
            else if (calc == "Div"){
                var total = prevCalc / num;
                document.frmCalc.txtNumber.value = total;
            }
            else if (calc == "Mult"){
                var total = prevCalc * num;
                document.frmCalc.txtNumber.value = total;
            }
            else if (calc == "Pow"){
                var total = prevCalc ** num;
                document.frmCalc.txtNumber.value = total;
            }
        calculated = true;
    
        
}}

function clearText() {
	document.frmCalc.txtNumber.value = "";
	prevCalc = 0;
	calc = "";
}