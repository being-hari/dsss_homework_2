import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_problem_result


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Generated number {rand_num} is out of range!")

    def test_generate_random_operator(self):
        """
        Test if the random operator is one of the valid operators: '+', '-', '*'.
        """
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random selections
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators, f"Invalid operator: {operator}")

    def test_calculate_problem_result(self):
        """
        Test if the problem string and the result are calculated correctly.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (3, 4, '*', '3 * 4', 12),
            (9, 3, '-', '9 - 3', 6),
            (6, 2, '+', '6 + 2', 8),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_problem_result(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem mismatch: expected {expected_problem}, got {problem}")
            self.assertEqual(answer, expected_answer, f"Answer mismatch: expected {expected_answer}, got {answer}")
            print(answer)
            print(problem)

if __name__ == "__main__":
    unittest.main()
