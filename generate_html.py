from datetime import datetime

html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Ma Page</title>
</head>
<body>
    <h1>last update : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h1>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML generated successfully.")
