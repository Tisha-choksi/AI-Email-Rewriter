# AI Email Rewriter

A professional email rewriting application powered by OpenAI's GPT models. Transform your emails with AI-powered tone and clarity enhancement.

## 📁 Project Structure

```
ai-email-rewriter/
├── backend/
│   ├── __init__.py
│   └── email_rewriter.py    # Backend logic for OpenAI API integration
├── app.py                   # Streamlit frontend application
├── requirements.txt         # Project dependencies
└── README.md               # Documentation
```

## ✨ Features

- 📝 Paste any email text
- 🎭 Choose from multiple tones:
  - Professional
  - Friendly
  - Persuasive
  - Apologetic
- 🤖 AI-powered rewriting using OpenAI GPT-3.5/GPT-4
- 📋 Copy to clipboard functionality
- 🔄 Diff view to highlight changes
- 📱 Responsive design
- 🎨 Modern, clean interface

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
  - Custom EmailRewriter class for OpenAI API integration
  - Modular design with separate backend package
- **Language Model**: OpenAI GPT-3.5/GPT-4
- **API Integration**: OpenAI Python SDK
- **Styling**: Custom CSS

## 🚀 Setup & Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd ai-email-rewriter
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and go to the URL shown in the terminal (usually http://localhost:8501)

5. Enter your OpenAI API key in the sidebar

## 🌐 Deployment Options

### Streamlit Cloud
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your OpenAI API key to the secrets
5. Deploy

### Vercel
1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```
2. Deploy:
   ```bash
   vercel
   ```
3. Add environment variables in Vercel dashboard

## 💡 Usage

1. Enter your OpenAI API key in the sidebar
2. Paste your email text in the input area
3. Select your desired tone from the dropdown
4. Choose between GPT-3.5 and GPT-4 models
5. Click "Rewrite Email"
6. Toggle "Show changes" to see differences
7. Use "Copy to Clipboard" to copy the rewritten email

## ⚙️ Backend Module

The `backend` package contains the core email rewriting functionality:

- `EmailRewriter`: Main class for handling OpenAI API interactions
  - Validates API keys
  - Constructs prompts
  - Makes API calls
  - Handles errors
- `EmailConfig`: Configuration dataclass for rewriting parameters
  - Tone selection
  - Model selection (GPT-3.5/GPT-4)
  - Temperature and token settings

## 🔒 Security

- API keys are handled securely and never stored
- All communications with OpenAI API are encrypted
- No emails are stored or logged

## 📝 Requirements

- Python 3.7+
- Streamlit
- OpenAI API key
- Internet connection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
