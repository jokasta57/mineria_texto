import nltk
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Descargar datos necesarios de nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Leer el archivo de texto
file_path = 'implementacion_IA.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

#Limpiar el texto:
def limpiar_texto(text):
    # Convertir a minúsculas
    text = text.lower()
    # Tokenizar el texto
    words = word_tokenize(text)
    # Eliminar puntuación y palabras vacías
    words = [word for word in words if word.isalpha()]
    stop_words = set(stopwords.words('spanish'))
    words = [word for word in words if word not in stop_words]
    return words

words = limpiar_texto(text)

#Crear una tabla de frecuencias de palabras:
from collections import Counter

# Contar la frecuencia de las palabras
frecuencia_palabras = Counter(words)

# Convertir a DataFrame
df_frecuencia_palabras = pd.DataFrame(frecuencia_palabras.items(), columns=['word', 'frequency']).sort_values(by='frequency', ascending=False)


# Visualizar las palabras más frecuentes:
# Mostrar las 20 palabras más frecuentes
top_n = 20
df_top_words = df_frecuencia_palabras.head(top_n)

plt.figure(figsize=(10, 8))
plt.barh(df_top_words['word'], df_top_words['frequency'], color='skyblue')
plt.xlabel('Frecuencia')
plt.title('Frecuencia de Palabras')
plt.gca().invert_yaxis()
plt.show()


#6.- Generar una nube de palabras:

# Crear y mostrar una nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frecuencia_palabras)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()






















