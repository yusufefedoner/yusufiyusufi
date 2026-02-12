import sqlite3
import matplotlib.pyplot as plt

DB_NAME = "cities.db"


def get_city_coordinates(city_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT latitude, longitude FROM cities WHERE LOWER(name)=LOWER(?)",
        (city_name,)
    )

    result = cursor.fetchone()
    conn.close()

    return result


def get_all_cities():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, latitude, longitude FROM cities")
    results = cursor.fetchall()

    conn.close()
    return results


def create_graph(cities):
    plt.figure()

    # Dünya sınırları
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Selected Cities")

    for city in cities:
        name, lat, lon = city
        plt.scatter(lon, lat)
        plt.text(lon, lat, name)

    file_name = "map.png"
    plt.savefig(file_name)
    plt.close()

    return file_name
