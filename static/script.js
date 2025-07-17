async function analyzeTopic() {
  const topic = document.getElementById('topicInput').value.trim();
  const subreddits = document.getElementById('subredditInput').value.trim(); // NEW

  if (!topic) return alert('Please enter a topic.');

  const res = await fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ topic, subreddits }) // UPDATED
  });

  const data = await res.json();
  const counts = data.counts;
  const samples = data.samples;

  // Create pie chart
  const ctx = document.getElementById('sentimentChart').getContext('2d');
  if (window.sentimentChart instanceof Chart) {
    window.sentimentChart.destroy();
  }
  window.sentimentChart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Positive', 'Negative', 'Neutral'],
      datasets: [{
        data: [counts.positive, counts.negative, counts.neutral],
        backgroundColor: ['#36A2EB', '#FF6384', '#FFCE56']
      }]
    }
  });

  // Render sample posts with links
  const sampleContainer = document.getElementById('samples');
  sampleContainer.innerHTML = '';

  for (const [sentiment, messages] of Object.entries(samples)) {
    const block = document.createElement("div");
    block.className = "sentiment-block";

    const header = document.createElement("h3");
    header.textContent = sentiment.toUpperCase();

    const ul = document.createElement("ul");
    messages.forEach(post => {
      const li = document.createElement("li");
      const link = document.createElement("a");
      link.href = post.url;
      link.target = "_blank";
      link.textContent = post.title;
      li.appendChild(link);
      ul.appendChild(li);
    });

    block.appendChild(header);
    block.appendChild(ul);
    sampleContainer.appendChild(block);
  }
}
