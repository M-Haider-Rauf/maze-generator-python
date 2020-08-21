# maze-generator-python
A program for generating random and complete mazes, I made using Python and pygame...
So this is one of my favorite uses of backtracking... At it's core, this algorithm is used when you require ALL nodes of graph to
be traversed, in a random manner. By this means it's a simple Breadth First Search (but neighbour nodes selected randomly)
I particualrly like this algorithm because it guarantees completeness and it's pleasant to 
visualize too. You can observe that the cursor will try to draw the longest path that it can and as long as it finds that its
backed in a corner it'll backtrack to the last cell where it had a valid available path... The image of generated image is saved at exit.

# dependencies
pygame


![img](https://i.ibb.co/C7jF0dW/sc-1597993104.png)
## a maze generated using my program
