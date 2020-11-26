import Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

StopFactory = StopWordRemoverFactory()
stopwords = StopFactory.get_stop_words()
stopwords2 = StopFactory.get_stop_words()

# Add stopword
stopwords2.append('tambahannich')
# Remove stopword
stopwords.remove('ok')

print(stopwords)
print(stopwords2)
