It’s been a while since I’ve written a post for the newsletter. At least I’m still doing programming!

I’ve been busy with real work, including a couple of side projects that I think are really important. Below is the result of one of those projects: an augmentation of a model to help our policy makers decide what to do with this whole pandemic thing. I’m starting to get some traction with the Colorado government, so that’s great! But I figured that since my readership is far and wide and a good collection of smart and connected folks, maybe someone else might find this useful or know of someone in their government that might find this useful. Please share with anyone who you think may find this or something similar useful.

If you want a well formatted PDF, let me know. Substack leaves a lot to be desired if you want to publish anything other than basic HTML (but I guess that’s their market).

# Pandemic: Decision Support For A Novel Problem And Its Challenges

The sudden emergence of the coronavirus global pandemic has created a novel challenge for Colorado's decision makers. This virus is especially contagious, transmitting rapidly from person-to-person, and its effects on infected individuals range from asymptomatic to extended hospitalizations and death. Additionally, the long incubation period, as long as 14 days, means that any data used to support decisions is out-of-date. The challenge policy makers face is determining actions to slow the virus in order to prevent unnecessary human suffering and to save lives.

The virus appears to be primarily transmitted by airborne droplets. The highest rates of transmission happen when people are close together indoors for extended periods and not wearing masks. This suggests that the solution is to encourage or enforce some level of quarantine or stay-at-home policy to minimize person-to-person contact. A strict stay-at-home policy will stop the virus; however, it contributes to personal suffering via economic harm, unemployment, and problems related to social isolation (e.g., abuse, mental health). **We must balance the need to stay apart to slow the virus with the need to be together to keep the economy progressing.**

We face a dilemma: closing down the state too much to slow the spread of the virus comes with severe economic repercussions, while opening up the state too much in an attempt to save jobs allows the virus to get a foothold. There are both political and game-theoretic pressures on how and when to open up: a state that opens early will pull economic activity from its neighbors. When policy makers face such high-stakes trade-offs, emotion and bias inevitably creep in. **A mathematical and scientific approach that minimizes human bias and helps us to decide the optimal course of action can provide critical inputs to the decision process.**

# Predictive Model

Deciding what level of economic shut-down to enforce is difficult because any infection or hospital usage data is, at best, representative of the state two weeks ago. The Colorado COVID-19 modeling group has been putting in a heroic effort to create a predictive model based on the empirical data collected from hospitals around the state. Using this model we are able to extrapolate how the virus spreads. The Colorado COVID response team has been using this model to inform policy and prepare the hospitals for high demand.

The model that the team has created is a SEIR (**S**usceptible, **E**xposed, **I**nfected, **R**ecovered) model. The most basic form of this model can be described as follows:

[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c6220a80-cb76-4271-8363-23fb344e48a1_560x54.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6220a80-cb76-4271-8363-23fb344e48a1_560x54.png)

There are a number of *susceptible* people in the population. They are exposed to the virus at some rate, r1. The *exposed* population becomes infected at another rate, r2. The *infected* population recovers (or, unfortunately, dies) at another rate, r3, resulting in the *recovered* population. This assumes that recovered people have (at least temporary) immunity and don't become susceptible again.

How do we affect r1? We can make r1 smaller through interventions like a stay-at-home order, gathering and business restrictions, or mask wearing, slowing the rate of exposure. That's the only control a policy maker has over this virus.

How do we affect r2? We can't: r2 is a biological function of how the virus interacts with an exposed person. Presuming that an individual gets enough viral load to become sick they will become infected at this rate. Otherwise they will go back to simply being susceptible. This isn’t shown in this simplified example, but the full Colorado COVID-19 model takes this into account.

How do we affect r3? We can improve efficacy of treatment to increase r3 and reduce the length of hospital stays. Keep in mind that the *infected* category includes people that are asymptomatic and may not even be aware of their infection, people that are ill and have a a few days of flu-like symptoms, and people that need intensive care at the hospital. The full Colorado COVID-19 model accounts for all of this complexity, which we simplify here to just the rate r3. As our doctors and scientists learn more, they have the largest effect on r3 by tailoring the care the infected people receive.

# Prescriptive Model

Clearly, we can beat this virus and prevent it from causing death and suffering by keeping the exposure rate, r1, small. We can make this rate nearly zero by instituting a *very* restrictive stay-at-home policy. However, that decision will cause increased unemployment and economic harm, which may also cause widespread death and suffering. **There are trade-offs to consider between fully stay-at-home and a fully open economy that balance the risk of the death and suffering caused by the virus and the risk suffering caused by state-wide economic harm.**

