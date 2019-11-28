// Author - Sandya Manoharan
// Date Modified - 11/25/19

Chart.defaults.global.legend.display = false;
var student_no=["S101","S102","S103","S104","S105"]

var grades = [100,95,43,56,70]

var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: student_no,
    display: false,
    datasets: [
      {
        data: grades,
        borderColor: "white",
        backgroundColor:"#213534",
        pointBackgroundColor: "red",
        pointRadius: "6",
        fill: true,

      }
    ]

  }
  

});


var assgn_no = ["A1","A2","A3"]
var completion = [90,23,70]
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: student_no,
    display: false,
    datasets: [
      {
        data: grades,
        borderColor: "white",
        backgroundColor:"#213534",
        pointBackgroundColor: "red",
        pointRadius: "6",
        fill: true,

      }
    ]

  }
  

});
