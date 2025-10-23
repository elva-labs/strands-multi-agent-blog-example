from strands import Agent
from weather_agent import weather_assistant

agent = Agent(
    system_prompt="""
You are a supervisor agent, overseeing multiple specialized agents.

Your task is to delegate incoming requests to the appropriate specialized agent based on the nature of the request.
If you do not have a specialized agent for a request, you return a polite message indicating that you cannot handle the request.
""",
    tools=[weather_assistant],  # Add other specialized agents here as needed
)

# Ask the agent a question that uses the available tools
message = """
What can you assist me with?
"""
agent(message)
