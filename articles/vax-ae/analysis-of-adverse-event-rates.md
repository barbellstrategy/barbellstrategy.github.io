*Note, this is a section that is in a yet-to-be published longer article.  To fit the journal length requirements, much of what I wrote here had to be cut.  I wanted to have the full analysis here so that people can reproduce the results in total.  The reasons for choosing these AE and the context is elsewhere in the main paper (which I will link to when it’s published).  This is just the math part.*

# Analysis of Adverse Event Rates

Here we compare the rate of Global and US reports of post-vaccination adverse events (AE), for the COVID-19 vaccine and the Influenza vaccine. For each of the AE, we compare three relevant rates of reporting: i) the rate of reported AE per unit time, ii) the rate of reported AE per dose given, and iii) the rate of reported AE per person vaccinated. 

In Table 1 below, we report the period used for normalizing the data, Global values are reported on the top line, US value on the second line.

| Vaccine   | Time Tracked | Billion Doses Given     | Billion People Vaccinated               |
| --------- | ------------ | ----------------------- | --------------------------------------- |
| COVID-19  | 18 Months    | 12.07<br />0.596        | 5.23<br />0.260                         |
| Influenza | 294 Months   | 66 (estimated)<br />3.3 | 7.71 (simulated)<br />0.313 (simulated) |

*Table 1*

Counting the number of people vaccinated with the COVID-19 vaccine is straightforward because there has only been one worldwide attempt at vaccination and the data has been tracked from day one. The Influenza vaccine is harder because individuals are not tracked and there are yearly seasons where an individual may choose to receive a subsequent vaccinations. We run a Monte Carlo simulation to estimate the number of people that have received at least one Influenza vaccine in the US since 1998. 

