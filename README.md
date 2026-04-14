# AI Log Analyzer

AI Log Analyzer is a Python and Streamlit web application that allows users to upload log files and receive AI-generated security analysis. The app reviews uploaded logs, identifies suspicious activity, assigns a severity level, and suggests recommended actions in a clean cybersecurity-themed dashboard.

## Features

* Upload `.txt` or `.log` files
* AI-generated log analysis
* Suspicious activity detection
* Severity classification
* Recommended next steps
* Downloadable analysis report
* Custom dark cybersecurity UI with background styling

## Tech Stack

* Python
* Streamlit
* OpenAI API
* python-dotenv

## Project Demo

This project analyzes uploaded logs and returns structured results in the following format:

* Summary
* Suspicious Activity
* Severity
* Recommended Actions

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/farasali12/Ai-Log-Analyzer.git
   ```

2. Move into the project folder:

   ```bash
   cd Ai-Log-Analyzer
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root folder and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the application:

   ```bash
   streamlit run app.py
   ```

## Example Use Case

A user uploads a sample log file containing failed login attempts and unauthorized access events. The application sends the log content to an AI model, which analyzes the patterns and returns a structured security summary with severity and response suggestions.

## Why I Built This

I built this project to combine Python, AI, and cybersecurity into a practical tool that simulates a lightweight security analysis workflow. It demonstrates API integration, prompt-based analysis, file handling, and user interface design in a real-world style project.

## Future Improvements

* Add support for more log formats
* Add timestamp-based filtering
* Highlight suspicious IP addresses automatically
* Store previous analysis history
* Export results as PDF

## Author

**Faras Ali**
GitHub: [farasali12](https://github.com/farasali12)
