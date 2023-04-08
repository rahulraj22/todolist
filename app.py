from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)

# Configure db
db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# r1
# postgres://todo_c08y_user:0LayywEl7wt5l8w6sVi3o4eFa2L8is6e@dpg-cghisvl269v15eml0dq0-a.oregon-postgres.render.com/todo_c08y

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    
    # take input from the user :-
    if request.method == 'POST':
        userDetails = request.form
        todoTitle = userDetails['title']
        todoDesc = userDetails['descb']
        todoTime = userDetails['time']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO todos(title, descb, date_created) VALUES(%s, %s, %s)", (todoTitle, todoDesc, todoTime))
        mysql.connection.commit()
        cur.close()
    
    todoDetails = {}  # to overcome this error: UnboundLocalError: local variable 'todoDetails' referenced before assignment
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select * from todos")
    if resultValue > 0:
        todoDetails = cur.fetchall()
        cur.close()
    
    return render_template('index.html', todoDetails = todoDetails)
    # return 'Hello, World!'


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    # return 'update query'

    if request.method == 'POST':
        userDetails = request.form
        todoTitle = userDetails['title']
        todoDesc = userDetails['descb']
        todoTime = userDetails['time']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE todos SET title = %s, descb = %s, date_created = %s WHERE sno = %s", (todoTitle, todoDesc, todoTime, sno))
        mysql.connection.commit()
        # cur.close()
        return redirect("/")

    cur = mysql.connection.cursor()
    # result = cur.execute("SELECT * FROM todos WHERE sno = %s", (sno, ))
    cur.execute("SELECT * FROM todos WHERE sno = %s", (sno,))
    result = cur.fetchone()   # IMP*** [in case of update]
    return render_template('update.html', result = result)
    

@app.route('/delete/<int:sno>')  # delete will take an integer, in order delete a specific row(with sno) from table
def delete(sno):
    cur = mysql.connection.cursor()
    cur.execute("delete from todos where sno = %s", (sno, ))
    mysql.connection.commit()
    cur.close()

    # we don't want to print this after deletion operation rather we want to redirect to home page as shown below
    # return 'row deleted Successfully'

    return redirect('/')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

# Example of how to create different routes
# @app.route('/products')
# def products():
#     return '<h1>This is products page</h1>'




# to start our flask webapp
if __name__ == "__main__":
    app.run(debug=True)