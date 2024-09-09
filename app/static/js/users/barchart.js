const barChat = document.getElementById("myBarChart").getContext("2d");

const data = {
  labels: ["Obakhavbaye", "Ihama", "Ikeja", "Ajah", "Abeokuta", "Asaba"],
  datasets: [
    {
      label: "File Size",
      backgroundColor: [
        "#FF6384",
        "#36A2EB",
        "#FFCE56",
        "#4BC0C0",
        "#9966FF",
        "#FF9F40",
      ],
      data: [500, 800, 300, 900, 600, 1000], // Numbers corresponding to each section
    },
  ],
};

const options = {
  responsive: true,
  plugins: {
    legend: {
      display: false, // Hide the legend since we only have one dataset
    },
    datalabels: {
      color: "white",
      anchor: "end",
      align: "start",
      offset: 20,
      font: {
        weight: "bold",
        size: 12,
      },
      formatter: (value) => {
        return value + " GB";
      },
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      max: 1000,
      ticks: {
        stepSize: 100,
      },
    },
  },
};

Chart.register(ChartDataLabels); // Register the datalabels plugin

const myBarChart = new Chart(barChat, {
  type: "bar",
  data: data,
  options: options,
});
