var restart = document.querySelector("#b");
var box = document.querySelectorAll("td");

// Function had to be separate from addEventListener
function clearBoard(){
  for (var i=0; i<box.length; i++){
    box[i].textContent = "";
  }
};

restart.addEventListener("click", clearBoard)

// Would have not guess to use 'this'.
// The other method was to assign each <td> an id.

// Create a function that will check the square marker
function changeMarker(){
    if(this.textContent === ''){
      this.textContent = 'X';
      // console.log(marker)
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};

// box.addEventListener('click', changeMarker);

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < box.length; i++) {
    box[i].addEventListener('click', changeMarker);
}
