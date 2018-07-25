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

@app.route('/index')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <input type="text" id="txt"><br>
    <button id="myButton" class="float-left submit-button">Submit</button>

    <script type="text/javascript">
        document.getElementById("myButton").onclick=function(){
            var txtVal = document.getElementById("txt").value;
            if (txtVal=="page2"){
                window.location.href = "/page2";
            }
            if (txtVal=="Kelly"){
                window.location.href = "https://bing.com";
            }
        }
    </script>

    </html>
    """

@app.route('/page2')
def image_page():
    return"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page Title</title>
    </head> 

    <body>
        <img src="./media/1111.jpg" alt="Family shoppers">

        <script type="text/javascript">
            setTimeout(function(){
                window.location.href = "/index";
            }, 5000)
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



#    <form method="GET" action="my_result.php">
#        <input type="text" name="customer_id">
#        <input type="submit">
#    </form>
