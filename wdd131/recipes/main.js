import recipes from "./recipes.mjs";

console.log(recipes);

function getRandomIdex(maxNum) {
    return Math.floor(Math.random() * maxNum);
}

alert(getRandomIdex(recipes.length));