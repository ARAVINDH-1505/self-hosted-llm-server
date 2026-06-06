# Local LLM Network Server using Ollama

## Overview

This project demonstrates how to deploy a local Large Language Model (LLM) using Ollama and expose it across a Local Area Network (LAN) so that multiple devices can access the same model without installing it individually.

The setup transforms a single laptop into an AI inference server while other devices act as clients.

---

## Features

* Local LLM deployment
* LAN-based model sharing
* No cloud API costs
* Multi-device access
* Simple REST API communication
* Works with Llama 3, Mistral and other Ollama-supported models

---

## Architecture

```text
                   ┌─────────────────────┐
                   │     Friend Laptop   │
                   │  Python Client App  │
                   └──────────┬──────────┘
                              │
                              │ HTTP
                              │
                              ▼
                    ┌─────────────────┐
                    │   WiFi Network  │
                    └────────┬────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │      AI Server Laptop    │
                │      Ollama Service      │
                │      Mistral / Llama3    │
                └──────────────────────────┘
```

---

## Prerequisites

* Windows / Linux / macOS
* Ollama Installed
* Python 3.10+
* Same WiFi Network

---

## Step 1: Install Ollama

Download and install:

https://ollama.com

Verify installation:

```bash
ollama --version
```

---

## Step 2: Download a Model

Example:

```bash
ollama run mistral
```

or

```bash
ollama run llama3
```

Wait for the download to finish.

Test:

```text
>>> hello
```

If the model responds, installation is successful.

---

## Step 3: Configure Ollama for LAN Access

Open Command Prompt:

```cmd
setx OLLAMA_HOST 0.0.0.0
```

Restart terminal.

---

## Step 4: Start Ollama Server

```cmd
ollama serve
```

Expected output:

```text
Listening on [::]:11434
```

Leave this terminal running.

---

## Step 5: Verify Port Binding

```cmd
netstat -ano | findstr 11434
```

Expected:

```text
0.0.0.0:11434 LISTENING
```

---

## Step 6: Find Server IP

```cmd
ipconfig
```

Locate:

```text
IPv4 Address
```

Example:

```text
192.168.18.5
```

---

## Step 7: Configure Windows Firewall

Open:

Windows Defender Firewall
→ Advanced Settings
→ Inbound Rules
→ New Rule

Settings:

```text
Rule Type: Port
Protocol: TCP
Port: 11434
Action: Allow
Profile: Private
```

Finish setup.

---

## Step 8: Verify Server

On server machine:

```text
http://SERVER_IP:11434
```

Example:

```text
http://192.168.18.5:11434
```

Expected:

```text
Ollama is running
```

---

## Step 9: Verify from Client Machine

Open browser:

```text
http://SERVER_IP:11434
```

Expected:

```text
Ollama is running
```

---

## Step 10: Install Client Dependencies

```bash
pip install requests
```

---

## Step 11: Configure Client

Update:

```python
OLLAMA_URL = "http://SERVER_IP:11434/api/generate"
```

Example:

```python
OLLAMA_URL = "http://192.168.18.5:11434/api/generate"
```

---

## Step 12: Run Client

```bash
python ollama_client.py
```

Example:

```text
You: Explain machine learning

AI: Machine learning is...
```

---

## Supported Models

```bash
ollama run mistral
ollama run llama3
ollama run gemma3
ollama run qwen3
```

---

## Performance Notes

System Used:

```text
GPU:
NVIDIA GTX 1650
VRAM: 4GB
```

Recommended:

```text
Mistral
```

Reason:

* Faster inference
* Lower memory usage
* Better for multiple LAN users

---

## Use Cases

* Local AI Assistant
* Team Knowledge Base
* Classroom Demonstrations
* Offline LLM Access
* LAN-Based AI Infrastructure
* Research Experiments

---

## Future Improvements

* Open WebUI Integration
* Authentication Layer
* Multi-user Chat Interface
* MCP Tool Integration
* Database-backed Conversations
* Remote VPN Access

---

## License

MIT License
