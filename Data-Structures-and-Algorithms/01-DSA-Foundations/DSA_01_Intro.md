# DSA Preparation for Interviews

![rainbow](https://github.com/ancilcleetus/My-Learning-Journey/assets/25684256/839c3524-2a1d-4779-85a0-83c562e1e5e5)

## Flow of mastering DSA:

- Complete a DSA topic
- Implement that Data Structure / Algorithm from scratch
- Solve coding problems for that topic
    
    You can choose problems from any of the below:
    
    1. [NeetCode](https://neetcode.io/practice) $\Rightarrow$ Start with NeetCode150, then solve all the other problems (NeetCodeAll has 580 problems)
    2. [Kunal Kushwaha's DSA course](https://github.com/kunal-kushwaha/DSA-Bootcamp-Java) $\Rightarrow$ Easy problems $\rightarrow$ 240+, Medium problems $\rightarrow$ 200+, Hard problems $\rightarrow$ 100+
    3. [LeetCode](https://leetcode.com/)
    
    **Note**
    
    Solving all problems from NeetCodeAll is sufficient for Interviews.

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
    - Input [1, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0] $\Rightarrow$ Output [1, 2, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
3. Come up with a Brute Force Solution $\Rightarrow$ How would a human manually solve this ?
    - For these examples, the result keeps returning an array of the non-zeros plus an array of the zeros at the end. Thinking through a very basic implementation, what I've been doing is: iterating through, finding the non-zeros, and just putting them in an another `temp` array. Then I've been filling the rest of the result array with `0`s until we've gotten the original length.
4. Use Pseudocode to clarify your thoughts
    - Unless an algorithm is simple, write pseudocode in the first pass.
    - Then, we can optimize the pseudocode. Once enough optimization is achieved, it can be coded and tested
    - Additionally, thinking in pseudocode is much easier to modify if you encounter an error
    - For above problem, pseudocode for Brute Force Solution is as below:
    ```
    result = []
    zero_count = 0
    for value in array:
        if non-zero, append to result
        if zero, increment zero_count
        
    for zero_count times:
        append 0 to result
        
    return result
    ```
5. Optimize the Brute Force Solution with Patterns and Abstractions
    - After you've done enough coding challenges, you'll begin to recognize patterns you can leverage.
    - Since this is an array, we need to go through each element to create a zero-ending array. Hence, Time Complexity cannot be optimized better than $O(n)$. Can we optimize the Space Complexity ? Can we do this without instantiating a new array ?
        - Solution:
        ```
        def zeros_to_end(array):
            consec_zeros_flag = False
            consec_zeros_count = 0
            for i in range(len(array) - 1):
                current_ = array[i]
                next_ = array[i + 1]
                if current_ != 0 and next_ == 0:
                    pass
                elif current_ != 0 and next_ != 0:
                    pass
                elif current_ == 0 and next_ != 0:
                    if not consec_zeros_flag:
                        array[i + 1] = current_
                        array[i] = next_
                    else:
                        array[i - consec_zeros_count + 1] = next_
                        array[i + 1] = current_
                elif current_ == 0 and next_ == 0:
                    if not consec_zeros_flag:
                        consec_zeros_flag = True
                        consec_zeros_count = 2
                    else:
                        consec_zeros_count += 1
                        
            return array

        array_1 = [0, 1]
        array_2 = [0, 4, 0]
        array_3 = [1, 0, 2, 0, 4, 0]
        array_4 = [1, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0]

        print(f"Input = {array_1}, Output = {zeros_to_end(array_1)}")
        print(f"Input = {array_2}, Output = {zeros_to_end(array_2)}")
        print(f"Input = {array_3}, Output = {zeros_to_end(array_3)}")
        print(f"Input = {array_4}, Output = {zeros_to_end(array_4)}")
        ```
        
        ```
        Input = [0, 1], Output = [1, 0]
        Input = [0, 4, 0], Output = [4, 0, 0]
        Input = [1, 0, 2, 0, 4, 0], Output = [1, 2, 4, 0, 0, 0]
        Input = [1, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0], Output = [1, 2, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        === Code Execution Successful ===
        ```
        - Time Complexity:
        The time complexity of this function is $O(n)$, where n is the number of elements in the input array. This is because the function iterates through the array once, checking each element and potentially swapping elements if they are zeros.
        - Space Complexity:
        The space complexity is $O(1)$ because the function only uses a constant amount of extra space (for variables `consec_zeros_flag` and `consec_zeros_count`) regardless of the size of the input array.
    - Also check whether we can transform the input to ease the optimization
        - If it's a collection, does sorting / grouping help ?
        - If it's a tree, can we transform it into an array or a linked list ?
    - Introduce a Data Structure or Abstract Data Type
        - This is where the study of data structures (and experience implementing and using them) really helps. If you can identify the bottleneck, you can start to try to throw data structures at the problem to see if there are any performance or spatial gains.
        - Note that the data structure doesn't need to be fancy. In above optimized solution, we introduced a boolean variable `consec_zeros_flag` and an integer variable `consec_zeros_count` and reduced the Space Complexity. Sometimes that's all you need.
    - Introduce an Algorithm Technique
        - Divide and Conquer, Recursion, Memoization etc.
    - If none of the above worked
        - Ask more questions
        - Ask for a hint
6. After you have a working solution
    - Manually run the optimized pseudocode through 1-3 example inputs step by step to make sure it works.
    - During this exercise, sometimes you'll also be able to weed out incorrect assumptions or make important realizations and correct some mistakes that you overlooked earlier.
    - Can we optimize this even further ?
        - An even better solution:
        ```
        def zeros_to_end(array):
            current_nonzero_position = 0
            for i in range(len(array)):
                if array[i] != 0:
                    array[current_nonzero_position] = array[i]
                    current_nonzero_position += 1
                    
            for i in range(current_nonzero_position, len(array)):
                array[i] = 0
                
            return array

        array_1 = [0, 1]
        array_2 = [0, 4, 0]
        array_3 = [1, 0, 2, 0, 4, 0]
        array_4 = [1, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0]

        print(f"Input = {array_1}, Output = {zeros_to_end(array_1)}")
        print(f"Input = {array_2}, Output = {zeros_to_end(array_2)}")
        print(f"Input = {array_3}, Output = {zeros_to_end(array_3)}")
        print(f"Input = {array_4}, Output = {zeros_to_end(array_4)}")
        ```
        
        ```
        Input = [0, 1], Output = [1, 0]
        Input = [0, 4, 0], Output = [4, 0, 0]
        Input = [1, 0, 2, 0, 4, 0], Output = [1, 2, 4, 0, 0, 0]
        Input = [1, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0], Output = [1, 2, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        === Code Execution Successful ===
        ```
        - Time Complexity:
        Despite having two loops, the time complexity simplifies to $O(n)$.
        - Space Complexity:
        The space complexity is $O(1)$ because the function only uses a constant amount of extra space (for variable `current_nonzero_position`) regardless of the size of the input array.
    - If the input-outputs check in, write final optimized code from pseudocode.

![rainbow](https://github.com/ancilcleetus/My-Learning-Journey/assets/25684256/839c3524-2a1d-4779-85a0-83c562e1e5e5)
