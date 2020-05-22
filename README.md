## hassio-freebox

Un add-on Hassio ([Home Assistant](https://www.home-assistant.io/)) pour [assistant-freebox](https://github.com/Aymkdn/assistant-freebox). assistant-freebox permet de contrôler la FreeBox Revolution via Google Home.

Pour pouvoir utiliser cet add-on (et le plugin) , il vous faut un compte [pushbullet](https://www.pushbullet.com/) et un compte [ifttt](https://ifttt.com/).

## Version de hassio testées
* Supervisor : 222
* Hassio : 0.110.1

## Installation

* Créer et récupérer votre token pushbullet
* Dans hassio, ajouter un nouveau repository en ajoutant l'url : https://github.com/frazrepo/hassio-freebox

![images/hassio-repository.png](images/hassio-repository.png)

* Cliquer sur Install pour installer l'add-on **Freebox Add-On** (Attendre un petit moment le temps qu'il récupère les packages assistant-plugins et assistant-freebox)

![images/hassio-addon-1.png](images/hassio-addon-1.png)

* Dans la section Config, renseigner votre token pushbullet, votre code telecommande et éventuellement remplacer hd1 par hd2.

![images/hassio-addon-1.png](images/hassio-addon-2.png)

* Cliquer sur Start pour démarrer
> Le premier démarrage est un peu lent le temps qu'il construit la première image docker.

> Vérifier au niveau de la Freebox **pour valider le plugin** (flèche droite) ! Cette étape de validation est à faire à chaque fois que la machine qui héberge le plugin redémarre


# Exemple de Logs

## Log du supervisor

```
mai 22 10:16:28 nuc hassio-supervisor[2975]: 20-05-22 10:16:28 INFO (MainThread) [supervisor.addons] Create Home Assistant add-on data folder /data/addons/data/7xxx9029_fbx_ac
mai 22 10:16:28 nuc hassio-supervisor[2975]: 20-05-22 10:16:28 INFO (SyncWorker_11) [supervisor.docker.addon] Start build 7xxx9029/amd64-addon-fbx_ac:1.1
mai 22 10:19:07 nuc hassio-supervisor[2975]: 20-05-22 10:19:07 INFO (SyncWorker_11) [supervisor.docker.addon] Build 7xxx9029/amd64-addon-fbx_ac:1.1 done
mai 22 10:19:07 nuc hassio-supervisor[2975]: 20-05-22 10:19:07 INFO (MainThread) [supervisor.addons] Add-on '7xxx9029_fbx_ac' successfully installed
```

## Log du plugin au démarrage

```

[s6-init] making user provided files available at /var/run/s6/etc...exited 0.
[s6-init] ensuring user provided files have correct perms...exited 0.
[fix-attrs.d] applying ownership & permissions fixes...
[fix-attrs.d] done.
[cont-init.d] executing container initialization scripts...
[cont-init.d] done.
[services.d] starting services
[services.d] done.
[fbx-addon] Checking node version : v12.15.0
[fbx-addon] Generating freebox plugin configuration file...
[fbx-addon] Reading add-on configuration datas...
[fbx-addon] Configuration written to configuration.json
[fbx-addon] Starting Freebox Assistant Config Add-on...
[assistant] Assistant v2.0.13 : Chargement en cours...
[assistant] 1 plugin trouvé.
[assistant] Chargement du plugin 'freebox' (v2.0.15)
[assistant-freebox] Demande d'autorisation auprès du Freebox Server...
[assistant-freebox] Approuvez le plugin en allant sur l'écran LCD de votre Freebox Serveur et en utilisant la flèche de droite sur celui-ci.
[assistant-freebox] Le plugin a été autorisé sur la Freebox
[assistant-freebox] Configuration terminée. Vous êtes prêt à utiliser le plugin Freebox.
[assistant-freebox] Récupération des chaines télé...
[assistant-freebox] Configuration sauvegardée.
[assistant-freebox] Récupération des chaines terminée !
[assistant-freebox] Plugin chargé et prêt.
[assistant] Connexion au flux de PushBullet...
[assistant] (2020-05-23 12:20:05) Connecté ! Prêt à exécuter les ordres.
```

## Utilisation

* Activer les [applets Freebox](https://ifttt.com/search/query/freebox) dans IFTTT

## Commandes
* OK Google, zappe sur France 5
* OK Google, zappe sur la une

## Crédits
* [Home Assistant](https://www.home-assistant.io/)
* [assistant-freebox](https://github.com/Aymkdn/assistant-freebox)

