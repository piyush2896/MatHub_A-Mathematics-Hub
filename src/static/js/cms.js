
$(document).ready(function () {
console.log("Inside func");
  var table = document.getElementById("myTable");
  var row = table.insertRow(1);

  var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);
var cell3 = row.insertCell(2);
var cell4 = row.insertCell(3);
cell1.innerHTML = "User1";
cell2.innerHTML = "User2";
cell3.innerHTML = "User3";
cell4.innerHTML = "User4";
 });
