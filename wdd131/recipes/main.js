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
        <img src="${recipe.image}" alt="${recipe.name}" />
        <figcaption class="recipe-content">
            <span class="recipe-label">${recipe.tags.join(", ")}</span>
            <h1 class="recipe-name">${recipe.name}</h1>
            <span class="rating">${ratingTemplate(recipe.rating)}</span>
            <p class="recipe-description">${recipe.description}</p>
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

document.getElementById("searchimg").addEventListener("click", searchHandler);

function searchHandler(event) {
    event.preventDefault();
    const query = document.getElementById("search").value.toLowerCase();
    const filteredRecipes = filterRecipes(query);
    renderRecipes(filteredRecipes);
}

function filterRecipes(query) {
    return recipes.filter(recipe =>
        recipe.name.toLowerCase().includes(query) ||
        recipe.description.toLowerCase().includes(query) ||
        recipe.tags.find(tag => tag.toLowerCase().includes(query)) ||
        recipe.recipeIngredient.find(ingredient => ingredient.toLowerCase().includes(query))
    ).sort((a, b) => a.name.localeCompare(b.name));
}

function renderRecipes(recipes) {
    const recipeContainer = document.getElementById("recipe");
    recipeContainer.innerHTML = "";

    recipes.forEach(recipe => {
        recipeContainer.innerHTML += recipeTemplate(recipe);
    });
}
