// courses.js
const aCourse = {
    code: "CSE121b",
    name: "Javascript Language",
    sections: [
        { sectionNum: 1, roomNum: "STC 273", enrolled: 26, days: 30, instructor: "Luc Comeau" },
        { sectionNum: 2, roomNum: "STC 373", enrolled: 28, days: 31, instructor: "Kermit T. Frog" }
    ],
    enrollStudent: function (sectionNum) {
        const sectionIndex = this.sections.findIndex((section) => section.sectionNum == sectionNum);

        if (sectionIndex >= 0) {
            this.sections[sectionIndex].enrolled++;
        }
        renderSections(this.sections);
    },
    dropStudent: function (sectionNum) {
        const sectionIndex = this.sections.findIndex((section) => section.sectionNum == sectionNum);

        if (sectionIndex >= 0) {
            this.sections[sectionIndex].enrolled--;
        }
        renderSections(this.sections);
    },
};

function renderCourseDetails(course) {
    document.querySelector("#courseName").textContent = course.name;
    document.querySelector("#courseCode").textContent = course.code;
}

function sectionTemplate(section) {
    return `<tr>
            <td>${section.sectionNum}</td>
            <td>${section.roomNum}</td>
            <td>${section.enrolled}</td>
            <td>${section.days}</td>
            <td>${section.instructor}</td>
            </tr>`;
}
function renderSections(sections) {
    const html = sections.map(sectionTemplate);
    document.querySelector("#sections").innerHTML = html.join("");
}

document.querySelector("#enrollStudent").addEventListener("click", function () {
    const sectionNum = document.querySelector("#sectionNumber").value;
    aCourse.enrollStudent(sectionNum);
})

document.querySelector("#dropStudent").addEventListener("click", function () {
    const sectionNum = document.querySelector("#sectionNumber").value;
    aCourse.dropStudent(sectionNum);
})

renderCourseDetails(aCourse);

renderSections(aCourse.sections);