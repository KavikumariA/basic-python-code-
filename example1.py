from collections import Counter, namedtuple
a = "aaaafyghjnjjljknhu"
print(Counter(a))
b = Counter(a)
print(b.most_common(2))
