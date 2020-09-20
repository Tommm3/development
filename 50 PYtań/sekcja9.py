# import string
#
# x = 'myszydokazujągdykotanieczują'
# D = {}
# count = 0
# for character in string.ascii_lowercase:
#     if character in x:
#         D[character] = x.count(character)
#
# print(D)

# x = 'myszydokazujągdykotanieczują'
# D = {}
#
# for character in x:
#     if character not in D:
#         D[character] = 1
#     else:
#         D[character] += 1
#
# print(D)

S = {x:x+1 for x in range(10000) if x%23 == 0}

print(7430 in S)
