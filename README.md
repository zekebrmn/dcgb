# Grok Bot for Discord

A Python-based Discord bot to mimic the functionality of xAI's Grok

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/zekebrmn/dcgb.git
cd dcgb
```

### 2. Create a `.env` file

```bash
cp .env.example .env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt 
```

### 4. Run the bot
```bash
python main.py
```

## Environment Variables

| Key       | Description                                       |
|-----------|---------------------------------------------------|
| BOT_TOKEN | Your Discord bot token                            |
| HF_MODEL  | Hugging Face model ID (default: zekebrmn/dcgb)    |

## Local Model

This project uses [`zekebrmn/dcgb`](https://huggingface.co/zekebrmn/dcgb), a fine-tuned DistilBERT model trained to classify intent for Grok-style prompts.

You can use your own model by updating the `HF_MODEL` variable.
