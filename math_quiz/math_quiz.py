import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.

    Arguments:
        min_value (int or float): The lower bound for the random number.
        max_value (int or float): The upper bound for the random number.

    Returns:
        int: A random integer between min_value and max_value.

    """
    try:
        # Convert min and max to integers
        return random.randint(int(min_value), int(max_value))
    except ValueError as e:
        print(f"Error generating random integer: {e}")
        raise  # Re-raise the exception for the caller to handle

def generate_random_operator():
    """
    Generates a random operator from the set {+, -, *}.

    Returns:  A random operator as a string.
    """
    return random.choice(['+', '-', '*'])

def calculate_problem_result(num1, num2, operator):
    """
    Calculates the result of a mathematical operation on num1 and num2 based on the operator.

    Args:
        num1 (int): The first number in the operation.
        num2 (int): The second number in the operation.
        operator (str): The operator for the operation ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the problem as a string and the result of the operation.
    """
    problem = f"{num1} {operator} {num2}"
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise ValueError(f"Unsupported operator: {operator}")
    
    return problem, result

def math_quiz_game():
    """
    Runs the Math Quiz Game where the player is asked a series of math questions.

    The game will generate a random math problem for the user, and the user will have to provide the correct answer.
    The game continues for a pre-set number of questions, and the player's score is displayed at the end.
    """
    score = 0  # The player's score starts at 0
    total_questions = 3  # Number of questions to ask in the game

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the number of questions
    for _ in range(int(total_questions)):
        try:
            # Generate random numbers and an operator
            num1 = generate_random_integer(1, 10)
            num2 = generate_random_integer(1, 5.5)  # The second number could be float but will be truncated
            operator = generate_random_operator()

            # Generate the problem and its correct answer
            problem, correct_answer = calculate_problem_result(num1, num2, operator)

            # Display the problem and ask for the user's answer
            print(f"\nQuestion: {problem}")
            user_input = input("Your answer: ")

            # Attempt to convert the user's input to an integer
            try:
                user_answer = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue  # Skip this iteration if input is invalid

            # Check if the user's answer is correct
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")

        except ValueError as e:
            # Handle any value errors (e.g., invalid operator)
            print(f"Error: {e}")
            break  # End the game if an error occurs

    print(f"\nGame over! Your final score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_game()
