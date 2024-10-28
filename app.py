from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/products")
def products():
    return render_template("products.html")
@app.route("/product1")
def product1():
    return render_template("product1.html")
@app.route("/product2")
def product2():
    return render_template("product2.html")
@app.route("/product3")
def product3():
    return render_template("product3.html")
@app.route("/product4")
def product4():
    return render_template("product4.html")
@app.route("/product5")
def product5():
    return render_template("product5.html")
@app.route("/product6")
def product6():
    return render_template("product6.html")
@app.route("/product7")
def product7():
    return render_template("product7.html")
@app.route("/product8")
def product8():
    return render_template("product8.html")
@app.route("/product9")
def product9():
    return render_template("product9.html")
@app.route("/product10")
def product10():
    return render_template("product10.html")
@app.route("/payment")
def payment():
    return render_template("payment.html")


if __name__ =='__main__':
    app.run(debug=True)