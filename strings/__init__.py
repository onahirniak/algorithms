from .string_helper import StringHelper
class StringsRunner():
    @staticmethod
    def run():
        print("RABIN KARP")

        string_helper = StringHelper()

        sub_indexes = string_helper.rabin_karp("abcdefg", "de")

        print(sub_indexes)

        sub_indexes = string_helper.rabin_karp("abcdefg", "text")

        print(sub_indexes)