class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        statements = []
        while self.current < len(self.tokens):
            statements.append(self.statement())
        return statements

    def statement(self):
        if self.match('LET'):
            return self.assignment()
        elif self.match('PRINT'):
            return self.print_statement()
        else:
            return self.expression_statement()

    def assignment(self):
        variable = self.consume('VARIABLE', 'Expected variable name after let')
        self.consume('ASSIGN', 'Expected = after variable')
        value = self.expression()
        self.consume('SEMICOLON', 'Expected ; after expression')
        return ('assignment', variable, value)

    def print_statement(self):
        self.consume('LPAREN', 'Expected ( after print')
        expr = self.expression()
        self.consume('RPAREN', 'Expected ) after expression')
        self.consume('SEMICOLON', 'Expected ; after print statement')
        return ('print', expr)

    def expression_statement(self):
        expr = self.expression()
        self.consume('SEMICOLON', 'Expected ; after expression')
        return ('expression', expr)

    def expression(self):
        return self.binary_operation()

    def binary_operation(self):
        expr = self.primary()

        while self.match('PLUS'):
            operator = self.previous()
            right = self.primary()
            expr = ('binary', operator, expr, right)

        return expr

    def primary(self):
        if self.match('NUMBER', 'STRING', 'BOOLEAN'):
            return self.previous()
        elif self.match('VARIABLE'):
            return ('variable', self.previous())
        else:
            raise SyntaxError('Expected expression')

    def match(self, *types):
        if self.current >= len(self.tokens):
            return False
        if self.tokens[self.current][0] in types:
            self.current += 1
            return True
        return False

    def consume(self, type, message):
        if self.match(type):
            return self.previous()
        raise SyntaxError(message)

    def previous(self):
        return self.tokens[self.current - 1][1]
