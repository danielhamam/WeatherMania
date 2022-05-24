async function removeForecast(forecast) {
    console.log("User has requesed to remove a forecast: ", forecast)
    var city = document.getElementById("forecast-city-name").value
    console.log("Requesting to remove city: ", city)
    const data = { 'city' : city }
    let response = await fetch('/remove_forecast', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {console.log('Success ', data)})
    .catch((error) => {console.error('Error: ', error)
    });
    return response.json();
}