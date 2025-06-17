from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Your text input
text = "a man is honest intelligent good honest"

# Create the WordCloud object
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=STOPWORDS
).generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Remove axis
plt.show()
