#!/usr/bin/env python3
"""
Capstone M6 evidence (not a trial): how much memory each part of the service adds.

    python diag_memory.py

One fresh Python process imports the same pieces the service uses, in the same
order, and prints psutil's memory_info().rss (MB = 10^6 bytes) after each one.
Used to diagnose Capstone 4's memory miss. Run by .github/workflows/capstone-diag.yml.
"""

import os
import platform
import sys

import psutil

os.environ.setdefault("AI201_DEBUG", "0")
proc = psutil.Process()


def mb():
    return round(proc.memory_info().rss / 1e6, 1)


rows = [("Python started", mb())]
import flask  # noqa: E402,F401
import flask_limiter  # noqa: E402,F401
import requests  # noqa: E402,F401
rows.append(("+ Flask, Flask-Limiter, requests", mb()))
import torch  # noqa: E402
rows.append((f"+ import torch {torch.__version__}", mb()))
from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: E402,F401
rows.append(("+ import transformers (model classes)", mb()))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import detector  # noqa: E402
model, _ = detector._load()
rows.append(("+ GPT-2 loaded (detector._load)", mb()))
text = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples", "ai-1.txt"),
            encoding="utf-8").read().strip()
detector.model_signal(text)
rows.append(("+ first scoring of ai-1", mb()))
for _ in range(3):
    detector.model_signal(text)
rows.append(("+ three more scorings", mb()))

n = sum(t.numel() for t in model.parameters())
print(f"machine: {platform.system()} {platform.machine()}, Python {platform.python_version()}, "
      f"torch {torch.__version__}, CUDA build: {torch.version.cuda}, threads: {torch.get_num_threads()}")
print(f"GPT-2 parameters: {n}, dtype {next(model.parameters()).dtype}, at 4 bytes each: {round(n * 4 / 1e6, 1)} MB")
prev = 0.0
for name, value in rows:
    print(f"{name:42} {value:8.1f} MB   (+{value - prev:.1f})")
    prev = value
