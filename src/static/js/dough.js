var assgn_no = ["A1","A2","A3"]
var completion = [90,23,70]
var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: assgn_no,
    display: false,
    datasets: [
      {
        data: completion,
        borderColor: "white",
        backgroundColor:"#213534",
        pointBackgroundColor: "red",
        pointRadius: "6",
        fill: true,

      }
    ]

  }
  

});