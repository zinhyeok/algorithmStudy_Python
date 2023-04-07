

N = int(input())
must_in = "666"
count = 0
movie_num = 666
while True:
    if must_in in str(movie_num):
        count += 1
    if count==N:
        break
    movie_num += 1

print(movie_num)