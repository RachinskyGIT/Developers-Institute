// ex2
const winBattle = () => {
    return true;
    };
let experiencePoints;
winBattle() ? experiencePoints = 10 : experiencePoints = 1;

console.log (experiencePoints)

// ex3
const isString = (input) => {
    return (typeof input === 'string');
    };

console.log (isString(3))    

// ex4 + ex5
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];
let suffix;
colors.forEach((element, idx) => { 
    idx === 0 ? suffix = ordinal[1] : idx === 1 ? suffix = ordinal[2] : idx === 2 ? suffix = ordinal[3] : suffix = ordinal[0];
    console.log(`#${idx+1}${suffix} is ${element}`)
}); 


// ex6
let bankAmount = 1000; // Initial bank amount
const VAT = 0.17; // VAT percentage
const details = ["+200", "-100", "+146", "+167", "-2900"]; // Monthly expenses array
// Calculate and modify the expenses to include VAT
details.forEach((element) => {
  const expense = parseFloat(details[element]); // Parse the expense value as a float
  const modifiedExpense = expense + (expense * VAT); // Calculate the expense with VAT
  details[element] = modifiedExpense.toFixed(2); // Update the array element with the modified expense
});
// Calculate the total bank amount at the end of the month
for (const expense of details) {
  bankAmount += parseFloat(expense);
}
console.log("Bank Amount: $" + bankAmount.toFixed(2)); // Display the final bank amount
