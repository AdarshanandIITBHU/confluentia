# demo.py
import streamlit as st
from ai_core.agent import run_agent
import time

st.set_page_config(layout="wide")
st.title("🤖 Multimodal AI Agent for Enterprise Calls")

# Sample prompts for the user to click
sample_prompts = [
    "Create a chart of calls per salesperson",
    "Make a video of all the closing moments",
    "What were the main objections raised by customers?"
]

prompt = st.text_input("Ask anything about your calls, or choose an example below:", "")

if st.button("Generate Insight"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner('Thinking... The AI is processing your request. This may take a moment, especially for video generation.'):
            start_time = time.time()
            result = run_agent(prompt)
            end_time = time.time()
            
            st.success(f"Done in {end_time - start_time:.2f} seconds!")
            
            if result['type'] == 'text':
                st.write(result['content'])
            elif result['type'] == 'image':
                st.image(result['path'], caption="Generated Chart")
            elif result['type'] == 'video':
                st.video(result['path'])
            elif result['type'] == 'error':
                st.error(result['content'])

st.markdown("---")
st.subheader("Or, try one of these examples:")
for p in sample_prompts:
    if st.button(p):
        st.session_state.prompt = p
        # This will rerun the script with the prompt pre-filled in the text box
        # The user still needs to click "Generate Insight"
        st.rerun()

# This part ensures the prompt is pre-filled when a button is clicked
if 'prompt' in st.session_state:
    st.text_input("Ask anything about your calls, or choose an example below:", value=st.session_state.prompt, key="prompt_box")