OptTek Systems, in Boulder, CO, specializes in solving exactly these kinds of complex problems. We propose a solution that extends the Colorado COVID-19 *predictive* model so that it can become a *prescriptive* model that helps policy makers better evaluate the impact of varying levels of restriction. (Here we will use restrictions to refer to policies on social distancing, mask wearing, gatherings, retail, services, restaurants, bars, and public facilities, from guidelines all the way up to enforced stay-at-home policies.) Our model aims to find the level of restrictions that keeps our population healthy and out of the hospital but that does not result in undue economic harm.

Every week, the Colorado COVID-19 Modeling team updates their model with the latest parameters to 1) assess the effectiveness of the previous week's interventions and 2) predict outcomes for the next few weeks. As more Coloradans wear masks, the value of r1 gets smaller, which takes the the pressure off our hospitals. Likewise, as our policy makers implement different levels of restrictions, we can affect the exposure rate. The existing model uses a "social distance factor," or S, to capture the effects of different restrictions.

An S value of 1.0 means 100% social distancing, everyone stays home, the exposure rate is small, and the economy suffers. An S value of 0.0 means no social distancing, life is like before March 2020, the virus spreads like wildfire, and hospitals and ICUs are overwhelmed, resulting in a much higher death rate for infected individuals.

We believe that by using historic data we can map restriction levels to values for S. A notional example is:

[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/a1ac0787-2732-4a6b-bfb6-8644dbf5d55d_921x361.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1ac0787-2732-4a6b-bfb6-8644dbf5d55d_921x361.png)

*These levels and numbers presented here are just an example of how this would operate. We anticipate that the Colorado COVID-19 Modelling team has internal data that can actually translate between proposed restriction levels and a social distance factor. The actual values and the actual number of levels can be applied to our model with no additional effort.*

Using the Colorado COVID-19 Model, we can use these values of S and predict values such as the daily hospitalization rate, daily ICU bed use, and other patient outcomes. Naturally, as the ICU begins to get overwhelmed, we will need to go to a higher level of restrictions, but when do we make that call? This is especially difficult when the available data, current daily infections, is a lagging indicator for hospitalizations!

We have updated the Colorado COVID-19 Model to dynamically adjust the value of S in response to the level of restrictions. Additionally, the model will dynamically adjust the value of the restriction level as a response to how many ICU beds are in use. What does this mean? We are using *ICU beds in use* as a proxy for the human cost of the virus. When we run the model, we calculate *ICU beds in use* for each day. Then, as the model is running, we use *ICU beds in use* to adjust the restriction level. When the restriction level changes, the value of S changes in real time.

The advantage of using a measurement like *ICU beds in use* for the feedback is that it behaves like a low-pass filter and we remove the noise in the data related to virology testing. The current level of testing is not as accurate as we would like and it's highly dependent on the amount of testing and *who* gets tested. All of that is filtered out by monitoring a more slowly changing value like *ICU beds in use*.

We have also added a measure of economic impact to the Colorado COVID-19 Model. *Economic impact* is responsive to the restriction level. As the restriction level increases, there will be less exposure to the virus and *ICU beds in use* will decrease, but the (negative) *economic impact* will increase.

Using OptTek's simulation-optimization software, SimWrapper, we are able to determine when to switch restriction levels based on *ICU beds in use*. We create ranges of *ICU beds in use* for each restriction level. When *ICU beds in use* is greater than the upper bound of the range, we increase the restriction level, and when *ICU beds in use* drops, we decrease the restriction level. We then systematically search for specific ranges that minimize both the human suffering due to the virus and the human suffering due to economic harm.

# An Example

As an example, using the Colorado COVID-19 Model published on 3 July 2020, a fixed value of S=0.65 returns a prediction of *ICU beds in use* like this:



[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/3088b885-43cd-41aa-9905-a5014cf93b76_560x420.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3088b885-43cd-41aa-9905-a5014cf93b76_560x420.png)



The early peak is historical data from when the situation was dire early in the spring. The second half of the plot is the prediction of *ICU beds in use* based on the fixed value of social distancing.

With the extended model, as it is computing the results of each day, we can inspect the daily *ICU beds in use*. Using that information, we can change the level of restrictions *while running the model*.

As a notional example, consider these conditions:



[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/fe1e4598-009e-45f4-8f19-50b510b0b44f_921x472.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe1e4598-009e-45f4-8f19-50b510b0b44f_921x472.png)



The challenge is to optimally determine the ranges for each policy. Using the notional ranges, the Colorado COVID-19 Model reports *ICU beds in use* like this:



[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/0c70e117-e475-483b-99b3-422821afd9df_560x560.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0c70e117-e475-483b-99b3-422821afd9df_560x560.png)



