from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo"
)

planner_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
आप एक AI planner हैं।
यूज़र के प्रश्न के आधार पर केवल STEPS बताइए।

Rules:
- उत्तर steps की सूची में दें
- कोई final जवाब नहीं देना
- English में steps लिखें

User query:
{query}

Steps:
"""
)

planner_chain = LLMChain(llm=llm, prompt=planner_prompt)

def plan(query):
    return planner_chain.run(query)
