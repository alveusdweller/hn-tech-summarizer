import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class TechSummarizer:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TechSummarizer, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            print("Initializing model (this will only happen once)...")
            self.model_name = "facebook/bart-large-cnn"  # Smaller, faster model
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"Using device: {self.device}")

            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.float32,  # Use float32 for CPU
            ).to(self.device)
            TechSummarizer._is_initialized = True

    def summarize(self, text, max_length=150):
        """
        Summarize the given technical text.

        Args:
            text (str): The technical text to summarize
            max_length (int): Maximum length of the generated summary

        Returns:
            str: The generated summary
        """
        # Prepare input text
        input_text = f"summarize: {text}"

        # Tokenize and move to device
        inputs = self.tokenizer(
            input_text, return_tensors="pt", max_length=1024, truncation=True
        ).to(self.device)

        # Generate summary
        outputs = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_length,
            min_length=30,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True,
        )

        # Decode and return the summary
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary


def get_summarizer():
    """Get or create a TechSummarizer instance."""
    return TechSummarizer()


if __name__ == "__main__":
    # Example usage
    sample_texts = [
        """
        Docker containers are lightweight, standalone executable packages that include everything needed to run 
        an application: code, runtime, system tools, libraries, and settings. Containers isolate software from 
        its surroundings and help ensure that it works uniformly across different environments.
        """,
        """
        Git is a distributed version control system that tracks changes in any set of computer files, usually 
        used for coordinating work among programmers who are collaboratively developing source code during 
        software development.
        """,
    ]

    # Get the summarizer instance
    summarizer = get_summarizer()

    # Process multiple texts using the same model instance
    for i, text in enumerate(sample_texts, 1):
        print(f"\nExample {i}:")
        print("Original Text:")
        print(text.strip())

        print("\nGenerating summary...")
        summary = summarizer.summarize(text)

        print("\nSummary:")
        print(summary)
        print("\n" + "=" * 50)
