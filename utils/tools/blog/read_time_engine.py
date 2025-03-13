import re
from math import ceil
import markdown
from bs4 import BeautifulSoup

class PostReadTimeEngine:

    @staticmethod
    def word_count(text):
        words = re.findall(r"\w+", text)
        return len(words)
    
    @staticmethod
    def markdown_to_text(markdown_text):
        html = markdown.markdown(markdown_text)
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()

    @staticmethod
    def estimate_reading_time(post, word_per_minute=250, seconds_per_image=10, seconds_per_tag=2):

        post_body = PostReadTimeEngine.markdown_to_text(str(post.body))
        post_title = str(post.title)

        body_word_count = PostReadTimeEngine.word_count(post_body)
        title_word_count = PostReadTimeEngine.word_count(post_title)
        total_word_count = body_word_count + title_word_count

        reading_time = total_word_count / word_per_minute

        if post.cover:
            reading_time += seconds_per_image / 60
        
        tag_count = post.tags.count()
        reading_time += (tag_count * seconds_per_tag) / 60

        reading_time = ceil(reading_time)

        return reading_time
