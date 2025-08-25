from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse


# Tell the agent what tools it can use
tools = [TavilySearch()]

# Instantiate the LLM
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)

prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tool_names"],
    # partial_variables={"format_instructions": output_parser.get_format_instructions()},
).partial(format_instructions=output_parser.get_format_instructions())

# Create the agent instance with the LLM, tools, and prompt
agent = create_react_agent(llm, tools, prompt=prompt_with_format_instructions)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

extract_output = RunnableLambda(lambda x: x["output"])
parse_output = RunnableLambda(lambda x: output_parser.parse(x))
chain = agent_executor | extract_output | parse_output


def main():
    # Invoke the agent executor
    result = chain.invoke(
        {
            "input": "Search for 3 job postings for AI Engineer in Melbourne, Australia on LinkedIn and list their details"
        }
    )
    print(result)


if __name__ == "__main__":
    main()
