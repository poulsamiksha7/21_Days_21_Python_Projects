import random

quotes=[
    "🤍YOU're not gaining weight,you are gaining strength!",
    "🧡Healthy weight is a form of self love",
    "⭐You glow diffrently when you grow intentionally"
]

selected=random.choice(quotes)

html_content=f"""
<html>
<head>
<title>Daily affirmation</title>
<style>
   body{{
   font-family:Arial;
   background: #fef6e4;
   display:flex;
   justify-content:center;
   align-items:center;
   height:100vh;
   }}
   .card{{
   padding:30px;
   border-radius:15px;
   background:white;
   box-shadow:0 4px 8px rgba(0,0,0,0.2);
   text-align:center;
   font-size:24px;
   }}
</style>
</head>
<body>
<div class="card">{selected}</div>
</body>
</html>
 """

with open("affirmation.html","w",encoding="utf-8") as file:
    file.write(html_content)

print("😍Affirmation generated! Open 'affirmation.html'")
