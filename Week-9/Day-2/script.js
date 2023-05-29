function testNum(number) {
    return new Promise((resolve, reject) => {
      if (number < 10) {
        resolve('number is less than 10, success!!!');
      } else {
        reject('number is greater or equal to 10, error!!!');
      }
    });
  }
  
  // Example usage
  testNum(5)
    .then((result) => {
      console.log(result); // Output: number is less than 10, success!!!
    })
    .catch((error) => {
      console.log(error); // This will not be executed for the given example
    });
  
  testNum(15)
    .then((result) => {
      console.log(result); // This will not be executed for the given example
    })
    .catch((error) => {
      console.log(error); // Output: number is greater or equal to 10, error!!!
    });
  