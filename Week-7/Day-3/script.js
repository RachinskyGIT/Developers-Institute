
// ex1
const people = ["Greg", "Mary", "Devon", "James"];

const index = people.indexOf("Greg");

if (index !== -1) {
  people.splice(index, 1);
}

console.log(`people values: ${people}`);

const index_james = people.indexOf("James");
index_james !== -1 ? people[index_james] = "Jason" : null;

console.log(`people values: ${people}`);

mary_index = people.indexOf("Mary");
console.log(`Mary's index: ${mary_index}`);

peoples_copy = people.slice(); // or peoples_copy = [...people];
console.log(`peoples_copy: ${peoples_copy}`);

console.log(`Foo's index: ${people.indexOf("Foo")}`);

last_man = people.slice(-1)
console.log(`peoples last element: ${last_man}`);

for (var i = 0; i < people.length; i++) {
  console.log(`people's element №${i+1}: ${people[i]}`);
}
console.log('##########################')


for (var i = 0; i < people.length; i++) {
  if (people[i] == 'Devon'){
    console.log(`fuck Devon`);
    break
  }
  console.log(`good people's element №${i+1}: ${people[i]}`);
}

// // ex3

// // Gets user input
// var name = prompt("What is your name?");
// var num = prompt("What is your favorite number? ");

// // Uses user input to print out information
// println("Hello " + name + "!");
// println(num + "?! That's my favorite number too!");

// // Prints out the variable type
// println("Name is a " + typeof name);
// println("Num is a " + typeof num);

// ex4
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
      firstFloor: 3,
      secondFloor: 4,
      thirdFloor: 9,
      fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent:  {
      sarah: [3, 990],
      dan:  [4, 1000],
      david: [1, 500],
  },
}

console.log(`number of floors: ${building.numberOfFloors}`)

for (var i = 1; i <= building.numberOfFloors; i++) {
  if (i === 1 || i === 3) {
    var floorName = i === 1 ? "first" : "third";
    console.log(`number of appts on ${i}'th floor: ${building.numberOfAptByFloor[`${floorName}Floor`]}`);
  }
}

second_tenant = building.nameOfTenants[1];
console.log(`${building.nameOfTenants[1]}`);
console.log(`Number of ${second_tenant}'s rooms: ${building.numberOfRoomsAndRent[second_tenant.toLowerCase()][0]}`);


if (building.numberOfRoomsAndRent["sarah"][1] > building.numberOfRoomsAndRent["dan"][1] || 
    building.numberOfRoomsAndRent["david"][1] > building.numberOfRoomsAndRent["dan"][1]) {
  building.numberOfRoomsAndRent["dan"][1] = 1200
  console.log(`Congratulations Dan! Now your rent amount has been negatively reduced! Your new rental amount: 1200`);
} else {
  console.log(`Live today, bastard. Next time I'll raise your rent.`);
}

// ex5

let family = {
  father: "John",
  mother: "Mary",
  children: ["Alex", "Emily"],
  pets: {
    dog: "Buddy",
    cat: "Whiskers"
  },
  location: "New York"
};

console.log(family);

// Iterate over the keys
console.log('Iterate over the keys:');
for (let key in family) {
  console.log(key);
}

// Iterate over the values
console.log('Iterate over the values:');
for (let key in family) {
  console.log(family[key]);
}

// ex6
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

// output: my name is Rudolf the raindeer
console.log(`${Object.keys(details)[0]} ${details.my} ${Object.keys(details)[1]} ${details.is} ${Object.keys(details)[2]} ${details.the}`)


// ex7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
const societyName = names
  .map(name => name[0]) // Extract the first letter of each name
  .sort() // Sort the letters in alphabetical order
  .join(""); // Convert the sorted letters back to a string
  
console.log(societyName);