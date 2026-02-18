let selectedFile = null;
let selectedURL = null;

const preview = document.getElementById("preview");


document.getElementById("fileInput").onchange = function(e){

selectedFile = e.target.files[0];
selectedURL = null;

const reader = new FileReader();

reader.onload = function(){
preview.innerHTML = `<img src="${reader.result}">`;
}

reader.readAsDataURL(selectedFile);

}


document.getElementById("urlInput").oninput = function(e){

selectedURL = e.target.value;
selectedFile = null;

preview.innerHTML = `<img src="${selectedURL}">`;

}



async function predict(){

const resultBox = document.getElementById("result");

resultBox.innerText = "Analyzing...";

try{

let formData = new FormData();

if(selectedFile){

formData.append("image", selectedFile);

}else if(selectedURL){

formData.append("image_url", selectedURL);

}else{

alert("Select image or enter URL");
return;

}


const res = await fetch("http://127.0.0.1:5000/predict",{

method:"POST",
body:formData

});

const data = await res.json();
resultBox.innerText = data[0].plate;

}catch(err){

resultBox.innerText =
"Prediction failed.";

}

}
const RATE_PER_HOUR = 50; // change price rate here


async function loadLogbook(){

    const res = await fetch("http://127.0.0.1:5000/logbook");

    const data = await res.json();

    const container = document.getElementById("logbookList");

    container.innerHTML = "";

    Object.keys(data).forEach(plate => {

        data[plate].forEach(record => {

            const status =
            record.exit_time ? "EXIT" : "ENTRY";

            const duration =
            record.duration_hours ?
            record.duration_hours + " hrs"
            : "--";

            const price =
            record.duration_hours ?
            "₹" + (record.duration_hours * RATE_PER_HOUR).toFixed(2)
            : "₹" + (1 * RATE_PER_HOUR).toFixed(2);

            container.innerHTML += `

            <div class="logbook-card">

                <div class="logbook-left">

                    <div class="plate">
                        ${plate}
                    </div>

                    <div class="status ${status.toLowerCase()}">
                        ${status}
                    </div>

                    <div class="duration">
                        Duration: ${duration}
                    </div>

                </div>

                <div class="price">
                    ${price}
                </div>

            </div>

            `;

        });

    });

}


// load automatically
loadLogbook();

// refresh every 5 seconds
setInterval(loadLogbook, 5000);