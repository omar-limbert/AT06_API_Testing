class StringToLetterDictionary:

    @classmethod
    def convert_to_dictionary(cls, sentence_string):
        dictionary_result = {}
        for i in range(0, len(sentence_string) - 1):
            if sentence_string[i] != " ":
                dictionary_result[sentence_string[i].lower()] = sentence_string.count(sentence_string[i])

        return sorted(dictionary_result.items())
