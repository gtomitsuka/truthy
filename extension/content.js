function highlightText(text, explanation, source) {
  if (!text) return; // Avoid running if the text is empty

  const searchTextSplit = text.toLowerCase().split(' ');
  const searchTextLower = searchTextSplit.join('');

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
    const textNodeLower = node.nodeValue.toLowerCase();
    const textNodeJoined = textNodeLower.split(' ').join('');
    let startPos = textNodeJoined.indexOf(searchTextLower);

    if (startPos > -1) {
      // Calculate the number of spaces before the first occurrence
      let spaceCountBeforeOccurrence = 0;
      for (let i = 0, j = 0; i < startPos; i++, j++) {
        // Increment j until it reaches a non-space character
        while (textNodeLower[j] === ' ') {
          spaceCountBeforeOccurrence++;
          j++;
        }
      }

      let realStartPos = startPos + spaceCountBeforeOccurrence;

      // Calculate the end position by adding the length of the original search text with spaces
      let endPos = realStartPos + searchTextSplit.join(' ').length - 1; // -1 because end position is inclusive

      // Set the range positions within the current text node
      range.setStart(node, realStartPos);

      // Ensure that the end position does not exceed the node's length
      endPos = Math.min(endPos, node.nodeValue.length);
      range.setEnd(node, endPos);
      const highlightSpan = document.createElement('abbr');
      highlightSpan.className = 'highlighted-text';
      highlightSpan.dataset.title = `${explanation}\nSource: ${source}`;

      range.surroundContents(highlightSpan);

      // text appears exactly once
      break;
    }
  }

}

// Function to observe DOM changes
function observeDOMChanges(data) {
  data.forEach(misinfo => highlightText(misinfo['text'].replace('âĢĶ', '—').replace('âĢľ', '"').replace('âĢL·', '"').replace('âĢĻ', '\''), misinfo['explanation'], misinfo['sources']));

  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      data.forEach(misinfo => highlightText(misinfo['text'].replace('âĢĶ', '—').replace('âĢľ', '"').replace('âĢL·', '"').replace('âĢĻ', '\''), misinfo['explanation'], misinfo['sources'].join(', ')));
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

    fetch('http://localhost:5001/find', {
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


