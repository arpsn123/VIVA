from .llm import llm
from .prompts import (
    question_prompt,
    evaluation_prompt
)

# these are the langchain architecture;
question_chain = (
    question_prompt | llm
)

evaluation_chain = ( 
    evaluation_prompt | llm
)