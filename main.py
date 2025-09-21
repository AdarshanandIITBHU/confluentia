# main.py

import os
from ai_core.agent import Agent
from process_data import process_transcript_data
from generated_outputs.chart_generator import ChartGenerator

class Application:
    def __init__(self):
        self.agent = Agent()
        self.chart_generator = ChartGenerator()
        self.transcript_data = None

    def load_transcript(self, file_path):
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return False
        with open(file_path, 'r', encoding='utf-8') as f:
            transcript = f.read()
        self.transcript_data = process_transcript_data(transcript)
        print(f"Transcript '{file_path}' loaded and processed.")
        return True

    def run(self):
        print("Welcome to the Transcript Analysis Application!")
        while True:
            file_path = input("Please enter the path to the transcript (.txt) file (or 'quit' to exit): ")
            if file_path.lower() == 'quit':
                break

            if self.load_transcript(file_path):
                while True:
                    user_prompt = input("Ask a question about the transcript or request a chart (e.g., 'summarize this call', 'generate sales chart', or 'back' to load another transcript): ")
                    if user_prompt.lower() == 'back':
                        break
                    elif user_prompt.lower() == 'quit':
                        return

                    if "chart" in user_prompt.lower() and self.transcript_data:
                        chart_type = self.get_chart_type_from_prompt(user_prompt)
                        if chart_type:
                            self.chart_generator.generate_chart(self.transcript_data, chart_type)
                            print(f"Chart '{chart_type}' generated.")
                        else:
                            print("Could not determine chart type from your request. Please be more specific (e.g., 'sales chart', 'sentiment chart').")
                    elif self.transcript_data:
                        response = self.agent.respond(user_prompt, self.transcript_data)
                        print("AI Response:", response)
                    else:
                        print("Please load a transcript first.")
            else:
                print("Failed to load transcript. Please try again.")

    def get_chart_type_from_prompt(self, prompt):
        # Simple keyword matching for chart types
        if "sales chart" in prompt.lower():
            return "sales"
        elif "sentiment chart" in prompt.lower():
            return "sentiment"
        # Add more chart types as needed
        return None

if __name__ == "__main__":
    app = Application()
    app.run()

