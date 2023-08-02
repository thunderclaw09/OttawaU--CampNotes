console.log("Hello");
function display(val)
{
    document.getElementById("result").value += val;
}

function myFunction(event) // This just changes the textbox when we press a button.
{
    if(
        event.key == '0' || event.key == '1' || 
        event.key == '2' || event.key == '3' || 
        event.key == '4' || event.key == '5' || 
        event.key == '6' || event.key == '7' || 
        event.key == '8' || event.key == '9' ||
        event.key == '+' || event.key == '=' || 
        event.key == '.' || event.key == '*' ||
        event.key == '/' || event.key == '-')
        {
            document.getElementById("result").value += event.key;
            console.log(event.key);
        }
    
}

var calc = document.getElementById("calculator");
calc.onkeyup = function(event){
    if (event.keyCode === 13) // The code of enter 
    {
        console.log("Enter");
        let resultValue = document.getElementById("result").value;
        solve();
    }
}

function solve() // This is the equivalent of the equals sign.
{
    let resultValue = document.getElementById("result").value;
    clr();
    let mathResult = evaluate(resultValue);
    console.log("mathResult:", mathResult);
    //let mathResult = math.evaluate(resultValue); // This is where it can fail should it be a weird equation.
  
    document.getElementById("result").value = mathResult; // Changes the field to be the answer
}

function evaluate(result)
{
    return eval(result);
    /*
    var equation = result.split("");
    console.log(equation);

    var a = 0;
    var b = 0;

    var answer = 0;

    while (true)
    {
        if (equation.includes("*"))
        {
            console.log("Notices the *");
            var index = equation.findIndex("*");
            console.log(index);
            

            a = parseInt(equation[index - 1]);
            b = parseInt(equatoin[index + 1]);

            answer = a*b
            equation[index] = answer

            equation[index - 1] = "";
            equation[index + 1] = "";

            console.log(answer)


        }else{
            console.log("done.")
            return answer;
        }
    } */
}

function clr() // This clears the field.
{
    document.getElementById("result").value = "";
    console.log("cleared");
}

function cls()
{
    clr();
}