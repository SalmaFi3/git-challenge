# C08 - .gitignore : ignorer des fichiers

## Qu'est-ce que .gitignore ?

`.gitignore` est un fichier qui indique à Git quels fichiers ou dossiers
il doit **ignorer complètement** — ils ne seront jamais trackés ni commités.

## Pourquoi en a-t-on besoin ?

Certains fichiers ne doivent jamais être dans un repo :
- **Fichiers temporaires** : `*.tmp`, `*.log`
- **Données sensibles** : `.env` (mots de passe, clés API)
- **Dépendances** : `node_modules/` (trop lourdes, régénérables)
- **Fichiers système** : `.DS_Store` (Mac), `Thumbs.db` (Windows)

## Ce que j'ai fait dans ce challenge

1. Créé `notes.tmp` → apparu en rouge dans `git status`
2. Ajouté `*.tmp` dans `.gitignore`
3. Relancé `git status` → `notes.tmp` n'apparaît plus ✅
4. Commité `.gitignore` uniquement

## Contenu de mon .gitignore

# Fichiers temporaires
*.tmp

# Fichiers système
.DS_Store
Thumbs.db

# Logs
*.log

# Variables d'environnement
.env

## Règles de syntaxe .gitignore

| Syntaxe | Signification |
|---------|---------------|
| `*.tmp` | Ignore tous les fichiers .tmp |
| `notes.tmp` | Ignore ce fichier précis |
| `logs/` | Ignore tout le dossier logs |
| `!important.log` | Exception : ne pas ignorer ce fichier |

---
*Rédigé avec l'aide de Claude (Anthropic) — compris et appliqué personnellement.*