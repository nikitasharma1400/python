import requests
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM # pyright: ignore[reportMissingImports]

api_key = "pub_74bf11b861ca426f88751f231acf8241"
topic = "artificial intelligence"
model_name = "sshleifer/distilbart-cnn-12-6"

def get_news(q):
    url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={q}&language=en"
    try:
        resp = requests.get(url)
        data = resp.json()
        return data.get('results', []) if data.get('status') == 'success' else []
    except:
        return []

print("loading ai...")
tk = AutoTokenizer.from_pretrained(model_name)
mdl = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def start():
    items = get_news(topic)
    if not items:
        print("nothing found.")
        return

    print(f"\n>> updates: {topic}")
    print("-" * 30)

    for i, item in enumerate(items[:3]):
        head = item.get('title')
        # check both content and description
        txt = item.get('content') or item.get('description') or ""

        print(f"\n[{i+1}] {head}")
        
        # lowered the limit so it tries to summarize even shorter text
        if len(txt) > 50: 
            bits = tk(txt[:1024], return_tensors="pt", truncation=True)
            outs = mdl.generate(bits["input_ids"], max_length=60, min_length=15, do_sample=False)
            sumry = tk.decode(outs[0], skip_special_tokens=True)
            print(f"tl;dr: {sumry}")
        else:
            print("tl;dr: text too short.")

if __name__ == "__main__":
    start()