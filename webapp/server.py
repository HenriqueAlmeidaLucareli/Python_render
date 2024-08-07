import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='dpg-cqpmg42j1k6c73dt55n0-a',
                            database='movies_7hy4',
                            user='henriquefelipe',
                            password='6u1dDXIsOQ3ZzfCPZ2voFCXSDpq8HNuJ')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM movies;')
    movies = [] 
    moviesFet = cur.fetchall()
    cur.close()
    conn.close()
    
    """
    HTML (<li>) de todos os dados.
    """
    html = ""
    
    for row in moviesFet:
        movies.append({"name": row[0], "rating": row[1]})
    
    for movie in movies:
    
        html = html + """
            <li class="list-group-item">
                <span class="badge">%s
                    <span class="glyphicon glyphicon-star"></span>
                </span>
                %s
            </li>
        """ % (movie['rating'], movie['name'])
       
    return open('index.html').read()  % (html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)