def json_formatter(json_string: str, indentor: str = '  ') -> str:
    res = ''
    indent_level = 0
    temp = ''
    for i, char in enumerate(json_string):
        if char in '{[':
            res += indentor * indent_level + temp.strip() + char + '\n'
            indent_level += 1
            temp = ''
        elif char in '}]':
            res += indentor * indent_level + temp.strip() + '\n' + indentor * (indent_level - 1) + char
            indent_level -= 1
            temp = ''
        elif char in ',':
            res += indentor * (0 if json_string[i - 1] in '{}[]' else indent_level) + temp.strip() + char + '\n'
            temp = ''
        else:
            temp += char
    return res


def dict_raise_on_duplicates(ordered_pairs):
    """
    Reject duplicate keys
    """
    my_dict = {}
    for key, values in ordered_pairs:
        if key in my_dict:
            raise ValueError("Duplicate key: {}".format(key,))
        else:
            my_dict[key] = values
    return my_dict


from queue import LifoQueue


def reverse_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}


def is_valid_brackets(text: str):
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    brackets_close = reverse_dict(brackets)
    stack = LifoQueue()

    for c in text:
        if c in brackets:
            stack.put(c)

        elif c in brackets_close:
            if (not stack.empty()) and stack.get_nowait() != brackets_close[c]:
                return False

    return stack.empty()


valid_json = """{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}"""


invalid_json = "({)}"

print(is_valid_brackets(valid_json))
print(is_valid_brackets(invalid_json))
