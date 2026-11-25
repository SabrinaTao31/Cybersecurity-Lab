# SENTINEL — Local Security Studio

**Learn cybersecurity by practising in an interactive, browser-based laboratory.**

[Launch SENTINEL](https://sabrinatao31.github.io/Cybersecurity-Lab/) · [Profil GitHub](https://github.com/SabrinaTao31)

![HTML](https://img.shields.io/badge/HTML-183B2B?style=flat-square&logo=html5)
![CSS](https://img.shields.io/badge/CSS-183B2B?style=flat-square&logo=css)
![JavaScript](https://img.shields.io/badge/JavaScript-183B2B?style=flat-square&logo=javascript)
![Web%20Crypto](https://img.shields.io/badge/Web_Crypto_API-183B2B?style=flat-square)

## Le projet

SENTINEL est un laboratoire pédagogique de cybersécurité défensive destiné aux débutants. Son interface rétro, son bouclier 3D interactif et ses exercices permettent de découvrir des concepts de sécurité sans compte ni infrastructure externe.

## Les huit stations

| Station | Objectif |
| --- | --- |
| 01 — File Fingerprint | Calculer une empreinte SHA-256 et comparer deux empreintes |
| 02 — Base64 Studio | Comprendre l'encodage et sa différence avec le chiffrement |
| 03 — Input Inspector | Découvrir la validation des entrées |
| 04 — Cryptography Lab | Expérimenter le chiffrement authentifié AES-GCM |
| 05 — Network Lab | Explorer des simulations de réseau, DNS et HTTP |
| 06 — Digital Forensics | Résoudre des enquêtes fictives et analyser des indices |
| 07 — Password Lab | Découvrir les mots de passe et l'authentification multifacteur |
| 08 — Cyber Academy | Suivre un parcours progressif avec exercices et retours |

## Expérience utilisateur

- Interface responsive, thèmes clair et sombre.
- Navigation entre accueil, laboratoire et historique.
- Lexique pédagogique et consoles de résultats.
- Progression locale et import/export JSON pour l'Academy.

## Architecture

Application statique en HTML, CSS et JavaScript, utilisant Canvas et Web Crypto API. Les scripts sont organisés par station ; `navigation.js` gère les vues et `world.js` le rendu interactif.

## Lancer localement

```sh
git clone https://github.com/SabrinaTao31/Cybersecurity-Lab.git
cd Cybersecurity-Lab
python -m http.server 8000
```

Ouvrir http://localhost:8000. Le serveur Python sert uniquement les fichiers statiques ; le laboratoire s'exécute dans le navigateur.

## Sécurité et limites

- Les exercices réseau et les enquêtes sont simulés.
- Les opérations cryptographiques et les empreintes sont calculées localement.
- La clé de chiffrement de session n'est pas une sauvegarde permanente.
- Une politique CSP et des limites de taille des entrées sont intégrées.
- Ne pas utiliser de secrets, mots de passe réels ou données confidentielles dans les exercices.
- Le projet est un outil pédagogique, pas un antivirus, un service de stockage sécurisé ou une certification. Aucun audit exhaustif n'est revendiqué.

Le dépôt conserve également les exercices Python historiques. Voir [le guide d'apprentissage](docs/learning-guide.md).

---

**Projet développé par [Sabrina Taouchichet](https://github.com/SabrinaTao31).**
