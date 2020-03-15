"""
Balanced bracket evaluation
"""


def is_balanced_expression(test_str):
	"""
	This function evaluates a string in regards to balanced brackets.

	:param test_str: string expression to be evaluated
	:type test_str: str
	:return: Boolean expression where True = balanced string and False = unbalanced string
	:rtype: bool
	"""
	stack = list()
	# Define open/closing brackets
	open_brackets = ["(", "{", "["]  # List operation: add
	closing_brackets = [")", "}", "]"]  # List operation: remove

	for ch in test_str:
		if ch in open_brackets:
			stack.append(ch)
		elif ch in closing_brackets:
			if stack and open_brackets[closing_brackets.index(ch)] == stack[-1]:
				stack.pop()
			else:
				return False
	# Evaluate if stack/list is empty. If so: balanced and returns True
	return bool(stack) is False


if __name__ == "__main__":
	test_balanced_strings = ["()", "(())", "{(([]))}", "{{}}[]", "[](){}", "{{}}{}()[]"]
	test_unbalanced_strings = [")(", "{()", "[][])", "}}}}", "((()", "[{](){}", "{{(([]))}"]
	test_strings = [*test_balanced_strings, *test_unbalanced_strings]

	for test_no, test_string in enumerate(test_strings):
		print(f"Test {test_no} - {test_string} \nIs balanced: {is_balanced_expression(test_string)} \n")
