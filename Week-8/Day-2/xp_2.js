// // ex1
// const sum = (num1, num2) => num1 + num2;
// console.log(sum(3,5))

// // ex2
// // Function Declaration
// function convertToGrams1(weightInKg) {
//     return weightInKg * 1000;
//   }
  
//   convertToGrams1(2); // Invoking the Function Declaration
//   console.log(convertToGrams1(2))


//   // Function Expression
//   const convertToGrams2 = function(weightInKg) {
//     return weightInKg * 1000;
//   };
  
//   convertToGrams2(2); // Invoking the Function Expression
//   console.log(convertToGrams2(2))


//   // Difference between Function Declaration and Function Expression:
//   // Function declarations are hoisted, meaning they can be called before they are defined in the code. Function expressions, on the other hand, cannot be hoisted and must be defined before they are called.
  
//   // One line Arrow Function
//   const convertToGrams3 = weightInKg => weightInKg * 1000;
  
//   convertToGrams3(2); // Invoking the Arrow Function
//   console.log(convertToGrams3(2))

// // ex3
// (function(numberOfChildren, partnerName, location, jobTitle) {
//     const sentence = `You will be a ${jobTitle} in ${location}, and married to ${partnerName} with ${numberOfChildren} kids.`;
//     document.getElementById("fortune").textContent = sentence;
//   })(2, "John", "New York", "Software Engineer");
  
// // ex4
// (function(name) {
//     var userProfileDiv = document.createElement('div');
//     userProfileDiv.classList.add('navbar-text', 'text-white');
//     userProfileDiv.innerHTML = `
//       <span class="mr-2">Welcome, ${name}</span>
//       <img src="path_to_profile_picture.jpg" alt="Profile Picture" class="rounded-circle" width="30" height="30">
//     `;
    
//     var navbarNav = document.querySelector('.navbar-nav');
//     navbarNav.appendChild(userProfileDiv);
//   })('John');

// ex5
  function makeJuice(size) {
    const ingredients = [];
  
    function addIngredients(ingredient1, ingredient2, ingredient3) {
      ingredients.push(ingredient1, ingredient2, ingredient3);
    }
  
    function displayJuice() {
      const juiceDetails = `The client wants a ${size} juice, containing ${ingredients.join(", ")}.`;
      document.getElementById("juice-details").textContent = juiceDetails;
    }
  
    addIngredients("apple", "banana", "orange");
    addIngredients("strawberry", "pineapple", "mango");
    displayJuice();
  }
  
  makeJuice("medium");
  