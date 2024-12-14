document.getElementById('search-button').addEventListener('click', function() {
    let query = document.getElementById('search-input').value;  // Arama kutusundaki değer
    let resultsContainer = document.getElementById('search-results');  // Sonuçları yerleştireceğimiz alan

    // AJAX isteği
    fetch(`/search-recipes/?query=${query}`)
        .then(response => response.json())
        .then(data => {
            resultsContainer.innerHTML = '';  // Önceki sonuçları temizleyelim

            if (data.recipes.length > 0) {
                data.recipes.forEach(recipe => {
                    let recipeElement = document.createElement('div');
                    recipeElement.classList.add('recipe-item');
                    recipeElement.innerHTML = `
                        <h3>${recipe.baslik}</h3>
                        <p><strong>Kategori:</strong> ${recipe.kategori}</p>
                        <p><strong>Malzemeler:</strong> ${recipe.malzemeler}</p>
                        <p><strong>Tarif:</strong> ${recipe.tarif}</p>
                        ${recipe.resim ? `<img src="${recipe.resim}" alt="${recipe.baslik}" style="width: 200px; height: 200px; object-fit: cover;">` : ''}
                    `;
                    resultsContainer.appendChild(recipeElement);
                });
            } else {
                resultsContainer.innerHTML = '<p>No recipes found.</p>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultsContainer.innerHTML = '<p>Error fetching data.</p>';
        });
});
