with open("index.html", "a+") as file:
    file.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Save Our Environment</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f8f5;
            color: #333;
        }

        header {
            background-color: #2e8b57;
            color: white;
            text-align: center;
            padding: 20px;
        }

        nav {
            background-color: #3cb371;
            padding: 10px;
            text-align: center;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-weight: bold;
        }

        section {
            padding: 20px;
        }

        footer {
            background-color: #2e8b57;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
</head>
<body>

    <header>
        <h1> Save Our Environment</h1>
        <p>Protect Nature for Future Generations</p>
    </header>

    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>

    <section>
        <h2>Why Environment Matters</h2>
        <p>
            The environment gives us air, water, food, and shelter.
            We must protect it for future generations.
        </p>
    </section>

    <footer>
        <p>© 2026 Save Environment Initiative</p>
    </footer>

</body>
</html>
''')

print("HTML file created successfully!")