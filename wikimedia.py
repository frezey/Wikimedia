import wikipedia

def search_articles(query, language):
  wikipedia.set_lang(language)
  articles = wikipedia.search(query)
  result = { article: wikipedia.summary(article, sentences=1) for article in articles }
  for i in range(0, len(result)-1):
    print "[{}] {}".format(i + 1, result.keys()[i])
    print "{}\n".format(result.values()[i])
search_articles("Apple", "fr")
