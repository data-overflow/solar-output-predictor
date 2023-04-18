# solar-output-predictor
ENIGMATIC ENERGISERS! <br>
THEME NAME : Prediction of electricity generation by solar panel at any location, date. <br>
(7th SDG Goal - Affordable and Clean Energy) <br>
PROBLEM STATEMENT! <br>
To create a user friendly model which calculates the electricity generated by the solar panels on a given specific date and location. <br>
SOLUTION <br>
WE CREATED A MOBILE APPLICATION WHICH IS VERY USER FRIENDLY AND CAN BE USED BY COMMON PEOPLE TO FIND THE ELECTRICITY GENERATED BY SOLAR PANELS! <br>
It has the ability to calculate for past, live and future dates. <br>
It also covers the whole globe in terms of location. <br>
It considers factors like wind speed, temperature and other weather conditions. <br>
INTRODUCING YOU OUR APPLICATION – RA WATTS (THE solar output predictor)! <br>
REQUIRED INPUTS: <br>
PLACE NAME <br>
COUNTRY NAME <br>
START DATE <br>
END DATE <br>
NUMBER OF SOLAR PANELS/ AREA OF SOLAR PANEL <br>
RATING OF SOLAR PANEL <br>
We calculate the latitude and longitude of the given using geopy python libraries. <br>
The sunlight period of a place is calculated using suntime python libraries. <br>
We created a new function which calculates efficiency based on inputs like location, date, solar panel rating and considers factors like solar position, irradiance, dni, ghi, dhi. <br>
Finally we calculate the electricity produced by multiplying the variables of number of solar panels, ratings of solar panels, efficiency, sunlight period. <br>
TECHNOLOGY STACKs USED <br>
Front end <br>
Godot game engine <br>
Back end <br>
Flask and Python <br>
math library <br>
panda library <br>
datetime library <br>
geopy library <br>
suntime library <br>