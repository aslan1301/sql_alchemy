# Dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Set up database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)



# Assign the classes to the matching tables
measurement = Base.classes.measurement
station = Base.classes.station

# Create app
app = Flask(__name__)

# Create the session
session = Session(engine)
