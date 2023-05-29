// ex1
const compareToTen = (num) => {

const comparing = new Promise((resolve, reject) => {
  console.log("I'm comparing!");
  //let's say compareToTen() takes a few seconds
  console.log("The number is", num);
  if(num<10) {
    resolve();
  } else {
    reject();
  }
})
.then(() => {
  console.log("I have compared, this is good number")
})
.catch(() => {
    console.log("The number is not less that 10, very bad!")//use `.catch()` to do something after `reject()` has been called
  })
  .finally(() => {
    console.log("I finished my work")//use `.finally()` to do something either way
  })
};

// compareToTen(11)


// // ex2
// const myPromise = new Promise((resolve, reject) => {
//     setTimeout(() => {
//       resolve("success");
//     }, 4000);
//   });
  
//   myPromise
//     .then((result) => {
//       console.log(result);
//     })
//     .catch((error) => {
//       console.log('Ooops something went wrong');
//     });

    
// ex3
const promise1 = Promise.resolve(3);

const promise2 = Promise.reject("Boo!");

promise1.then(value => {
  console.log("Resolved:", value);
}).catch(error => {
  console.error("Error:", error);
});

promise2.then(value => {
  console.log("Resolved:", value);
}).catch(error => {
  console.error("Error:", error);
});
