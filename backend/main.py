from parser.parser import get_parser
from parser.extractor import extract_functions

def test_parser():
    parser = get_parser()

    with open("sample.c", "rb") as f:
        code = f.read()

    tree = parser.parse(code)
    funcs = extract_functions(tree, code)

    for i, func in enumerate(funcs):
        print(f"\nFunction {i+1}:\n")
        print(func["code"])

if __name__ == "__main__":
    test_parser()