from flask import Flask, jsonify, request;

@app.route('/')
def root ():
    return "Home"

app= Flask (__name__)
if __name__ == "__main__":
    app.run(debug=True)

     