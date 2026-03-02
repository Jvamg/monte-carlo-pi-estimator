# 🎯 Monte Carlo Pi Estimator & NumPy Benchmark

A computational physics and data engineering project that estimates the value of Pi ($\pi$) using the Monte Carlo method. 

The primary goal of this project is to serve as a **performance benchmark**, demonstrating the massive execution speed difference between standard Python `for` loops and **NumPy's vectorized operations** when handling millions of data points.

## 🧠 The Math Behind It
Imagine a circle with radius $r$ inscribed inside a square. 
The ratio of the circle's area to the square's area is exactly $\pi/4$. 

By throwing millions of "random darts" (X and Y coordinates) into the square, we can count how many land inside the circle ($x^2 + y^2 \le 1$). Multiplying the ratio of (darts inside / total darts) by 4 gives us an extremely accurate estimation of Pi, without ever using its actual formula.

## 🚀 Performance Comparison

To prove the efficiency of data vectorization, the simulation was run with **100,000 (100k) iterations**. 

* **Pure Python (`for` loop):** Calculated point by point.
* **NumPy:** Generated and calculated 100k points simultaneously in RAM using arrays and boolean masks.

![Performance Bar Chart](assets/bar_chart.png)

**Results:** NumPy completed the massive calculation in a fraction of a second, proving to be exponentially faster than standard Python loops for mathematical operations. Both methods successfully estimated Pi to `~3.141` (more iterations, means higher accuracy).

## 🎨 Visualizing the Simulation

Below is a scatter plot rendering of the Monte Carlo simulation. 
It's important to note that **no circular lines were drawn**. The perfect circle emerges purely from the chaos of random data points being filtered by a NumPy boolean mask (Blue = Inside, Red = Outside).

![Monte Carlo Scatter Plot](assets/scatter_plot.png)

## 🛠️ Tech Stack
* **Python 3.11+**
* **NumPy:** For high-performance matrix operations and boolean masking.
* **Matplotlib:** For data visualization.
* **Jupyter Notebook:** For interactive execution and plotting.

## ⚙️ How to Run
Clone the repository and run the Jupyter Notebook to see the benchmarking in real-time.

```bash
git clone [https://github.com/Jvamg/monte-carlo-pi-estimator.git](https://github.com/Jvamg/monte-carlo-pi-estimator.git)
cd monte-carlo-pi-estimator
pip install -r requirements.txt
jupyter notebook plotting.ipynb