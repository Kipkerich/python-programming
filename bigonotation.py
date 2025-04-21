# Example of O(1)
colors = ['red', 'blue', 'green', 'yellow']

def constant(colors):
    print(colors[0])

constant(colors)

#Example of O(n)
def linear(colors):
    for color in colors:
        print(color)

linear(colors)

#Example of O(n^2)
def quadratic(colors):
    for color in colors:
        for color2 in colors:
            print(color, color2)
            
quadratic(colors)

#Example of O(n^3)
def cubic(colors):
    for color in colors:
        for color2 in colors:
            for color3 in colors:
                print(color, color2, color3)

cubic(colors)