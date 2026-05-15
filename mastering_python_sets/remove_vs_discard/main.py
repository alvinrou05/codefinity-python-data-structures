marvel_movies = {
    'Avengers: Endgame',
    'Black Panther',
    'Iron Man',
    'The Dark Knight',
    'Spider-Man: No Way Home',
    'Guardians of the Galaxy',
    'Justice League'
}

# Write your code here
marvel_movies.remove("The Dark Knight") #remove删除没有对应的字符串会直接报错结束执行

marvel_movies.discard("Justice League") #discard就算字符串没有找到也是继续下一步

# Testing
print("Updated set:", marvel_movies)