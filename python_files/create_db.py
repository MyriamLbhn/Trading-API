import sqlite3

connexion = sqlite3.connect("bdd_trading.db")
curseur = connexion.cursor()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    mdp TEXT NOT NULL
                )
                """)
connexion.commit()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS action (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    entreprise TEXT NOT NULL,
                    prix FLOAT NOT NULL
                )
                """)
connexion.commit()


curseur.execute("""
                CREATE TABLE IF NOT EXISTS "transaction" (
                    user_id INTEGER,
                    action_id INTEGER,
                    prix_achat FLOAT NOT NULL,
                    date_heure_achat DATETIME NOT NULL,
                    prix_vente FLOAT,
                    date_heure_vente DATETIME,
                    FOREIGN KEY(user_id) REFERENCES user(id),
                    FOREIGN KEY(action_id) REFERENCES action(id)
                )
                """)
connexion.commit()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS user_follows_user (
                    following_user_id INTEGER,
                    followed_user_id INTEGER,
                    FOREIGN KEY(following_user_id) REFERENCES user(id),
                    FOREIGN KEY(followed_user_id) REFERENCES user(id)
                )
                """)
connexion.commit()


connexion.close()