def main():
    print("Hello from openai-chainlit!")


if __name__ == "__main__":
    main()


# from openai import RateLimitError
from typing import Callable
import asyncio
import os
from agents import Agent, Tool, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
import chainlit as cl
from chainlit.message import Message
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client,

)
run_config = RunConfig(
    model=model,
    tracing_disabled=True
)

agent1 = Agent(
    # name="Panaversity support agent",
    name="joker",
    instructions="You are a helpful assisstent",
    # instructions="You are a helpful assisstent that can answer questions about and help with tasks."
)
result = Runner.run_sync(
    agent1,   
    input="Tell me five jokes",
    run_config=run_config,
)
print(result.final_output)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello i am a Panaversity Support Agent! How can I assist you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    msg = cl.Message(content="")
    await msg.send()

    history.append({"role": "user", "content": message.content})
    result = Runner.run_streamed(
        agent1,
        input=history,
        run_config=run_config,
    )
    async for event in result.stream_events():
      if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        await msg.stream_token(event.data.delta)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    # await cl.Message(content=result.final_output).send()
    