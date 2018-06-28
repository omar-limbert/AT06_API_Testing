class Replace:

    @classmethod
    def replace_in_string(cls, string_value, string_to_replace, new_string):
        split_string = string_value.split(string_to_replace)
        return new_string.join(split_string)
