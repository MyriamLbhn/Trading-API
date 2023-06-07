# Trading-API

## Objectif : 
Développer une API de trading social à l'aide de FastAPI.

## Arborescences des fichiers : 

- **create_db.py** : création de la base de donnée *bdd_trading.db*  

- **crud.py** : Ce fichier contient les fonctions suivantes  

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
        - 🚨 *Fonction qu'il reste à implémenter* 🚨 : vérifier la validité du JWT

    - UPDATE : 
        - update_token : changer de JWT
        - update_action_buying, update_action_selling, update_transaction_selling : mettre à jour le status de l'action en cas de vente/achat et les transactions
        - update_price_action : changer la valeur d’une action
        - update_mail : changer de mail 
        -  🚨 *Fonction qu'il reste à implémenter* 🚨 : changer de mot de passe
        
    - DELETE :
        - delete_action : supprimer une action
        - delete_user : supprimer un utilisateur 
        - user_unfollows : arrêter de suivre 

- **main.py** : Contient les endpoints pour acceder aux fonctions CRUD  
     🚨 *Endpoint qu'il reste à implémenter* 🚨 : 
        - voir les actions des personnes que l'on suit
        - changer de mail
        - changer de JWT
        - changer de mot de passe

## Requirements :
Les packages requis pour exécuter ce projet sont répertoriés dans le fichier requirements.txt. Pour installer ces packages, exécutez la commande suivante dans un terminal : pip install -r requirements.txt.

## Comment lancer l'API avec FastAPI

Pour utiliser l'API, il vous suffit de vous rendre dans le répertoire où se trouve le fichier **main.py* et d'exécuter la commande suivante dans un terminal : `uvicorn main:app --reload`.  
On ouvre son navigateur à http://127.0.0.1:8000/nom_du_endpoint (les adresses des endpoints sont définies dans main.py). On obtient un réponse JSON.  
Vous pouvez acceder à une documentation automatique intéreactive à l'adresse : http://127.0.0.1:8000/docs#/


On peut utiliser POSTMAN pour envoyer des reqêtes à l'API :  


Pour utiliser votre API avec Postman, vous pouvez suivre les étapes suivantes :
- Assurez-vous d'avoir votre API en cours d'exécution, prête à recevoir des requêtes.
- Ouvrez Postman sur votre ordinateur.
- Créez une nouvelle requête en cliquant sur le bouton "New" dans l'interface de Postman.
- Dans le champ de sélection de la méthode de requête (à gauche de l'URL), choisissez la méthode appropriée (GET, POST, PUT, DELETE)
- Dans le champ de l'URL, saisissez l'URL de l'API, http://127.0.0.1:8000/nom_du_endpoint 
- Si votre API nécessite des paramètres, vous pouvez les ajouter en cliquant sur l'onglet "Params" situé juste en dessous de l'URL et en spécifiant les clés et les valeurs.
- Si votre API nécessite un corps de requête (par exemple, pour les requêtes POST ou PUT), vous pouvez spécifier le contenu dans l'onglet "Body".
- Cliquez sur le bouton "Send" pour envoyer la requête à votre API.
- Vous verrez la réponse JSON de votre API s'afficher dans la section de réponse de Postman, avec le code de statut, le corps de la réponse et d'autres détails pertinents.

