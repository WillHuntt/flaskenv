from flask import Flask, render_template
app = Flask(__name__)

@app.route("/products")
def products():
    return render_template("products.html")

def product_formatter(products):
    formatted_products = []
    for product in products:
        formatted_products.append({
            "id": product[0],
            "title": product[1],
            "description": product[2],
            "img_sources": json.loads(product[3]),
            "tags": product[4].split(","),
            "price": product[5],
            "specifications": json.loads(product[6]),
            "availabilty": product[7],
            "in_banner": product[8],
            "company": product[9],
            "main_category": product[10],
        })

    return formatted_products


if __name__ == "__main__":
    app.run(debug=True)