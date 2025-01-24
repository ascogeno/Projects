const menuToggle = document.getElementById("menu-toggle");
const menuItems = document.querySelector("#menu-items");

function handleResize() {
    if (window.innerWidth >= 1000) {
        // Larger screens: always show the menu and hide the toggle button
        menuItems.style.display = "flex";
    } else {
        // Smaller screens: hide the menu and show the toggle button
        menuItems.style.display = "none";
    }
}

handleResize();

window.addEventListener("resize", handleResize);

menuToggle.addEventListener("click", () => {
    // If the menu is hidden, show it; if it's visible, hide it
    if (window.innerWidth <= 1000) {
        if (menuItems.style.display === "none") {
            menuItems.style.display = "flex"; // Show the menu
        } else {
            menuItems.style.display = "none"; // Hide the menu
        }
    }
});

