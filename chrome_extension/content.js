const currentUrl = window.location.href;

fetch("http://127.0.0.1:5000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ url: currentUrl })
})
.then(res => res.json())
.then(data => {
  if (data.result === "phishing") {
    alert("🚨 PHISHING SITE DETECTED! BE CAREFUL!");
  }
});