We track a sample population where each year a fraction of the eligible (old enough) population is vaccinated, $f_{v}$, a fraction of the population dies (some of whom may be vaccinated), $f_d$, and a new fraction of the population is becomes eligible (none of whom are vaccinated), $f_e$. By simulating the demographics change yearly, we can estimate the total number of people who have received at least one Influenza vaccine by 2022. We use the UN population data to estimate $f_e$ and $f_d$ each year (reference: https://population.un.org/) and the conditional probability of Influenza vaccination from Kwong, et al. (reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6961264/). Kwong reports that roughly 57% (33,234 out of 58,021) of the population in their study who receives a Influenza shot in one year repeats it a subsequent year. The CDC reports that approximately 50% of the population receives the vaccine in any given year. From that, we approximate $f_v=0.57$ for previously vaccinated individuals and $f_v=0.43$ for previously unvaccinated individuals, which will result in the rough CDC approximation of 50% of the population being vaccinated any given year. 

To allow simulation “burn in” for the stochastic nature of this experiment, we start in 1980 with a sample of the eligible population of 100,000,000 people with 50% of them "pre-vaccinated" from previous years. From 1980 to 1997 we grow the population by $f_e$, shrink it by $f_d$, and vaccinate individuals by the conditional $f_v$ based on their current vaccination status, by 1997 we can see that the fraction of vaccinated population has stabalized. We continue the simulation until 2021 with the addition that in 1998 we start accumulating the number of people who were vaccinated and died. The results of that simulation are shown below in Table 2.

|End of Year|Sample Population<br/>(Thousands)|Vaccinated Population<br/>(Thousands)|Total Vaccinated<br/>Since 1998<br/>(Thousands)|
|---| --: | --: | --: |
| 1980 | 100685 | 70921 (70.4%) | -- |
| 1981 | 101328 | 82921 (81.8%) | -- |
| 1982 | 101936 | 89923 (88.2%) | -- |
| 1983 | 102629 | 94190 (91.8%) | -- |
| 1984 | 103253 | 96842 (93.8%) | -- |
| 1985 | 103924 | 98746 (95.0%) | -- |
| 1986 | 104615 | 100133 (95.7%) | -- |
| 1987 | 105344 | 101170 (96.0%) | -- |
| 1988 | 106017 | 102026 (96.2%) | -- |
| 1989 | 106742 | 102790 (96.3%) | -- |
| 1990 | 107434 | 103590 (96.4%) | -- |
| 1991 | 108187 | 104335 (96.4%) | -- |
| 1992 | 108919 | 105104 (96.5%) | -- |
| 1993 | 109637 | 105790 (96.5%) | -- |
| 1994 | 110313 | 106507 (96.5%) | -- |
| 1995 | 110959 | 107191 (96.6%) | -- |
| 1996 | 111615 | 107893 (96.7%) | -- |
| 1997 | 112289 | 108579 (96.7%) | -- |
| 1998 | 112919 | 109203 (96.7%) | 110157 (97.6%) |
| 1999 | 113542 | 109799 (96.7%) | 111722 (98.4%) |
| 2000 | 114182 | 110390 (96.7%) | 113264 (99.2%) |
| 2001 | 114821 | 111055 (96.7%) | 114889 (100.1%) |
| 2002 | 115497 | 111745 (96.8%) | 116497 (100.9%) |
| 2003 | 116175 | 112461 (96.8%) | 118139 (101.7%) |
| 2004 | 116819 | 113102 (96.8%) | 119745 (102.5%) |
| 2005 | 117465 | 113757 (96.8%) | 121371 (103.3%) |
| 2006 | 118119 | 114412 (96.9%) | 122989 (104.1%) |
| 2007 | 118792 | 114997 (96.8%) | 124521 (104.8%) |
| 2008 | 119496 | 115736 (96.9%) | 126181 (105.6%) |
| 2009 | 120074 | 116317 (96.9%) | 127789 (106.4%) |
| 2010 | 120665 | 116899 (96.9%) | 129362 (107.2%) |
| 2011 | 121265 | 117562 (96.9%) | 130979 (108.0%) |
| 2012 | 121819 | 118175 (97.0%) | 132571 (108.8%) |
| 2013 | 122308 | 118774 (97.1%) | 134195 (109.7%) |
| 2014 | 122830 | 119335 (97.2%) | 135733 (110.5%) |
| 2015 | 123360 | 119866 (97.2%) | 137231 (111.2%) |
| 2016 | 123855 | 120378 (97.2%) | 138736 (112.0%) |
| 2017 | 124287 | 120819 (97.2%) | 140225 (112.8%) |
| 2018 | 124730 | 121263 (97.2%) | 141695 (113.6%) |
| 2019 | 125123 | 121666 (97.2%) | 143178 (114.4%) |
| 2020 | 125570 | 122107 (97.2%) | 144657 (115.2%) |
| 2021 | 125981 | 122575 (97.3%) | 146200 (116.0%) |

*Table 2*

After running the simulation, in 2021 our sample population grew to 125,981,000, with a total of 146,200,000 (current vaccinated living plus the accumulated vaccinated dead) receiving at least one dose of the Influenza vaccine since 1998 (116% of the current population). Now, we scale this estimate to the true 2022 the total eligible population of 269.5 million (329.5 million minus 60 million who are too young) (reference: https://population.un.org/), we estimate the same fraction of 116% of the current population vaccinated since 1998, that results in roughly a total 313 million people in the US that have received at least one dose of Influenza vaccine. Using the same scaling factor for an eligible world population of 6.65 (7.95 billion minus 1.3 billion), we get an estimate of 7.71 billion people worldwide who have received at least one dose of the Influenza vaccine since 1998. These are all rough estimates given the limited data available; however, even if these estimates are high by a factor of 2 (highly unlikely), the signals reported below are still significant. 

Kwong, et al. track the number of vaccine doses a population of 38,766 people had over a 10-year period (Table 4 in their paper). A weighted average of the number of doses given per peson over that 10-year period is 0.62 doses/person/year. Our estimates of 7.71 billion people receiving 66 billion doses globally (0.30 doses/person/year) and 313 million people receiving 3.3 billion doses in the US (0.35 doses/person/year) provide more evidence that our estimates are not wildly inconsistent with existing studies. Kwong, et al. are specifically studying people in the 65+ age category, which has roughtly double the uptake of the general population (reference:https://www.cdc.gov/Influenza/fluvaxview/coverage-1819estimates.htm), consistent with our estimates.

In Table 3 below we show the count of AE reported post vaccine in VAERS along with the mean rate of report over the time tracked, the mean rate of report per billion doses given, and the mean rate of report per billion people vaccinated. Report count and rates for the COVID-19 Vaccine are on the top line with the counts and rates for the Influenza vaccine below them for each AE. The same data for global counts and rates is shown in Table 4.

| Adverse Event | US Count of AE reports post Vaccine | US Rate of reported AE<br/>(count/Month) | US Rate of reported AE<br/>(count/billion doses) | US Rate of reported AE<br/>(count/billion people vaccinated) |
| --- | --: | --: | --: | --: |
| Menstrual abnormality | 6352<br/>54 | 353<br/>0.184 | 10700<br/>16.4 | 24400<br/>173 |
| Miscarriage | 1232<br/>259 | 68.4<br/>0.881 | 2070<br/>78.5 | 4740<br/>827 |
| Fetal chromosomal abnormalities | 7<br/>0 | 0.389<br/>0.00 | 11.7<br/>0.00 | 26.9<br/>0.00 |
| Fetal malformation | 2<br/>1 | 0.111<br/>0.00340 | 3.35<br/>0.303 | 7.69<br/>3.19 |
| Fetal cystic hygroma | 5<br/>0 | 0.278<br/>0.00 | 8.39<br/>0.00 | 19.2<br/>0.00 |
| Fetal cardiac disorders | 10<br/>2 | 0.556<br/>0.00680 | 16.8<br/>0.606 | 38.5<br/>6.39 |
| Fetal arrhythmia | 3<br/>0 | 0.167<br/>0.00 | 5.03<br/>0.00 | 11.5<br/>0.00 |
| Fetal cardiac arrest | 3<br/>0 | 0.167<br/>0.00 | 5.03<br/>0.00 | 11.5<br/>0.00 |
| Fetal vascular mal-perfusion | 5<br/>0 | 0.278<br/>0.00 | 8.39<br/>0.00 | 19.2<br/>0.00 |
| Fetal growth abnormalities | 59<br/>20 | 3.28<br/>0.0680 | 99.0<br/>6.06 | 227<br/>63.9 |
| Fetal abnormal surveillance | 125<br/>36 | 6.94<br/>0.122 | 210<br/>10.9 | 481<br/>115 |
| Fetal placental thrombosis | 5<br/>0 | 0.278<br/>0.00 | 8.39<br/>0.00 | 19.2<br/>0.00 |
| Fetal stillbirth | 168<br/>42 | 9.33<br/>0.143 | 282<br/>12.7 | 646<br/>134 |
| Low amniotic fluid | 11<br/>1 | 0.611<br/>0.00340 | 18.4<br/>0.303 | 42.3<br/>3.19 |


*Table 3*

| Adverse Event | Global Count of AE reports post Vaccine | Global Rate of reported AE<br/>(count/Month) | Global Rate of reported AE<br/>(count/billion doses) | Global Rate of reported AE<br/>(count/billion people vaccinated) |
| --- | --: | --: | --: | --: |
| Menstrual abnormality | 12843<br/>65 | 714<br/>0.221 | 1060<br/>0.985 | 2460<br/>8.43 |
| Miscarriage | 3338<br/>325 | 185<br/>1.11 | 277<br/>4.92 | 638<br/>42.2 |
| Fetal chromosomal abnormalities | 10<br/>0 | 0.556<br/>0.00 | 0.829<br/>0.00 | 1.91<br/>0.00 |
| Fetal malformation | 22<br/>2 | 1.22<br/>0.00680 | 1.82<br/>0.0303 | 4.21<br/>0.259 |
| Fetal cystic hygroma | 8<br/>0 | 0.444<br/>0.00 | 0.663<br/>0.00 | 1.53<br/>0.00 |
| Fetal cardiac disorders | 18<br/>2 | 1.00<br/>0.00680 | 1.49<br/>0.0303 | 3.44<br/>0.259 |
| Fetal arrhythmia | 5<br/>0 | 0.278<br/>0.00 | 0.414<br/>0.00 | 0.956<br/>0.00 |
| Fetal cardiac arrest | 20<br/>0 | 1.11<br/>0.00 | 1.66<br/>0.00 | 3.82<br/>0.00 |
| Fetal vascular mal-perfusion | 12<br/>0 | 0.667<br/>0.00 | 0.994<br/>0.00 | 2.29<br/>0.00 |
| Fetal growth abnormalities | 188<br/>24 | 10.4<br/>0.0816 | 15.6<br/>0.364 | 35.9<br/>3.11 |
| Fetal abnormal surveillance | 178<br/>45 | 9.89<br/>0.153 | 14.7<br/>0.682 | 34.0<br/>5.84 |
| Fetal placental thrombosis | 6<br/>0 | 0.333<br/>0.00 | 0.497<br/>0.00 | 1.15<br/>0.00 |
| Fetal stillbirth | 402<br/>64 | 22.3<br/>0.218 | 33.3<br/>0.970 | 76.9<br/>8.30 |
| Low amniotic fluid | 17<br/>1 | 0.944<br/>0.00340 | 1.41<br/>0.0152 | 3.25<br/>0.130 |


*Table 4*

For all AE, the rates of reports post COVID-19 vaccine are higher than the Influenza vaccine across all three normalization methods: by unit time, by dose given, and by person vaccinated. We proceed with two analyses below: 1) compute the p-value to determine if the AE report rates are statistically different between the two vaccines, and 2) compute the relative rate and 95% CI of AE reports after the COVID-19 vaccine versus the Influenza vaccine. That is, we answer the questions: 1) “Are the rate of AE reports post COVID-19 vaccine (statistically) different than the rates of report post Influenza vaccine?” and 2) “How much more frequently is an AE reported after the COVID-19 vaccine than after the Influenza vaccine?”

