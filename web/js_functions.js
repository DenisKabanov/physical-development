async function take_values (){
    let last_name = document.getElementById("last_name").value;
    let first_name = document.getElementById("first_name").value;
    let dad_name = document.getElementById("dad_name").value;
    let dob = document.getElementById("dob").value;
    let doi = document.getElementById("doi").value;
    //let gender = document.getElementByName("gender").value;
    const result = await eel.convert_value_py(last_name, first_name, dad_name, dob, doi)();
    document.getElementById("output").value = result;
    }
document.getElementById("submit").onclick = take_values;

