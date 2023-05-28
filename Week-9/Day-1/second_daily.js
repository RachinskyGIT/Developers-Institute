function allTruthy(...values) {
    return values.every((value) => Boolean(value));
  }
  

  console.log(allTruthy(true, true, true)); // Output: true
  console.log(allTruthy(true, false, true)); // Output: false
  console.log(allTruthy(5, 4, 3, 2, 1, 0)); // Output: false
  