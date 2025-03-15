# HN Tech Summarizer

A Python tool that fetches top stories from Hacker News and generates concise summaries using Hugging Face transformers. The project uses BART-CNN model for efficient summarization, making it easy to stay updated with tech news without reading full articles.

## Features

- 🤖 Uses BART-CNN model for efficient text summarization
- 📰 Fetches and summarizes top Hacker News stories
- 🔄 Singleton pattern for efficient model loading
- 💾 Memory-efficient processing
- 🚀 Easy to extend for other news sources
- ⚡ Fast processing with optimized parameters

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

Example output:

```
Story 1:
Title: Example Tech Article
By: author123
Score: 100
URL: https://example.com/article

Summary: A concise summary of the technical article...
=====================================
```

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
- `requirements.txt`: Project dependencies

## Configuration

The summarizer can be configured with different parameters:

- `max_length`: Maximum length of generated summaries (default: 150)
- Story limit: Number of HN stories to process (default: 5)
- Model parameters:
  - `num_beams`: Number of beams for beam search (default: 4)
  - `length_penalty`: Length penalty for generation (default: 2.0)
  - `early_stopping`: Whether to stop generation early (default: True)

## Future Improvements

- [ ] Add proper article extraction using newspaper3k or trafilatura
- [ ] Add GPU support for faster processing
- [ ] Implement caching for article content
- [ ] Add filtering options (by score, type, etc.)
- [ ] Create a web interface

## Limitations

- Currently fetches only article preview (first 5000 chars)
- Basic HTML parsing
- CPU-only implementation (can be extended for GPU)

## Contributing

Contributions are welcome! Areas that need help:

- Improving article extraction
- Adding tests
- Implementing caching
- Creating a web interface

Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Hacker News API](https://github.com/HackerNews/API)
- [BART-CNN Model](https://huggingface.co/facebook/bart-large-cnn)
