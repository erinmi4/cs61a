from urllib.request import urlopen

shakespeare = urlopen('https://www.composingprograms.com/shakespeare.txt')

words = set(shakespeare.read().decode().split())

