# C14 - Squash : nettoyer l'historique avant livraison

## Qu'est-ce que le squash ?

Le squash consiste à **fusionner plusieurs commits en un seul**
avant de merger vers main. Cela garde un historique propre et lisible.

## Avant squash (historique de feature/squash)
wip: étape 3 finalisation

wip: étape 2 correction

wip: étape 1 brouillon

## Après squash (sur main)
feat: squash de 3 commits en 1 commit propre pour C14

## Commande utilisée
```bash
git merge --squash feature/squash
git commit -m "feat: squash de 3 commits en 1 commit propre"
```

## Pourquoi utiliser le squash ?

- Les commits `wip:` sont du bruit dans l'historique
- En production, on veut 1 commit = 1 fonctionnalité complète
- Facilite les `git bisect` et la lecture de l'historique
- Utilisé dans les PR GitHub via "Squash and merge"

## Squash vs Merge normal

| | Merge normal | Squash merge |
|---|---|---|
| **Historique** | Tous les commits visibles | 1 seul commit |
| **Lisibilité** | Moins claire | Très claire |
| **Usage** | Features importantes | Nettoyage de WIP |

---
*Rédigé avec l'aide de Claude (Anthropic)*