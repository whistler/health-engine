Inputs
======

Sensor based
------------
- Pulse
- Sleep
- BP
- Activity

User parameters
---------------
- Age
- Weight
- Height
- Takes pills?

Processing
==========

Instance Recommender
--------------------
Takes only the current readings for the user as input and provides recommendations based on a single point in time. These recommendations are
based on a lookup table which sets limits beyond which a particular
recommendation would be triggered.

Time Series Recommender
-----------------------
Takes all available values in the time series and finds statistical parameters over a range of time such as gradient, range, etc and uses another lookup table
which triggers a recommendation if any of these parameters are beyond a set
limit.

Post Processor
--------------
Combines the recommendations produced by the two recommenders and suggests if
a current problem might be caused by earlier problems.

Outputs
=======
- Recommendation
- Source
- Severity

