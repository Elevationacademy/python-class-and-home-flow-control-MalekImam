def my_accumulate(sequence_number):
    sequence_result = []
    sum = 0
    for i, num in enumerate(sequence_number):
        sum += num
        sequence_result[i] = sum
    return sequence_result
