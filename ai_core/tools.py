# ai_core/tools.py
from dotenv import load_dotenv
load_dotenv()
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from openai import OpenAI

client = OpenAI()
PROCESSED_DATA_DIR = "processed_data"
OUTPUT_DIR = "generated_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_chart(topic: str) -> dict:
    """Generates a chart based on analysis of all call data."""
    print(f"✅ TOOL EXECUTED: Generating chart for topic: '{topic}'")
    all_metadata = []
    for filename in os.listdir(PROCESSED_DATA_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(PROCESSED_DATA_DIR, filename), 'r') as f:
                data = json.load(f)
                all_metadata.append(data['metadata'])

    if not all_metadata:
        return {"type": "text", "content": "No processed data found to generate a chart."}

    df = pd.DataFrame(all_metadata)
    salesperson_counts = df['salesperson'].value_counts()
    
    salesperson_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Calls Per Salesperson')
    plt.ylabel('Total Calls')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    file_path = os.path.join(OUTPUT_DIR, "sales_chart.png")
    plt.savefig(file_path)
    plt.close()
    return {"type": "image", "path": file_path}

def generate_video_highlights(topic: str) -> dict:
    """This feature is disabled as it requires FFMPEG."""
    print(f"⚠️ TOOL SKIPPED: Video generation is disabled.")
    return {"type": "text", "content": "Video and audio processing is currently disabled due to system configuration issues. Please try a text-based request."}

def answer_question(prompt: str) -> dict:
    """Answers a question based on the content of the text calls."""
    print(f"✅ TOOL EXECUTED: Answering question: '{prompt}'")
    
    all_transcripts = ""
    for filename in os.listdir(PROCESSED_DATA_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(PROCESSED_DATA_DIR, filename), 'r') as f:
                data = json.load(f)
                all_transcripts += f"--- Content from {data['filename']} ---\n{data['full_transcript']}\n\n"

    if not all_transcripts:
        return {"type": "text", "content": "No processed data found to answer the question."}

    system_prompt = f"""
    You are an expert analyst. Based ONLY on the provided call transcripts, answer the user's question.
    Transcripts:
    ---
    {all_transcripts[:4000]} 
    ---
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return {"type": "text", "content": response.choices[0].message.content}
