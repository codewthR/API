function performSearch() {
    const query = document.getElementById('search-input').value;
    fetch(`/search?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            if (data.error) {
                resultsDiv.innerHTML = `<p>${data.error}</p>`;
            } else {
                resultsDiv.innerHTML = `
                    <p><strong>Address:</strong> ${data.formatted_address}</p>
                    <p><strong>Latitude:</strong> ${data.latitude}</p>
                    <p><strong>Longitude:</strong> ${data.longitude}</p>
                    <p><strong>Place ID:</strong> ${data.place_id}</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('results').innerHTML = '<p>An error occurred. Please try again.</p>';
        });
}
