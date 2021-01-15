# Introducion
This is a Django app to develop REST API for collecting Electronic device data from various website. This allows user to register and suscribe various topic like mobile, TV, drone. These suscribed topics data will only be displayed to user.


## Main Features
* Django REST API
* User Authentication
* Topic Subscription
* Display suscribed topic


## API endpoints
No | Method | Endpoint | Description | 
--- | --- | --- | --- 
1 | POST | /auth/register/ | register new user |
2 | POST | /auth/login/ | login |
3 | GET | /subscription/ | lists subscibed topic | 
4 | POST | /subscription/ | suscribe new topic |
5 | GET | /item/ | display suscribed topic's item 

## Overview
This app uses `APScheduler` library to automatically update content everyday. These content are stored in Item table. When a user request for an item, initially user suscribed topic are retrieved and only those topic will be displayed to user.






 
