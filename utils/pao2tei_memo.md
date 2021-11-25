Memo de conversion des positions depuis la PAO
===

Le workflow actuel :

1. Conversion InDesign → docx (par Delphine) : validation et quelques reprises manuelles
2. Conversion docx → odt : correction du stylage (Titre du document, hiérachie des titres de niveau en particulier)
3. Conversion odt → XML/TEI : automatique avec odt2tei
4. Reprise du XML/TEI afin de valider avec `encpos.rng`
5. Insertion du `teiHeader`

Ce document liste les particularités des conversions XML/TEI (od2tei) des exports traitement de texte des positions depuis InDesign.

À ce stade du projet, on applique des filtres regex. Une implémentation XSLT sera sans doute à entreprendre pour automatiser le worflow.


## Analyse

### Typographie

On trouve de nombreux `seg[@rend]`. Valeurs rencontrées :

-  19 `typoitalique` : ne contient que des hi[@rend='i']. On supprime ces seg
-  17 `typosc` : les petites caps des siècles : `<seg rend="typosc">xvi</seg>`
-  14 `typoexposant` : les exposants
-   4 `typoscitalic`
-   2 `typoexposantitalic`
-   1 `typomajuscule`
-   1 `typoitalicgras`
-   1 `typogras`

`//seg[@rend='typoitalique']//element()[name()!='hi']`

NB. des cas complexes, liés au mauvais stylage PAO au niveau caractère, par ex. 

```xml
<seg rend="typoitalique">
  <hi rend="i">La noblesse et l’Église en Provence, fin</hi>
</seg>
<seg rend="typoscitalic">
  <hi rend="i"><num>x</num></hi>
</seg>
<seg rend="typoexposantitalic">e</seg>
<seg rend="typoitalique">
  <hi rend="i">-début</hi>
</seg>
<seg rend="typoscitalic">
  <hi rend="i"><num>xiv</num></hi>
</seg>
<seg rend="typoexposantitalic">e</seg>
<seg rend="typoitalique">
  <hi rend="i"> siècle/hi>
</seg>
…
```

devient 

```xml
<hi rend="i">La noblesse et l’Église en Provence, 
fin <num>x</num><hi rend="sup">e</hi>-début <num>xiv</num><hi rend="sup">e</hi> siècle :
l’exemple des familles d’Agoult-Simiane, de Baux et de Marseille</hi>
```

Il faudra enfin penser à reformater les siècles conformément au schéma (voir plus bas).

Essayer de repérer ces cas (les valeurs de `@rend` minoritaires) et les traiter manuellement. Pénible !

**Astuce : on détecte ces cas grâce aux valeurs de `@rend` improbables : par ex `typoexposantitalic` ou `typoscitalic ` qui témoignent des mauvaises segmentations typo.**

### Siècles

Attention à la standardisation des siècle !!


## Reprise

### Ordre des reprises à implémenter


#### Appeler le bon schéma pour validation

`<?xml-model href="../encpos.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>`

#### Appeler le bon scénarion de transformation pour visualisation

`<?xml-stylesheet type="text/xsl" href="../../../hteiml/xsl/tei2html.xsl"?>`

#### Supprimer les commentaires inutiles

Supprimer : `<!--[^>]+>\n` → vide


#### Déterminer si des `seg` sont vides

On rencontre souvent des caractères invisibles qui ont été stylés typographiquement (par exemple des espaces en italique…).

Analyser et remplacer soit par rien, soit par une espace : `<seg[^>]+>[  ]+</seg>` → ` `

#### Analyser et reprendre manuellement les segmentations typographiques bordéliques

Par ex. : 

- `//seg[@rend='typoscitalic']`
- `//seg[@rend='typoexposantitalic']`
- `//seg[@rend='typomajuscule']`
- `//seg[@rend='typoitalicgras']`
- `//seg[@rend='typogras']`

#### Reprendre les exposants

`<seg rend="typoexposant">([^<]+)</seg>` → `<hi rend="sup">$1</hi>`

#### Reprendre les petites caps des siècles

`<seg rend="typosc">([^<]+)</seg>` → `<num>$1</num>`

#### Reprendre les italiques

A. S'assurer que tous les segments en italiques, contiennent de l’italique :

- xpath: `//seg[@rend='typoitalique'][not(hi[@rend='i'])]`
- Corriger manuellement les cas problématiques.

B. Supprimer les `seg[@rend='typoitalique']` encapsulant les `hi[@rend='i']`

Supprimer `<seg rend="typoitalique">` et `</seg>` en prenant soin de ne pas casser le XML…

#### Reprendre les siècle

Le format attendu : `au <num>xix<hi rend="sup">e</hi></num> siècle`

`<num>([^<]+)</num>(<hi rend="sup">e</hi>)` → `<num>$1$2</num>`

Vérifier qu’il ne reste pas des cas : `<num><hi`



#### Utiliser le schéma pour les reprises

- renseigner `TEI/@xml:id`
- renseigner `TEI/@xml:lang`

#### Byline

Baliser manuellement avec l’aide du schéma, car on ne dispose pas de la distinction prénom/nom…

#### Standardisation

- Virer les espaces inutiles, par ex : `[  ]+</p>` ou `<p>[  ]+`
- suppression des scories issues de la conversion depuis l’odt, par ex. `//anchor`
- Vérifier les `</hi>[^  ]`
- Ou des segmentations foireuses : `e </hi>siècle`
- Indenter

#### Vérifier le rendu HTML

La table, etc.