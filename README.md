<div id="top"></div>
<h3 align="center">CT421 Artificial Intelligence - Assignment 1</h3>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-repo">About The Repo</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#part-a">Part A</a>
      <ul>
        <li><a href="#i-one-max-problem">i): One-max problem</a></li>
        <li><a href="#ii-evolving-to-a-target-string">ii): Evolving to a target string</a></li>
        <li><a href="#iii-deceptive-landscape">iii): Deceptive Landscape</a></li>
        <li><a href="#iv-evolving-to-a-target-string-with-a-larger-alphabet">iv): Evolving to a target string with a larger alphabet</a></li>
      </ul>
    </li>
    <li>
      <a href="#part-b">Part B</a>
    </li>
  </ol>
</details>

<!-- ABOUT THE REPO -->
## About The Repo
This repo holds all of my code solutions for assignment 1 of CT421: Artificial Intelligence.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- BUILT WITH -->
### Built With
These solutions were written using the latest version of python (currently 3.10.2).
These are the requirements for using these scripts:
* [Python](https://www.python.org/downloads/) (3.10.1 or better)
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- PART A -->
## Part A

<!-- I: ONE-MAX PROBLEM -->
### i): One-max problem
Solution: [one_max.py](./one_max.py)<br>
This genetic algorithm uses a population of 30 bit-long ints. The target is
a bit-string with 1s in each position i.e. 1,073,741,823 base 10.
It uses a randomly generated population, standard mutation, one-point crossover
and tournament selections between generations. The average fitness of each
generation is then plotted using matplotlib.

The fitness of a chromosome is equal to how many binary 1 are present.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- II: EVOLVING TO A TARGET STRING -->
### ii): Evolving to a target string
Solution: [target_string.py](./target_string.py)<br>
This GA is an extension of the [One-max](#i-one-max-problem) algorithm. Here,
the target of all 1s is replaced by some random 30 bit integer which is
generated at runtime.

The fitness of a chromosome is equal to the number of bits it has in common
with the target string.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- III: DECEPTIVE LANDSCAPE -->
### iii): Deceptive Landscape
Solution: [deceptive_landscape.py](./deceptive_landscape.py)<br>
This GA is an extension of the [One-max](#i-one-max-problem) algorithm. This GA
is used to illustrate some of the shortcomings of the Genetic Algorithm. We
insert a second target alongside the 30 bit string with ones. We also reward a
bit-string of all 0s i.e. 0 base 10. A bit-string of 0 is scored double the
fitness of a bit-string with all ones.

It is observed that the GA never achieves the global optimum of 0. Even if a
value of 0 is present in the initial random population, it will be lost in
the next generation due to mutation and crossover.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- IV: EVOLVING TO A TARGET STRING WITH A LARGER ALPHABET -->
### iv): Evolving to a target string with a larger alphabet
Solution: [digit_target_string.py](./digit_target_string.py)<br>
This GA is an extension of the ["Evolving to a target string"](#ii-evolving-to-a-target-string)
algorithm. Here, the alphabet of [0, 1] is replaced with the range [0, 9]. This
massively increases the search space, making it harder to find the global
optimum.

Mutation in this algorithm consists of either incrementing or decrementing
the value of some digit in the chromosome by 1.

A chromosome is scored by how close a certain digit is to the digit in the
same position in the target string. If the digits are equal, the maximum
fitness is awarded for that digit. The difference between digits is based on
how many mutations would be required to turn the chromosome digit into the
target digit. For example:

|Target Digit|Chromosome Digit|Observed Difference|
|------------|----------------|-------------------|
|5|8|3|
|0|9|1|
|8|2|4|
|3|6|3|

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- PART B -->
## Part B
Solution: [knapsack_ga.py](./knapsack_ga.py)<br>
This GA uses the methods explored in Part A in conjunction with the
[Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem#:~:text=The%20knapsack%20problem%20is%20a,is%20as%20large%20as%20possible.).
The knapsack is represented by an ```n``` bit binary string, where n is the number
of possible items. A 1 in some position ```i``` in the bit string means that item ```i```
is being included in the knapsack. A 0 means that item is excluded.

The value and weight sets used in my solution were randomly generated by using
numpy.random.randint().
Fitness is assigned to each chromosome based on the value of all items inside.
If the knapsack exceeds the weight limit assigned, a fitness of 0 is given.
The best knapsack and average score of each generation is graphed using
matplotlib.

<p align="right">(<a href="#top">back to top</a>)</p>
