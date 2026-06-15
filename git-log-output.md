# C06 - Historique Git

## Commande : git log --oneline

D:\git-challenge>git log --oneline
29a9773 (HEAD -> main, origin/main) C06(3/3): ajout de log-3.txt pour tester git log [AI used: Claude]
b7cf92e C06(2/3): ajout de log-2.txt pour tester git log [AI used: Claude]
825a518 C06(1/3): ajout de log-1.txt pour tester git log [AI used: Claude]
d5f2801 docs: README complet avec structure, progression et apprentissages [AI used: Claude]
fb55210 C04: Mise à jour AI_USAGE.md [AI used: Claude]
5d30bd2 C04: Staging sélectif - ajout de a.txt uniquement (b.txt exclu) [AI used: Claude]
7d4eeb5 C03: Mise à jour AI_USAGE.md [AI used: Claude]
99692a8 C03: Configuration Git user.name et user.email [AI used: Claude]
f2bfd47 C02: Mise à jour AI_USAGE.md [AI used: Claude]
a11768c C02: Comprendre le version control - création de version-control.md [AI used: Claude]
7619638 C01: Ajout du fichier AI_USAGE.md [AI used: Claude]
a92600e C01: Installation & setup - initialisation du repo [AI used: Claude]

D:\git-challenge>git show a92600e
commit a92600e6ea1706fc3772835438e4f404b1a00520
Author: Salma FILAHI <filahisalma3@gmail.com>
Date:   Mon Jun 15 21:16:48 2026 +0100

    C01: Installation & setup - initialisation du repo [AI used: Claude]

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..bff4fe9
--- /dev/null
+++ b/README.md
@@ -0,0 +1 @@
+"# Git Challenges - Salma"