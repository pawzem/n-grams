# n-grams
project which will find digrams and trigrams of given text 

run model creation:
ngrams.py language_name input.txt output.json

inputs for models"
fr - http://www.gutenberg.org/cache/epub/58501/pg58501.txt
de- http://www.gutenberg.org/cache/epub/39277/pg39277.txt
cz- https://manybooks.net/titles/zapisky-z-mrtveho-domu?ga_submit=lrf:wYPn083k0jJtKgu
hun- https://manybooks.net/titles/petofi-sandor-osszes-koltemenyei

requires nltk.download('punkt')


run analisys:
ngrams.py analise model_location.json analise_input/text_input.txt
