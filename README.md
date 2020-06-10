# maze-generator-python
A program for generating random and complete mazes, I made using Python and pygame...
So this is one of my favorite uses of backtracking... At it's core, this algorithm is used when you require ALL nodes of graph to
be traversed, in a random manner. I particualrly like this algorithm because it guarantees completeness and it's pleasant to 
visualize too. You can observe that the cursor will try to draw the longest path that it can and as long as it finds that its
backed in a corner it'll backtrack to the last cell where it had a valid available path...

# dependencies
## pygame
for installing pygame open your command line and enter `pip install pygame`
make sure both files are in same folder, and run "main.py"

