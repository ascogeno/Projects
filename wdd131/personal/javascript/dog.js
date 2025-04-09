document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".contact-form");
    const confirmationMessage = document.getElementById("confirmationMessage");

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const firstName = document.getElementById("firstName").value;

            form.reset();

            confirmationMessage.innerHTML = `<p>Thanks <strong>${firstName}</strong> for contacting us! We’ll get back to you soon.</p>`;
            confirmationMessage.style.display = "block";
            confirmationMessage.style.textAlign = "center";
        });
    }
});

function showMessage() {
    alert("This is just a test button, but if you would like to call please dial 364-5294.");
}

// Apply grayscale if preference is stored
if (localStorage.getItem('grayscale') === 'on') {
    document.body.style.filter = 'grayscale(100%)';
}

// Function to toggle grayscale mode
function toggleGrayscale() {
    const isGrayscale = localStorage.getItem('grayscale') === 'on';
    if (isGrayscale) {
        document.body.style.filter = 'none';
        localStorage.setItem('grayscale', 'off');
    } else {
        document.body.style.filter = 'grayscale(100%)';
        localStorage.setItem('grayscale', 'on');
    }
}

// Add event listener once DOM is loaded
window.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('grayscaleToggle');
    if (btn) {
        btn.addEventListener('click', toggleGrayscale);
    }

    // Apply Woof Mode if preference is stored
    if (localStorage.getItem('woofMode') === 'on') {
        enableWoofMode();
        woofModeEnabled = true;
    }

    const woofButton = document.getElementById(woofButtonId);
    if (woofButton) {
        woofButton.addEventListener('click', toggleWoofMode);
    }
});


// Woof Mode functionality
const dogSounds = ["Woof!", "Bark!", "Ruff!", "Arf!", "Grrr!", "Wuf!"];
let woofModeEnabled = localStorage.getItem('woofMode') === 'on' || false; // Initialize based on local storage
const woofButtonId = 'woofButton';

function applyWoofTransformation(element) {
    element.dataset.originalText = element.textContent;
    const words = element.textContent.split(/\s+/);
    const woofifiedWords = words.map(() => dogSounds[Math.floor(Math.random() * dogSounds.length)]);
    element.textContent = woofifiedWords.join(" ");
}

function revertWoofTransformation(element) {
    if (element.dataset.originalText) {
        element.textContent = element.dataset.originalText;
        delete element.dataset.originalText;
    }
}

function enableWoofMode() {
    const textElements = document.querySelectorAll(`
        h1, h2, h3, h4, h5, h6,
        p:not(:empty),
        a:not(#logo_link1):not(#logo_link2):not(.social > a),
        button:not(#${woofButtonId}),
        span, li, dt, dd, label, textarea, input[type="text"], input[type="email"], input[type="tel"],
        section.more > div /* Target the div within the section.more */
    `);

    textElements.forEach(element => {
        if (!element.dataset.originalText) { // Prevent re-woofing
            applyWoofTransformation(element);
        }
    });
    localStorage.setItem('woofMode', 'on');
}

function disableWoofMode() {
    const textElements = document.querySelectorAll(`
        h1, h2, h3, h4, h5, h6,
        p:not(:empty),
        a:not(#logo_link1):not(#logo_link2):not(.social > a),
        button:not(#${woofButtonId}),
        span, li, dt, dd, label, textarea, input[type="text"], input[type="email"], input[type="tel"],
        section.more > div /* Target the div within the section.more */
    `);

    textElements.forEach(element => {
        revertWoofTransformation(element);
    });
    localStorage.setItem('woofMode', 'off');
}

function toggleWoofMode() {
    if (woofModeEnabled) {
        disableWoofMode();
        woofModeEnabled = false;
    } else {
        enableWoofMode();
        woofModeEnabled = true;
    }
}

const woofButton = document.getElementById(woofButtonId);
if (woofButton) {
    woofButton.addEventListener('click', toggleWoofMode);
}