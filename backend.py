from flask import *
import mysql.connector
connection = mysql.connector.connect(
host='localhost',
user='root',
password='VSLYFTP143',
db='teja'
)
cursor = connection.cursor()
app=Flask(__name__)
@app.route("/")
def home_page():
    return render_template("display.html")
@app.route("/donar")
def registration_page():
    return render_template("reg.html")
@app.route("/receiver")
def receiver_page():
    return render_template("receiver.html")
@app.route("/submit",methods=['GET','POST'])
def submit():
    print('entered')
    try:

        birthday=request.form.get("birthdate")
        collegename=request.form.get("collegename")
        collegeid=int(request.form.get("collegeid"))
        collegearea=request.form.get("collegearea")
        password=request.form.get("password")
        name=request.form.get("name")
        branch=request.form.get("branch")
        bloodgroup=request.form.get("bloodgroup")
        print("bloodgrooup=",bloodgroup,type(bloodgroup))
        age=int(request.form.get("age"))
        collegecontactnumber=int(request.form.get("collegecontactnumber"))
        print(birthday,collegename,collegeid,collegearea,password,name,branch)
        cursor.execute(f"INSERT INTO blooddonar VALUES ('{birthday}','{collegename}',{collegeid},'{collegearea}','{password}','{name}','{branch}',{age},{collegecontactnumber},'{bloodgroup}' )")
        connection.commit()
        print('registered')
        return render_template("availability.html")
    except Exception as e:
        print(" failed")
        return(str(e))
@app.route('/processdata',methods=['GET','POST'])
def display_table():
    bloodgroup=request.form.get("bloodgroup")
    print(bloodgroup,type(bloodgroup))
    #session['bloodgroup'] = bloodgroup
    cursor.execute("SELECT * FROM blooddonar WHERE bloodgroup = %s", (bloodgroup,))

    data = cursor.fetchall()
    return render_template('informationtable.html', data=data)

if __name__=='__main__':
    app.run(debug=True)