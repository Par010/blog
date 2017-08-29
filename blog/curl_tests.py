'''
curl -X POST -d "username=test&password=testpassword" http://127.0.0.1:8000/api/auth/token/
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJ1c2VyX2lkIjo1LCJlbWFpbCI6ImFzZGFzZEBhc25kLmNvbSIsImV4cCI6MTUwNDAxOTU3NH0.EHaHwuRnHLcnfVEDhb4vr_lM9ivgN5RZpA47O005QO8
curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJ1c2VyX2lkIjo1LCJlbWFpbCI6ImFzZGFzZEBhc25kLmNvbSIsImV4cCI6MTUwNDAxOTU3NH0.EHaHwuRnHLcnfVEDhb4vr_lM9ivgN5RZpA47O005QO8"  http://127.0.0.1:8000/api/comments/

curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo1LCJleHAiOjE1MDQwMjEwOTcsImVtYWlsIjoiYXNkYXNkQGFzbmQuY29tIiwidXNlcm5hbWUiOiJ0ZXN0In0.gNCRkuehYajQacWmoTqnuQqzMm0JnhXctGqO09PvKLw" -H "Content-Type: application/json" -d '{"content":"reply content with JWT"}' 'http://127.0.0.1:8000/api/comments/create/?type=post&slug=another-new&parent_id=11'

curl  http://127.0.0.1:8000/api/comments/

'''
