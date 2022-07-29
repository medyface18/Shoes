from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()


@app.route('/about')
def about():
   return render_template('about.html')
# A decorator used to tell the application
# which URL is associated function


@app.route('/browse')
def browse():
    con = sqlite3.connect("helixhacks.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from Attractions")

    rows = cur.fetchall()
    return render_template("browse.html", rows=rows)

@app.route('/search')
def search():
   return render_template('search.html')


@app.route('/upload')
def upload():
    con = sqlite3.connect("helixhacks.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from Attractions")

    rows = cur.fetchall()
    return render_template("upload.html", rows=rows)







@app.route('/gfg', methods=["GET", "POST"])

def gfg():

    if request.method == "POST":
        # getting input with name = fname in HTML form
        global first_name
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        global last_name
        last_name = request.form.get("lname")
        global middle_name
        middle_name = request.form.get("mname")
        global middle_name1
        middle_name1 = request.form.get("mname1")
        global middle_name2
        middle_name2 = request.form.get("mname2")
    setup_db()
    return "Your name is " + first_name + " " + last_name

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Attractions(Location,Access1,Access2, Access3, Access4)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO users(username,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def setup_db():
    database = "/Users/sriyasth/PycharmProjects/flask-project2/helixhacks.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = (first_name, last_name, middle_name, middle_name1, middle_name2);
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        #create_task(conn, task_1)
        #create_task(conn, task_2)
    return "hi"

def main():
    gfg()

if __name__ == '__main__':
    main()