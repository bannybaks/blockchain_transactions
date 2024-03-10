import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()


def connect_to_database() -> GraphDatabase:
    url = os.getenv("URL_DB")
    auth = (os.getenv("USER_DB"), os.getenv("PASSWORD_DB"))
    with GraphDatabase.driver(url, auth=auth) as driver:
        driver.verify_connectivity()
    return driver