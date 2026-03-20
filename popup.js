document.getElementById("generateBtn").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value;
    const resultDiv = document.getElementById("result");

    if (!text) {
        resultDiv.innerHTML = "❌ Please enter an idea!";
        return;
    }

    resultDiv.innerHTML = "⏳ Generating tasks...";

    try {
        const response = await fetch("https://ideal-rotary-phone-wr7jx9v9v6j6hgrp-8000.app.github.dev/generate-tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        if (data.tasks) {
            resultDiv.innerHTML = "<h3>✅ Tasks:</h3><ul>" +
                data.tasks.map(task => `<li>${task}</li>`).join("") +
                "</ul><p>📌 Added to Notion!</p>";
        } else {
            resultDiv.innerHTML = "❌ Error generating tasks";
        }

    } catch (error) {
        resultDiv.innerHTML = "❌ Server error";
    }
});