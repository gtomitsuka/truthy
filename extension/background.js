chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.highlightCount !== undefined) {
      // Convert the count number to a string to set as badge text
      const badgeText = String(request.highlightCount);
      chrome.action.setBadgeText({ text: badgeText, tabId: sender.tab.id });
      chrome.action.setBadgeBackgroundColor({ color: '#FF0000' });
      chrome.action.setBadgeTextColor({color: '#FFFFFF'});
    }
  }
);

