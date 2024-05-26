# Data Structures and Algorithms

# ![Data Structures and Algorithms](data/animations/DSA-01.gif)

> **`Note 1`**: Use ![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat) (recommended) in order to view the jupyter notebooks (nbviewer loads the notebook really fast compared to GitHub). You can see all the codes and the outputs in nbviwer without running the whole code again.

> **`Note 2`**: If you want to edit the notebooks and rerun cells, open notebooks in ![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat).

> **`Note 3`**: It has been observed that sometimes both ![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat) and ![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat) fail to properly render Table of Contents and complex equations for some of the notebooks. In that case, render notebook in ![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat) itself.

![rainbow](https://github.com/ancilcleetus/My-Learning-Journey/assets/25684256/839c3524-2a1d-4779-85a0-83c562e1e5e5)

## Status:

1. DSA Foundations ![10%](https://progress-bar.dev/10)
    1. Intro to DSA ![100%](https://progress-bar.dev/100) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](01-DSA-Foundations/DSA_01_Intro.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/My-Learning-Journey/blob/main/Data-Structures-and-Algorithms/01-DSA-Foundations/DSA_01_Intro.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/My-Learning-Journey/blob/main/Data-Structures-and-Algorithms/01-DSA-Foundations/DSA_01_Intro.ipynb)
2. DSA Challenges ![10%](https://progress-bar.dev/10)

![rainbow](https://github.com/ancilcleetus/My-Learning-Journey/assets/25684256/839c3524-2a1d-4779-85a0-83c562e1e5e5)

## Flow of mastering DSA:

- Complete a DSA topic
- Implement that Data Structure / Algorithm from scratch
- Solve Assignment problems (from [LeetCode](https://leetcode.com/)) for that topic from [Kunal Kushwaha's DSA course](https://github.com/kunal-kushwaha/DSA-Bootcamp-Java) $\Rightarrow$ Easy problems $\rightarrow$ 240+, Medium problems $\rightarrow$ 200+, Hard problems $\rightarrow$ 100+

    For each problem,
    
    1. Commit to about 20-30 minutes of trying to solve it by yourself before going to the solution. Really try to get some semblance of a correct output. Brute force it if you have to - just try to reason about any kind of working solution, no matter how slow. It will help you understand the necessities to optimize later.
    2. If you get stuck, start by looking at a hint. Then keep trying to solve it. Repeat until there are no more hints.
    3. No hints? Start going through the walkthrough or solution very slowly. As soon as you get unstuck, STOP READING.
    4. Use the bit of insight to start trying to code again.
    5. Make note of
        - which DSA topic
        - which type of problem
        - which type of patterns / techniques used for optimization
    6. Repeat above steps until we cannot optimize further
    7. Write the solution again in another programming language. This forces you to think through the abstractions again, and helps with retention.
- If required, solve more LeetCode problems from that topic (use tags)
- Repeat above steps for all the DSA topics
- Optional: Create a DSA Visualizer Personal Project for visualizing different Data Structures and Algorithms

![rainbow](https://github.com/ancilcleetus/My-Learning-Journey/assets/25684256/839c3524-2a1d-4779-85a0-83c562e1e5e5)

## Flow of attempting a coding problem during interviews:

Consider the below problem:

    - Question: Write a method that moves all zeros in an array to its end.
    
During the interview, we can follow  the flow below:

    1. Clarify the requirements $\Rightarrow$ Until you know exactly what the problem is, you have no business trying to come up with a solution
        - Question: Write a method that moves all zeros in an array to its end.
        - Requirement (derived after discussion with the interviewer): We want to move all the zeros to the back, while keeping nonzeros in front. We want to also keep the order the nonzeros were originally in, and the algorithm should run in linear time i.e. $O(n)$.
    2. Start With Inputs and Outputs $\Rightarrow$ Create your own testcases (inputs and corresponding outputs). Start with small inputs and then increase the size of inputs.
        - Input [0, 1] $\Rightarrow$ Output [1, 0]
        - Input [0, 4, 0] $\Rightarrow$ Output [4, 0, 0]
        - Input [1, 0, 2, 0, 4, 0] $\Rightarrow$ Output [1, 2, 4, 0, 0, 0]
    3. Come up with a Brute Force Solution
    

