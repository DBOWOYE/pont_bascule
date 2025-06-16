
// Courbe de consommation carburant mois en cours
const ctx = document.getElementById('dist-carburant-mois');
const engins = document.getElementById('engins');
const vls = document.getElementById('engins-conso')


fetch('/amr/dist-carburant-mois-encours')
.then(res => res.json())
.then(data =>new Chart(ctx, {
    type: 'line',
    data: {
        labels: data.labels,
        datasets: [{
        label: 'Quantié (t)',
        data: data.data,
        borderColor: '#36A2EB',
        borderWidth: 2
        }]
    },
    options: {
        scales: {
        y: {
            beginAtZero: true
        }
        }
    }
    }));

// Stock carburant par cuve
fetch('/amr/cuve-stock')
.then(res => res.json())
.then(data => new Chart(engins, {
    type: 'pie',

    data: {
      labels: data.labels,
      datasets: [{
        axis: 'y',
        label: 'STOCK CARBURANT PAR CUVE',
        data: data.data,
        backgroundColor: [
            'rgba(255, 19, 132)',
            'rgba(255, 159, 64 )',
            'rgba(255, 205, 86)',
            'rgba(75, 192, 192)',
            'rgba(54, 162, 235)',
            'rgba(153, 102, 255)',
            'rgba(201, 203, 207)'
        ],
        borderWidth: 1
      }]
    },
    options: {
     
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  }));

  // Consommation des engins
fetch('/amr/conso-vl')
.then(res => res.json())
.then(data => new Chart(vls, {
    type: 'bar',

    data: {
      labels: data.labels,
      datasets: [{
        axis: 'y',
        label: 'Les 10 engins qui consomment de plus',
        data: data.data,
        backgroundColor: [
            'rgba(0, 125, 255)',
            'rgba(255, 59, 64 )',
            'rgba(255, 205, 86)',
            'rgba(75, 192, 192)',
            'rgba(54, 162, 235)',
            'rgba(153, 102, 255)',
            'rgba(201, 203, 207)'
        ],
        borderWidth: 1
      }]
    },
    options: {
        indexAxis: 'y',
        scales: {
            
            y: {
            beginAtZero: true
            }
        }
    }
  }));
