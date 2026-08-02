# Find the longest substring without repeating characters.
text = input("Enter a Text: ")

longest = ""

for i in range(len(text)):
    current = ""
    for j in range(i, len(text)):
        if text[j] not in current:
            current += text[j]
            if len(current) > len(longest):
                longest = current
        else:
            break
print("Longest substring:", longest)
print("Length:", len(longest))


# Check whether a string is a valid palindrome ignoring spaces and punctuation.
text = input("Enter a String: ")

clean = ""

for ch in text:
    if ch.isalnum():
        clean += ch.lower()

if clean == clean[::-1]:
    print("Valid Palindrome")
else:
    print("Not a Palindrome")


# Find the longest palindromic substring.
text =input("Enter a String: ")

longest = ""

for i in range(len(text)):
    for j in range(i, len(text)):
        sub = text[i:j+1]
        if sub == sub[::-1]:
            if len(sub) > len(longest):
                longest = sub

print("Longest Palindromic Substring:", longest)
print("Length:", len(longest))


# Determine if one string can be formed from another string.
source = input("Enter Source String: ")
target = input("Enter target String: ")

possible = True

for ch in target:
    if target.count(ch) > source.count(ch):
        possible = False
        break
if possible:
    print("Yes, target can be formed.")
else:
    print("No, target cannot be formed.")


# Find the common characters between two strings.
str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

common = ""

for ch in str1:
    if ch in str2 and ch not in common:
        common += ch
print("Common Characters:", common)


# Find the minimum number of character deletions required to make two strings anagrams.
string1 = input("Enter First String: ")
string2 = input("Enter Second String: ")

deletions = 0

for ch in set(string1 + string2):
    deletions += abs(string1.count(ch) - string2.count(ch))

print("Minimum Deletions:", deletions)


# Group a list of words into anagram groups.
words = input("Enter words separated by space: ").split()

groups = {}

for word in words:
    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print("Anagram Groups:")

for group in groups.values():
    print(group)
    

# Find all substrings of a string.
text = input("Enter a String: ")

print("Substring: ")

for i in range(len(text)):
    for j in range(i, len(text)):
        print(text[i:j+1])


# Find all permutations of a string.
def permute(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        permute(left + right, ans + ch)

text = input("Enter a String: ")

print("Permutations:")
permute(text)


# Count all palindromic substrings in a string.
text = input("Enter a String: ")
count = 0

for i in range(len(text)):
    for j in range(i, len(text)):
        sub = text[i:j+1]
        if sub == sub[::-1]:
            count += 1

print("Total Palindromic Substrings:", count)