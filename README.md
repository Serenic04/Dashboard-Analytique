# Dashboard Analytique - Sessions Médicales

Application complète de dashboard analytique pour visualiser et analyser des sessions de consultation médicale avec filtres interactifs, graphiques avancés et indicateurs détaillés.

## 🎯 Objectifs Pédagogiques

- ✅ Construction d'une application de data analytics complète
- ✅ Structuration d'une architecture maintenable (backend Flask + frontend HTML/JS)
- ✅ Manipulation et visualisation d'un dataset complet avec pandas
- ✅ Interface utilisateur claire et intuitive
- ✅ Système de filtres dynamiques
- ✅ Chargement correct et robuste des données

## 📊 Fonctionnalités

### Visualisations Demandées

- ✅ **Top des langues** : Classement des 10 langues les plus utilisées avec graphique barres horizontal
- ✅ **Évolution du nombre de sessions** : Graphique temporel (ligne) montrant l'évolution mensuelle
- ✅ **Durée moyenne** : Visualisation par service et par langue avec graphiques barres
- ✅ **Répartition par service** : Graphique barres vertical montrant la distribution
- ✅ **Indicateurs qualité** : Score de qualité moyen, sessions haute/basse qualité
- ✅ **Interactions patient/praticien** : Comparaison des interactions et ratio détaillé
- ✅ **Notes praticiens** : Distribution des notes avec graphique barres

### Fonctionnalités Avancées

- ✅ **Filtres interactifs** :
  - Filtrage par service médical
  - Filtrage par langue
  - Filtrage par device (mobile/webapp)
  - Filtrage par plage de dates (début/fin)
  - Bouton de réinitialisation des filtres
  
- ✅ **Interface claire** :
  - Design moderne et professionnel (thème sombre)
  - Organisation par sections logiques
  - 7 cartes KPI principales
  - 11 graphiques interactifs organisés par thème
  - Responsive design (mobile-friendly)

- ✅ **Chargement robuste des données** :
  - Détection automatique du fichier CSV dans le dossier `data/`
  - Parsing intelligent des dates
  - Validation des colonnes requises
  - Gestion d'erreurs complète
  - Cache des données pour améliorer les performances
  - Messages d'erreur clairs pour l'utilisateur

## 🛠️ Installation

Dans un terminal à la racine du projet :

```bash
# Créer l'environnement virtuel (si pas déjà fait)
python -m venv .venv

# Activer l'environnement virtuel
# Windows PowerShell :
.venv\Scripts\Activate.ps1
# Windows CMD :
.venv\Scripts\activate.bat
# Linux/Mac :
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## 🚀 Lancer le serveur

```bash
python app.py
```

Puis ouvrir le navigateur sur `http://127.0.0.1:5000/`.

## 📁 Format des données

Le dashboard utilise automatiquement le premier fichier CSV trouvé dans le dossier `data/`. 

### Colonnes requises

Le fichier CSV doit contenir les colonnes suivantes :

- `session_id` : Identifiant unique de la session
- `date` : Date de la session (format YYYY-MM-DD)
- `service` : Service médical (ex: Urgences, Pédiatrie, Cardiologie)
- `langue` : Langue de la consultation
- `duree_minutes` : Durée en minutes
- `interactions_patient` : Nombre d'interactions du patient
- `interactions_praticien` : Nombre d'interactions du praticien
- `interactions_totales` : Nombre total d'interactions
- `note_praticien` : Note du praticien (sur 5)
- `qualite_score` : Score de qualité (0-1)
- `segments_non_reconnus` : Nombre de segments non reconnus (optionnel)
- `device` : Type d'appareil (mobile, webapp)

## 📈 Graphiques Disponibles

### 1. KPIs Principaux
- Sessions totales
- Durée moyenne
- Note moyenne praticien
- Score qualité moyen
- Interactions moyennes (total, patient, praticien)

### 2. Évolution et Répartition
- **Évolution du nombre de sessions** : Graphique ligne avec évolution mensuelle et durée moyenne
- **Répartition par service** : Graphique barres vertical

### 3. Top Langues
- **Top 10 des langues** : Classement horizontal des langues les plus utilisées
- **Répartition complète par langue** : Graphique donut avec toutes les langues

### 4. Durée Moyenne
- **Durée moyenne par service** : Graphique barres
- **Durée moyenne par langue** : Graphique barres

### 5. Indicateurs de Qualité
- **Distribution du score de qualité** : Graphique donut
- **Répartition par device** : Graphique donut

### 6. Interactions Patient/Praticien
- **Comparaison des interactions** : Graphique barres comparant patient/praticien/total
- **Ratio patient/praticien** : Graphique donut

### 7. Notes Praticiens
- **Distribution des notes** : Graphique barres par tranches (0-2, 2-3, 3-4, 4-4.5, 4.5-5, 5+)

## 🔧 Architecture Technique

### Backend (Flask)
- **Routes** :
  - `GET /` : Page principale du dashboard
  - `GET /api/stats` : Statistiques avec support des filtres (query parameters)
  - `GET /api/filters` : Options disponibles pour les filtres

- **Fonctionnalités** :
  - Chargement et cache des données CSV
  - Application dynamique des filtres
  - Calculs statistiques avec pandas
  - Gestion d'erreurs robuste

### Frontend (HTML/JavaScript)
- **Technologies** :
  - Chart.js 4.4.0 pour les graphiques interactifs
  - Vanilla JavaScript (pas de framework)
  - CSS moderne avec design sombre

- **Fonctionnalités** :
  - Filtres interactifs avec mise à jour dynamique
  - 11 graphiques interactifs
  - Interface responsive
  - Gestion des erreurs côté client

## 📝 Personnalisation

### Ajouter de nouveaux graphiques

1. Ajouter le calcul dans `api_stats()` dans `app.py`
2. Ajouter le canvas HTML dans le template
3. Créer la fonction JavaScript `createXXXChart(data)`
4. Appeler cette fonction dans `initDashboard()`

### Modifier les filtres

Les filtres sont automatiquement générés à partir des données. Pour ajouter un nouveau filtre :

1. Ajouter le calcul dans `api_filters()` 
2. Ajouter le champ HTML dans la section filtres
3. Modifier `apply_filters()` dans le backend
4. Mettre à jour `fetchStats()` dans le frontend

## 🐛 Dépannage

### Erreur : "Aucun fichier CSV trouvé"
- Vérifiez que votre fichier CSV est bien dans le dossier `data/`
- Vérifiez l'extension du fichier (doit être `.csv`)

### Erreur : "Colonnes manquantes"
- Vérifiez que votre CSV contient toutes les colonnes requises
- Vérifiez les noms des colonnes (sensible à la casse)

### Les graphiques ne s'affichent pas
- Vérifiez la console du navigateur (F12) pour les erreurs JavaScript
- Vérifiez que Chart.js se charge correctement
- Vérifiez que l'API `/api/stats` retourne des données valides

### Les filtres ne fonctionnent pas
- Vérifiez que l'endpoint `/api/filters` est accessible
- Vérifiez les paramètres de requête dans l'URL

## 📚 Dépendances

- `flask==3.0.3` : Framework web
- `pandas==2.2.3` : Manipulation et analyse de données
- `matplotlib==3.9.2` : Visualisation (optionnel, pour analyses futures)

## 📄 Licence

Projet éducatif - EPSI
