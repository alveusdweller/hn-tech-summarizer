# HN Tech Summarizer

A Python tool that fetches top stories from Hacker News and generates concise summaries using Hugging Face transformers. The project uses BART-CNN model for summarization, making it easy to stay updated with tech news without reading full articles.

## Features

- 🤖 Uses BART-CNN model for efficient text summarization
- 📰 Fetches and summarizes top Hacker News stories
- 🔄 Singleton pattern for efficient model loading (loads model only once)
- 💾 Memory-efficient processing with CPU support
- 🚀 Easy to extend for other news sources or custom text
- ⚡ Fast summarization with optimized parameters

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
- Display results with story metadata:
  - Title
  - Author
  - Score
  - URL
  - Summarized content

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
  - `min_length`: Minimum summary length (default: 30)
  - `length_penalty`: Controls summary length (default: 2.0)
  - `num_beams`: Beam search size (default: 4)
  - `early_stopping`: Whether to stop early in beam search (default: True)

## Future Improvements

- [ ] Add proper article extraction using newspaper3k or trafilatura
- [ ] Implement caching for faster repeated access
- [ ] Add GPU support for faster processing
- [ ] Add batch processing for multiple articles
- [ ] Support for other tech news sources
- [ ] Add progress bars for better UX
- [ ] Implement article categorization

## Contributing

Contributions are welcome! Some areas where you can help:

- Implementing the future improvements listed above
- Adding tests
- Improving documentation
- Reporting bugs
- Suggesting features

Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Hacker News API](https://github.com/HackerNews/API)
- [BART-CNN Model](https://huggingface.co/facebook/bart-large-cnn)
