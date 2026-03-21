from tree_sitter_languages import get_parser as tsl_get_parser


def get_parser():
    """Return a tree-sitter Parser configured for C using tree_sitter_languages.get_parser."""
    return tsl_get_parser("c")

