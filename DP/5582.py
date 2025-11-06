a = input().rstrip()
b = input().rstrip()

def get_longest_common_string(a,b):
    pre = [0] * len(b)

    max_len = 0
    
    for i in range(len(a)):
        now = [0] * len(b)
        for j in range(len(b)):
            if a[i] == b[j]:
                if j == 0:
                    now[j] = 1
                else:
                    now[j] = pre[j-1] +1
                    max_len = max(max_len, now[j])
        pre = now
    return max_len

print(get_longest_common_string(a,b))