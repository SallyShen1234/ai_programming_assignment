def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in the given string."""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count

# Test the function
print(count_vowels("Data Science is amazing!"))
