// events.js
let tasks = [];
const taskButton = document.getElementById("submitTask");

function renderTasks(tasks) {
  // get the list element from the DOM
  const toDo = document.getElementById("todoList");
  toDo.innerHTML = "";
  // loop through the tasks array. transform (map) each task object into the appropriate HTML to represent a to-do.
  for (const task of tasks) {
    let li = document.createElement("li");
    li.innerHTML =
      `${task.completed ? 'class="strike"' : ""}
        <p>${task.detail}</p> 
        <div>
          <span data-function="delete">❎</span>
          <span data-function="complete">✅</span>
        </div>`;
    toDo.appendChild(li);
  }
}

function newTask() {
  // get the value entered into the #todo input
  let input = document.getElementById("todo").value;
  // add it to our arrays tasks
  tasks.push({ detail: input, completed: false });
  // render out the list
  renderTasks(tasks);
}

function removeTask(taskElement) {
  // Note the use of Array.filter to remove the element from our task array
  // Notice also how we are using taskElement instead of document as our starting point?
  // This will restrict our search to the element instead of searching the whole document.
  tasks = tasks.filter(
    (task) => task.detail != taskElement.querySelector('p').innerText
  );

  // this line removes the HTML element from the DOM
  taskElement.remove();
}


//Hi! For some reason, the original completeTask function didn't work in the slightest, and I've got no idea what it was doing.
//Much like most of the code here, it might as well be hieroglyphics to me. I had to get an AI fix, sorry.
function completeTask(taskElement) {
  const taskText = taskElement.querySelector("p").innerText; // Get the text properly

  // Find the index based on correct text retrieval
  const taskIndex = tasks.findIndex((task) => task.detail === taskText);

  if (taskIndex === -1) {
    console.error("Task not found in tasks array:", taskText);
    return; // Exit the function to prevent errors
  }

  // Toggle completed status
  tasks[taskIndex].completed = !tasks[taskIndex].completed;

  // Toggle class for strikethrough effect
  taskElement.classList.toggle("strike");
}

function manageTasks(event) {
  // did they click the delete or complete icon?
  console.log(event.target);
  const parent = event.target.closest("li");
  if (event.target.dataset.function === "delete") {
    removeTask(parent);
  }
  if (event.target.dataset.function === "complete") {
    completeTask(parent);
  }
}

document.querySelector("#submitTask").addEventListener("click", newTask);
document.getElementById("todoList").addEventListener("click", manageTasks);
// Add your event listeners here
// We need to attach listeners to the submit button and the list. Listen for a click, call the 'newTask' function on submit and call the 'manageTasks' function if either of the icons are clicked in the list of tasks.