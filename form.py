from flask import Flask, request, render_template

import sqlite3
from sqlite3 import Error


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

@app.route('/sendingRatings',  methods=["GET", "POST"])
def sendingRatings():
    # getting input with name = fname in HTML form

    access1 = request.form.get("fname")
    # getting input with name = lname in HTML form

    access2 = request.form.get("lname")

    access3 = request.form.get("mname")

    access4 = request.form.get("mname1")


    print("hi")
    sql = "INSERT INTO Ratings(ID, access1, acesss2, acesss3, acesss4) VALUES ({ID},{one},{two},{three},{four})".format(
        ID=teeHee,
        one=access1,
        two=access2,
        three=access3,
        four=access4

    )
    conn = sqlite3.connect("helixhacks.db")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    return render_template('ratings.html')

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
   return render_template('upload.html')


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

@app.route('/searchByName', methods=['GET', 'POST'])
def searchByName():

    if request.method == "POST":
        # getting input with name = fname in HTML form
        global hi
        hi = request.form.get("fname")
    con = sqlite3.connect("helixhacks.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()

    sql = "SELECT *  FROM Attractions WHERE Name = '{Name}'".format(
        Name=hi
    )
    cur.execute(sql)
    rows = cur.fetchall()
    return render_template("new.html", rows=rows)


@app.route('/findRatings', methods=["GET", "POST"])
def findRatings():

    if request.method == "POST":
        # getting input with name = fname in HTML form
        global teeHee
        teeHee = request.form.get("fname")
    con = sqlite3.connect("helixhacks.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()

    sql = "SELECT ratingID, access1, acesss2, acesss3, acesss4  FROM Ratings WHERE ID = {ID}".format(
        ID=teeHee
    )
    cur.execute(sql)
    rows = cur.fetchall()
    len2 = 0
    len2 = len(rows)
    rows = rows
    a = 0
    b = 0
    c = 0
    d = 0
    if (len2 != 0):
        for row in rows:
            a += row["access1"]
            b += row["acesss2"]
            c += row["acesss3"]
            d += row["acesss4"]
        a /= len2
        b /= len2
        c /= len2
        d /= len2

    sql2 = "SELECT Location,Category,Hours,Name  FROM Attractions WHERE ID = {ID}".format(
        ID=teeHee
    )
    cur.execute(sql2)
    rows = cur.fetchall()
    for row in rows:

        e=row["Location"]
        f=row["Category"]
        g=row["Hours"]
        h=row["Name"]

    return render_template("hello.html",p1=a,p2=b,p3=c,p4=d,p5=e,p6=f,p7=g,p8=h)


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
    sql = ''' INSERT INTO Attractions(Location,Category,Hours, Name)
              VALUES(?,?,?,?) '''
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
        project = (last_name, middle_name, middle_name1,first_name);
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