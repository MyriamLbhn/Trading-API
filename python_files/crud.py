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


# Modifier éléments

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
    
update_transaction(54000, 1)