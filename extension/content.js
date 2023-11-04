function highlightText(text) {
  if (!text) return; // Avoid running if the text is empty

  const searchTextLower = text.toLowerCase();

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
    let startPos = textNodeLower.indexOf(searchTextLower);

    if (startPos > -1) {
      range.setStart(node, startPos);
      range.setEnd(node, startPos + searchTextLower.length);
      const highlightSpan = document.createElement('span');
      highlightSpan.style.backgroundColor = 'yellow';
      highlightSpan.className = 'highlighted-text';
      range.surroundContents(highlightSpan);

      // Move the walker past the newly created highlightSpan
      walker.currentNode = highlightSpan.nextSibling;
    }
  }

  // Add click event to all highlighted spans
  const highlightedSpans = document.querySelectorAll('.highlighted-text');
  highlightedSpans.forEach(span => {
    span.addEventListener('click', function() {
      showPopup(this);
    });
  });
}

function showPopup(element) {
  const popup = document.createElement('div');
  popup.className = 'text-popup';
  popup.textContent = 'This is a popup for the highlighted text!';
  popup.style.position = 'absolute';
  popup.style.left = `${element.getBoundingClientRect().left}px`;
  popup.style.top = `${element.getBoundingClientRect().top + element.getBoundingClientRect().height}px`;
  popup.style.backgroundColor = '#FFF';
  popup.style.border = '1px solid #000';
  popup.style.padding = '5px';
  document.body.appendChild(popup);
}

window.addEventListener('DOMContentLoaded', (event) => {
	console.log('reached');
	highlightText('Before a single ballot was cast, Louisiana Democrats knew they couldn’t win control of the State Legislature this year.');
	//highlightText('Hamas is attempting to sneak militants out of the Gaza Strip among civilians under evacuation.');
});

