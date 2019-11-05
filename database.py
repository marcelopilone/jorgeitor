import configparser
import sqlalchemy as db


config = configparser.ConfigParser()

class conexionBaseDeDatos():
	config.read('config.ini')
	host = config['DB']['host']
	port = config['DB']['port']
	user = config['DB']['user']
	pswd = config['DB']['pass']
	
	conexion = db.create_engine("mysql+mysqlconnector://"+user+":"+pswd+"@"+host+":"+port+"/jorgeitor")