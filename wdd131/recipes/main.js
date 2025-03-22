import recipes from "./recipes.mjs";

console.log(recipes);

function getRandomIdex(maxNum) {
    return Math.floor(Math.random() * maxNum);
}

function getRandomListEntry(list) {
    const listLength = list.length;
    const randomNum = getRandomIdex(listLength);
    return list[randomNum];
}

function recipeTemplate(recipe) {
    return `<figure class="recipe">
	<img src= ${recipe.image} alt=${recipe.name} />
	<figcaption>
		<ul class="recipe__tags">
        ${tagsTemplate(recipe.tags)}
		</ul>
		<h2><a href="#">${recipe.name}</a></h2>
		<p class="recipe__ratings">
            ${ratingTemplate(recipe.rating)}
		</p>
		<p class="recipe__description">
			${recipe.description}
		</p>
</figcaption>
</figure>`;
}

function tagsTemplate(tags) {
    return tags.map(tag => `<li>${tag}</li>`).join('');
}

function ratingTemplate(rating) {
    let html = `<span class="rating" role="img" aria-label="Rating: ${rating} out of 5 stars">`;

    for (let i = 1; i <= 5; i++) {
        if (i <= rating) {
            html += `<span aria-hidden="true" class="icon-star">⭐</span>`;
        } else {
            html += `<span aria-hidden="true" class="icon-star-empty">☆</span>`;
        }
    }

    html += `</span>`;
    return html;
}

function init() {
    const recipe = getRandomListEntry(recipes);

    renderRecipes([recipe]);
}

init();

document.getElementById("search-button").addEventListener("click", searchHandler);

function searchHandler(event) {
    event.preventDefault();

    const query = document.getElementById("search-input").value.toLowerCase();
    const filteredRecipes = filterRecipes(query);

    renderRecipes(filteredRecipes);
}

function filterRecipes(query) {
    return recipes.filter(recipe =>
        recipe.name.toLowerCase().includes(query) ||
        recipe.description.toLowerCase().includes(query) ||
        recipe.tags.find(tag => tag.toLowerCase().includes(query)) ||
        recipe.ingredients.find(ingredient => ingredient.toLowerCase().includes(query))
    ).sort((a, b) => a.name.localeCompare(b.name));
}

function renderRecipes(recipes) {
    const recipeContainer = document.getElementById("recipe-container");
    recipeContainer.innerHTML = "";

    recipes.forEach(recipe => {
        const recipeElement = document.createElement("div");
        recipeElement.classList.add("recipe");
        recipeElement.innerHTML = `
            <h3>${recipe.name}</h3>
            <p>${recipe.description}</p>
            <p><strong>Tags:</strong> ${recipe.tags.join(", ")}</p>
            <p><strong>Ingredients:</strong> ${recipe.ingredients.join(", ")}</p>
        `;
        recipeContainer.appendChild(recipeElement);
    });
}
