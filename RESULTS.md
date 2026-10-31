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
  
## Part A 
- Step A4, status codes when the other user reads, changes and deletes: 
  - GET: 404
  - PUT: 400
  - DELETE: 400

## Part B 
1. API tests เจอปัญหา เช่น server/database ทำงานร่วมกันผิดพลาด และปัญหาเครือข่ายหรือ load balancer ซึ่ง unit test ที่ใช้ stub หาไม่ได้ ส่วน unit test ยังจำเป็นเพราะรันเร็ว ผลคงที่ และช่วยแยกตรวจ logic ของโค้ดส่วนเล็ก ๆ ได้
2. แต่ละ test สร้าง user ใหม่เพื่อไม่ให้ข้อมูลของคนอื่นหรือ test อื่นมารบกวนกัน และไม่ควรแก้ไขข้อมูลผ่าน public token ใน Project 2 จะสร้างข้อมูล shop/hotel ของ test เองด้วยชื่อหรือรหัสแบบสุ่ม แล้วลบหรือแยกข้อมูลหลังจบ test
3. Session เก็บ cookie เช่น AWSALB ทำให้ request หลังจาก create/login ไปยัง server เดิม จึงเห็น user และข้อมูลที่สร้างไว้ หากไม่ใช้ session load balancer อาจส่งไปคนละ server จน login หรือ request ล้มเหลวแบบไม่แน่นอน 
4. ไม่ได้ทำ Step 0.12
5. Base choice coverage ต้องใช้ : 1 + (3-1) + (4-1) + (2-1) + (3-1) = 9 tests
All combinations coverage ต้องใช้: 3 × 4 × 2 × 3 = 72 tests
6. Other user ได้ status ดังนี้: GET = 404, PUT = 400, DELETE = 400 // คาดหวังให้ทุก request ถูกปฏิเสธด้วย 4xx เช่น 403 หรือ 404 เพื่อป้องกันไม่ให้ user อื่นอ่าน แก้ หรือ ลบ rating ได้ หากได้ 2xx ถือเป็น defect ด้านสิทธิ์การเข้าถึง ส่วน 403 กับ 404 อาจไม่ใช่ defect เพราะบางระบบตั้งใจตอบ 404 เพื่อไม่เปิดเผยว่าข้อมูลนั้นมีอยู่
7. API ตอบ 200 แม้ token เป็น token ปลอมที่มีความยาว 16 ตัวอักษร นี่เป็น defect เพราะระบบตรวจเพียงรูปแบบหรือความยาวของ token ไม่ได้ตรวจว่าเป็น token ของ user จริง ในระบบจริง คนแปลกหน้าอาจอ่านข้อมูลส่วนตัวหรือข้อมูลลูกค้าได้
8. API test ตรวจ status code, JSON และข้อมูลที่ส่งกลับได้แม่นยำและรวดเร็วกว่า ส่วน web-page test ตรวจสิ่งที่ผู้ใช้เห็นและใช้งานได้จริง
