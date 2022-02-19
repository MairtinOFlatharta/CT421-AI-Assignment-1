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
        <li><a href="#i):-one-max-problem">i): One-max problem</a></li>
        <li><a href="#ii):-evolving-to-a-target-string">ii): Evolving to a target string</a></li>
        <li><a href="#iii):-deceptive-landscape">iii): Deceptive Landscape</a></li>
        <li><a href="#iv):-evolving-to-a-target-string-with-a-larger-alphabet">iv): Evolving to a target string with a larger alphabet</a></li>
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

<!-- BUILT WITH -->
### Built With
These solutions were written using the latest version of python (currently 3.10.2).
These are the requirements for using these scripts:
* Python 3.10.*
* numpy
* matplotlib

<!-- PART A -->
## Part A

<!-- I: ONE-MAX PROBLEM -->
### i): One-max problem
Solution: [one_max.py](./one_max.py)<br>
This genetic algorithm uses a population of 30 bit-long ints. The target is
a bit-string with 1s in each position i.e. 1,073,741,823 base 10.
It uses a randomly generated population, standard mutation and one-point crossover.
The average fitness of each generation is then plotted using matplotlib.

<!-- II: EVOLVING TO A TARGET STRING -->
### ii): Evolving to a target string
Solution: [target_string.py](./target_string.py)

<!-- III: DECEPTIVE LANDSCAPE -->
### iii): Deceptive Landscape
Solution: [deceptive_landscape.py](./deceptive_landscape.py)

<!-- IV: EVOLVING TO A TARGET STRING WITH A LARGER ALPHABET -->
### iv): Evolving to a target string with a larger alphabet
Solution: [digit_target_string.py](./digit_target_string.py)

<!-- PART B -->
## Part B
Solution: [knapsack_ga.py](./knapsack_ga.py)
