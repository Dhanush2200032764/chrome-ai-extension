document.getElementById("summarizeBtn").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value;

    if (!text) {
        alert("Enter text first!");
        return;
    }

    document.getElementById("output").innerText = "Processing...";

    try {
        const response = await fetch("http://127.0.0.1:8000/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();
        document.getElementById("output").innerText = data.summary;

    } catch (error) {
        document.getElementById("output").innerText = "Error connecting to API";
    }
});
