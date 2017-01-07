# restaurant-health
Georgetown Data Science Restaurant Health Inspection Rating Prediction Project

Data Science Capstone Project Proposal

Team members: Sarah Khederian (coordinator), Matt Steele, David Barnhart, Mary Mallampalli

Domain chosen: Retail/Industry

Hypothesis or project topic: Using Yelp reviews to create a predictive model determining health inspection ratings.

Available data sources (or where you’re going to get the data from):
•	Yelp API for present data – written reviews, star ratings, number of reviews, neighborhoods
•	State/Local health inspection grade data and report rhetoric (one city will be chosen based on the robustness and variance in the data) 
o	DC: http://data.codefordc.org/dataset/restaurant-inspection-data 
o	Omaha: http://www.douglascountyhealth.com/images/stories/food/Rating%20List%20as%20of%20080116.pdf 
o	Seattle: http://www.kingcounty.gov/healthservices/health/ehs/foodsafety/inspections/data.aspx 
o	Dallas: http://www2.dallascityhall.com/FoodInspection/SearchScoresAction.cfm?PageNum_q_search=1 
o	NYC: http://www1.nyc.gov/site/doh/services/restaurant-grades.page 

A brief description of what you will do: 

According to the CDC, one in six Americans contracts a foodborne illness each year. Given that half of all money spent on food is spent in restaurants according to one 2008 study, many Americans are becoming sick from food they consume in restaurants. The health of these patrons is increasingly important to state and local governments; however, health department inspectors are frequently overwhelmed by the increasing number of restaurants in their purview. For example, the abundance of food trucks has slowed licensing, inspection, and food entrepreneurship, to a halt in Salt Lake City. We propose to train a model to incorporate Yelp’s written reviews, star ratings, and check-ins to determine a restaurant’s health inspection score. This will allow health inspectors to more efficiently allocate resources to the most at-risk food establishments. This model will then take recent reviews to determine how health inspection scores have fluctuated since the last date of inspection, allowing the Health Department to target those restaurants between set inspection dates.

We imagine our process to be the following:
-	Determine the city we will examine and gather historical and present Yelp and Health Department data from it.
-	Train a model to:
o	Perform sentiment analysis on the written reviews and health inspection reports to identify indicators of poor/good health/sanitation alongside the restaurants' respective health scores
o	Identify correlations between a restaurant’s Yelp star ratings, check-ins, neighborhood and other available data points with their respective health scores 
o	Examine not just a restaurant’s most recent reviews/health inspection scores, but its historical data demonstrating how health inspection scores fluctuate alongside Yelp reviews
-	Test the accuracy of the model against the most recent health inspection grade and coinciding period of Yelp reviews.
-	Test the accuracy of the model against other cities’ Yelp reviews/health inspection grades.
-	Use the model to predict, based on Yelp reviews posted after the last date of inspection, how a restaurant’s health inspection score has changed/make recommendations to Health Department for increased resources. 

Questions/issues with the project design:
•	Restaurant health inspection scores range from letter grades, violation counts (for example, 1-28 in New York City) or on a 1-100 scale. We’re trying to determine the city with the best kind of data in order to increase the accuracy of our model. One additional issue here is that the vast majority of health inspection scores are what would be in the ‘A’ range. Would this decrease the accuracy of a model predicting scores outside of that range?
•	Given the variance of restaurant names by city, we're anticipating having to reconcile Yelp restaurant reviews and their health inspection ratings either using name or address.
o	One way to address this issue (and determine the city that we will examine) could be to determine the highest match rate between Yelp restaurants and Health Department restaurants. 

Avenues of exploration required for the project:
•	Using geographically distinct neighborhoods or cities to identify differences in rhetoric related to health/sanitation – for example, will a model trained on data in DC have the same level of accuracy when applied to Dallas?
•	Determining correlations between star reviews, check-ins, etc. with good/poor health inspection ratings.
•	How does Yelp review rhetoric change as health inspection scores fluctuate (per restaurant)? Can this rhetoric be used in the algorithm?
