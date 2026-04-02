import gradio as gr
import requests

API = "http://127.0.0.1:7860"

def get_easy():
    r = requests.get(API + "/api/reset?task=easy")
    return r.json()["observation"]["code_snippet"]

def get_medium():
    r = requests.get(API + "/api/reset?task=medium")
    return r.json()["observation"]["code_snippet"]

def get_hard():
    r = requests.get(API + "/api/reset?task=hard")
    return r.json()["observation"]["code_snippet"]

with gr.Blocks() as demo:

    gr.Markdown("# 🧠 Code Review OpenEnv Environment")

    with gr.Row():
        easy = gr.Button("Easy - Syntax Errors")
        medium = gr.Button("Medium - Security Issues")
        hard = gr.Button("Hard - Advanced Security")

    output = gr.Code()

    easy.click(get_easy, outputs=output)
    medium.click(get_medium, outputs=output)
    hard.click(get_hard, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)