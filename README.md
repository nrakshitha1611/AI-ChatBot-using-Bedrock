# AI ChatBot using AWS Bedrock

## Overview
This project was created as part of learning **AWS Bedrock**. Special thanks to [@trevorspires](https://github.com/trevorspires) for guidance, inspiration of the project and teaching AWS Bedrock integration setup.
It leverages **LangChain**, **Streamlit**, and **Claude v3 (Haiku)** to build a simple multilingual chatbot that runs locally using Bedrock's LLM capabilities.

---

## Features
- Streamlit-based interactive chat UI
- Supports Claude v3 (Haiku) model via AWS Bedrock
- Dynamically generates responses in different languages
- Simple plug-and-play Python code using LangChain

---

## Tech Stack
- Python
- AWS Bedrock (Claude v3)
- LangChain
- Streamlit
- Boto3

---

## Project Structure
```
AI-ChatBot-using-Bedrock/
│
├── main.py                # Main application logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Setup & Run Locally

### 🔧 Prerequisites
- Python 3.10+
- AWS credentials configured (with Bedrock access)
- AWS profile set up in your environment (e.g., `~/.aws/config`)
- Bedrock service permissions enabled for your AWS account

### Installation
```bash
# Clone the repo
git clone https://github.com/nrakshitha1611/AI-ChatBot-using-Bedrock.git
cd AI-ChatBot-using-Bedrock

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

### Run the app
```bash
python -m streamlit run main.py
```

---

## Environment Variables

Make sure you set your AWS profile in the script or terminal:

```bash
export AWS_PROFILE=your profile name
```

---

## Screenshot

![Chatbot UI](https://github.com/nrakshitha1611/AI-ChatBot-using-Bedrock/blob/main/AI_ChatBot_Snapshot.png)

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Author
**Rakshitha Nagaraj**  
[GitHub](https://github.com/nrakshitha1611) | [LinkedIn](https://linkedin.com/in/rakshitha-n-b262128a/)
