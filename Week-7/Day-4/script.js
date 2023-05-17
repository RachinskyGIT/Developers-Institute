function myAge(){

    var myAge = document.getElementById("ageInput").valueAsNumber;

    mom = myAge*2
    dad = mom*1.2
    console.log(`my age: ${myAge}`);
    console.log(`mom age: ${mom}`);
    console.log(`dad age: ${dad}`);

    var resultContainer = document.getElementById("resultContainer");
    resultContainer.innerHTML = "My age is: " + myAge + "<br>" + "My mum's age is: " + mom + "<br>" + "My dad's age is: " + dad;
}


