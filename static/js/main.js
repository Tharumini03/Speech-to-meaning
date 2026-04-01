// ====== Grab references to HTML elements ======
const recordBtn = document.getElementById("recordBtn");
const statusEl = document.getElementById("status");
const rawTextEl = document.getElementById("rawText");
const improvedTextEl = document.getElementById("improvedText");
const translatedTextEl = document.getElementById("translatedText");
const inputLangSelect = document.getElementById("inputLanguage");
const outputLangSelect = document.getElementById("outputLanguage");

// ====== Speech Recognition setup ======
let recognition = null;
let isRecording = false;

// Check if browser supports SpeechRecognition
if ("SpeechRecognition" in window || "webkitSpeechRecognition" in window) {
    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    recognition = new SpeechRecognition();

    // We want final results only, not partial ones
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    // When recognition gets a result
    recognition.addEventListener("result", (event) => {
        // event.results is like a 2D array: [ [ { transcript, confidence } ] ]
        const transcript = event.results[0][0].transcript;
        console.log("Recognized:", transcript);

        // Show raw transcript in the UI
        rawTextEl.textContent = transcript;

        // Send transcript to backend for processing
        sendTextToBackend(transcript);
    });

    // When recognition starts
    recognition.addEventListener("start", () => {
        statusEl.textContent = "Status: Listening... please speak";
    });

    // When recognition ends (user stopped talking or we called stop())
    recognition.addEventListener("end", () => {
        isRecording = false;
        recordBtn.textContent = "🎙️ Start Recording";
        if (statusEl.textContent.startsWith("Status: Listening")) {
            statusEl.textContent = "Status: Finished recording";
        }
    });

    // When there is an error
    recognition.addEventListener("error", (event) => {
        console.error("Speech recognition error:", event.error);
        statusEl.textContent = "Status: Speech recognition error: " + event.error;
        recordBtn.classList.remove("recording");
        isRecording = false;
        recordBtn.textContent = "🎙️ Start Recording";
    });
} else {
    // Browser does not support Web Speech API
    statusEl.textContent =
        "Status: Speech recognition not supported in this browser. Try Chrome desktop.";
}

// ====== Button click behaviour ======
recordBtn.addEventListener("click", () => {
    // If we don't have recognition (unsupported browser), do nothing
    if (!recognition) {
        alert("Speech recognition not supported in this browser.");
        return;
    }

    if (!isRecording) {
        // Start recording
        isRecording = true;

        // Set recognition language to chosen input language
        recognition.lang = inputLangSelect.value;

        statusEl.textContent = "Status: Starting to listen...";
        recordBtn.textContent = "⏹️ Stop Recording";

        // Start the Web Speech API
        recognition.start();
    } else {
        // Stop recording if already recording
        statusEl.textContent = "Status: Stopping...";
        recognition.stop();
    }
});

function addToHistory(raw, improved, translated) {
    const historyList = document.getElementById("historyList");
    const li = document.createElement("li");

    li.textContent = `${new Date().toLocaleTimeString()} — ${raw} → ${translated}`;
    
    // Add to top
    historyList.prepend(li);
}

// ====== Function to call backend /process route ======
async function sendTextToBackend(text) {
    try {
        statusEl.textContent = "Status: Sending to server...";

        const response = await fetch("/process", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: text,
                input_lang: inputLangSelect.value,
                output_lang: outputLangSelect.value,
            }),
        });

        const data = await response.json();

        // Update result boxes
        improvedTextEl.textContent = data.improved_text;
        translatedTextEl.textContent = data.translated_text;
        addToHistory(text, data.improved_text, data.translated_text);

        statusEl.textContent = "Status: Done";
    } catch (error) {
        console.error("Backend error:", error);
        statusEl.textContent = "Status: Error talking to server";
    }
}
