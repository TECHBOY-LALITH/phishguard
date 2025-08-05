document.getElementById("check").addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  let url = tab.url;

  fetch("http://localhost:5000/check_url", {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ url: url })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText = data.result;
    if (data.result === "phishing") alert("⚠️ Phishing site detected!");
  });
});
