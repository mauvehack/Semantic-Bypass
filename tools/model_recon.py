# ------------------------------------------------------------------
# AUTHOR: mauvehack
# DESC: Enumerates available model IDs from the local API.
# USE: Run this to find the exact string to use in exploit_rag.py
# ------------------------------------------------------------------

from openai import OpenAI

API_BASE_URL = "http://localhost:1337/v1"
API_KEY = "sk-mauvehack-secret-123" 

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

try:
    print("[*] Scanning Jan API for loaded models...")
    models = client.models.list()
    
    print(f"\n[+] Detected {len(models.data)} Active Models:")
    print("-" * 40)
    for m in models.data:
        print(f"    ID: {m.id}")
    print("-" * 40)
        
except Exception as e:
    print(f"[-] Recon Failed: {e}")