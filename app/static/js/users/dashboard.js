// Reports Chart
document.addEventListener("DOMContentLoaded", () => {
  new ApexCharts(document.querySelector("#reportsChart"), {
    series: [
      {
        name: "Branch",
        data: [4, 5, 6, 6, 6, 6, 6],
      },
      {
        name: "Files",
        data: [10, 15, 35, 32, 34, 52, 41],
      },
      {
        name: "Clients",
        data: [20, 11, 32, 18, 60, 24, 11],
      },
    ],
    chart: {
      height: 350,
      type: "area",
      toolbar: {
        show: false,
      },
    },
    markers: {
      size: 4,
    },
    colors: ["#4154f1", "#2eca6a", "#ff771d"],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 1,
        opacityFrom: 0.3,
        opacityTo: 0.4,
        stops: [0, 90, 100],
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "smooth",
      width: 2,
    },
    xaxis: {
      type: "datetime",
      categories: [
        "2024-07-10T00:00:00.000Z",
        "2024-07-11T01:30:00.000Z",
        "2024-07-12T02:30:00.000Z",
        "2024-07-13T03:30:00.000Z",
        "2024-07-14T04:30:00.000Z",
        "2024-07-15T05:30:00.000Z",
        "2024-07-16T06:30:00.000Z",
      ],
    },
    tooltip: {
      x: {
        format: "dd/MM/yy HH:mm",
      },
    },
  }).render();

  // Previous Storage chart
  const categories = [
    "Ihama",
    "Obakhavbaye",
    "Ikeja",
    "Ajah",
    "Abeokuta",
    "Asaba",
    "Free",
  ];

  const values = [20, 25, 33, 18, 15, 12, 60];

  // Render the previous pie chart
  const options = {
    chart: {
      type: "pie",
    },
    series: values,
    labels: categories,
    dropShadow: {
      enabled: true,
      top: 1,
      left: 1,
      blur: 1,
      opacity: 0.45,
    },
    responsive: [
      {
        breakpoint: 480,
        options: {
          chart: {
            width: 400,
          },
          legend: {
            position: "bottom",
          },
        },
      },
    ],
  };

  const storageChart = new ApexCharts(
    document.querySelector("#storageChart"),
    options
  );
  storageChart.render();

  //  New Storage Chart
  const ctx = document.getElementById("myPieChart").getContext("2d");
  const myPieChart = new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Obakhavbaye", "Ihama", "Ikeja", "Ajah", "Abeokuta", "Asaba"],
      datasets: [
        {
          data: [10, 20, 30, 10, 20, 10], // Numbers corresponding to each section
          backgroundColor: [
            "#FF6384",
            "#36A2EB",
            "#FFCE56",
            "#4BC0C0",
            "#9966FF",
            "#FF9F40",
          ],
          hoverBackgroundColor: [
            "#FF6384",
            "#36A2EB",
            "#FFCE56",
            "#4BC0C0",
            "#9966FF",
            "#FF9F40",
          ],
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
        tooltip: {
          callbacks: {
            label: function (tooltipItem) {
              const value =
                myPieChart.data.datasets[0].data[tooltipItem.dataIndex];
              const total = myPieChart.data.datasets[0].data.reduce(function (
                a,
                b
              ) {
                return a + b;
              },
              0);
              const percentage = Math.round((value / total) * 100);
              return " (" + percentage + "%) Used";
            },
          },
        },
      },
    },
  });

  // Bar chart
});
