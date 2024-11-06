import time

class SpellChecker:
    def __init__(self, word_dict_file=None, n_gram_size=2):
        # Load the dictionary and store in lowercase
        with open(word_dict_file, 'r') as file:
            data = file.read().split(",")
            self.dictionary = list(set(word.strip().lower() for word in data))
        self.n_gram_size = n_gram_size
    
    def n_grams(self, word):
        """Generate n-grams for a given word."""
        return {word[i:i + self.n_gram_size] for i in range(len(word) - self.n_gram_size + 1)}

    def calculate_similarity(self, word1, word2):
        """Calculate similarity based on shared n-grams."""
        ngrams1 = self.n_grams(word1)
        ngrams2 = self.n_grams(word2)
        common_ngrams = ngrams1.intersection(ngrams2)
        return len(common_ngrams) / max(len(ngrams1), len(ngrams2))

    def check(self, string_to_check):
        """Set the string to be checked and split into words."""
        self.string_to_check = string_to_check.lower()
        self.words_to_check = self.string_to_check.split()

    def suggestions(self, threshold=0.3):
        """Provide suggestions based on n-gram similarity."""
        suggestions = {}
        for word in self.words_to_check:
            word_suggestions = []
            for dict_word in self.dictionary:
                similarity = self.calculate_similarity(word, dict_word)
                if similarity >= threshold:
                    word_suggestions.append((dict_word, similarity))
            # Sort suggestions by similarity and add the top suggestions
            suggestions[word] = sorted(word_suggestions, key=lambda x: -x[1])[:5]
        return suggestions

    def correct(self):
        """Return the corrected string based on the highest similarity suggestion."""
        corrected_words = []
        for word in self.words_to_check:
            best_match = max(self.suggestions()[word], key=lambda x: x[1], default=(word, 0))
            corrected_words.append(best_match[0])
        return " ".join(corrected_words)

# Usage
spell_checker = SpellChecker('words.txt')
string_to_be_checked = "gld narow"
spell_checker.check(string_to_be_checked)

# Getting suggestions and corrected output
print("Suggestions:", spell_checker.suggestions())
print("Corrected Text:", spell_checker.correct())

# Performance Metrics

start_time = time.time()
corrected_text = spell_checker.correct()
end_time = time.time()

speed = len(string_to_be_checked.split()) / (end_time - start_time)  

