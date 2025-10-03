#!/usr/bin/env python3
"""Quick API key test"""

import os
import google.generativeai as genai

# Load .env
api_key = None
if os.path.exists('.env'):
    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('GOOGLE_API_KEY='):
                api_key = line.split('=', 1)[1].strip()
                break

if not api_key:
    print("No API key found in .env file")
    exit()

print(f"API Key: {api_key[:20]}...")

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Test")
    print("✅ API key works!")
    print(f"Response: {response.text[:100]}...")
except Exception as e:
    print(f"❌ API key failed: {e}")