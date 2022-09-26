import sqlite3
import json

def main():
    connection = sqlite3.connect('current_destiny_manifest.sqlite3')

    cursor = connection.execute('SELECT id, json FROM DestinyVendorDefinition WHERE id > 0')
    response = []
    for row in cursor:
        response.append(json.loads(row[1]))

    for object in response:
        if object['displayProperties']['name'] == 'Ada-1':
            print(object['hash'], object['displayProperties']['name'])

    connection.close()

if __name__ == '__main__':
    con = sqlite3.connect('current_destiny_manifest.sqlite3')
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for table in cursor.fetchall():
        print(table)
    # main()