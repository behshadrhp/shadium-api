import re
from math import ceil


class PostReadTimeEngine:

    @staticmethod
    def word_count(text):
        words = re.findall(r"/w", text)
        return len(words)
    
    @staticmethod
    def estimate_reading_time(post, word_per_minute=250, seconds_per_image=10, seconds_per_tag=2):
        post_body = PostReadTimeEngine.word_count(post.body)
        post_title = PostReadTimeEngine.word_count(post.title)

        total_word_count = post_body + post_title

        reading_time = total_word_count / word_per_minute

        if post.cover:
            reading_time += seconds_per_image / 60
        
        tag_count = post.tags.count()
        reading_time += (tag_count * seconds_per_tag) / 60

        reading_time = ceil(reading_time)

        return reading_time
