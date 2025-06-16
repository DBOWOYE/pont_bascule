
const emp_partenaires = document.getElementById('part-emp');

// Stock carburant par cuve
fetch('/personnel/par-partenaire')
.then(res => res.json())
.then(data => new Chart(emp_partenaires, {
    type: 'bar',

    data: {
      labels: data.labels,
      datasets: [{
        axis: 'y',
        label: '',
        data: data.data,
        backgroundColor: [

            'rgba(20, 220, 207)'
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

  //
  const emp_departement = document.getElementById('emp-dept');
   // Consommation des engins
fetch('/personnel/par-departement')
.then(res => res.json())
.then(data => new Chart(emp_departement, {
    type: 'bar',

    data: {
      labels: data.labels,
      datasets: [{
        axis: 'y',
        label: '',
        data: data.data,
        backgroundColor: [

            'rgba(25, 159, 254 )',

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

  const emp_genre = document.getElementById('emp-genre');
   // Consommation des engins
fetch('/personnel/par-genre')
.then(res => res.json())
.then(data => new Chart(emp_genre, {
    type: 'doughnut',

    data: {
      labels: data.labels,
      datasets: [{
        axis: 'y',
        label: '',
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