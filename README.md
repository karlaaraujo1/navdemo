# Navigator - Discharge Planning Assistant

A Streamlit-based AI chat application that provides expert guidance for healthcare discharge planning scenarios. Built with Langflow integration for intelligent responses to complex patient cases.

## Features

- 🤖 AI-powered discharge planning assistance
- 💬 Real-time chat with streaming responses
- 🏥 Healthcare-focused example scenarios
- 🔐 Secure API key management
- 🎨 Clean, professional interface
- 📱 Mobile-friendly design

## Quick Start

### 1. Clone or Download the Project

```bash
# If you have the folder, navigate to it
cd discharge-app
```

### 2. Set Up Environment Variables

First, copy the example environment file:

```bash
cp .env.example .env
```

Then edit the `.env` file with your credentials:

```bash
# Your Langflow API key
LANGFLOW_API_KEY=your_api_key_here

# Your Langflow flow URL
LANGFLOW_URL=your_flow_url_here
```

### 3. Get Your Langflow Credentials

#### API Key
1. Go to your Langflow settings
2. Navigate to **Settings > Langflow API Keys**
3. Generate a new API key
4. Copy the key and paste it in your `.env` file

#### Flow URL
1. Open your Langflow flow
2. Click **Publish**
3. Go to **API Access**
4. Click **cURL**
5. Copy the URL from the cURL command
6. Paste it in your `.env` file

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

### Example Scenarios

The app includes pre-built example scenarios you can click on:

- **Dementia & Elopement Risk**: Patient with dementia and elopement risk cannot return to prior home and has unclear finances
- **Encephalopathy & Aggressive Behavior**: Patient with encephalopathy and aggressive behavior needs adult day program but faces dual denial of level of care
- **Guardianship & ALF Placement**: Patient under guardianship needs ALF placement near Baltimore County, but options are cost-restrictive
- **Shelter Discharge**: Patient discharging to shelter needs follow-up support but lacks stable housing
- **ED Patient with Family Refusal**: Patient remains in ED under outpatient status but family refuses all discharge options including LTC, ALF, and home

### Chat Interface

- **Ask Questions**: Type your specific discharge planning questions
- **Streaming Responses**: Watch AI responses appear word-by-word
- **Chat History**: View your conversation history during the session
- **New Conversation**: Start fresh with the sidebar button

## File Structure

```
discharge-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .env               # Your environment variables (create this)
├── ss_logo.jp2        # Application logo
└── README.md          # This file
```

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `LANGFLOW_API_KEY` | Your Langflow API key | `sk-abc123...` |
| `LANGFLOW_URL` | Your Langflow flow URL | `https://your-domain.com/api/v1/run/flow-id` |

## Troubleshooting

### Common Issues

1. **"LANGFLOW_API_KEY environment variable not found"**
   - Make sure you've created the `.env` file
   - Verify the API key is correctly set in the `.env` file
   - Restart the application after making changes

2. **"Error making API request"**
   - Check your internet connection
   - Verify your Langflow URL is correct
   - Ensure your API key has proper permissions

3. **Logo not displaying**
   - The app will fall back to text if the logo file is missing
   - This doesn't affect functionality

### Getting Help

- **API Issues**: Contact your Langflow administrator
- **Setup Problems**: Check that all environment variables are set correctly
- **Dependencies**: Ensure all packages are installed with `pip install -r requirements.txt`

## Customization

You can customize the app by:

- **Adding Example Scenarios**: Edit the `example_queries` list in `app.py`
- **Changing Styling**: Modify the CSS in the `st.markdown` section
- **Updating Logo**: Replace `ss_logo.jp2` with your own logo file

## Support

For technical support or questions about the Navigator discharge planning assistant, please contact your system administrator.

---

**Navigator** - Compressing time and keeping teams focused, like working alongside a master discharge planner who's seen 10,000 cases. 