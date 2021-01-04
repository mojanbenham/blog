# Probability and Statistics for Engineering and the Sciences
#### Jay Devore - Eighth Edition

## Chapter One - Overview and Descriptive Statistics

- Statistics is how we make judgements in the presence of uncertainty and variation.
- A **census** is all desired information for every object in the **population**.
   - Since census' are typically infeasible, a **sample** is required.
  
<img width="200" src="./photos/devore1.png">

- We can *deduce* from population to sample with probability, and *infer* from sample to population with statistics.
- A major issue with collecting data is that the sample may not be reflective of the population.

### Types of samples:
1. *simple random sample*: every object has the same chance of being selected.
2. *stratified sample*: objects are split into nonoverlapping groups and each group is sampled.
3. *convenience sample*: sampling without systematic randomization.

- Types of descriptive displays: stem-and-leaf, dotplots, histograms, boxplots.
  - For boxplots, the left box boundary is the lower fourth (median of smaller half of data) and the right boundary is the upper fourth. The midline is the median of the whole dataset and the "whiskers" stretch to the lowest and highest data points.
- Distributions can be (a) unimodal, bimodal, multimodal and (b) symmetrical, positively skewed, negatively skewed.
- Think of the sample **mean** as the balance point fulcrum, where each object is a weight on a horizontal scale: <img width="60" src="./photos/devore2.png">
- The sample **median** (denoted by \tilde x) is insensitive to outliers, while the mean is sensitive to outliers.
  - a middle ground between mean and median is the **trimmed mean**, where a percentage of data points are trimmed from either end of the range.
  - if a dataset is negatively skewed, the mean will be less than the median and vice versa.
  
- variance and standard deviation are measures of variability that involve deviations from the mean.
  - the sum of deviations from the mean equals zero.
- **sample variance**: <img width="100" src="./photos/devore3.png">
  - note that we divide by n - 1 rather than n because we tend to underestimate in samples (proof not included). Divide by n for populations.
- **standard deviation**: <img width="60" src="./photos/devore4.png">
  - think of this as the typical deviation from the sample mean that you can expect from each data point.
