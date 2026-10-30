from detection import check_transaction

# Test Case 1
result1 = check_transaction(
    amount=60000,
    is_new_recipient=True,
    failed_attempts=3,
    unusual_time=True
)

print("Test Case 1")
print(result1)

print("-------------------")

# Test Case 2
result2 = check_transaction(
    amount=2000,
    is_new_recipient=False,
    failed_attempts=0,
    unusual_time=False
)

print("Test Case 2")
print(result2)