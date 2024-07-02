# toy-lang-1
it's a very crude coding language i made.
the syntax is quite simple:
To create an integer variable, use the integer command followed by the variable name and its initial value. For example:
integer my_var = 42

To update an existing variable, use the set command:
set my_var = 100

Creating Functions:
Define a function using the function command. Specify the function name, parameters, and the code block. For instance:
function add(a, b) {
    return a + b
}

To call a function, use the call command:
call add 10 20

Conditional Statements:
Use if statements to execute code conditionally:
if my_var > 50 {
    print "Large value"
} else {
    print "Small value"
}

Loops:
Create a while loop with a condition:
while my_var < 100 {
    my_var = my_var + 10
}

Or use a for loop:
for i = 0 to 5 step 2 {
    print i
}

Class Definitions:
Define a class using the defclass command:
defclass MyClass extends BaseClass

Add methods to the class using defmethod:
defmethod MyClass my_method(x, y) {
    return x * y
}

Remember to adapt the examples above to your specific use case. Feel free to explore and experiment with your ToyLanguageInterpreter
