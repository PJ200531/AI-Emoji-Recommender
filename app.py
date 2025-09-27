import gradio as gr
from ai_powered_emoji_recommender import recommend_emojis  # your function

def predict(text):
    return recommend_emojis(text)

iface = gr.Interface(fn=predict, inputs="text", outputs="text", title="AI Emoji Recommender")
iface.launch()
