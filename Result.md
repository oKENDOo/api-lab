# API lab results 

## Part 0 
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401 Unauthorized
- Step 0.4, the name of your pizza: The Fresh Bolognese
- Step 0.12, results of the three runs without a session (optional): -
- Step 0.16, blocks of "how many of the three tools are excluded":  
    - 0 tools: []
    - 1 tool: ["Knife"] / ["Scissors"]
    - 2 tools: ["Knife", "Pizza cutter"]
    - 3 tools: ["Knife", "Pizza cutter", "Scissors"]
  
## Defect report 
- Title: Excluding all pizza tools causes an internal server error
- Request: POST /api/pizza with excludedTools set to Knife, Pizza cutter, and Scissors
- Expected result: 400 Bad Request with a JSON error message
- Actual result: 500 Internal Server Error with an empty response body
- Severity: Medium
  
## Part A - Step A4, status codes when the other user reads, changes and deletes: 

## Part B 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
