var first = prompt("Please enter your first name:");
var last = prompt("Please enter your last name:");
var age = prompt("How old are you?");
var height = prompt("How tall are you in centimeters?");
var pet = prompt("What is the name of your pet?");

alert("Thank you so much for the information.");

var spy = "Welcome Comrade! You've passed the Spy Test.";

var name_cond = false;
var age_cond = false;
var height_cond = false;
var pet_cond = false;

if (first[0] === last[0]){
  name_cond = true;
}
console.log(name_cond)

if (age > 20 && age < 30){
  age_cond = true;
}
console.log(age_cond)

if (height >= 170){
  height_cond= true;
}
console.log(height_cond)

if (pet[pet.length-1] === "y"){
  pet_cond = true;
}
console.log(pet_cond)

if (name_cond && age_cond && height_cond && pet_cond){
  console.log(spy);
} else{
  console.log("Nothing to see here");
}
