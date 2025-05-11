import os
import sys

from dotenv import load_dotenv
import discord
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# load env vars
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
MODEL_ID = os.getenv("HF_MODEL")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID)
model.eval()

id2label = model.config.id2label

def classify_intent(text):
	# tokenize input
	inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
	with torch.no_grad():
		logits = model(**inputs).logits
		predicted_intent = torch.argmax(logits, dim=-1).item()
		return id2label[predicted_intent]

# bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")

client.run(TOKEN)
