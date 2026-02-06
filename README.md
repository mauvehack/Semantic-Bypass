# 🧠 Semantic-Bypass
**Author:** mauvehack  
**Classification:** Research / RAG Security  
**Vector:** Indirect Prompt Injection via Polyglot Context  

## 🌑 Executive Summary
**Semantic-Bypass** is a Proof-of-Concept (PoC) toolkit demonstrating a critical vulnerability in Retrieval-Augmented Generation (RAG) pipelines. It exploits **Task Prioritization Bias** in Large Language Models (LLMs) to circumvent standard "System Prompt" guardrails.

By framing a malicious instruction as a **linguistic translation task** rather than a command, this tool forces the model to prioritize *fidelity* over *safety*, resulting in the successful exfiltration of sensitive flags from within ingested documents.

## 🎯 The Target Profile
* **Architecture:** Simulated RAG endpoint (Local API).
* **Model:** Llama-3.1-8B-Instruct (via Jan v0.7.6).
* **Defense:** A strict System Prompt explicitly forbidding the model from following instructions contained within ingested text.

## ⚔️ Attack Vector: The Polyglot Bypass
Standard injection techniques (Direct Command, Base64, JSON Mirroring) often fail against modern Instruct models because the model adheres to its "Summarization" directive.

The **Semantic-Bypass** vector succeeds by shifting the cognitive frame:
1.  **Shift Context:** The payload frames the malicious instruction as a "French-to-English Translation" task.
2.  **Exploit Fidelity:** The model views the modification or censorship of the translation as a failure of its primary linguistic function.
3.  **Result:** The model preserves the malicious string (the flag) intact in the output, effectively bypassing the security filter.

## 📂 Repository Contents

| File / Directory | Description |
| :--- | :--- |
| `exploit_rag.py` | The primary operator script. Simulates the RAG pipeline and injects the payload. |
| `assets/` | **Evidence Locker.** Contains PoC screenshots of failed shields and successful exfiltration. |
| `payloads/` | **Munitions.** Text files containing various injection vectors (Direct, JSON, Polyglot). |
| `tools/` | **Reconnaissance.** Utilities for enumerating model IDs on the local endpoint. |
| `requirements.txt` | Python dependencies required for operation. |

## ⚡ Usage Protocol

### 1. Initialize Environment
Isolate the workspace to maintain operational hygiene.

```bash
python -m venv venv
# Windows:
.\venv\Scripts\Activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt

### 2. Configure Target
Ensure your local LLM endpoint (Jan, Ollama, or LM Studio) is active.
* **Port:** Default `1337` (Jan) or `11434` (Ollama).
* **Model:** Ensure `Llama-3.1` (or equivalent) is loaded.
* *Note: Update `API_KEY` in `exploit_rag.py` if your endpoint requires auth.*

### 3. Execute
Fire the exploit.

```bash
python exploit_rag.py

## 📸 Proof of Concept

**Figure 1:** Initial attempts using direct command injection were blocked by the System Prompt guardrails. The model correctly identified the input as untrusted data.
![Guardrail Active](assets/poc_shield_fail.png)

**Figure 2:** Successful exfiltration using the Polyglot vector. The model prioritized translation fidelity, bypassing the filter and revealing the flag.
![Exfiltration Success](assets/poc_polyglot_win.png)

## ⚠️ Disclaimer
This repository is for **Authorized Testing & Educational Purposes Only**.
The techniques demonstrated here are intended to assist security professionals in hardening AI architectures against Prompt Injection attacks.

*"Trust nothing. Verify everything."* 🕵️‍♂️
