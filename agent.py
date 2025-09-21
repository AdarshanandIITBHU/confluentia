# ai_core/agent.py
import json
from openai import OpenAI
from . import tools

client = OpenAI()

def run_agent(prompt: str) -> dict:
    print(f"▶️ Agent received prompt: '{prompt}'")

    system_prompt = """
    You are an expert routing agent. Based on the user's prompt, you must choose one of the following tools to call.
    Respond ONLY with a single JSON object with two keys: "tool_name" and "arguments".
    The "arguments" value must also be a JSON object.

    Available Tools:
    - "generate_chart": Use for any requests about charts, graphs, or data visualization. The argument should be "topic". Example: {"tool_name": "generate_chart", "arguments": {"topic": "calls per salesperson"}}
    - "generate_video_highlights": Use for requests to create a video, clip, or show moments. The argument should be "topic". Example: {"tool_name": "generate_video_highlights", "arguments": {"topic": "closing statements"}}
    - "answer_question": Use for all other questions, like summarization, analysis, or specific queries about the content. The argument should be "prompt". Example: {"tool_name": "answer_question", "arguments": {"prompt": "What was the main objection raised by customers?"}}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    decision = json.loads(response.choices[0].message.content)
    print(f"✅ LLM decided: {decision}")
    
    tool_name = decision.get("tool_name")
    arguments = decision.get("arguments", {})

    if tool_name == "generate_chart":
        result = tools.generate_chart(**arguments)
    elif tool_name == "generate_video_highlights":
        result = tools.generate_video_highlights(**arguments)
    elif tool_name == "answer_question":
        result = tools.answer_question(**arguments)
    else:
        result = {"type": "text", "content": "Sorry, I'm not sure how to handle that request."}
        
    return result