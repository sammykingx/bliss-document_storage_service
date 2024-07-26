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

  // Prepare the data for the chart
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

  // Render the pie chart
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
});
