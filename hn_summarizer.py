import time

import requests

from tech_summarizer import get_summarizer


class HNStoriesSummarizer:
    def __init__(self):
        self.base_url = "https://hacker-news.firebaseio.com/v0"
        self.summarizer = get_summarizer()

    def get_top_stories(self, limit=5):
        """Fetch IDs of top stories from Hacker News."""
        response = requests.get(f"{self.base_url}/topstories.json")
        story_ids = response.json()[:limit]
        return story_ids

    def get_story_details(self, story_id):
        """Fetch details of a specific story."""
        response = requests.get(f"{self.base_url}/item/{story_id}.json")
        return response.json()

    def get_article_text(self, url):
        """Get the main text content from the article URL."""
        try:
            response = requests.get(url, timeout=10)
            # For this example, we'll just return the first part of the page
            # In a production environment, you'd want to use a proper article extraction library
            text = response.text[:5000]  # Get first 5000 chars
            return text
        except Exception as e:
            print(f"Error fetching article: {e}")
            return None

    def process_top_stories(self, limit=5):
        """Fetch and summarize top stories."""
        print(f"Fetching top {limit} stories from Hacker News...")
        story_ids = self.get_top_stories(limit)

        summaries = []
        for idx, story_id in enumerate(story_ids, 1):
            story = self.get_story_details(story_id)
            if not story:
                continue

            print(f"\nProcessing story {idx}/{limit}: {story.get('title', 'No title')}")

            # Create a summary text from title and URL
            if "url" in story:
                summary_text = f"Title: {story['title']}\n\n"
                article_text = self.get_article_text(story["url"])
                if article_text:
                    summary_text += article_text
            else:
                summary_text = f"Title: {story['title']}\n\n{story.get('text', '')}"

            # Generate summary
            try:
                summary = self.summarizer.summarize(summary_text)
                summaries.append(
                    {
                        "title": story["title"],
                        "url": story.get("url", ""),
                        "summary": summary,
                        "score": story.get("score", 0),
                        "by": story.get("by", "unknown"),
                    }
                )
            except Exception as e:
                print(f"Error summarizing story: {e}")

            # Be nice to the API
            time.sleep(1)

        return summaries


def print_summaries(summaries):
    """Print the summaries in a nice format."""
    for idx, summary in enumerate(summaries, 1):
        print(f"\n{'='*80}")
        print(f"Story {idx}:")
        print(f"Title: {summary['title']}")
        print(f"By: {summary['by']}")
        print(f"Score: {summary['score']}")
        if summary["url"]:
            print(f"URL: {summary['url']}")
        print("\nSummary:")
        print(summary["summary"])
        print(f"{'='*80}")


if __name__ == "__main__":
    # Create an instance of HNStoriesSummarizer
    hn_summarizer = HNStoriesSummarizer()

    # Get and summarize top 5 stories
    print("Initializing summarizer and fetching stories...")
    summaries = hn_summarizer.process_top_stories(limit=5)

    # Print the results
    print("\nTop Hacker News Stories Summaries:")
    print_summaries(summaries)
