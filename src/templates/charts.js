
var student_no=[1,2,3,4,5,6,7,8,9,10]
//For drawing lines
var grades = [100,95,43,56,70,23,45,6,90,18]


var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: student_no,

    datasets: [
      { 
        data: grades,
        borderColor: "blue",
        backgroundColor:"#88ceb2",
      }
    ]
  }
});