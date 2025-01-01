from pydantic import BaseModel, validate_call

from .Utils import is_braces, is_space


class InputValidator(BaseModel):

    @staticmethod
    @validate_call
    def validate_input(user_input: str) -> list[str] | None:
        argv = []
        word = ""
        braces = False
        size = len(user_input)

        try:
            for index in range(size):
                if len(argv) >= 4:
                    return argv

                if braces and not is_braces(user_input[index]):
                    # useful in case of spaces
                    word += user_input[index]

                elif braces and is_braces(user_input[index]):
                    braces = False
                    argv.append(word[1:])
                    word = ""

                elif not braces and is_braces(user_input[index]):
                    braces = True
                    word += user_input[index]

                elif is_space(user_input[index]):
                    if word:
                        argv.append(word)
                        word = ""

                elif not is_space(word):
                    word += user_input[index]

                if braces and index == size - 1:
                    raise IndexError

                if index == size - 1 and not is_space(user_input[index]):
                    if word:
                        argv.append(word)

        except IndexError:

            print(f'Invalid input "{word}" doesn\'t have closing {word[0]}\n')
            return None

        return argv
