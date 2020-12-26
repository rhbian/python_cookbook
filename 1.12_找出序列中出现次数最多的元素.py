from collections import Counter
words = ["this", "is", "an", "apple", "this", "is", "a", "pen", "this", "is", "what"]

print(Counter(words).most_common(3))

word_counts = Counter(words)
print(word_counts["this"])

morewords = ["why", "are",  "this", "you", "not", "looking", "in", "my", "eyes"]
# for word in morewords:
#     word_counts[word] += 1

# 使用update方法来更新
word_counts.update(morewords)
print(word_counts["this"])

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
print(a+b)
print(a-b)
