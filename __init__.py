from mysql.connector import connect

from .piano import *

connection = connect(
	host="localhost",
	port=3306,
	user="root",
	password="sairam",
	database="music"
)
cursor = connection.cursor()


def execute(query, *values):
	cursor.execute(query, values)


def field(query, *values):
	cursor.execute(query, values)

	if row := cursor.fetchone():
		return row[0]


def record(query, *values):
	cursor.execute(query, values)

	return cursor.fetchone()
