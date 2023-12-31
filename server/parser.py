from bs4 import BeautifulSoup
import json
import html

def get_content(html_content):
  """Extracts content from a news article URL.

  Makes a GET request to the article URL to retrieve
  the HTML. Parses the HTML with BeautifulSoup and
  extracts the article title, text, author and source
  from structured data.

  Args:
      html_content (str): News article

  Returns:
      tuple:
          (title, text, author, source) extracted
          from article metadata.
  """
  # Create a BeautifulSoup object and specify the parser
  soup = BeautifulSoup(html_content, 'html.parser')

  # Main text of the article
  article = soup.find(type="application/ld+json")
  content = article.string

  # website, title, author, content
  source = json.loads(content)['publisher']['name']
  title = json.loads(content)['headline']

  if source in { 'Daily Mail', 'The Sun' }:
    # Title
    title = soup.find('title').text

    # Main text of the article
    main_text = [html.unescape(p.text) for p in soup.find_all('p')]
    main_text = '\n'.join(main_text)
  else:
    main_text = [html.unescape(p.text) for p in soup.find_all('p')]
    main_text = '\n'.join(main_text)

  author = json.loads(content)['author']
  if type(author) == dict:
    author = author['name']
  elif type(author) == list:
    author = author[0]['name']

  return title, main_text, author, source
