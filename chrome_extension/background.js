chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url.startsWith('http')) {
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: tab.url })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("API call failed: " + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log("Prediction:", data.prediction);

            chrome.scripting.executeScript({
                target: { tabId: tab.id },
                func: (prediction) => {
                    const div = document.createElement('div');
                    div.style.position = 'fixed';
                    div.style.bottom = '10px';
                    div.style.right = '10px';
                    div.style.padding = '12px';
                    div.style.backgroundColor = prediction === 'phishing' ? '#ff4d4d' : '#4CAF50';
                    div.style.color = 'white';
                    div.style.zIndex = '9999';
                    div.style.fontWeight = 'bold';
                    div.style.borderRadius = '5px';
                    div.textContent = prediction === 'phishing' ?
                        '⚠️ PHISHING SITE DETECTED – BE CAREFUL' :
                        '✅ This site appears safe';
                    document.body.appendChild(div);
                },
                args: [data.prediction]
            });

        })
        .catch(error => {
            console.error("Error during phishing check:", error);
        });
    }
});