Again, that initial peak is historical data that we can't change. Notice, however, that after August 15 (when the model does the dynamic adjustment of S), *ICU beds in use* fluctuates according to the restriction level. Note: we did include a time constraint so that the level doesn't change any faster than 3 weeks. That value can be configured easily; we were avoiding too-frequent changing of the rules for practical reasons.

It may seem that a single stable set of policies would be the easiest to implement. When dealing with exponential growth and natural variance of compliance among Coloradans it's impossible to find a single rule that works. By allowing the level of our response to track the growth of the virus, we can manage the situation more reliably. Of course we can update the model in the future to reflect new information, for example, when we find a effective vaccine or learn a better treatment.

Additionally, at each restriction level, we keep track of an *economic impact* factor. For our notional model, we simply track a value between 0 and 1 for each restriction level each day. (0 is good: no impact, 1 is really bad: economy is crushed.) The daily sum of that is *economic impact*. Ideally, we would have unemployment data or something similar to create a more realistic model. The numbers presented here are notional to show how this would work, and can easily be substituted with real numbers when they're available.



[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/b8b9307c-bda8-4f63-946c-875d93e5e4d2_1063x361.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8b9307c-bda8-4f63-946c-875d93e5e4d2_1063x361.png)



We then run the model with a set of ranges (like the ones in the table above). We sum *ICU beds in use* and the *economic impact* for the entire run of the model and use OptTek's SimWrapper to systematically search for a set of ranges that minimizes both metrics of human suffering. SimWrapper works by selecting parameters, running the model with those parameters, collecting outputs, and deciding which new parameters to run. The full cycle looks like this:



[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/0eaaec52-51a4-4a48-8d2e-04fad9117921_560x382.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0eaaec52-51a4-4a48-8d2e-04fad9117921_560x382.png)



SimWrapper quickly tests tens of thousands of model parameters to quickly determine an optimal set. This specific problem is an optimization of two conflicting metrics, so the method we are using finds the efficient frontier, or Pareto frontier. Points along this frontier are the optimal options to present to our policy makers. The output of SimWrapper is a plot like this where the result of each simulation run is plotted based on the model outputs of both *ICU Beds In Use* and *Economic Impact*.



[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/a54edf3c-7b2a-47d1-91a9-f136b538a4e8_560x560.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa54edf3c-7b2a-47d1-91a9-f136b538a4e8_560x560.png)



Ideally, we could find a state in the bottom left corner of the plot where there is no hospital usage and no economic harm. Unfortunately, we can't, but the blue line is as close to that corner as we can get. In some configurations (A, for example), we've minimized hospital usage at the cost of great economic harm, and in other configurations (B, for example), we've done the opposite. The plot shows the entire space of trade-offs that are possible.

Additionally, policy makers will not want to consider certain scenarios. For example, the red points in the above plot represent any set of ranges that allow the daily ICU beds in use to exceed 1000. While we may want to minimize the amount of ICU beds in use over time, there is also a limit to the maximum that can be in use at any one time. For this notional model, we chose 1000 since it has a safe buffer below the Colorado maximum of 1800 beds. Any scenarios that appear in the red region can be immediately dismissed as infeasible solutions.

The goal is to find a knee in the plot, at C, for example, where we are doing as well as we can in both metrics. We can then examine the configuration at that point to see what the best set of ranges are. In this notional example we find these ranges at the knee in the frontier.



[![img](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/ec233317-ed49-416f-9529-e06693efa00e_921x361.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fec233317-ed49-416f-9529-e06693efa00e_921x361.png)



For comparison: the top of the range for *Complete Stay-at-home* in scenario A is 100, this minimized hospital usage but causes more unemployment. At scenario B, the the number of *ICU beds in use* where we begin restricting *Bars, Night Clubs, and Gyms* doesn't happen until over 1500, clearly that's too late! Seeing the frontier of trade-offs makes it much more clear to our decision makers on what the ranges should be. It easy to make a simple rule where we track *ICU beds in use* each day and use that to set the restriction level, and the frontier tells us at which levels to make those decisions.

These ranges came from running the predictive Colorado COVID-19 model, which accurately handles the 14-day lagging behavior. That means that our optimization will implicitly include the lag while searching for the ranges at which restriction level changes. No guesswork is needed to take into account the lag, since that's built into the the model. In fact, all of the dynamics of the original predictive model are automatically included in our prescriptive model. Additionally this need not be a single state-wide model, but could be tailored to individual counties producing a specific set of policies based on the hospital capacity and economic factors in each county.

# Conclusion

We propose this prescriptive model as valuable tool to determine policy in a transparent and scientifically defensible way to manage the trade-offs in the difficult problem of managing both the economy and public health of Colorado. We monitor one metric, *ICU beds in use*, and that directly points to a restriction level that has been optimized to minimize death and suffering by both the virus and economic harm.