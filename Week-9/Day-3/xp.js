// xp1
const apiUrl = "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error("Request failed with status: " + response.status);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("Error:", error);
  });


// xp2
const apiUrl2 = "https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=10&offset=2";

// xp3
async function fetchData() {
    try {
      const response = await fetch("https://www.swapi.tech/api/starships/9/");
      if (!response.ok) {
        throw new Error("Request failed with status: " + response.status);
      }
      const data = await response.json();
      console.log(data.result);
    } catch (error) {
      console.error("Error:", error);
    }
  }
  
  fetchData();
  


// xp4
function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();

// Outcome:
// When the code is executed, the following will be the outcome:

// 'calling' will be logged to the console immediately.
// The execution will be paused for 2 seconds (due to the delay in resolveAfter2Seconds function).
// After the delay, 'resolved' will be logged to the console as the value of result.
// In summary, the code will log 'calling' first, and after a 2-second delay, it will log 'resolved'.