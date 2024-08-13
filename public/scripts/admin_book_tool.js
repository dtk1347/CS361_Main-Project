document.addEventListener("DOMContentLoaded", function () {
    fetch('/Microservice_A/Bookdata.json')
        .then(response => response.json())
        .then(data => {
            const dataDisplay = document.getElementById("dataDisplay");

            // Create HTML elements to display the JSON data
            const authorElement = document.createElement("p");
            nameElement.textContent = "Author: " + data.author;

            const titleElement = document.createElement("p");
            nameElement.textContent = "Title: " + data.title;

            const urlElement = document.createElement("p");
            ageElement.textContent = "URL: " + data.url;

            const descriptionElement = document.createElement("p");
            cityElement.textContent = "Description: " + data.description;

            // Append the elements to the "dataDisplay" div
            dataDisplay.appendChild(authorElement);
            dataDisplay.appendChild(titleElement);
            dataDisplay.appendChild(urlElement);
            dataDisplay.appendChild(descriptionElement);
        })
        .catch(error => console.error("Error fetching JSON data:", error));
});