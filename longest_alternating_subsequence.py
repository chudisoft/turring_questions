def longest_alternating_subsequence(X):
    if not X:
        return 0

    count = 1  # Always include the first element
    for i in range(1, len(X)):
        if X[i] != X[i - 1]:
            count += 1

    return count

print(longest_alternating_subsequence([0, 1, 0, 1, 0]))  # Output: 5
print(longest_alternating_subsequence([0]))              # Output: 1
print(longest_alternating_subsequence([1, 1, 1, 1]))      # Output: 1
print(longest_alternating_subsequence([0, 1, 1, 0, 1]))   # Output: 4
