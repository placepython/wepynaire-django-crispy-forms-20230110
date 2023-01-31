# WePynaire Crispy-Forms du 30 janvier 2023

Le projet herbergé dana ce dépôt a servi de support au WePynaire que j'ai donné en janvier 2023 intitulé "sonnaliser le rendu de vos formulaires avec Django-crispy-forms ?". Pour utiliser et tester ce projet, il faut **installer pipenv** et suivre les étapes suivantes:

1. Cloner ce dépôt de code et ouvrir un terminal à la racine du projet
2. Installer les dépendances avec la commande `pipenv install`
3. Activer l'environnement virtuel avec la commande `pipenv shell`
4. Exéxutez les migrations à l'aide de la commande `python manage.py migrate`

Pour les outils frontend, il vous faut installer node.js la méthode d'inatallation officielle pour votre système d'exploitation. Cela vous donnera accès à npm, le pipenv des développeur front. Voici les commandes à exécuter pour préparer les outils pour le dev front-end:

1. Vous rendre dans le répertoire frontend avec la commande `cd frontend`
2. Installer les dépendances front avec `npm install`
3. Compiler le code front avec la commande `npm run build`
