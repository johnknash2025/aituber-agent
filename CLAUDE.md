# Claude Code Instructions for aituber-agent

This repository contains an AI-powered virtual YouTuber agent with text-to-speech and streaming capabilities.

## Project Overview

The aituber-agent is a Python application that:
- Processes YouTube comments and generates responses
- Converts text to speech using multiple TTS engines (Google TTS, Voicevox)
- Integrates with OBS Studio for streaming
- Uses Ollama for local AI inference
- Handles real-time video streaming workflows

## Development Setup

This project uses `uv` for dependency management:

```bash
# Install dependencies
uv sync

# Run the application
uv run python main.py
```

## Key Files

- `main.py` - Main application entry point
- `youtube_util.py` - YouTube API integration
- `google_tts_util.py` - Google Text-to-Speech utilities
- `voicevox_util.py` - Voicevox TTS integration
- `ollama_util.py` - Ollama AI model utilities
- `obs_util.py` - OBS Studio integration
- `get-comment.py` - Comment processing utilities
- `pyproject.toml` - Project configuration and dependencies

## Code Style

- Follow PEP 8 for Python code style
- Use type hints where appropriate
- Keep functions focused and well-documented
- Use Google-style docstrings

## AI/ML Context

This project heavily integrates with AI services:
- **Text-to-Speech**: Multiple engines for voice synthesis
- **AI Inference**: Local models via Ollama
- **Real-time Processing**: Stream processing for live interactions
- **Media Integration**: OBS Studio for video streaming

## Testing

When adding new features:
- Consider the real-time nature of streaming applications
- Test TTS integration carefully
- Verify API integrations work correctly
- Consider rate limiting and API quotas

## Common Tasks

- **Adding new TTS engines**: Follow the pattern in existing `*_tts_util.py` files
- **YouTube integration**: Extend `youtube_util.py` for new API features
- **OBS integration**: Modify `obs_util.py` for streaming enhancements
- **AI model changes**: Update `ollama_util.py` for new models or parameters

## Dependencies

This project uses modern Python tooling:
- `uv` for fast dependency management
- Key dependencies managed in `pyproject.toml`
- Lock file maintained in `uv.lock`