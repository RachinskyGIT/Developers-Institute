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
console.log(mary_index);

peoples_copy = people.slice(); // or peoples_copy = [...people];
console.log(`peoples_copy: ${peoples_copy}`);

console.log(`Foo's index: ${people.indexOf("Foo")}`);
