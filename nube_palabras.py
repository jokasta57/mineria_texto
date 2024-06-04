import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 0.- Instalar
# pip install --upgrade pip
# pip install --upgrade Pillow
# pip install wordcloud nltk matplotlib

# Descargar datos necesarios de nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Leer el archivo de texto
file_path = 'derechos_humanos_IA.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Función para limpiar el texto
def limpiar_texto(text):
    # Convertir a minúsculas
    text = text.lower()
    # Tokenizar el texto
    words = word_tokenize(text)
    # Eliminar puntuación y palabras vacías
    words = [word for word in words if word.isalpha()]
    stop_words = set(stopwords.words('spanish'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Limpiar el texto
texto_limpio = limpiar_texto(text)

# Crear una nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_limpio)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nube de Palabras')
plt.show()
