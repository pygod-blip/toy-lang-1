import re

# Token types
TOKEN_TYPES = [
    ('NUMBER', r'\d+(\.\d*)?'),     # Matches numbers, e.g., 123, 45.67
    ('STRING', r'"([^"\\]|\\.)*"'), # Matches strings, e.g., "hello"
    ('BOOLEAN', r'true|false'),     # Matches booleans, true or false
    ('VARIABLE', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Matches variable names
    ('PLUS', r'\+'),                # Matches the + operator
    ('ASSIGN', r'='),               # Matches the = symbol
    ('PRINT', r'print'),            # Matches the print keyword
    ('LET', r'let'),                # Matches the let keyword
    ('LPAREN', r'\('),              # Matches the left parenthesis (
    ('RPAREN', r'\)'),              # Matches the right parenthesis )
    ('SEMICOLON', r';'),            # Matches the semicolon ;
]

# Combine all token types into a single regular expression
TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)

def tokenize(program):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, program):
        token_type = match.lastgroup
        token_value = match.group()
        tokens.append((token_type, token_value))
    return tokens
