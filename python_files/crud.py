import sqlite3
import datetime

#######################################################################################################
#############################################   CREATE    #############################################
#######################################################################################################

def new_user(nom:str, email:str, mdp:str, jwt:str) -> int:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""
                    INSERT INTO user 
                        VALUES (NULL, ?, ?, ?, ?)
                    """, (nom, email, mdp, jwt))
    id_user = curseur.lastrowid
    connexion.commit()

    connexion.close()
    return id_user

def user_follows(following_user_id : int, followed_user_id : int):
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO user_follows_user
                        VALUES (?, ?)
                ''', (following_user_id, followed_user_id))
    
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
                    prix_achat: float):
    
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO "transaction"
                        VALUES (?, ?, ?, CURRENT_TIMESTAMP, NULL, NULL)
                ''', (user_id, action_id, prix_achat))

    connexion.commit()
    connexion.close()




def creer_article(titre:str, contenu:str, auteur_id:int) -> None: ####### à fusionner avec new_action()
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""
                    INSERT INTO article 
                        VALUES (NULL, ?, ?, ?, ?)
                    """, (titre, contenu, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"), auteur_id))
    # En savoir plus sur les dates : http://www.python-simple.com/python-modules-autres/date-et-temps.php
    connexion.commit()
    connexion.close()

#######################################################################################################
#############################################    READ     #############################################
#######################################################################################################

def get_jwt_by_email_mdp(email:str, mdp:str):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""
                    SELECT jwt FROM utilisateur WHERE email=? AND mdp=?
                    """, (email, mdp))
    resultat = curseur.fetchone()
    connexion.close()
    return resultat
    
# def get_users_by_mail(mail:str):
#     connexion = sqlite3.connect("bdd.db")
#     curseur = connexion.cursor()
#     curseur.execute("""
#                     SELECT * FROM utilisateur WHERE email=?
#                     """, (mail,))
#     resultat = curseur.fetchall()
#     connexion.close()
#     return resultat

def get_id_user_by_email(email:str):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""
                    SELECT id FROM utilisateur WHERE email=?
                    """, (email,))
    resultat = curseur.fetchone()
    connexion.close()
    return resultat

    
def get_users_actions(id_user:int) -> list:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""
                    SELECT * FROM article WHERE auteur_id = 1
                    """, (id_user,))
    resultat = curseur.fetchall()
    connexion.close()
    return resultat

#######################################################################################################
#############################################   UPDATE   ##############################################
#######################################################################################################

def update_token(id, token:str)->None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""
                    UPDATE utilisateur
                        SET jwt = ?
                        WHERE id=?
                    """,(token, id))
    connexion.commit()
    connexion.close()

def update_transaction(prix_vente:float, action_id:int):
    connexion = sqlite3.connect("bdd_trading.db")
    curseur = connexion.cursor()
    
    curseur.execute("""
                    UPDATE "transaction"
                        SET prix_vente = ?, date_heure_vente = CURRENT_TIMESTAMP
                        WHERE action_id = ?
                    """, (prix_vente, action_id))
    
    connexion.commit()
    connexion.close()

#######################################################################################################
#############################################   DELETE   ##############################################
#######################################################################################################

def user_unfollows(unfollowing_user_id : int, unfollowed_user_id : int):
    connexion = sqlite3.connect("bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute("""
                    DELETE FROM user_follows_user
                        WHERE following_user_id = ? AND followed_user_id = ?
                    """, (unfollowing_user_id, unfollowed_user_id))
    
    connexion.commit()
    connexion.close()