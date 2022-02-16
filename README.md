# CSCI570-FinalProject
Click **[here](https://github.com/VincentAC-stack/CSCI570-FinalProject/blob/main/CSCI570_Fall2021_FinalProject.pdf)** for project description

# Graphical Visualization
![MemoryPlot](https://github.com/VincentAC-stack/CSCI570-FinalProject/blob/main/MemoryPlot.png "MemoryPlot")
![CPUPlot](https://github.com/VincentAC-stack/CSCI570-FinalProject/blob/main/CPUPlot.png "CPUPlot")

# Summary
From the result and graph, we can see that as increasing problem size(m * n), the line of DP's memory is linear(y = k * m * n), and the line of the DP&DC's memory is almost close to x-axis. In result, the complexity of DP's memory is O(m * n), but the complexity of DP&DC's memory is O(m + n). In the Time Graph, the time complexity of DP and DP&DC are both O(m * n). However, the line of DP&DC is steeper than DP which means DP&DC uses more time than DP.

# How to Execute
```python
python3 String_generator.py input.txt
python3 9451263998_5033799212_7197616609_basic.py
```
```python
python3 String_generator.py input.txt
python3 9451263998_5033799212_7197616609_efficient.py
```
9451263998_5033799212_7197616609_basic.py file generates an output_basic.txt file as output. 
9451263998_5033799212_7197616609_efficient.py file generates an output_efficient.txt file as output.
<br>
There are four lines in our output files: first 50 and last 50 characters in the first alignment, first 50 and last 50 characters in the second alignment, total runtime, and total space used.
