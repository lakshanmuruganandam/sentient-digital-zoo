import gradio as gr
import time
import random

custom_css = """
.gradio-container {background-color: #0d1117; color: #c9d1d9;}
.h1-text {color: #ff4757; font-family: 'Courier New', monospace; text-align: center; text-shadow: 0 0 15px #ff4757; font-weight: bold; font-size: 2.5em;}
.desc-text {text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 1.2em; font-style: italic;}
.box-glow {border: 1px solid #30363d; border-radius: 8px; padding: 15px; background: #161b22; box-shadow: 0 0 15px rgba(255, 71, 87, 0.3);}
.execute-btn {background: linear-gradient(90deg, #ff4757, #ff6b81) !important; color: white !important; font-weight: bold !important; border: none !important; box-shadow: 0 0 20px #ff4757 !important;}
.execute-btn:hover {background: #ff6b81 !important; box-shadow: 0 0 25px #ff4757 !important; transform: scale(1.02); transition: 0.2s;}
"""

def run_assassin(user_input):
    yield "🎯 Acquiring target competitor..."
    time.sleep(0.5)
    yield "⚡ Booting Overkill Local Swarm..."
    time.sleep(0.5)
    yield "💥 Obliterating competitor's baseline metrics..."
    time.sleep(0.8)
    yield f"""### 🏆 ASSASSINATION COMPLETE
**Competitor Destroyed.**
The Advanced swarm has successfully deployed an exponentially superior solution.
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("""<h1 class='h1-text'>☠️ SENTIENT DIGITAL ZOO</h1>""")
    gr.Markdown("""<div class='desc-text'>THE ULTIMATE COMPETITOR KILLER</div>""")
    
    with gr.Column(elem_classes="box-glow"):
        gr.Markdown("### 💀 Deployment Directive")
        user_input = gr.Textbox(label="Target Acquired", placeholder="Initiate launch sequence...")
        btn = gr.Button("🔥 OBLITERATE COMPETITION", elem_classes="execute-btn")
        output = gr.Markdown("*Awaiting launch...*")
        
    btn.click(fn=run_assassin, inputs=[user_input], outputs=[output])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