*Statistical Significance*

We treat each AE report as discrete independent events occurring at the mean rate specified in Tables 1 and 2 which we model as a Poisson distribution. Given two rates $\lambda_1$ and $\lambda_2$ over a period, $P$, we perform a Poisson E-test [reference: https://userweb.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf] to compute the p-value. The E-test is used for Poisson statistics analogous to the traditional t-test used for Gaussian statistics. The p-value is interpreted in the same way: the probability that the observed events came from the same probability distribution. Or stated another way: the probability that the means (in this case rates) are same by random chance.

We use the rates in Tables 1 and 2 above and normalize the event counts over each window, $W$: the time-, dose-, or people-vaccinated-window and report the p-values below in Table 5. Where there is sufficient data, the p-values are small, and where 0.0 is reported, it was too small to represent as a double precision floating point number in our E-test function [reference: https://github.com/nolanbconaway/poisson-etest]. 

*Estimating Relative Reporting Rates* 

For the rates that have non-zero counts in the reporting period, we compute ratio of rates of AE reports for each vaccine and the 95% confidence interval (We do not use the p-value as a metric here to avoid claims of p-hacking, the full confidence interval is shown and the reader can deduce significance from that). That is, we compute how much more often a post COVID-19 vaccination AE is reported compared to post Influenza vaccination. Consider a case were Event A is reported at a rate of 100 per month and Event B is reported at a rate of 10 per month. The naïve approach is to simply state that Event A is reported $\frac{100/month}{10/month}=10$ times as often as Event B. However, events do not occur at uniform frequency, independent events occur at frequencies described by the Poisson distribution. We proceed by computing the ratio distribution, $R$, which is the distribution of the ratio of two different Poisson distributions. That is, given two Poisson distributions, $P(\lambda_1)$ and $P(\lambda_2)$, we aim to compute the ratio distribution, $R$, which represents the probability distribution of the ratio of the distribution of events.

$$
R(\lambda_1,\lambda_2)=\frac{P(\lambda_1)}{P(\lambda_2)}
$$

We estimate the shape of $R$ for each AE and window, $W$, by performing Monte Carlo simulations. We draw 1,000,000 random samples from Poisson distributions with rates $\lambda_1$ and $\lambda_2$ resulting in a sample of paired event counts $n_1$ and $n_2$ , respectively, over the observation window $W$ .

$$
n_i \leftarrow P(\lambda_i)
$$

That is, we create a set of 1,000,000 tuples of event counts $\left\{(n_1,n_2)_1,(n_1,n_2)_2,\dots,(n_1,n_2)_{1000000}\right\}$ drawn from the two Poisson distributions. The ratio distribution, $R$, is built up from the ratio of the draws of each pair of $n_1$ and $n_2$ 

$$
R(\lambda_1,\lambda_2)=\left\{\left(\frac{n_1}{n_2}\right)_1,\left(\frac{n_1}{n_2}\right)_2,\dots,\left(\frac{n_1}{n_2}\right)_{1000000}\right\}
$$

The mean of $R$ is is the expectation value for the ratio of the two Poisson distributions and the empirically-derived quantile function of $R$ is used to estimate the 95% CI of the mean. All computed values have converged to a precision of 1% or better. For AE that are reported infrequently post Influenza vaccine there is finite probability that $n_2$ is zero resulting in $R$ being undefined. To mitigate this problem, we use the zero-truncated Poisson distribution [reference: https://www.jstor.org/stable/2527552] and only count instances of non-zero $n_2$ draws. This approach skews the $R$ distribution to the left [reference: https://epubs.siam.org/doi/10.1137/0134043] and makes the AE rates for the COVID-19 vaccine actually look better. That is, in these cases, the AE rate is actually a lower bound.

We report in Table 5 below the relative rate of post COVID-19 vaccine AE reports to post Influenza vaccine AE report. Global values are the top line and US values are in the bottom line for each AE. A relative rate greater than 1 implies that there are more post COVID-19 vaccine AE reports than post Influenza vaccine AE report. According to CDC’s Standard Operating Procedures for COVID-19 [reference: https://www.cdc.gov/vaccinesafety/pdf/VAERS-v2-SOP.pdf] when doing a Proportional Reporting Ratio (PRR) analysis (which is analogous to the analysis presented here in this paper), a 2x increase in reporting is a sufficient signal to be concerned.

| Adverse Event | Relative Rate<br/>(by time) | Relative Rate<br/>(by dose) | Relative Rate<br/>(by person vaccinated) |
| --- | --: | --: | --: |
| Menstrual abnormality | 4257 [1589.1-12893] p=0.0 <br/>2524 [894.57-6419.0] p=0.0| 1192 [673.95-2162.8] p=0.0<br/>738 [391.6-1584] p=0.0| 298 [223.0-406.0] p=0.0<br/>145 [108.6-197.4] p=0.0|
| Miscarriage | 177 [114.4-283.5] p=0.0 <br/>83 [50.8-143] p=0.0| 57 [44.3-74.7] p=0.0<br/>27 [20.2-36.5] p=0.0| 15 [13.3-17.5] p=0.0<br/>6 [5.0-6.7] p=0.0|
| Fetal chromosomal abnormalities |  p=0.00058 <br/> p=0.0048|  p=0.00058<br/> p=0.0048|  p=0.00058<br/> p=0.0048|
| Fetal malformation | 21 [10.0-32.0] p=1.9x10^-07^ <br/>2 [0.0-5.0] p=0.20| 20 [7.67-31.0] p=1.9x10^-07^<br/>2 [0.0-5.0] p=0.20| 15 [4.50-30.0] p=2.1x10^-06^<br/>2 [0.0-5.0] p=0.20|
| Fetal cystic hygroma |  p=0.0024 <br/> p=0.020|  p=0.0024<br/> p=0.020|  p=0.0024<br/> p=0.020|
| Fetal cardiac disorders | 17 [8.00-27.0] p=2.6x10^-06^ <br/>10 [4.00-17.0] p=0.00058| 16 [6.00-26.0] p=2.6x10^-06^<br/>9 [3.0-16] p=0.00058| 12 [3.60-25.0] p=2.7x10^-05^<br/>6 [1.5-15] p=0.0047|
| Fetal arrhythmia |  p=0.020 <br/> p=0.088|  p=0.020<br/> p=0.088|  p=0.020<br/> p=0.088|
| Fetal cardiac arrest |  p=6.9x10^-07^ <br/> p=0.088|  p=6.9x10^-07^<br/> p=0.088|  p=6.9x10^-07^<br/> p=0.088|
| Fetal vascular mal-perfusion |  p=0.00015 <br/> p=0.020|  p=0.00015<br/> p=0.020|  p=0.00015<br/> p=0.020|
| Fetal growth abnormalities | 126 [42.00-210.0] p=0.0 <br/>43 [14.0-72.0] p=0.0| 56 [20.7-189] p=0.0<br/>22 [7.14-64.0] p=0.0| 12 [7.42-21.4] p=0.0<br/>4 [2.2-6.8] p=3.2x10^-07^|
| Fetal abnormal surveillance | 83 [26.9-193] p=0.0 <br/>68 [21.6-140] p=0.0| 25 [12.2-58.7] p=0.0<br/>24 [10.1-63.0] p=0.0| 6 [4.1-9.0] p=0.0<br/>4 [2.9-6.6] p=0.0|
| Fetal placental thrombosis |  p=0.0096 <br/> p=0.020|  p=0.0096<br/> p=0.020|  p=0.0096<br/> p=0.020|
| Fetal stillbirth | 135 [48.25-412.0] p=0.0 <br/>82 [26.5-184] p=0.0| 38 [21.1-73.0] p=0.0<br/>26 [12.2-60.0] p=0.0| 9 [6.9-13] p=0.0<br/>5 [3.4-7.2] p=0.0|
| Low amniotic fluid | 17 [8.00-25.0] p=5.1x10^-06^ <br/>11 [5.00-18.0] p=0.00029| 16 [7.00-25.0] p=5.1x10^-06^<br/>11 [4.00-18.0] p=0.00029| 14 [4.67-25.0] p=5.1x10^-06^<br/>9 [2.5-17] p=0.00029|

*Table 5*

In the Figures below we show the Global and US relative rates of the reports of AE after the COVID-19 vaccine versus the Influenza vaccine for the rates of AE by unit time, by dose given, and by person vaccinated. A value greater than 1 implies that the AE is reported more frequently after the COVID-19 vaccine than after the Influenza vaccine. Note the log scale spanning multiple orders of magnitude indicating a large effect across many different AE - all (much) greater than 1. 

![forest-Dose (Global)](forest-Dose%20(Global).png)

![forest-Dose (US)](forest-Dose%20(US).png)

![forest-Month (Global)](forest-Month%20(Global).png)

![forest-Month (US)](forest-Month%20(US).png)

![forest-People (Global)](forest-People%20(Global).png)

![forest-People (US)](forest-People%20(US).png)

## Extra Plots

![](Fetal%20abnormal%20surveillance-Dose%20(Global).png)

![Fetal abnormal surveillance-Dose (US)](Fetal%20abnormal%20surveillance-Dose%20(US).png)

![Fetal abnormal surveillance-Month (Global)](Fetal%20abnormal%20surveillance-Month%20(Global).png)

![Fetal abnormal surveillance-Month (US)](Fetal%20abnormal%20surveillance-Month%20(US).png)

![Fetal abnormal surveillance-People (Global)](Fetal%20abnormal%20surveillance-People%20(Global).png)

![Fetal abnormal surveillance-People (US)](Fetal%20abnormal%20surveillance-People%20(US).png)

![Fetal arrhythmia-Dose (Global)](Fetal%20arrhythmia-Dose%20(Global).png)

![Fetal arrhythmia-Dose (US)](Fetal%20arrhythmia-Dose%20(US).png)

![Fetal arrhythmia-Month (Global)](Fetal%20arrhythmia-Month%20(Global).png)

![Fetal arrhythmia-Month (US)](Fetal%20arrhythmia-Month%20(US).png)

![Fetal arrhythmia-People (Global)](Fetal%20arrhythmia-People%20(Global).png)

![Fetal arrhythmia-People (US)](Fetal%20arrhythmia-People%20(US).png)

![Fetal cardiac arrest-Dose (Global)](Fetal%20cardiac%20arrest-Dose%20(Global).png)

![Fetal cardiac arrest-Dose (US)](Fetal%20cardiac%20arrest-Dose%20(US).png)

![Fetal cardiac arrest-Month (Global)](Fetal%20cardiac%20arrest-Month%20(Global).png)

![Fetal cardiac arrest-Month (US)](Fetal%20cardiac%20arrest-Month%20(US).png)

![Fetal cardiac arrest-People (Global)](Fetal%20cardiac%20arrest-People%20(Global).png)

![Fetal cardiac arrest-People (US)](Fetal%20cardiac%20arrest-People%20(US).png)

![Fetal cardiac disorders-Dose (Global)](Fetal%20cardiac%20disorders-Dose%20(Global).png)

![Fetal cardiac disorders-Dose (US)](Fetal%20cardiac%20disorders-Dose%20(US).png)

![Fetal cardiac disorders-Month (Global)](Fetal%20cardiac%20disorders-Month%20(Global).png)

![Fetal cardiac disorders-Month (US)](Fetal%20cardiac%20disorders-Month%20(US).png)

![Fetal cardiac disorders-People (Global)](Fetal%20cardiac%20disorders-People%20(Global).png)

![Fetal cardiac disorders-People (US)](Fetal%20cardiac%20disorders-People%20(US).png)

![Fetal chromosomal abnormalities-Dose (Global)](Fetal%20chromosomal%20abnormalities-Dose%20(Global).png)

![Fetal chromosomal abnormalities-Dose (US)](Fetal%20chromosomal%20abnormalities-Dose%20(US).png)

![Fetal chromosomal abnormalities-Month (Global)](Fetal%20chromosomal%20abnormalities-Month%20(Global).png)

![Fetal chromosomal abnormalities-Month (US)](Fetal%20chromosomal%20abnormalities-Month%20(US).png)

![Fetal chromosomal abnormalities-People (Global)](Fetal%20chromosomal%20abnormalities-People%20(Global).png)

![Fetal chromosomal abnormalities-People (US)](Fetal%20chromosomal%20abnormalities-People%20(US).png)

![Fetal cystic hygroma-Dose (Global)](Fetal%20cystic%20hygroma-Dose%20(Global).png)

![Fetal cystic hygroma-Dose (US)](Fetal%20cystic%20hygroma-Dose%20(US).png)

![Fetal cystic hygroma-Month (Global)](Fetal%20cystic%20hygroma-Month%20(Global).png)

![Fetal cystic hygroma-Month (US)](Fetal%20cystic%20hygroma-Month%20(US).png)

![Fetal cystic hygroma-People (Global)](Fetal%20cystic%20hygroma-People%20(Global).png)

![Fetal cystic hygroma-People (US)](Fetal%20cystic%20hygroma-People%20(US).png)

![Fetal growth abnormalities-Dose (Global)](Fetal%20growth%20abnormalities-Dose%20(Global).png)

![Fetal growth abnormalities-Dose (US)](Fetal%20growth%20abnormalities-Dose%20(US).png)

![Fetal growth abnormalities-Month (Global)](Fetal%20growth%20abnormalities-Month%20(Global).png)

![Fetal growth abnormalities-Month (US)](Fetal%20growth%20abnormalities-Month%20(US).png)

![Fetal growth abnormalities-People (Global)](Fetal%20growth%20abnormalities-People%20(Global).png)

![Fetal growth abnormalities-People (US)](Fetal%20growth%20abnormalities-People%20(US).png)

![Fetal malformation-Dose (Global)](Fetal%20malformation-Dose%20(Global).png)

![Fetal malformation-Dose (US)](Fetal%20malformation-Dose%20(US).png)

![Fetal malformation-Month (Global)](Fetal%20malformation-Month%20(Global).png)

![Fetal malformation-Month (US)](Fetal%20malformation-Month%20(US).png)

![Fetal malformation-People (Global)](Fetal%20malformation-People%20(Global).png)

![Fetal malformation-People (US)](Fetal%20malformation-People%20(US).png)

![Fetal placental thrombosis-Dose (Global)](Fetal%20placental%20thrombosis-Dose%20(Global).png)

![Fetal placental thrombosis-Dose (US)](Fetal%20placental%20thrombosis-Dose%20(US).png)

![Fetal placental thrombosis-Month (Global)](Fetal%20placental%20thrombosis-Month%20(Global).png)

![Fetal placental thrombosis-Month (US)](Fetal%20placental%20thrombosis-Month%20(US).png)

![Fetal placental thrombosis-People (Global)](Fetal%20placental%20thrombosis-People%20(Global).png)

![Fetal placental thrombosis-People (US)](Fetal%20placental%20thrombosis-People%20(US).png)

![Fetal stillbirth-Dose (Global)](Fetal%20stillbirth-Dose%20(Global).png)

![Fetal stillbirth-Dose (US)](Fetal%20stillbirth-Dose%20(US).png)

![Fetal stillbirth-Month (Global)](Fetal%20stillbirth-Month%20(Global).png)

![Fetal stillbirth-Month (US)](Fetal%20stillbirth-Month%20(US).png)

![Fetal stillbirth-People (Global)](Fetal%20stillbirth-People%20(Global).png)

![Fetal stillbirth-People (US)](Fetal%20stillbirth-People%20(US).png)

![Fetal vascular mal-perfusion-Dose (Global)](Fetal%20vascular%20mal-perfusion-Dose%20(Global).png)

![Fetal vascular mal-perfusion-Dose (US)](Fetal%20vascular%20mal-perfusion-Dose%20(US).png)

![Fetal vascular mal-perfusion-Month (Global)](Fetal%20vascular%20mal-perfusion-Month%20(Global).png)

![Fetal vascular mal-perfusion-Month (US)](Fetal%20vascular%20mal-perfusion-Month%20(US).png)

![Fetal vascular mal-perfusion-People (Global)](Fetal%20vascular%20mal-perfusion-People%20(Global).png)

![Fetal vascular mal-perfusion-People (US)](Fetal%20vascular%20mal-perfusion-People%20(US).png)

![forest-Dose (Global)](forest-Dose%20(Global).png)

![forest-Dose (US)](forest-Dose%20(US).png)

![forest-Month (Global)](forest-Month%20(Global).png)

![forest-Month (US)](forest-Month%20(US).png)

![forest-People (Global)](forest-People%20(Global).png)

![forest-People (US)](forest-People%20(US).png)

![Low amniotic fluid-Dose (Global)](Low%20amniotic%20fluid-Dose%20(Global).png)

![Low amniotic fluid-Dose (US)](Low%20amniotic%20fluid-Dose%20(US).png)

![Low amniotic fluid-Month (Global)](Low%20amniotic%20fluid-Month%20(Global).png)

![Low amniotic fluid-Month (US)](Low%20amniotic%20fluid-Month%20(US).png)

![Low amniotic fluid-People (Global)](Low%20amniotic%20fluid-People%20(Global).png)

![Low amniotic fluid-People (US)](Low%20amniotic%20fluid-People%20(US).png)

![Menstrual abnormality-Dose (Global)](Menstrual%20abnormality-Dose%20(Global).png)

![Menstrual abnormality-Dose (US)](Menstrual%20abnormality-Dose%20(US).png)

![Menstrual abnormality-Month (Global)](Menstrual%20abnormality-Month%20(Global).png)

![Menstrual abnormality-Month (US)](Menstrual%20abnormality-Month%20(US).png)

![Menstrual abnormality-People (Global)](Menstrual%20abnormality-People%20(Global).png)

![Menstrual abnormality-People (US)](Menstrual%20abnormality-People%20(US).png)

![Miscarriage-Dose (Global)](Miscarriage-Dose%20(Global).png)

![Miscarriage-Dose (US)](Miscarriage-Dose%20(US).png)

![Miscarriage-Month (Global)](Miscarriage-Month%20(Global).png)

![Miscarriage-Month (US)](Miscarriage-Month%20(US).png)

![Miscarriage-People (Global)](Miscarriage-People%20(Global).png)

![Miscarriage-People (US)](Miscarriage-People%20(US).png)
