const menuToggle = document.getElementById("menu-toggle");
const menuItems = document.querySelector("#menu-items");
const gallery = document.querySelector(".gallery");

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

function viewerTemplate(pic, alt) {
    return `<div class="viewer">
    <button class="close-viewer">X</button>
    <img src="${pic}" alt="${alt}">
    </div>`;
}

function viewHandler(event) {
    // create a variable to hold the element that was clicked on from event.target
    let pic = event.target;
    // get the src attribute from that element and 'split' it on the "-"
    let src = pic.src.split("-");
    // construct the new image file name by adding "-full.jpeg" to the first part of the array from the previous step
    src.pop();
    src.push("-full.jpeg");
    let srcString = src.join("");
    // insert the viewerTemplate into the top of the body element
    // (element.insertAdjacentHTML("afterbegin", htmltoinsert))
    document.body.insertAdjacentHTML("afterbegin", viewerTemplate(srcString, "Picture but its bigger"));
    const imgClose = document.querySelector(".close-viewer");
    // add a listener to the close button (X) that calls a function called closeViewer when clicked
    imgClose.addEventListener("click", closeViewer);
}

gallery.addEventListener("click", viewHandler);

function closeViewer() {
    document.querySelector(".viewer").remove();
}