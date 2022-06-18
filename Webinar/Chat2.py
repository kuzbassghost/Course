
import json
from sklearn.feature_extraction.text import CountVectorizer

config_file = open("/content/big_bot_config.json", "r")
BIG_CONFIG = json.load(config_file)

BIG_CONFIG.keys()

dict_keys(['intents', 'failure_phrases'])

len(BIG_CONFIG["intents"])

X = [] # Фразы
y = [] # Намерения

# Собираем фразы и интенты из BIG_CONFIG в X,y
for name, intent in BIG_CONFIG["intents"].items():
  for example in intent["examples"]:
    X.append(example)
    y.append(name)

len(X)

# Подготовка данных к обучению модели
# NLP = Natural Language Processing

# Векторайзер = превращает тексты в наборы чисел (вектора)

# Мама круто мыла раму => [1,2,3,4]
# Круто мама раму мыла => [2,1,4,3]
# Мыла мама круто раму => [3,1,2,4]

vectorizer = CountVectorizer() # Можно указать настройки
vectorizer.fit(X) # Учится вот эти конкретные тексты превращать в числа

CountVectorizer()

arr = vectorizer.transform(["друг друг друг друг привет"]).toarray()[0]
for a in arr:
  if a!=0:
    print(a, end=',')






