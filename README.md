# Tri-70B-preview-SFT — vLLM Model Plugin

A lightweight, off‑the‑tree vLLM integration for the **`trillionlabs/Tri-70B-preview-SFT`** model. This README shows how to install the plugin, serve the model with vLLM, and call it using HTTP (OpenAI-compatible) and Python.

For details regarding the `Tri-70B-preview-SFT` model, please checkout its [huggingface repo](https://huggingface.co/trillionlabs/Tri-70B-preview-SFT). 

---

## Table of Contents

* [Prerequisites](#prerequisites)
* [Quick Start](#quick-start)
* [Client Examples](#client-examples)
  * [cURL (Chat Completions)](#curl-chat-completions)
  * [Python (OpenAI SDK)](#python-openai-sdk)
  * [Python (vLLM local inference)](#python-vllm-local-inference)
* [License](#license) 

---

## Prerequisites

* **Python** 3.10+
* **CUDA**-capable GPUs (recommended). Our code has been tested mostly on H100 GPU.
* **vLLM** `0.10.1.1` (other versions may work but are not guaranteed).

> A 70B parameter model typically requires **multi‑GPU** setups. Ensure you have enough VRAM and set `--tensor-parallel-size` appropriately for your hardware.

---

## Quick Start

Install the off‑the‑tree model integration plugin and serve the model using vLLM:

```bash
# install off-the-tree model integration plugin
git clone https://github.com/trillion-labs/trillion-deployment-utils.git
cd trillion-deployment-utils && pip install -e .

vllm serve trillionlabs/Tri-70B-preview-SFT --trust-remote-code
```

If you need multiple GPUs, add `--tensor-parallel-size <N>`:

```bash
vllm serve trillionlabs/Tri-70B-preview-SFT \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --port 8000
```

> The server exposes an **OpenAI-compatible** API by default at `http://127.0.0.1:8000/v1`.


---

## Client Examples

### cURL (Chat Completions)

```bash
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "trillionlabs/Tri-70B-preview-SFT",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Give me a haiku about large models."}
    ],
    "temperature": 0.7,
    "max_tokens": 256
  }' | jq .
```

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="sk-no-key-required")

resp = client.chat.completions.create(
    model="trillionlabs/Tri-70B-preview-SFT",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize LoRA fine-tuning in 3 bullets."}
    ],
    temperature=0.2,
    max_tokens=200,
)

print(resp.choices[0].message.content)
```

### Python (vLLM local inference)

If you want to run inside Python without the HTTP server:

```python
from vllm import LLM, SamplingParams

llm = LLM(model="trillionlabs/Tri-70B-preview-SFT", trust_remote_code=True, tensor_parallel_size=8)
params = SamplingParams(temperature=0.7, max_tokens=256)

prompts = [
    "Write a short poem about distributed inference.",
]
outputs = llm
```

## License

This repository’s integration code follows Trillion licence. 
