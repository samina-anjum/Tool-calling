from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, function_tool

import os
from dotenv import load_dotenv
import requests




load_dotenv()
set_tracing_disabled(disabled=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider)



agent = Agent(
    name="Assistant",
    instructions= " you are a  helpfull assistant")


result = Runner.run_sync(
        agent=agent,
        input="how are you"
        
    )
print(result.final.output)




