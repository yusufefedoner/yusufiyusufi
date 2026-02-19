import sqlite3
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

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


def create_graph(cities, marker_color="red"):
    fig = plt.figure(figsize=(12, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Kara ve deniz renkleri
    ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
    ax.add_feature(cfeature.LAND, facecolor="lightgreen")

    # Coğrafi detaylar
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.RIVERS)
    ax.add_feature(cfeature.LAKES)
    ax.add_feature(cfeature.MOUNTAIN_RANGES)

    ax.set_global()
    ax.set_title("World Cities Map")

    for city in cities:
        name, lat, lon = city
        ax.scatter(lon, lat, color=marker_color, s=60, transform=ccrs.PlateCarree())
        ax.text(lon, lat, name, transform=ccrs.PlateCarree())

    file_name = "map.png"
    plt.savefig(file_name)
    plt.close()

    return file_name
