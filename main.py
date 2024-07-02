class ToyLanguageInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def parse_line(self, line):
        tokens = line.split()
        command = tokens[0]

        if command == "integer":
            var_name, value = tokens[1], int(tokens[3])
            self.variables[var_name] = value
        elif command == "set":
            var_name, value = tokens[1], int(tokens[3])
            self.variables[var_name] = value
        elif command == "add":
            var1, var2 = tokens[1], tokens[2]
            self.variables[var1] += self.variables[var2]
        elif command == "print":
            var_name = tokens[1]
            print(f"Result: {self.variables.get(var_name, 'Variable not found')}")
        elif command == "function":
            func_name, params, code = tokens[1], tokens[3:-1], " ".join(tokens[4:-1])
            self.functions[func_name] = (params, code)
        elif command == "call":
            func_name, args = tokens[1], tokens[2:]
            if func_name in self.functions:
                func_params, func_code = self.functions[func_name]
                local_vars = {param: self.variables[arg] for param, arg in zip(func_params, args)}
                self.execute_code(func_code, local_vars)
            else:
                print(f"Function '{func_name}' not defined.")
        elif command == "if":
            condition, true_code, false_code = tokens[1], " ".join(tokens[3:-2]), tokens[-1]
            if eval(condition, self.variables):
                self.execute_code(true_code, {})
            else:
                self.execute_code(false_code, {})
        elif command == "while":
            condition, loop_code = tokens[1], " ".join(tokens[3:-1])
            while eval(condition, self.variables):
                self.execute_code(loop_code, {})
        elif command == "for":
            var_name, start, end, step = tokens[1], int(tokens[3]), int(tokens[5]), int(tokens[7])
            for value in range(start, end, step):
                self.variables[var_name] = value
                self.execute_code(" ".join(tokens[8:-1]), {})
        elif command == "defclass":
            class_name, base_class = tokens[1], tokens[3]
            self.variables[class_name] = {}
            self.variables[class_name]["__base__"] = base_class
        elif command == "defmethod":
            class_name, method_name, params, code = tokens[1], tokens[3], tokens[5:-1], " ".join(tokens[6:-1])
            self.variables[class_name][method_name] = (params, code)
        else:
            print("Invalid command.")

    def execute_code(self, code, local_vars):
        for line in code.split(";"):
            self.parse_line(line.strip())
            self.variables.update(local_vars)

    def run(self):
        while True:
            line = input("> ")
            self.parse_line(line)

if __name__ == "__main__":
    interpreter = ToyLanguageInterpreter()
    interpreter.run()
