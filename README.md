# Strands Multi-Agent System Example

This repo is an example repo used in the blog: https://blog.elva-group.com/supercharge-yourself-with-your-own-team-of-agents

## Requirements

- Python 3.13
- uv
- AWS Credentials

## Getting started

1. Run `uv sync`
2. Activate venv via `source .venv/bin/activate`
3. Set your AWS Credentials as environment variables or similar
4. Run `uv run src/main.py` to start the multi-agent system locally

### Running the standalone weather agent

To skip the multi-agent framework and test the weather agent directly, run the `weather_agent.py` standalone:

```bash
uv run src/weather_agent.py
```

Adjust the last line in `weather_agent.py` to play around with different weather queries like: `weather_agent("Is it going to rain in Tokyo?")`

## Deployment

- https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/

## Project Structure

- `src/main.py` - Supervisor agent that delegates requests to specialized agents
- `src/weather_agent.py` - Specialized weather agent with simulated external API tool
