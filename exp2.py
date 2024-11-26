def fsa_match(string):
    # Define states
    state = "START"
    # Process each character in the string
    for char in string:
        if state == "START":
            if char == 'a':
                state = "A"  # Transition to state A
            else:
                state = "START"  # Remain in the START state
        elif state == "A":
            if char == 'b':
                state = "AB"  # Transition to state AB
            elif char == 'a':
                state = "A"  # Stay in state A
            else:
                state = "START"  # Back to START
        elif state == "AB":
            if char == 'a':
                state = "A"  # Go to state A
            else:
                state = "START"  # Back to START
    
    # Accept if the final state is "AB"
    return state == "AB"

# Test the FSA
test_strings = ["ab", "aab", "babab", "helloab", "ababab", "abc"]
for test in test_strings:
    result = fsa_match(test)
    print(f"String '{test}' ends with 'ab': {result}")
