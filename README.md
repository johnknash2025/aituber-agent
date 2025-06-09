# Project Title (Replace with actual title)

(Add a brief description of your project here)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    (Add instructions for installing dependencies, e.g., using pip, poetry, etc.)
    ```bash
    # Example for pip:
    # pip install -r requirements.txt
    # Example for poetry:
    # poetry install
    ```
    This project uses `uv` for package management, similar to `pip`. If you don't have `uv` installed, you can install it via:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    Then install dependencies using:
    ```bash
    uv pip sync pyproject.toml
    ```


3.  **Set up environment variables:**
    Copy the `.env.example` file (if provided) to `.env` and fill in the necessary API keys and configurations.
    ```bash
    cp .env.example .env
    ```
    Ensure your `.env` file includes:
    *   `YOUTUBE_API_KEY`: Your YouTube Data API v3 key.
    *   `YOUTUBE_VIDEO_ID`: The ID of the YouTube live video.
    *   `OBS_HOST`: OBS WebSocket host (default: `localhost`).
    *   `OBS_PORT`: OBS WebSocket port (default: `4455`).
    *   `OBS_PASSWORD`: OBS WebSocket password.

## Running the Application

(Add instructions on how to run your application)
```bash
python get-comment.py
```

## Security Considerations

- Keep all dependencies up to date. Regularly check for vulnerabilities in dependencies using tools like `pip-audit` or enable automated dependency scanning (e.g., GitHub Dependabot).
- The `.env` file contains sensitive API keys and passwords. Ensure it is never committed to version control (it's already in `.gitignore`). On the deployment system, set restrictive file permissions for `.env` (e.g., readable only by the user running the application).
- The OBS WebSocket password should be strong and stored securely in the `.env` file.
- Regularly review the permissions and scopes associated with the `YOUTUBE_API_KEY` to ensure it only has the minimum necessary access.

## Contributing

(Optional: Add guidelines for contributing to the project)

## License

(Optional: Specify the license for your project)
