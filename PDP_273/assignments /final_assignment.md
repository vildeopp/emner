
### File: Call_7_Vehicle_3.txt 

|                        | Average objective | Best Objective| Improvement | avg. Runtime    |
|-----------             | ----------- | ----------- | -----------   | ----------- |             
| submitted code       | 1134176.0  | 1134176.0   |  65.023        |  10.326148  |       

best solution = [4, 4, 7, 7, 0, 2, 2, 0, 1, 5, 5, 3, 3, 1, 0, 6, 6]

### File: Call_18_Vehicle_5.txt

|                        | Average objective | Best Objective| Improvement | avg. Runtime    |
|-----------             | ----------- | ----------- | -----------   | ----------- |             
| submitted code       |2972872.4  | 2725820.0 |69.577        |  38.919 |   

best solution = [4, 4, 15, 15, 12, 12, 16, 16, 0, 6, 6, 11, 14, 11, 14, 0, 8, 3, 3, 18, 18, 8, 13, 13, 0, 9, 9, 5, 5, 17, 17, 0, 7, 7, 10, 10, 1, 1, 0, 2, 2]

### File: Call_35_Vehicle_7.txt

|                        | Average objective | Best Objective| Improvement | avg. Runtime    |
|-----------             | ----------- | ----------- | -----------   | ----------- |             
| submitted code       |9879556.0 |  9082456.0| 50.606       | 23.77497 |  

best solution = [15, 15, 30, 7, 7, 30, 18, 18, 0, 16, 16, 11, 11, 22, 22, 20, 20, 0, 8, 8, 27, 27, 28, 28, 2, 2, 0, 4, 4, 23, 23, 17, 5, 5, 17, 0, 9, 6, 6, 9, 33, 33, 31, 31, 0, 3, 3, 1, 13, 13, 32, 1, 32, 0, 14, 14, 35, 35, 10, 10, 0, 34, 34, 24, 24, 21, 21, 26, 26, 12, 12, 19, 19, 29, 29, 25, 25]

### File: Call_80_Vehicle_20.txt

|                        | Average objective | Best Objective| Improvement | avg. Runtime    |
|-----------             | ----------- | ----------- | -----------   | ----------- |             
| submitted code       |  21712358.7 |  20818454.0|  55.488        | 52.8134 |  

Best solution = [70, 18, 70, 18, 12, 12, 73, 73, 0, 41, 41, 68, 68, 37, 17, 37, 17, 0, 34, 65, 65, 34, 14, 14, 0, 30, 30, 69, 69, 33, 33, 0, 49, 67, 49, 72, 72, 67, 0, 61, 61, 55, 42, 42, 55, 0, 11, 11, 45, 44, 44, 45, 0, 63, 63, 5, 5, 10, 10, 0, 53, 21, 21, 53, 28, 28, 0, 32, 79, 79, 32, 80, 80, 0, 51, 51, 27, 27, 56, 56, 0, 46, 36, 46, 7, 7, 36, 0, 35, 35, 58, 58, 50, 50, 0, 57, 57, 2, 2, 6, 6, 0, 66, 9, 9, 66, 48, 77, 77, 48, 0, 25, 25, 71, 71, 75, 75, 0, 22, 22, 31, 31, 52, 52, 0, 23, 23, 76, 76, 16, 16, 0, 40, 40, 13, 13, 3, 3, 0, 1, 29, 29, 1, 24, 24, 0, 43, 43, 60, 60, 39, 39, 38, 38, 62, 62, 47, 47, 15, 15, 54, 54, 78, 78, 74, 74, 20, 20, 26, 26, 4, 4, 8, 8, 64, 64, 59, 59, 19, 19]

### File: Call_130_Vehicle_90.txt

|                        | Average objective | Best Objective| Improvement | avg. Runtime    |
|-----------             | ----------- | ----------- | -----------   | ----------- |             
| submitted code       |35335093.2 |  31112451.0 | 59.398        | 119.5086  |  


## OPERATORS 

### insert_two_exchange 
compares the length of each vehicle route and takes the smallest and longest route. if the difference of this is larger than a number (number of calls divided by a ratio, were ratio = num calls / num vehicles) it inserts a call from the longest route into the shortest route else it switches two calls from each route.
### try_for_best 
chooses a call from the dummy route and inserts it at best possible place in a suitable car
### shuffle_route 
Chooses a call a shuffles its route a number of times and if it finds a better combination returns the solution
### move_to_next_vehicle
chooses a vehicle and a call and finds the next suitable vehicle and inserts it there, 
### escape 

n = num_calls / num vehicles
chooses between 1 and n calls to insert back to dummy


