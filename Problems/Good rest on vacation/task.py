# put your python code here
days = int(input())
total_food_cost = int(input())
one_flight_cost = int(input())
cost_of_one_night = int(input())

print(total_food_cost * days + cost_of_one_night * (days - 1) + 2 * one_flight_cost)