xi = [0.3, 0.4]
yi = [0.5477, 0.6325]

x0 = 0.35
result = 0

for i in range(len(xi) ):
    l = 1

    for j in range(len(xi) ):
        if j != i:
            l = l * ( (x0 - xi[j] ) / (xi[i] - xi[j] ) )

    result = result + l * yi[i]

print(result)