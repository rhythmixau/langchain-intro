from langchain import hub
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# Tell the agent what tools it can use
tools = [TavilySearch()]

# Instantiate the LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)
react_prompt = hub.pull("hwchase17/react")


# Create the agent instance with the LLM, tools, and prompt
agent = create_react_agent(llm, tools, prompt=react_prompt)

# Create the agent executor
chain_agent = AgentExecutor(agent=agent, tools=tools, verbose=True)


def main():
    # Invoke the agent executor 
    result = chain_agent.invoke({"input": "What is the weather in Beaufort, VIC Australia and is it going to be good for a motorbike ride?"})
    print(result.output)

if __name__ == "__main__":
    main()