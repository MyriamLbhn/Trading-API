# Trading-API

## Objectif : 
Développer une API de trading social à l'aide de FastAPI.

## Arborescences des fichiers : 

- create_db.py : création de la base de donnée *bdd_trading.db*  

- crud.py : Ce fichier contient les fonctions suivantes  

    - CREATE :
        - new_user : créer un utilisateur
        - new_action : créer une nouvelle action
        - new_transaction_buying : créer une nouvelle ligne dans le registre
        - user_follow : permettre à un utilisateur d'en suivre un autre

    - READ :
        - get_jwt_by_email_mdp : obtenir le JWT avec le mail et le MDP
        - get_users_by_mail : obtenir l'utilisateur depuis son mail
        - get_id_user_by_email : obtenir l'ID utilisateur depuis son mail
        - get_users_actions : voir les actions d'un utilisateur (permet donc de voir les siennes ou celles des personnes que l'ont suit)
        - get_available_actions : sélectionner les actions disponibles
        - get_price_by_action_id : obtenir le prix de l'action
        - is_action_available : vérifier si l'action est disponible
        - is_following : vérifier si l'user suit un autre user
        - get_hashed_password : hasher le mdp
        - *🚨 Fonction qu'il reste à implémenter 🚨 *: vérifier la validité du JWT

    - UPDATE : 
        - update_token : changer de JWT
        - update_action_buying, update_action_selling, update_transaction_selling : mettre à jour le status de l'action en cas de vente/achat et les transactions
        - update_price_action : changer la valeur d’une action
        - update_mail : changer de mail 
        -  *🚨 Fonction qu'il reste à implémenter 🚨 *: changer de mot de passe
        
    - DELETE :
        - delete_action : supprimer une action
        - delete_user : supprimer un utilisateur 
        - user_unfollows : arrêter de suivre 

- main.py : Contient les endpoints pour acceder aux fonctions CRUD
    *🚨 Endpoint qu'il reste à implémenter 🚨 * : 
        - voir les actions des personnes que l'on suit
        - changer de mail
        - changer de JWT
        - changer de mot de passe

## Requirements :
Les packages requis pour exécuter ce projet sont répertoriés dans le fichier requirements.txt. Pour installer ces packages, exécutez la commande suivante dans un terminal : pip install -r requirements.txt.