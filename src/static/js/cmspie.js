ctx = document.getElementById('myChart').getContext('2d');
chart = new Chart(ctx, {
    type: 'pie',
    data: {
        datasets: [{
            label: 'Colors',
            data: [9, 8, 7],
            backgroundColor: ["#277070","#03fc90","#063629"]
        }],
        labels: ['Student','Teacher','Parent']
    },
    options: {
        responsive: true,
        title:{
            display: true,
           
        }
    }
});