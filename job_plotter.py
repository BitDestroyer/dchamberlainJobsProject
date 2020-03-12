import sqlite3
import xml.etree.ElementTree as ET
from opencage.geocoder import OpenCageGeocode
import plotly.graph_objects as go


def open_db(filename: str):
    connection = sqlite3.connect(filename)
    return connection

def show_map(cursor):
    mapbox_access_token = "pk.eyJ1IjoiZ2VvY2hhbWJlcmxhaW4iLCJhIjoiY2s3bzVydHBvMDN4ZDNscW9raDMwMDB6NCJ9.OVzJ4igyGBEqtTnNenWYYA"

    cursor.execute('SELECT lat FROM locals')
    lat_list = []
    for lat in cursor.fetchall():

        lat_list.append(str(lat[0]))

    cursor.execute('SELECT lng FROM locals')
    lng_list = []
    for lng in cursor.fetchall():
        lng_list.append(str(lng[0]))

    fig = go.Figure(go.Scattermapbox(
            lat=lat_list,
            lon=lng_list,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9
            ),

        ))

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=38.92,
                lon=-77.07
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig.show()


con = open_db("jobs.db")
cur = con.cursor()
show_map(cur)
