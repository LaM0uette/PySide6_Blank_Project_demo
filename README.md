# MyApp
## _Courte présentation_

MyApp est une sorte d'application "Modèle" qui a pour but de faciliter la création de multiples   
applications facilement et rapidement en customisant les différents Widgets de manière simple et efficace.

## Fonctions

- Comprend tout ce dont une application de base a besoin.
- Des Widgets 100% personnalisables.
- Des fenêtre de dialogue 100% personnalisables.
- Un menu d'option déjà pré fait.
- Des fonctions élémentaires préconstruite.

## Fonctionnement

> ### Initialisation :
> 
> Il s'agit d'un groupe de liste avec une fonction ainsi qu'une brève description.   
> Toute les fonctions mise à l'intérieur seront exécuté au début du programme.
> 
> ``` py
> self.INIT(
>     [self.IN_BASE, "Configuration des éléments principaux"],
>     [self.IN_SETUP_UI, "Setup de l'interface graphique"],
>     [self.IN_CLASSE, "Initialisation des Widgets"],
>     [self.IN_WG, "Configuration de base des Widgets"],
>     [self.IN_CONNECTIONS, "Ajout des connexions"],
>     [self.IN_ACT, "Fonctions de base"],
>     [self.IN_WG_BASE, "Etat de base des Widgets"],
>     [self.IN_TRAY, "Finalisation de la configuration"]
> )
> 
> self.IN_BASE:          Permet les configurations de base de l'application.   
> self.IN_SETUP_UI:      Configure l'interface graphique.   
> self.IN_CLASSE:        Initialise les classes de chaque Widgets.   
> self.IN_WG:            Initialise les Widgets (texte, img, dimension, ...).   
> self.IN_CONNECTIONS:   Créer les connections des Widgets.   
> self.IN_ACT:           Lance des fonctions au démarage.   
> self.IN_WG_BASE:       Initialise des états de base (CheckBox, CurrentItem, ...).   
> self.IN_TRAY:          Créer le trayIcon.   
> ```
> 
> Fichier de configuration : src > config > config.json
> 
> <br>
> 
> ### Palettes :
> Il y a des palettes mis à disposition et utilisable partout lors de l'import de "src".   
> Il suffit d'écrire : nom_palette().valeur()   
>    
> Voici un exemple pour chaque palette :   
> ```
> - Align:  Align().top()
> - Cur:  Cur().crayon()
> - Dim:  Dim().h4()
> - Font:  Font().h2()
> - Img:  Img().alerte()
> - Rgb:  Rgb().th2()
> - Scroll:  Scroll().on()
> - SelectionBehavior:  SelectionBehavior().row()
> - SpinButton:  SpinButton().plus_minus()
> - StyleBase:  StyleBase().border()
> ```
> 