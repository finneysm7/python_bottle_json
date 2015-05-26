from bottle import route, run
import json

@route('/goal_points')

def goal_points():
    return json.dumps({"total_points": 50000, "current_points": 10000, "reward": 50.00})

@route('/daily_points')
def daily_points():
    return json.dumps({
"2015-05-17": 0,
"2015-05-18": 100,
"2015-05-19": 2134,
"2015-05-20": 10})

@route('/message')
def message():
    return json.dumps(
{"message": "Go to Your Connected Apps", "href": "https://..."}
)

@route('/activity_feed')
def activity_feed():
    return json.dumps([{"date": "2015-05-24", 
"activities":[
{"activity": "steps", "message": "Walked 2931 steps and earned 29 points"},
{"activity": "weight", "message": "Weighed self 189.0lbs and earned 10 points"}
]},
    {"date": "2015-05-23", 
"activities":[
{"activity": "steps", "message": "Walked 6354 steps and earned 51 points"},
    {"activity": "steps", "message": "Walked 12403 steps and earned 89 points"},
{"activity": "weight", "message": "Ran 1.7 miles and earned 69 points"}
]},
    {"date": "2015-05-22", 
"activities":[
{"activity": "steps", "message": "Walked 3169 steps and earned 30 points"},
{"activity": "steps", "message": "Walked 7787 steps and earned 60 points"}
]}])

run(host='localhost', port=8080)
