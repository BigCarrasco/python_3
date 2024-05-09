##hard note: I had to find the correct anwer in internet

'''
Your task is to write a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. 
If end is not the result of an integer number of steps, then don't add it to the sum.
See the 4th example below.

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)

'''
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    elif (end - begin) % step != 0:
        end -= (end - begin) % step
    num_terms = (end - begin) // step + 1
    return (begin + end) * num_terms // 2

# Test cases
print(sequence_sum(2, 6, 2))  # Output: 12 (2 + 4 + 6 = 12)
print(sequence_sum(1, 5, 1))  # Output: 15 (1 + 2 + 3 + 4 + 5 = 15)
print(sequence_sum(1, 5, 3))  # Output: 5 (1 + 4 = 5)
print(sequence_sum(10, 1, 1))  # Output: 0 (begin > end)
print(sequence_sum(0, 10, 3))  # Output: 18 (0 + 3 + 6 + 9 = 18)