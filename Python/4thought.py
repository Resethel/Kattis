# Using Python 3
# https://open.kattis.com/problems/4thought

operators = [' // ', ' + ', ' - ', ' * ']

# First, create the dictionnary of all the solutions
if __name__ == "__main__":
    solutions = dict()
    for a in operators:
        for b in operators:
            for c in operators:
                expression = "4{:s}4{:s}4{:s}4".format(a, b, c)
                result = eval(expression)
                # Store the dictionnary the value with the expression corresponding to it
                solutions[result] = "{:s} = {:d}".format(expression.replace('//', '/'), result)

    # Then ask N times the user to input a solution
    # and check the result is in the table of solutions
    N = int(input())
    for _ in range(N):
        value = int(input())
        if value not in solutions:
            print("no solution")
        else:
            print(solutions[value])
