import datetime
import sqlite3

def new_user(name : str, email : str, password : str):
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO user
                        VALUES (NULL, ?, ?, ?)
                ''', (name, email, password))
    
    connexion.commit()
    connexion.close()

def user_follows(following_user_id : int, followed_user_id : int):
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO user_follows_user
                        VALUES (?, ?)
                ''', (following_user_id, followed_user_id))
    
    connexion.commit()
    connexion.close()

def user_unfollows(unfollowing_user_id : int, unfollowed_user_id : int):
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute("""
                    DELETE FROM user_follows_user
                        WHERE following_user_id = ? AND followed_user_id = ?
                    """, (unfollowing_user_id, unfollowed_user_id))
    
    connexion.commit()
    connexion.close()

def new_action(entreprise : str, prix : int):
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO action
                        VALUES (NULL, ?, ?)
                ''', (entreprise, prix))
    
    connexion.commit()
    connexion.close()

def new_transaction(user_id: int, action_id: int,
                    prix_achat: float,
                    date_heure_achat: int,
                    prix_vente = None,
                    date_heure_vente = None):
    
    timenow = datetime.datetime.now()
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO "transaction"
                        VALUES (?, ?, ?, CURRENT_TIMESTANP, ?, ?)
                ''', (user_id, action_id, prix_achat, date_heure_achat, prix_vente, date_heure_vente))

    connexion.commit()
    connexion.close()
