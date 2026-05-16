async function findCity() {

    const data = {
        cost: Number(document.getElementById("cost").value),
        safety: Number(document.getElementById("safety").value),
        internet: Number(document.getElementById("internet").value),
        climate: Number(document.getElementById("climate").value),
        nightlife: Number(document.getElementById("nightlife").value)
    }

    const response = await fetch(
        "http://127.0.0.1:8000/recommend",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    )

    const result = await response.json()

    let html = ""

    result.recommended_cities.forEach(city => {

        html += `
            <div class="city-card">

                <h2>${city.city}</h2>

                <p>Safety: ${city.safety}</p>
                <p>Internet: ${city.internet}</p>
                <p>Climate: ${city.climate}</p>
                <p>Nightlife: ${city.nightlife}</p>

            </div>
        `
    })

    document.getElementById("result").innerHTML = html
}