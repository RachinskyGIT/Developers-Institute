const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const gifForm = document.getElementById("gifForm");
const searchInput = document.getElementById("searchInput");
const gifContainer = document.getElementById("gifContainer");

gifForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const category = searchInput.value;
  searchGif(category);
});

async function searchGif(category) {
  try {
    const response = await fetch(
      `https://api.giphy.com/v1/gifs/random?tag=${category}&api_key=${apiKey}`
    );
    if (!response.ok) {
      throw new Error("Request failed with status: " + response.status);
    }
    const data = await response.json();
    const gifUrl = data.data.images.original.url;
    appendGif(gifUrl, category);
  } catch (error) {
    console.error("Error:", error);
  }
}

function appendGif(url, category) {
  const gifElement = document.createElement("div");
  gifElement.innerHTML = `
    <img src="${url}" alt="${category} gif">
    <br>
    <button class="deleteBtn">Delete</button>
  `;
  gifContainer.appendChild(gifElement);
  updateDeleteButtonVisibility();
}

gifContainer.addEventListener("click", (e) => {
  if (e.target.classList.contains("deleteBtn")) {
    e.target.parentNode.remove();
  }
});


const deleteAllBtn = document.getElementById("deleteAllBtn");

deleteAllBtn.addEventListener("click", () => {
  removeAllGifs();
});

function updateDeleteButtonVisibility() {
    if (gifContainer.children.length > 0) {
        deleteAllBtn.style.display = "block";
      } else {
        deleteAllBtn.style.display = "none";
      }
    }

function removeAllGifs() {
  while (gifContainer.firstChild) {
    gifContainer.firstChild.remove();
  }
  updateDeleteButtonVisibility();
}

// Call updateDeleteButtonVisibility initially
updateDeleteButtonVisibility();
