# Genetic Algorithm Applications in Artificial Creativity

## Conrad Dudziak

This capstone project studies the literature of genetic algorithms and their application to artificial creativity.
Genetic algorithms allow a computer to narrow a problem set through simulated evolution as prescribed in
Darwin’s theory of natural selection. To accomplish this evolutionary behavior, this capstone project follows
the construction of a genetic algorithm capable of recreating any image from a set of colored polygons.
Ultimately, this project resulted in a web hosted application that receives user input in the form of reference
images and configuration data. Through github pages and azure web services, the genetic algorithm is designed
to use HTTP requests to compute and return a stylized version of the input image, along with data on best-
fitness, average-fitness, and generational iterations.

Furthermore, this capstone project explores the adaptability of a generalized genetic algorithm implemented
with object-oriented programming. As a result, an API for the genetic algorithm was constructed with simple
integration into a wide variety of applications where the internal implementation of the DNA can be altered and
specified without refactoring the external behaviors of the population set.

Lastly, this capstone project offers an analysis on the tradeoffs of different fitness functions and breeding
strategies through the comparisons of generational iterations and accuracy scores. Primarily, this project
explores two breeding strategies: Parent breeding and mutation dependence. Parent breeding is a breeding
function dependent on two parenting individuals, where the parents randomly provide a resulting child with a
polygon. Mutation dependence is a breeding method that does not cross DNA sequences between individuals.
Rather, the best-fit individual in the population is monitored and replaced upon the random positive mutation
of another individual in the population. In this way, the only mechanism that introduces variation into the
population is mutation.

As a result, mutation dependence produced a 16% more best-fit individual than parent breeding in
approximately 49000 less iterations when at least 33% of the target image consisted of a single solid color.
In conclusion, object-oriented genetic algorithms dependent on random mutative breeding are a strong option
for the implementation of an image creating program.
