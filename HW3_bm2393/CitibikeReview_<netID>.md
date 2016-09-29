## Comment:</br>
1. Null and alternative hypotheses are formulated correctly.</br>
2. the data supports the project: define the 75 percentile age as old and use the tripduration as features</br>
3. The analysis is clear and good.</br> 
4. But I think the plot does not show the evidence that old people take longer tripduration, at least not intuitively.</br>
## Suggestion:</br>
It will be better if the average trip time of old people and young people can be plotted.</br>
## Test:</br>
\alpha
It's quite clear that z-test should be used to verify the hypothesis.</br>
First, calculate average time difference: T_{diff}=T_{old}-T_{young} to check if it's less than zero.</br>
Then, using z-test $$ z =\frac{T_old-T_young}{\sqrt{\sigma_1/n_1+\sigma_2/n_2}} $$
