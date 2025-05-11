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

id2label = {0: "analyze", 1: "context", 2: "explain", 3: "fact_check", 4: "joke", 5: "opinion", 6: "task_instruction"}

# bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")

client.run(TOKEN)
