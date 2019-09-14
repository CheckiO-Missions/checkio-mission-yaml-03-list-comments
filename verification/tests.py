"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
       {
        "input": ["""- write some
- "Alex Chii"
- 89"""],
        "answer": [
  "write some", 
  "Alex Chii", 
  89
]
        },{
        "input": ["""# comment
- write some # after
# one mor
- "Alex Chii #sir "
- 89 #bl"""],
        "answer": [
  "write some", 
  "Alex Chii #sir ", 
  89
]
        },{
        "input": ["""- 1
- 2
- 3

- 4



- 5"""],
        "answer": [
  1, 
  2, 
  3, 
  4, 
  5
]
        },{
        "input": ["""-
-
-
- 7"""],
        "answer": [
  None, 
  None, 
  None, 
  7
]
        }
    ],
    "Extra2": [
        {
            "input": ["""name: Alex
age: 12"""],
            "answer": { 
              "name": "Alex",
              "age": 12
            }
        },
        {
            "input": ["""name: Alex Fox
age: 12

class: 12b"""],
            "answer": {
              "age": 12, 
              "name": "Alex Fox", 
              "class": "12b"
            }
        },
        {
            "input": ["""name: "Alex Fox"
age: 12

class: 12b"""],
            "answer": {
              "age": 12, 
              "name": "Alex Fox", 
              "class": "12b"
            }
        },
        {
            "input": ["""name: "Alex \\"Fox\\""
age: 12

class: 12b"""],
            "answer": {
              "age": 12, 
              "name": "Alex \"Fox\"", 
              "class": "12b"
            }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
alive: false"""],
          "answer": {
            "name": "Bob Dylan", 
            "alive": False, 
            "children": 6
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding:"""],
          "answer": {
            "coding": None, 
            "name": "Bob Dylan", 
            "children": 6
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding: null"""],
          "answer": {
            "coding": None, 
            "name": "Bob Dylan", 
            "children": 6
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding: "null" """],
          "answer": {
            "coding": "null", 
            "name": "Bob Dylan", 
            "children": 6
          }
        }
    ],
    "Extra3": [
        {
            "input": ["""
name: Alex
age: 12"""],
            "answer": { 
              "name": "Alex",
              "age": 12
            },
            "explanation": "Extra space at the beginning"
        },
        {
            "input": ["""12: 12"""],
            "answer": {"12": 12},
            "explanation": 'Key can be int'
        },
        {
            "input": ["""name: Bob Dylan
burn: 24 May 1941
resident: Malibu, California, U.S

children: 6"""],
            "answer": {
              "resident": "Malibu, California, U.S", 
              "burn": "24 May 1941", 
              "name": "Bob Dylan", 
              "children": 6
            }
        }
    ]
}
