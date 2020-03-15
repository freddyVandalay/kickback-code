"""
Balanced bracket evaluation
"""


def is_balanced_expression(input_string):
	"""
	This function evaluates a string in regards to balanced brackets.

	:param input_string: string expression to be evaluated
	:type input_string: str
	:return: Boolean expression where True = balanced string and False = unbalanced string
	:rtype: bool
	"""
	# Initiate list object
	stack = list()
	# Define open/closing brackets
	open_brackets = ["(", "{", "["]
	closing_brackets = [")", "}", "]"]

	for ch in input_string:
		if ch in open_brackets:
			stack.append(ch)
		elif ch in closing_brackets:
			if stack and open_brackets[closing_brackets.index(ch)] == stack[-1]:
				stack.pop()
			else:
				return False

	return bool(stack) is False


if __name__ == "__main__":
	test_balanced_strings = ["()", "(())", "{(([]))}", "{{}}[]", "[](){}", "{{}}{}()[]"]
	test_unbalanced_strings = [")(", "{()", "[][])", "}}}}", "((()", "[{](){}", "{{(([]))}"]
	test_strings = [*test_balanced_strings, *test_unbalanced_strings]

	for test_no, test_string in enumerate(test_strings):
		print(f"Test {test_no} - {test_string} \nIs balanced: {is_balanced_expression(test_string)} \n")
