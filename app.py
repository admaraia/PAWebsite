from flask import Flask, render_template

app = Flask("Olá mundo!")
@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/teste")
def teste():
    return """<html>
    <head></head>
    <title>Flask</title>
    <body>
        <h1>Bom dia Pessoal!</h1>
        <br>
        <h3>código base</h3>
    </body>
    
    
    </html>"""
    
    
