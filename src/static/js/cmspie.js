
var student_no=["Student","Teacher","Parent"]
//For drawing lines
var grades = [5,6,6]


var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: student_no,

    datasets: [
      { 
        data: grades,
        borderColor: "blue",
        backgroundColor:"red",
        pointBackgroundColor: "yellow",
        pointRadius: "6",
        fill: true,
    
      }
    ]

  }
});

