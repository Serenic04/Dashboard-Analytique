# Architecture du Dashboard Analytique

## 📁 Structure du Projet

```
gen_ia/
├── app.py                          # Point d'entrée principal (simplifié)
├── config.py                       # Configuration centralisée
├── requirements.txt                # Dépendances Python
├── README.md                       # Documentation principale
│
├── backend/                        # 🎯 Module Backend
│   ├── __init__.py
│   ├── routes/                     # Routes Flask (Blueprints)
│   │   ├── __init__.py
│   │   ├── api.py                 # Routes API (/api/stats, /api/filters)
│   │   └── dashboard.py           # Route principale (/)
│   ├── services/                   # Services métier
│   │   ├── __init__.py
│   │   ├── data_service.py        # Gestion des données CSV
│   │   └── analytics_service.py   # Calculs statistiques
│   └── utils/                      # Utilitaires
│       ├── __init__.py
│       └── filters.py             # Application des filtres
│
├── frontend/                       # 🎨 Module Frontend
│   ├── templates/                  # Templates HTML
│   │   └── dashboard.html         # Template principal
│   └── static/                     # Assets statiques
│       ├── css/                    # Styles CSS (à créer)
│       └── js/                     # Scripts JavaScript (à créer)
│
└── data/                           # 📊 Données
    └── sessions_dataset_320.csv   # Dataset CSV
```