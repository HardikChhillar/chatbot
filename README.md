# Haridwar Travel Assistant

This project is a chatbot focused on providing information about Haridwar and nearby places. It utilizes the Claude API for logic and features a user-friendly interface that can be easily deployed on Vercel.

## Project Structure

```
haridwar-chatbot
├── src
│   ├── main.py               # Entry point of the application
│   ├── api
│   │   ├── __init__.py       # Marks the api directory as a package
│   │   └── claude_client.py   # Handles communication with the Claude API
│   ├── routes
│   │   └── chat.py           # Defines the chat route for the chatbot
│   ├── services
│   │   └── haridwar_knowledge.py # Provides methods to retrieve information about Haridwar
│   ├── models
│   │   └── schemas.py        # Defines data models and schemas
│   ├── ui
│   │   ├── index.html        # Main HTML file for the user interface
│   │   ├── app.js            # JavaScript code for frontend interactions
│   │   └── styles.css        # CSS styles for the chatbot UI
│   └── types
│       └── __init__.py       # Marks the types directory as a package
├── requirements.txt           # Lists project dependencies
├── pyproject.toml             # Configuration file for the project
├── vercel.json                # Configuration for deploying on Vercel
├── .gitignore                 # Specifies files to ignore in version control
└── README.md                  # Documentation for the project
```

## Local Development

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd haridwar-chatbot
   ```

2. **Set up a virtual environment and activate it:**
   - **macOS/Linux:**
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows:**
     ```
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up your API key:**
   ```
   export ANTHROPIC_API_KEY=YOUR_KEY
   ```

5. **Run the application:**
   ```
   python src/main.py
   ```

6. **Access the chatbot:**
   Open your web browser and navigate to `http://localhost:3000` (or the appropriate port).

## Usage Guidelines

- Interact with the chatbot by typing your queries related to Haridwar and nearby places.
- The chatbot will respond with relevant information using the Claude API.

## Deployment

To deploy the chatbot on Vercel, follow these steps:

1. Import the repository in Vercel or use the Vercel CLI with the `vercel` command.
2. Set the environment variables in the Vercel dashboard under Project → Settings → Environment Variables:
   ```
   ANTHROPIC_API_KEY=YOUR_KEY
   ```
   Choose the appropriate environment (Production/Preview/Development).
3. Build and deploy the project. The UI will be served at `/`, and the API will be available at `/api/chat`.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.