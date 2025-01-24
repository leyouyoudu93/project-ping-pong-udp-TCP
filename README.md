# Serveur de Chat TCP
<strong>Description :</strong><br>
Ce fichier contient le code source du serveur pour une application de chat en ligne utilisant le protocole TCP. Le serveur est capable de gérer plusieurs connexions clients en parallèle et permet une communication fluide entre eux.

## Fonctionnalités :
- Gestion de plusieurs clients simultanément grâce à l'utilisation des threads.
- Transmission des messages des clients vers tous les autres utilisateurs connectés.
- Affichage en temps réel des connexions, des déconnexions et des messages échangés.
- Contrôle des erreurs et gestion des connexions interrompues.

## Prérequis :
- Python installé sur la machine où le serveur sera exécuté.
- Accès réseau pour permettre la communication entre le serveur et les clients.
## Utilisation :
- Exécutez le script du serveur depuis un terminal (Frapper <strong>python serveur.py</strong>) ou directement depuis un éditeur de code (<strong>Vs Code</strong>).
- Par défaut, le serveur écoute sur l'adresse IP 127.0.0.1(localhost) et le port 12345. Vous pouvez modifier ces paramètres en éditant les variables HOST et PORT dans le fichier serveur.py.
- Une fois démarré, le serveur affichera les connexions des clients, les messages reçus et les déconnexions dans la console.
## Fonctionnement interne :
### Connexion des clients :
- Lorsqu'un client se connecte, le serveur crée un nouveau thread pour gérer la communication avec ce client sans bloquer les autres.

### Diffusion des messages :
- Tout message reçu d'un client est diffusé à tous les autres clients connectés.

### Déconnexion :
- Si un client se déconnecte, le serveur ferme la connexion avec ce client et retire ce dernier de la liste des connexions actives.
