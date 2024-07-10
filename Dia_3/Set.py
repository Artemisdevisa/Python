s1 = {1, 2, 3}
s2 = set({1, 2, 3})
s3 = s1.union(s2)
s3.add(4)
s3.discard(6)
print(s3)