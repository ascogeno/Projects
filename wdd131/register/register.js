let participantCount = 1;

function addParticpant() {
    participantCount++;
    let html = `<section class="participant1">
                    <p>Participant${participantCount}</p>
                    <div class="item">
                        <label for="fname"> First Name<span>*</span></label>
                        <input id="fname" type="text" name="fname" value="" required />
                    </div>
                    <div class="item activities">
                        <label for="activity">Activity #<span>*</span></label>
                        <input id="activity" type="text" name="activity" />
                    </div>
                    <div class="item">
                        <label for="fee">Fee ($)<span>*</span></label>
                        <input id="fee" type="number" name="fee" />
                    </div>
                    <div class="item">
                        <label for="date">Desired Date <span>*</span></label>
                        <input id="date" type="date" name="date" />
                    </div>
                    <div class="item">
                        <p>Grade</p>
                        <select>
                            <option selected value="" disabled selected></option>
                            <option value="1">1st</option>
                            <option value="2">2nd</option>
                            <option value="3">3rd</option>
                            <option value="4">4th</option>
                            <option value="5">5th</option>
                            <option value="6">6th</option>
                            <option value="7">7th</option>
                            <option value="8">8th</option>
                            <option value="9">9th</option>
                            <option value="10">10th</option>
                            <option value="11">11th</option>
                            <option value="12">12th</option>
                        </select>
                    </div>
                </section>`;

    document.querySelector(".participants").insertAdjacentHTML("beforeend", html);
}

function submitForm(event) {
    event.preventDefault();

    let totalFee = calculateTotalFees();//splitting this off was suggested by AI
    let adultName = document.getElementById("adult_name").value;

    document.querySelector("form").style.display = "none";

    document.getElementById("summary").innerHTML = `<p>Thank you ${adultName} for registering.</p>
        <p>You have registered ${participantCount} participants and owe $${totalFee} in fees.</p>`;
}

function calculateTotalFees() {
    let total = 0;
    let feeInputs = document.querySelectorAll("input[id^='fee']");//apparently this uses css selectors?? idk, this was suggested too

    feeInputs.forEach(fee => {
        total += Number(fee.value) || 0;
    });

    return total;
}


document.getElementById("add").addEventListener("click", addParticpant);
document.querySelector("form").addEventListener("submit", submitForm);
