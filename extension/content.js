function highlightText(text, explanation) {
  if (!text) return; // Avoid running if the text is empty

  const searchTextLower = text.toLowerCase().split(' ').join('');

  // Create a filter to skip already highlighted nodes
  const acceptNode = node => {
    return node.parentNode && node.parentNode.className === 'highlighted-text'
        ? NodeFilter.FILTER_REJECT
        : NodeFilter.FILTER_ACCEPT;
  };

  const range = document.createRange();
  const walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      { acceptNode },
      false
  );

  let node;

  while ((node = walker.nextNode())) {
    const textNodeSplit = node.nodeValue.toLowerCase().split(' ');
    const textNodeLower = textNodeSplit.join('');
    let startPos = textNodeLower.indexOf(searchTextLower);

    if (startPos > -1) {
      range.setStart(node, startPos);
      range.setEnd(node, startPos + searchTextLower.length + textNodeSplit.length - 1);
      const highlightSpan = document.createElement('abbr');
      highlightSpan.className = 'highlighted-text';
      highlightSpan.dataset.title = `${explanation}<br/><a href="a">View Reference</a>`;

      range.surroundContents(highlightSpan);

      // text appears exactly once
      break;
    }
  }

}

// Function to observe DOM changes
function observeDOMChanges(data) {
  data.forEach(misinfo => highlightText(misinfo['text'], misinfo['explanation']));

  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      data.forEach(misinfo => highlightText(misinfo['text'], misinfo['explanation']));
    });
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
}

function getPageHTML() {
  return document.documentElement.outerHTML;
}

window.addEventListener('DOMContentLoaded', (event) => {
	const htmlContent = getPageHTML();

    fetch('https://22b1-5-148-66-108.ngrok-free.app/find', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(htmlContent)
    })
    .then(response => response.json())
    .then(data => {
      observeDOMChanges(data['segments']);
      chrome.runtime.sendMessage({ highlightCount: data['segments'].length });
    })
    .catch(error => console.error('Error:', error));
});


