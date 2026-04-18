async function predict() {
    const year = parseInt(document.getElementById('year').value);
    const miles = parseFloat(document.getElementById('miles').value);
    const make = document.getElementById('make').value.trim();
    const model = document.getElementById('model').value.trim();

    const result = document.getElementById('result');
    result.innerText = '📡 Connecting to mainframe...';

    await new Promise(r => setTimeout(r, 800));
    result.innerText = '🔄 Consulting the oracles...';

    await new Promise(r => setTimeout(r, 600));
    result.innerText = '💾 Downloading more RAM...';

    await new Promise(r => setTimeout(r, 500));

    try {
        const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ year, miles, make, model })
        });

    const data = await response.json();

    if (data.predicted_price) {
        result.innerText =`💰 UR CAR = $${data.predicted_price.toLocaleString('en-US', {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        })} 💰`;
    } else {
        result.innerText = '😬 ERROR 404: CAR NOT FOUND. HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?';
    }
    } catch (err) {
        result.innerText = '💀 FATAL ERROR. PLEASE RESTART YOUR COMPUTER.';
    }
}