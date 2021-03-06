from django.core.management.base import BaseCommand, CommandError
import psycopg2

hostname = 'ec2-54-75-245-94.eu-west-1.compute.amazonaws.com'
user = 'igrtjmoefrebxh'
password = '01c0aa4065c571838b1b348c9e67ccb928e594fa9b0283a0a460846da40a394c'
database = 'dagkjbl47d8fje'


class Command(BaseCommand):

    help = "Create some tables in the database"

    def handle(self, *args, **options):
        cmds = [
            """CREATE TABLE IF NOT EXISTS web_app_categories (id SERIAL PRIMARY KEY, name VARCHAR(50))""",
            """CREATE TABLE IF NOT EXISTS web_app_products(id SERIAL PRIMARY KEY, name VARCHAR(255), store VARCHAR(255), grade CHAR(1), kj_100g INTEGER, cat_id_id INTEGER, foreign key (cat_id_id) REFERENCES web_app_categories(id), url VARCHAR(255), description TEXT, img_url VARCHAR(255), proteins_100g REAL, sugars_100g REAL, fat_100g REAL, salt_100g REAL, saturated_fat_100g REAL)""",
            """CREATE TABLE IF NOT EXISTS web_app_favs(id SERIAL PRIMARY KEY, prod_id INTEGER NOT NULL, foreign key (prod_id) REFERENCES web_app_products(id), prod_substitute_id INTEGER, foreign key (prod_substitute_id) REFERENCES web_app_products(id), user_id INTEGER NOT NULL, foreign key (user_id) REFERENCES auth_user(id))"""]

        conn = None

        try:
            conn = psycopg2.connect(host=hostname, user=user, password=password, database=database)
            cur = conn.cursor()
            for tables in cmds:
                cur.execute(tables)
                print("Done")
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

