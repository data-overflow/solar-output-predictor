# solar-output-predictor
ENIGMATIC ENERGISERS![image](https://user-images.githubusercontent.com/115616429/232687730-962de86a-7db4-435b-a0d0-12715b8abcf1.png)
THEME NAME : Prediction of electricity generation by solar panel at any location, date.
(7th SDG Goal - Affordable and Clean Energy)
![image](https://user-images.githubusercontent.com/115616429/232687755-233ac11b-c676-47be-a898-aea428c5bcb2.png)
![image](https://user-images.githubusercontent.com/115616429/232687782-4603b999-51cd-41a6-b511-2f3f79f75889.png)
PROBLEM STATEMENT![image](https://user-images.githubusercontent.com/115616429/232687812-adab2080-8485-4adf-92df-1f88d6b0697e.png)
To create a user friendly model which calculates the electricity generated by the solar panels on a given specific date and location.
![image](https://user-images.githubusercontent.com/115616429/232687833-666d0c36-2c8b-4203-b2ce-4836e5793b2b.png)
SOLUTION
![image](https://user-images.githubusercontent.com/115616429/232687866-baf4f955-cf04-4f5c-8b03-a5dff2501367.png)
WE CREATED A MOBILE APPLICATION WHICH IS VERY USER FRIENDLY AND CAN BE USED BY COMMON PEOPLE TO FIND THE ELECTRICITY GENERATED BY SOLAR PANELS![image](https://user-images.githubusercontent.com/115616429/232687882-1e42e012-a454-4245-b634-ff4614c2dd71.png)
It has the ability to calculate for past, live and future dates. 
It also covers the whole globe in terms of location.
It considers factors like wind speed, temperature and other weather conditions.
![image](https://user-images.githubusercontent.com/115616429/232687906-2a8988e5-7146-46c9-a3fd-73d5207e32b4.png)
INTRODUCING YOU OUR APPLICATION – RA WATTS (THE solar output predictor)![image](https://user-images.githubusercontent.com/115616429/232687938-c0a87421-78c9-446b-9347-3958ec57b1a9.png)
![image](https://user-images.githubusercontent.com/115616429/232687954-3cca7f02-9173-4f6e-b041-39e068a24e37.png)
![image](https://user-images.githubusercontent.com/115616429/232687968-28deb8cb-3ec5-4fde-8cc1-3ff7fc832358.png)
![image](https://user-images.githubusercontent.com/115616429/232687980-845ee333-05de-415b-becf-303294239390.png)
REQUIRED INPUTS:
PLACE NAME
COUNTRY NAME
START DATE
END DATE
NUMBER OF SOLAR PANELS/ AREA OF SOLAR PANEL
RATING OF SOLAR PANEL
![image](https://user-images.githubusercontent.com/115616429/232687992-ae7dffda-196f-445b-9538-413fe9ba44e7.png)
THE PROCESS![image](https://user-images.githubusercontent.com/115616429/232688022-38af2a0b-4815-4de7-8d64-532e6843e706.png)
We calculate the latitude and longitude of the given using geopy python libraries.

The sunlight period of a place is calculated using suntime python libraries.

We created a new function which calculates efficiency based on inputs like location, date, solar panel rating and considers factors like solar position, irradiance, dni, ghi, dhi.

Finally we calculate the electricity produced by multiplying the variables of number of solar panels, ratings of solar panels, efficiency, sunlight period.
![image](https://user-images.githubusercontent.com/115616429/232688044-d11906ec-e5b5-41e4-b123-5d13aaffa616.png)
TECHNOLOGY STACKs USED![image](https://user-images.githubusercontent.com/115616429/232688086-c4dda748-62e1-4698-89bd-88e91455934f.png)
Front end
![image](https://user-images.githubusercontent.com/115616429/232688111-5de74d78-1d9b-4fac-b9db-814a425ca94f.png)
Godot game engine
![image](https://user-images.githubusercontent.com/115616429/232688133-bd101a29-ade0-49f6-84f5-046172612edf.png)
Back end
![image](https://user-images.githubusercontent.com/115616429/232688153-069c8054-0d0a-4154-b033-aed8d3b73f2f.png)
Flask and Python
math library
panda library
datetime library
geopy library
suntime library
![image](https://user-images.githubusercontent.com/115616429/232688179-83a8bb44-61b0-450e-933b-4b8fd1de20cc.png)
