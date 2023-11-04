import os
import logging

from haystack import Pipeline
from haystack.nodes import PromptNode, PromptTemplate

from .consts import prompt_text

anthropic_key = os.getenv('ANTHROPIC_KEY')

stream = True
prompt_node = PromptNode(
    model_name_or_path="claude-2",
    default_prompt_template=PromptTemplate(prompt_text),
    api_key=anthropic_key,
    max_length=10000,
    model_kwargs={"stream": stream},
)

pipeline = Pipeline()
pipeline.add_node(component=prompt_node, name="PromptNode", inputs=["Query"])

logging.disable(logging.CRITICAL)


def format_query(title, main_text, author, source):
    return f"""<article>\n<title>{title}</title>\n<author>{author}</author>\n<source>{source}</source>\n<content>{main_text}</content>\n</article>"""


def query(q):
    return pipeline.run(query=q)
