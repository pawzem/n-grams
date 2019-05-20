import sys
import nltk
import json
from collections import Counter
import matplotlib.pyplot as plt


def main():
    if sys.argv[1] == 'analise':
        analise_text()
    else:
        generate_model()


def analise_text():
    print("analysing given text\n")
    reference_model_location = sys.argv[2]
    reference_model_file = open(reference_model_location, "r", encoding="utf8")
    reference_model = json.load(reference_model_file)
    input_model_location = sys.argv[3]
    input_model = prepare_model_analysis(input_model_location)
    plot_from_model(input_model, reference_model, 'digrams')
    plot_from_model(input_model, reference_model, 'trigrams')
    plot_from_model(input_model, reference_model, 'characters')


def plot_from_model(input_model, reference_model, model_type):
    ngram_output_reference_dict = {}
    ngram_output_input_dict = {}
    for input_key in input_model[model_type].keys():
        if input_key in reference_model[model_type].keys():
            ngram_output_reference_dict[input_key] = reference_model[model_type][input_key]
            ngram_output_input_dict[input_key] = input_model[model_type][input_key]
    plt.plot(list(ngram_output_reference_dict.keys()), list(ngram_output_reference_dict.values()), 'r--',
             label='reference model')
    plt.plot(list(ngram_output_input_dict.keys()), list(ngram_output_input_dict.values()), 'b--', label='input model')
    plt.xlabel('tokens')
    plt.ylabel('frequency')
    plt.title(model_type)
    plt.gca().legend(('reference model', 'input model'))
    plt.show()


def generate_model():
    print("performing analysis of digrams, trigrams and special chars\n")
    file_name = sys.argv[2]
    analysis = prepare_model_analysis(file_name)
    json_dumps = json.dumps(analysis)
    output_file = open(sys.argv[3], 'wt', encoding="utf8")
    output_file.write(json_dumps)


def prepare_model_analysis(file_name):
    file = open(file_name, "rt", encoding="utf8")
    lines = file.readlines()
    file.close()
    analysis = ngrams_analysis(lines)
    analysis['language'] = sys.argv[1]

    return analysis


def ngrams_analysis(lines):
    text = ''
    for line in lines:
        text += line
    tokens = nltk.word_tokenize(text)

    trigrams = nltk.trigrams(tokens)
    bigrams = nltk.bigrams(tokens)

    digrams = analize(bigrams, len(text))
    trigrams = analize(trigrams, len(text))
    characters = analize_characters(text)

    return {'digrams': digrams, 'trigrams': trigrams, 'characters': characters}


def analize_characters(text):
    result = {}
    counts = Counter(text)
    for character, count in counts.items():
        result[character] = count / len(text)
    return result


def analize(ngrams, length):
    result = {}
    dist = nltk.FreqDist(ngrams)
    for ngram, count in dist.items():
        result["{}".format(ngram)] = count / length
    return result


if __name__ == "__main__":
    main()
