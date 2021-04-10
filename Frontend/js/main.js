window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});


const localApi = 'http://localhost:7071/api/resumecounter/b513d94b-d78e-4c4c-a916-a9d24e8fd32a';
const functionApi = 'https://resumetrigger.azurewebsites.net/api/resumecounter/b513d94b-d78e-4c4c-a916-a9d24e8fd32a'; 

const getVisitCount = () => {
    let count = 30;
    document.getElementById('counter').innerText = 'Loading...';
    fetch(functionApi)
    .then(response => {
        return response.json();
    })
    .then(response => {
        console.log("Website called function API.");
        count = response[0].visitor_count;
        document.getElementById('counter').innerText = count;
    }).catch(function(error) {
        console.log(error);
      });
    return count;
}