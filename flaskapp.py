from flask import Flask
from string import Template
app = Flask(__name__)

HTML_TEMPLATE = Template("""
    <!DOCTYPE html>
    <html>
    <img src="./media/${id}.jpg">
    </html>
    """)

@app.route('/')
def homepage():
    return """
    <!DOCTYPE html>
    <html>
    <form method="GET" action="my_result.php">
        <input type="text" name="customer_id">
        <input type="submit">
    </form>
    </html>
    """

@app.route('/<customer_id>')
def image_page(customer_id):
    return(HTML_TEMPLATE.substitute(customer_id=id))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)