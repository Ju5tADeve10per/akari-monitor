from flask import Blueprint, request
from store import upsert_client

bp = Blueprint("routes", __name__)