import pandas as pd
from datetime import datetime

# Votre code pour générer le HTML
df = pd.DataFrame({
    'A': [1, 2, 3]
})

html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Ma Page</title>
</head>
<body>
    <h1>Dernière mise à jour : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h1>
    {df.to_html()}
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML generated successfully.")
