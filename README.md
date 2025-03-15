# HN Tech Summarizer

A Python tool that fetches top stories from Hacker News and generates concise summaries using Hugging Face transformers. The project uses BART-CNN model for summarization and provides both a general-purpose text summarizer and a Hacker News-specific implementation.

## Features

- 🤖 Uses BART-CNN model for efficient text summarization
- 📰 Fetches and summarizes top Hacker News stories
- 🔄 Singleton pattern for efficient model loading
- 💾 Memory-efficient processing
- 🚀 Easy to extend for other news sources

## Installation

1. Clone the repository:

```bash
git clone https://github.com/alveusdweller/hn-tech-summarizer.git
cd hn-tech-summarizer
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Summarize Hacker News Stories

Run the Hacker News summarizer:

```bash
python3 hn_summarizer.py
```

This will:

- Fetch the top 5 stories from Hacker News
- Generate concise summaries for each story
- Display results with story metadata (title, author, score, URL)

### Use the Tech Summarizer Directly

You can also use the tech summarizer for your own text:

```python
from tech_summarizer import get_summarizer

# Get summarizer instance (model loads only once)
summarizer = get_summarizer()

# Summarize text
text = """Your technical text here..."""
summary = summarizer.summarize(text)
print(summary)
```

## Project Structure

- `tech_summarizer.py`: Core summarization functionality using BART-CNN
- `hn_summarizer.py`: Hacker News integration and story processing
- `sentiment_analysis.py`: Example sentiment analysis implementation
- `requirements.txt`: Project dependencies

## Configuration

The summarizer can be configured with different parameters:

- `max_length`: Maximum length of generated summaries (default: 150)
- Story limit: Number of HN stories to process (default: 5)
- Model parameters: beam search, length penalty, etc.

## Limitations

- Currently fetches only article preview (first 5000 chars)
- Basic HTML parsing
- CPU-only implementation (can be extended for GPU)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Hacker News API](https://github.com/HackerNews/API)
- [BART-CNN Model](https://huggingface.co/facebook/bart-large-cnn)
