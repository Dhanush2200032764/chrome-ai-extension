document.getElementById("summarizeBtn").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value;

    const response = await fetch("http://YOUR_API_URL/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();

    document.getElementById("output").innerText = data.summary;
});
