from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
<html>
<body>

<h2>Welcome to Reminder Service</h2>

<form method="POST" action="/save_event">
  <label for="event_name">event_name:</label><br>
  <input type="text" name="event_name"><br>
  <label for="Day">Day:</label><br>
  <input type="integer" name="day"><br>
  <label for="Month"> Month:</label><br>
  <input type="integer" name="month" ><br><br>
  <input type="Submit" value="Submit">

</form>

</body>
</html>
    """

@app.post("/save_event")
async def save_event(event_name: str = Form(), day: int = Form(), month: int = Form()):
    return{"event_name":event_name, "Day":day, "Month":month}
    




