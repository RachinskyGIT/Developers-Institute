var rowCounter = 2; // Start with the initial row count

function insertRow() {
  var table = document.getElementById("sampleTable");
  var newRow = table.insertRow();

  var cell1 = newRow.insertCell();
  var cell2 = newRow.insertCell();

  rowCounter++; // Increment the row counter for the next row

  // Set the cell content
  cell1.innerHTML = "Row" + rowCounter + " cell1";
  cell2.innerHTML = "Row" + rowCounter + " cell2";

  }
  

function insertRow2(){
    let table = document.getElementById("sampleTable").firstElementChild;
    let row = table.firstElementChild;
    

}