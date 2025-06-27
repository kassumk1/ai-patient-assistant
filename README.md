# AI Patient Assistant (Offline)

A lightweight, local healthcare assistant built with Mistral-7B and `llama-cpp`. This tool runs fully offline and allows patients to ask health-related questions and receive AI-generated feedback, without sending any data online. Built with real-world AI engineering skills, it’s designed for privacy, performance, and accessibility.

TO RUN ASSISTANT: python main.py
---

## 🚀 Features

- ⚡ **Offline Language Model (Mistral-7B)** — Fast, private inference via `llama-cpp-python`
- 🤖 **Symptom Checker** — Custom prompts for health-related Q&A
- 🔐 **Privacy-first** — No API keys or internet connection required
- 🧠 **Prompt Tuning** — Tailored interactions to guide responses for symptom checking
- 🛠️ **Modular Python Code** — Easy to modify, scale, and test

---

## Getting Started

### Prerequisites

- Python 3.8 or newer  
- Mistral-7B model file (download separately)  
- `llama-cpp-python` installed

### Installation
This project uses the Mistral-7B-Instruct model from GPT4All, which is already in GGUF format and works with llama-cpp-python.

Visit: https://gpt4all.io/index.html
Scroll to the Downloads section
Choose the Mistral-7B-Instruct GGUF model
After downloading, place the .gguf file into your project directory, or update the model path in main.py if it's located elsewhere.
⚠️ Make sure the model is in GGUF format — other formats (like .safetensors) will not work with llama-cpp-python.
💡 Note: You can also use GGUF-format Mistral models from Hugging Face or other sources, as long as they are compatible with llama-cpp


```bash
git clone https://github.com/kassumk1/ai-patient-assistant.git
cd ai-patient-assistant
pip install -r requirements.txt
```
TO RUN ASSISTANT: python main.py




## My Goal for Developing this Project is to Demonstrate my Understanding of Technical Skills for AI Engineering:

* **Prompt Engineering** — Carefully crafted prompts to elicit medically relevant responses
* **Local Model Deployment** — Integrated Mistral-7B locally using llama-cpp, no APIs needed
* **AI Tool Integration** — Hands-on with model backends, token handling, and Python inference loops
* **AI-enhanced Data Interaction** — Engineered structured Q\&A using user intent analysis
* **System Design** — Architected a modular terminal-based tool for healthcare interaction
* **Open Source Dev Practices** — Used GitHub for collaboration, versioning, and transparency

---

## 📁 Project Structure

ai-patient-assistant/
├── main.py            # Runs the assistant
├── prompts.py         # Prompt logic and formatting
├── requirements.txt   # Dependencies
├── README.md          # You're here!


---

## 🛠 Future Plans

* Memory support for multi-turn conversations
* Web-based interface (Flask or Streamlit)
* Fine-tuning on open-source medical datasets
* Role-based prompt variation (e.g., nurse, specialist, chatbot)

---

## 📌 Notes

* This project is for educational and demo purposes.
* Not intended to replace medical advice from professionals.

---

## 📫 Connect with Me

**Kassum Khan**
Cognitive Science Major 
[LinkedIn](https://www.linkedin.com/in/kassum-khan-89484b310)
