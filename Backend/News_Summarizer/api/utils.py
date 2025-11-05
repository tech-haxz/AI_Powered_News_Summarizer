from newspaper import Article
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text

        if not text.strip():
            return {"error": "Could not extract text from URL."}

        summary = summarizer(text, max_length=130, min_length=40, do_sample=False)
        return {
            "title": article.title,
            "summary": summary[0]['summary_text']
        }
    except Exception as e:
        return {"error": str(e)}
