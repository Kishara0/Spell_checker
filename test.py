from fuzzywuzzy import fuzz
import time

# Load the word list
with open('words.txt', 'r') as f:
    dictionary = list(set(word.strip().lower() for word in f.read().split(",")))

# Define the test cases

test_cases = [
    {"input": "gld", "expected": "glad"},
    {"input": "narow", "expected": "narrow"},
    {"input": "arrea", "expected": "area"},
    {"input": "lite", "expected": "light"},
    {"input": "wid", "expected": "wide"},
    {"input": "brigt", "expected": "bright"},
    {"input": "cleen", "expected": "clean"},
    {"input": "clos", "expected": "close"},
    {"input": "streem", "expected": "stream"},
    {"input": "plce", "expected": "place"},
    {"input": "trvel", "expected": "travel"},
    {"input": "frend", "expected": "friend"},
    {"input": "famly", "expected": "family"},
    {"input": "hapy", "expected": "happy"},
    {"input": "littel", "expected": "little"},
    {"input": "exprss", "expected": "express"},
    {"input": "secnd", "expected": "second"},
    {"input": "srvice", "expected": "service"},
    {"input": "comfrt", "expected": "comfort"},
    {"input": "adventur", "expected": "adventure"}
]

class FuzzySpellChecker:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def correct(self, word):
        max_score = 0
        best_match = word
        for dict_word in self.dictionary:
            score = fuzz.ratio(word, dict_word)
            if score > max_score:
                max_score = score
                best_match = dict_word
        return best_match

    def suggestions(self, word):
        suggestions = sorted(
            [(dict_word, fuzz.ratio(word, dict_word)) for dict_word in self.dictionary],
            key=lambda x: -x[1]
        )[:5]
        return [s[0] for s in suggestions]

class NGramSpellChecker:
    def __init__(self, dictionary, n_gram_size=2):
        self.dictionary = dictionary
        self.n_gram_size = n_gram_size

    def n_grams(self, word):
        return {word[i:i + self.n_gram_size] for i in range(len(word) - self.n_gram_size + 1)}

    def calculate_similarity(self, word1, word2):
        ngrams1 = self.n_grams(word1)
        ngrams2 = self.n_grams(word2)
        return len(ngrams1.intersection(ngrams2)) / max(len(ngrams1), len(ngrams2))

    def correct(self, word):
        best_match = word
        max_similarity = 0
        for dict_word in self.dictionary:
            similarity = self.calculate_similarity(word, dict_word)
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = dict_word
        return best_match

    def suggestions(self, word):
        similarities = [
            (dict_word, self.calculate_similarity(word, dict_word))
            for dict_word in self.dictionary
        ]
        return [w[0] for w in sorted(similarities, key=lambda x: -x[1])[:5]]

# Initialize both spell checkers
fuzzy_checker = FuzzySpellChecker(dictionary)
ngram_checker = NGramSpellChecker(dictionary)

# Define metrics
metrics = {
    "Accuracy": [],
    "Speed (words/sec)": [],
    "Recall": [],
    "Precision": [],
    "Fixed": [],
    "Non-fixed with correction in top-5": [],
    "Broken": []
}

def evaluate_spell_checker(spell_checker, test_cases):
    fixed_count = 0
    top5_count = 0
    broken_count = 0
    start_time = time.time()

    for case in test_cases:
        input_word = case["input"]
        expected_word = case["expected"]

        # Get the top suggestion and top-5 suggestions
        top_suggestion = spell_checker.correct(input_word)
        top_5_suggestions = spell_checker.suggestions(input_word)

        if top_suggestion == expected_word:
            fixed_count += 1
        elif expected_word in top_5_suggestions:
            top5_count += 1
        else:
            broken_count += 1

    # Calculate speed
    end_time = time.time()
    words_per_sec = len(test_cases) / (end_time - start_time)

    # Calculate accuracy, recall, and precision
    total_cases = len(test_cases)
    accuracy = fixed_count / total_cases
    recall = fixed_count / (fixed_count + broken_count) if fixed_count + broken_count > 0 else 0
    precision = fixed_count / (fixed_count + top5_count) if fixed_count + top5_count > 0 else 0

    return {
        "Accuracy": accuracy,
        "Speed (words/sec)": words_per_sec,
        "Recall": recall,
        "Precision": precision,
        "Fixed": fixed_count,
        "Non-fixed with correction in top-5": top5_count,
        "Broken": broken_count
    }

# Evaluate both spell checkers
fuzzy_metrics = evaluate_spell_checker(fuzzy_checker, test_cases)
ngram_metrics = evaluate_spell_checker(ngram_checker, test_cases)

# Format results in table form
import pandas as pd

comparison_table = pd.DataFrame({
    "Metric": ["Accuracy", "Speed (words/sec)", "Recall", "Precision", "Fixed", "Non-fixed with correction in top-5", "Broken"],
    "FuzzyWuzzy Checker": [
        fuzzy_metrics["Accuracy"],
        fuzzy_metrics["Speed (words/sec)"],
        fuzzy_metrics["Recall"],
        fuzzy_metrics["Precision"],
        fuzzy_metrics["Fixed"],
        fuzzy_metrics["Non-fixed with correction in top-5"],
        fuzzy_metrics["Broken"]
    ],
    "NGram Checker": [
        ngram_metrics["Accuracy"],
        ngram_metrics["Speed (words/sec)"],
        ngram_metrics["Recall"],
        ngram_metrics["Precision"],
        ngram_metrics["Fixed"],
        ngram_metrics["Non-fixed with correction in top-5"],
        ngram_metrics["Broken"]
    ]
})

print(comparison_table)
