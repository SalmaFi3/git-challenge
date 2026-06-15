# C12 - Workflow Entreprise

## Organisation des branches

main

├── feature/a  (Authentification — 2 commits)

└── feature/b  (Dashboard — 2 commits)

## Ordre de merge
1. feature/a mergé en premier → fonctionnalité auth stable
2. feature/b mergé ensuite → dashboard ajouté sur base stable

## Pourquoi cet ordre ?
Dans un vrai projet, on merge les features critiques (auth) avant
les features secondaires (dashboard) pour éviter les dépendances
circulaires et garder main toujours stable.

## Commandes utilisées
```bash
git checkout -b feature/a
git checkout -b feature/b
git merge feature/a
git merge feature/b
git log --oneline --graph --all
```