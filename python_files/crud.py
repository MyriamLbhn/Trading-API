import sqlite3
import datetime

#######################################################################################################
#############################################   CREATE    #############################################
#######################################################################################################

def new_user(nom:str, est_entreprise:bool, email:str, mdp:str, jwt:str) -> int:
    connexion = sqlite3.connect("../bdd_trading.db")
    curseur = connexion.cursor()

    curseur.execute("""
                INSERT INTO user (nom, est_entreprise, email, mdp, jwt)
                    VALUES (?, ?, ?, ?, ?)
                """, (nom, est_entreprise, email, mdp, jwt))
    
    id_user = curseur.lastrowid
    connexion.commit()
    connexion.close()
    return id_user
# new_user("Myriam", False, "myriam@gmail.com", "azert", "eifonhzejofndjfvn")

def user_follows(following_user_id : int, followed_user_id : int):
    connexion = sqlite3.connect("../bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO user_follows_user
                        VALUES (?, ?)
                ''', (following_user_id, followed_user_id))
    
    connexion.commit()
    connexion.close()


def new_action(entreprise : str, prix : int,proprietaire_id: int):
    connexion = sqlite3.connect("../bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute('''
                    INSERT INTO action
                        VALUES (NULL, ?, ?, ?, ?)
                ''', (entreprise, prix, True, proprietaire_id))
    
    connexion.commit()
    connexion.close()

# new_action("SAFRAN", 51000, 2)
# new_action("THALES", 54000, 1)


def new_transaction_buying(user_id: int, action_id: int):
    
    connexion = sqlite3.connect("../bdd_trading.db")
    cursor = connexion.cursor()

    # Obtenir le prix de l'action correspondante
    cursor.execute('''
                    SELECT prix
                    FROM action
                    WHERE id = ?
                ''', (action_id,))
    prix_achat = cursor.fetchone()[0]

    # Mettre à jour la ligne correspondante de la table action
    cursor.execute('''
                    UPDATE action
                    SET proprietaire_id = ?, disponible = 0
                    WHERE id = ?
                ''', (user_id, action_id))

    # Insérer une nouvelle ligne dans la table "transaction"
    cursor.execute('''
                    INSERT INTO "transaction"
                        VALUES (?, ?, ?, CURRENT_TIMESTAMP, NULL, NULL)
                ''', (user_id, action_id, prix_achat))

    connexion.commit()
    connexion.close()



#######################################################################################################
#############################################    READ     #############################################
#######################################################################################################

def get_jwt_by_email_mdp(email:str, mdp:str):
    connexion = sqlite3.connect("../bdd_trading.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    SELECT jwt FROM user WHERE email=? AND mdp=?
                    """, (email, mdp))
    
    resultat = curseur.fetchone()
    connexion.close()
    return resultat
    
# def get_users_by_mail(mail:str):
#     connexion = sqlite3.connect("bdd.db")
#     curseur = connexion.cursor()
#     curseur.execute("""
#                     SELECT * FROM user WHERE email=?
#                     """, (mail,))
#     resultat = curseur.fetchall()
#     connexion.close()
#     return resultat

def get_id_user_by_email(email:str):
    connexion = sqlite3.connect("../bdd_trading.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    SELECT id FROM user WHERE email=?
                    """, (email,))
    
    resultat = curseur.fetchone()
    connexion.close()
    return resultat

    
def get_users_actions(id_user:int) -> list:
    connexion = sqlite3.connect("../bdd_trading.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    SELECT * FROM action WHERE proprietaire_id = ?
                    """, (id_user,))
    
    resultat = curseur.fetchall()
    connexion.close()
    return resultat

def get_available_actions() -> list:
    connexion = sqlite3.connect("../bdd_trading.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    SELECT * FROM actions WHERE available = 1
                    """)
    resultat = curseur.fetchall()

    connexion.close()
    return resultat


#######################################################################################################
#############################################   UPDATE   ##############################################
#######################################################################################################

def update_token(id, token:str)->None:
    connexion = sqlite3.connect("../bdd_trading.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    UPDATE user
                        SET jwt = ?
                        WHERE id=?
                    """,(token, id))
    
    connexion.commit()
    connexion.close()

# def update_transaction(prix_vente:float, action_id:int):
#     connexion = sqlite3.connect("../bdd_trading.db")
#     curseur = connexion.cursor()
    
#     curseur.execute("""
#                     UPDATE "transaction"
#                         SET prix_vente = ?, date_heure_vente = CURRENT_TIMESTAMP
#                         WHERE action_id = ?
#                     """, (prix_vente, action_id))
    
#     connexion.commit()
#     connexion.close()
    
def update_action(action_id:int):
    connexion = sqlite3.connect("../bdd_trading.db")
    curseur = connexion.cursor()
    
    curseur.execute("""
                    UPDATE "action"
                        SET propriaitaire_id = user_id
                        WHERE action_id = ?
                    """, (action_id))
    
    connexion.commit()
    connexion.close()
    
    
# def update_mail(mail:str, mdp:str)

#######################################################################################################
#############################################   DELETE   ##############################################
#######################################################################################################

def user_unfollows(unfollowing_user_id : int, unfollowed_user_id : int):
    connexion = sqlite3.connect("../bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute("""
                    DELETE FROM user_follows_user
                        WHERE following_user_id = ? AND followed_user_id = ?
                    """, (unfollowing_user_id, unfollowed_user_id))
    
    connexion.commit()
    connexion.close()

def delete_user(user_id):
    connexion = sqlite3.connect("../bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute("""
                    DELETE FROM user
                        WHERE id = ?
                    """, (user_id,))
    
    connexion.commit()
    connexion.close()

def delete_action(action_id):
    connexion = sqlite3.connect("../bdd_trading.db")
    cursor = connexion.cursor()

    cursor.execute("""
                    DELETE FROM action
                        WHERE id = ?
                    """, (action_id,))
    
    connexion.commit()
    connexion.close()
