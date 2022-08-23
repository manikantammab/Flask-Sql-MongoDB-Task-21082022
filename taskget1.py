from flask import Flask,request,jsonify
import mysql.connector as connection

app=Flask(__name__)

@app.route("/get_data")
def get_data_from():
    db=request.args.get("db")
    tn=request.args.get("tn")
    try:
        mydb=connection.connect(host="localhost",user="root",passwd="Mani12345@",database=db)
        cursor=mydb.cursor(dictionary=True)
        cursor.execute(f'select * from {tn}')
        data=cursor.fetchall()
        mydb.commit()
        mydb.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__=="__main__":
    app.run(port=5002)



