fetch('text.json')
            .then(response => response.json())
            .then(data => {
                document.getElementById('text').innerText = data.text;
            })
            .catch(error => console.error('Error:', error));