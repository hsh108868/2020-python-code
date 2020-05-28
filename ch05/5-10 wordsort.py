word = list('삶꿈정')
word.extend('복빛')
print(word)
word.sort() #오름차순 정렬
print(word)

fruit = ['복숭아', '자두', '골드키위', '귤']
print(fruit)
fruit.sort(reverse=True) #내림차순 정렬
print(fruit)

mix = word + fruit
print(sorted(mix))
print(sorted(mix, reverse=True))