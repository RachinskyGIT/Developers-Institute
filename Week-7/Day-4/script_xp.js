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


// ex1

function displayNumbersDivisible(div=23){ 
    var a = '';
    var sum = 0;
    for (var i = 1; i <= 500; i++) {
        if (i % div === 0) {
            a = a + i + " ";
            sum += i;
        }
    }
    console.log (a);
    console.log (sum);
}

displayNumbersDivisible(25);


// ex2
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

var shoppingList = {
    "banana": 1, 
    "orange": 1,
    "apple": 1 
}

function myBill(){
    sum = 0;
    for (var item in shoppingList){
        shoppingList_item_number = shoppingList[item];
        item_price = prices[item];
        if (stock[item] >= shoppingList_item_number){
                sum += (shoppingList_item_number * item_price);
                stock[item] -=1
        }
    }
    console.log(sum)
}

myBill()


// ex3
function changeEnough(itemPrice, amountOfChange) {
    sum = (amountOfChange[0]*0.25 + amountOfChange[1]*0.10 + amountOfChange[2]*0.05 + amountOfChange[3]*0.01);
    return (sum > itemPrice)
}

console.log(changeEnough(4.25, [0, 0, 5, 10]))


// ex4
function hotelCost() {
    var cost = 140
    var numberOfNights;
    while (true) {
        var input = prompt("How many nights would you like to stay in the hotel?");
        numberOfNights = parseInt(input);
        if (!isNaN(numberOfNights)) {
            break;
        }
        console.log("Invalid input. Please enter a valid number of nights.");
    }
    return cost*numberOfNights;
}

// hotelCost()

function  planeRideCost(){
    var destination;
    while (true){
        var input = prompt("What's your destination?");
        if (typeof input === 'string' && input.trim() !== '') { // input.trim() !== '' is used to ensure that the input is not an empty string after removing leading and trailing whitespace.
            destination = input;
            break;
        }
        console.log("Invalid input. Please enter a valid string");
    }
    var sum = 300;
    if (destination.toLowerCase() == "london") {sum = 183}
    else if (destination.toLowerCase() == "paris") {sum = 220}
    return sum;
}

// console.log(planeRideCost())


function rentalCarCost(){
    var cost = 40
    var discount = 0.05
    var numberOfDays;
    while (true) {
        var input = prompt("How many days would you like to rent the car?");
        numberOfDays = parseInt(input);
        if (!isNaN(numberOfDays)) {
            break;
        }
        console.log("Invalid input. Please enter a valid number of days.");
    }
    if (numberOfDays>10) {
        cost -= cost*discount
    }
    return cost*numberOfDays;
}

// console.log(rentalCarCost())


function totalVacationCost(){
    sum = (hotelCost() + planeRideCost() + rentalCarCost());
    return sum;
}



console.log(totalVacationCost());