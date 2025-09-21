# process_data.py
from dotenv import load_dotenv
load_dotenv()

import os
import json
from openai import OpenAI

client = OpenAI()

def extract_metadata_from_text(text_content, filename):
    """Uses GPT-4o-mini to extract structured data from text."""
    print(f"Extracting metadata from {filename}...")
    system_prompt = """
    You are an expert sales call analyst. Analyze the following call notes and extract the following information in a valid JSON format:
    1. "summary": A concise, one-paragraph summary of the call.
    2. "salesperson": The name of the salesperson. If unknown, use "Unknown".
    3. "key_moments": A list of important moments, each with a "label" (e.g., "introduction", "pricing_discussion", "objection", "closing_moment") and the "text" of that moment.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": text_content}],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)

def main():
    raw_dir = "raw_calls"
    processed_dir = "processed_data"
    os.makedirs(processed_dir, exist_ok=True)
    
    print(f"Looking for .txt files in '{raw_dir}'...")
    for filename in os.listdir(raw_dir):
        if filename.lower().endswith('.txt'):
            file_path = os.path.join(raw_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = extract_metadata_from_text(content, filename)
            
            final_data = {
                "filename": filename,
                "full_transcript": content,
                "metadata": metadata
            }
            
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(processed_dir, output_filename)
            with open(output_path, 'w') as f:
                json.dump(final_data, f, indent=4)
            print(f"Successfully processed {filename}\n")

if __name__ == "__main__":
    main()