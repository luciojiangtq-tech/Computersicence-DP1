
#def superdigit(n):
#    ans = sum([int(i) for i in str(n)])
#    if len(ans) == 1:
#        return ans
#    else:
#        return ans + superdigit(ans)


def superdigit2(n):
    if len(str(n)) == 1:
        return n
    return superdigit2(sum([int(i) for i in str(n)]))


def palindrome(n):
    if len(str(n)) == 1:
        return True
    if str(n)[1] == str(n)[-1]:
        palindrome(int(list(n)[1:-1]))
    else:
        return False
    pass
#……？

if palindrome(121):
    print("yes")
print(superdigit2(33550336))


     