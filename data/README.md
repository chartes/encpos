Métadonnées des positions de thèses
===

**Documentation en cours de rédaction**

L’application est pilotée par le tableau `encpos.tsv` :

- les attributs sont injectés dans les fichiers `__capitains__.xml` grâce à un [Capitainizer](https://github.com/chartes/capitainizer).
- les métadonnées sont ainsi accessibles grâce à un *endpoint* DTS.

Une position de thèse et un résumé d’une thèse d’École des chartes publié dans le volume annuel des positions des thèses.


## Métadonnées

### `id`

Identifiant de la position

- format : `ENCPOS_{AAAA}_{NN}`. `AAAA` : année ;  `NN` : numéro d’ordre dans le volume.
- par exemple : `ENCPOS_1972_18`

Cet identifiant permet de désigner :

- la source XML/TEI : `ENCPOS_1972_18.xml`
- le fichier PDF : `ENCPOS_1972_18.pdf`
- le manifeste IIIF


### `title_rich`

Titre de la position, avec des enrichissements typographiques

- format : HTML5
- par exemple : `<i>Ciperis de Vignevaux</i>, chanson de geste du début du <small>XV</small><sup>e</sup> siècle. Étude et édition`

Recours à 3 balises HTML5 :

- `small` : pour les petites caps, par ex. `<small>XV</small><sup>e</sup> siècle`. Permet de conserver la chaîne de caractères en MAJ, pour l’export texte brut.
- `sup`
- `i` : pour les titres, expressions en langue étrangère

Ce titre devrait être le titre de référence. Mais les collègues de la bibliothèque ont crée et corrigé prioritairement le champ `title_text` plus en cohérence avec les usages SIGB. Il faudrait reporter les corrections dans `title_rich` de manière à en faire le titre de référence et pouvoir supprimer `title_text` qui doit être généré par suppression des balises.

NB. Déterminer dans quelle mesure ce champ n’est pas corrigé à nouveau à l’import Omeka, pour définir la meilleure stratégie de reprise.

NB. A partir de 2016, nous avons des titres **et des sous-titres** inscrits dans les `teiHeader` -> récupérer l’information.

NB. Des thèses ont presque le même titre. Donnée à explorer et proposer du rebond (thèse similaire).


### `title_text`

Titre de la position, sans enrichissement typographique, pour export SIGB : `title_rich`, sans les balises. C’est le champ qui a été corrigé.

NB. `title_text` doit disparaître, pour être dérivé de `title_rich`.


### `author_name`

Nom de l’auteur de la position, en minuscules avec majuscules initiales :

- `Bastard, De`
- `Delisle`
- `La Borderie, De`

Pour les tris, par exemple sur la recherche.

NB : problème du formatage du `dc:creator` dans la réponse DTS, par ex `La Borderie, De, Louis-Arthur`: [`https://dev.chartes.psl.eu/dts/collections?id=ENCPOS_1852_01`](https://dev.chartes.psl.eu/dts/collections?id=ENCPOS_1852_01)


### `author_firstname`

Prénom de l’auteur, en minuscules avec majuscules initiales.

Pour affichage trié par nom.


### `author_idref-key`

[`Champ 900 code $a`](https://www.loc.gov/marc/bibliographic/bd9xx.html) pour la description de l’auteur.

- `Bastard d'Estang, Léon de (1822-1860 ; Cte)`
- `Delisle, Léopold (1826-1910)`
- `La Borderie, Arthur Le Moyne de (1827-1901)`

Moins utile à présent, d’autant que la donnée est récupérable via API. Évaluer l’opportunité de conserver ce champ, au profit du seul `PPN`.


### `author_idref-id`

Le [`PPN`](https://data.idref.fr/) IdRef de l’auteur : identifiant à 9 caractères (NB. peut commencer par un `0`).

- Il faut couvrir autant que possible notre corpus – Cf action en cours avec l’ABES.
- Renommer l’attribut `author_idref-ppn`, plus explicite.


### `promotion_year`

Année du volume de la position. Revoir avec VS la valeur sémantique précise : promotion ? soutenance ? publication ?


### `pagination`

Pagination de la position dans le volume annuel : `startPage-endPage`.


### `author_gender`

Genre de l’auteur :

- `1` : masculin
- `2` : féminin

Permet d’observer le bouleversement de l’équilibre des genres sur 150 ans.


### `topic_notBefore` et `topic_notAfter`

Indexation sujet, bornes chronologiques du sujet traité par la thèse.

- TODO : standardiser les dates, [EDTF](https://www.loc.gov/standards/datetime/).
- Voir avec VS si ces données sont enrichies.


### `enc_teacher`

Booléen pour déterminer si l’auteur de la position a par la suite été professeur à l’École des chartes.


### `these_ppn-sudoc`

Identifiant pérenne de la notice de la position de thèse dans le Sudoc. Par ex. `234764724` pour [https://www.sudoc.fr/234764724](https://www.sudoc.fr/234764724)

À conserver absolument.


### `site:id`, `these_id`, `these_biblionumber-benc`

Différents liages au gré des différentes tentatives d’identification.

- `site:id` : concaténation `{AAAA}{numéro-ordre}`, par ex. `197218` pour `ENCPOS_1972_18`. Ajout des M2TNAH ? Quelle utilité ? Supprimer ?
- `these_id` : `{AAAA}THESE{numéro-ordre}`, par ex. `1972THESE18`. Cote BENC : toujours utilisé ? on garde ?
- `these_biblionumber-benc` : identifiant BENC, par ex. [`125235`](https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber=125235). Cote BENC : toujours utilisé ? on garde ?

### Ce qui nous manque :

- Lien vers ThENC@
- Lien HAL vers la thèse
- Construire les liages (auteurs), cf plus bas



## Liages

### Auteurs

Notre donnée pivot est le [`PPN`](https://data.idref.fr/) IdRef : le `PPN` est l’identifiant à 9 caractères de la ressource.

Ex. Michel Pastoureau :

- PPN : `027059952 `
- notice : [https://www.idref.fr/027127133](https://www.idref.fr/027059952)

**Objectif. Obtenir les liages pour :**

- data.bnf : pour la notice
- ark de la notice du catalogue général BnF : pour la biblio (via PPN et services Sudoc)
- Wikidata : pour le lien et la photo
- DBPedia : pour la description
- Wikipedia

-> essayer d’obtenir le graphe des co-auteurs par la suite.


Pour les liages, il existe différents [services](http://documentation.abes.fr/aideidrefdeveloppeur/index.html#WebServiceRest), plus ou moins à jour… 

- [IdRef2id](http://documentation.abes.fr/aideidrefdeveloppeur/index.html#MicroWebIdref2id) : [https://www.idref.fr/services/idref2id/027059952](https://www.idref.fr/services/idref2id/027059952). On accède au :
	- VIAF : `//result[source='VIAF']/identifiant`
	- BnF catalogue : `//result[source='BNF']/identifiant`
	- WIKIDATA (parfois) `//result[source='WIKIDATA']/identifiant`
- Export XML de la notice : [https://www.idref.fr/027059952.xml](https://www.idref.fr/027059952.xml). On accède au :
	- 	VIAF : `//datafield[@tag='035'][subfield[@code='2']='VIAF']/subfield[@code='a']`
	-  BnF catalogue : `//datafield[@tag='033'][subfield[@code='2']='BNF']/subfield[@code='a']`
	-  WIKIDATA (parfois) : `//datafield[@tag='035'][subfield[@code='2']='WIKIDATA']/subfield[@code='a']`
- Export RDF de la notice : [https://www.idref.fr/027059952.rdf](https://www.idref.fr/027059952.rdf)
	- Embarque aussi une bibliographie

Frustrant car quel que soit le service, il semble qu’on ne puisse pas accéder à tous les liages. Pour Pastoureau, on ne récupère que la notice du catalogue général de la BnF et le lien VIAF.

Autres méthodes :

- [Yasgui](https://data.idref.fr/yasgui.html) (éditeur de requête SPARQ du Sudoc)
- utiliser data.bnf.fr

Sur data.bnf les liages sont riches et permettent de construire du service, par ex : 

- ark data.bnf.fr
- catalogue général : [https://catalogue.bnf.fr/search.do?mots0=NRI;-1;0;Jean-Claude+Schmitt&mots1=ALL;0;0;&&pageRech=rav](https://catalogue.bnf.fr/search.do?mots0=NRI;-1;0;Jean-Claude+Schmitt&mots1=ALL;0;0;&&pageRech=rav) //// NB. information moins bonne sur le Sudoc qui donne accès à l’ark de la notice du catalogue général…
- Wikidata -> on récupère image
- Wikipedia
- DBPedia -> `dbpedia-owl:abstract`

On pourrait faire ressortir les auteurs associés dans d’autres bases : co-auteurs dans le futur… Visualiser le graphe des co-auteurs.

### Thèses

Exporter les données de ThENC@.

Notamment les liens HAL lorsque le thèse à été déposée.



## Exports

### XML/TEI

```xml
<teiHeader>
    <fileDesc>
      <titleStmt>
        <title>{html2tei(rich_title)}</title>
        <author sameAs="{author_idref-id}">{author_firstname} {author_name}</author>
      </titleStmt>
      <editionStmt>
        <funder>École nationale des chartes</edition>
      </editionStmt>
      <publicationStmt>
        <publisher>École nationale des chartes</publisher>
        <date when="2021"/>
        <availability status="restricted">
          <licence target="http://creativecommons.org/licenses/by-nc-nd/3.0/fr/"/>
        </availability>
      </publicationStmt>
      <seriesStmt>
        <title>Positions des thèses</title>
        <idno type="ISSN">0755-2976</idno>
        <idno type="URI">http://www.sudoc.fr/013565311</idno>
      </seriesStmt>
      <sourceDesc>
        <bibl><title>Positions des thèses soutenues par les élèves de la promotion de {promotion_year} pour obtenir le diplôme d’archiviste paléographe</title>, <pubPlace>Paris</pubPlace>, <publisher>École des chartes</publisher>, <date>{promotion_year}</date>.</bibl>
      </sourceDesc>
    </fileDesc>
    <profileDesc>
      <creation>
        <date when="{promotion_year}"/>
      </creation>
      <langUsage>
        <language ident="fre"/>
      </langUsage>
    </profileDesc>
  </teiHeader>
```

Exemple

```xml
<teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Le bestiaire héraldique au Moyen_Âge</title>
        <author sameAs="https://www.idref.fr/027059952">Michel Pastoureau</author>
      </titleStmt>
      <editionStmt>
        <edition>École nationale des chartes</edition>
      </editionStmt>
      <publicationStmt>
        <publisher>École des chartes</publisher>
        <date when="2021"/>
        <availability status="restricted">
          <licence target="http://creativecommons.org/licenses/by-nc-nd/3.0/fr/"/>
        </availability>
      </publicationStmt>
      <seriesStmt>
        <title>Positions des thèses</title>
        <idno type="ISSN">0755-2976</idno>
        <idno type="URI">http://www.sudoc.fr/013565311</idno>
      </seriesStmt>
      <sourceDesc>
        <bibl><title>Positions des thèses soutenues par les élèves de la promotion de 2016 pour obtenir le diplôme d’archiviste paléographe</title>, <pubPlace>Paris</pubPlace>, <publisher>École des chartes</publisher>, <date>2016</date>.</bibl>
      </sourceDesc>
    </fileDesc>
    <profileDesc>
      <creation>
        <date when="2016"/>
      </creation>
      <langUsage>
        <language ident="fre"/>
      </langUsage>
    </profileDesc>
  </teiHeader>
```


### CapiTains

Voir [http://capitains.org/pages/guidelines](http://capitains.org/pages/guidelines)

TODO :

- valider
- ajouter des champs, notamment :
	- `title_rich`
	- liages Wikidata, data.bnf, etc.

```xml
<?xml-model href="../../../capitains.rng" schematypens="http://relaxng.org/ns/structure/1.0"?>
<cpt:collection xmlns:ti="http://chs.harvard.edu/xmlns/cts" xmlns:dct="http://purl.org/dc/terms/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cpt="http://purl.org/capitains/ns/1.0#" xmlns:owl="http://www.w3.org/2002/07/owl#" xmlns:bib="http://bibliotek-o.org/1.0/ontology/" xmlns:cts="http://chs.harvard.edu/xmlns/cts" xmlns:foaf="http://xmlns.com/foaf/0.1/">
  <cpt:identifier>{id}</cpt:identifier>
  <cpt:parent>{id[:-3]}</cpt:parent>
  <dc:title xml:lang="fre">{html2txt(title_rich)}</dc:title>
  <dc:type>dts:work</dc:type>
  <cpt:members>
    <cpt:collection readable="true" path="./{id}.xml">
      <cpt:identifier>{id}</cpt:identifier>
      <cpt:parent>{id[:-3]}</cpt:parent>
      <dc:title xml:lang="fre">{html2txt(title_rich)}</dc:title>
      <dc:type>dts:edition</dc:type>
      <dc:creator>{author_name}, {author_firstname}</dc:creator>
      <dc:date>{promotion_year}</dc:date>
      <dc:publisher xml:lang="mul">École nationale des chartes</dc:publisher>
      <dc:language>fre</dc:language>
      <dc:coverage>{topic_notBefore}-{topic_notAfter}</dc:coverage>
      <dc:format>application/tei+xml</dc:format>
      <cpt:structured-metadata>
        <dct:extend>{pagination}</dct:extend>
        <dct:creator>https://www.idref.fr/{author_idref-id}</dct:creator>
        <dct:isPartOf>https://www.sudoc.fr/{these_ppn-sudoc}</dct:isPartOf>
        <dct:isPartOf>https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber={125235}</dct:isPartOf>
      </cpt:structured-metadata>
    </cpt:collection>
  </cpt:members>
</cpt:collection>
```

Exemple

```xml
<?xml-model href="../../../capitains.rng" schematypens="http://relaxng.org/ns/structure/1.0"?>
<cpt:collection xmlns:ti="http://chs.harvard.edu/xmlns/cts" xmlns:dct="http://purl.org/dc/terms/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cpt="http://purl.org/capitains/ns/1.0#" xmlns:owl="http://www.w3.org/2002/07/owl#" xmlns:bib="http://bibliotek-o.org/1.0/ontology/" xmlns:cts="http://chs.harvard.edu/xmlns/cts" xmlns:foaf="http://xmlns.com/foaf/0.1/">
  <cpt:identifier>ENCPOS_1972_18</cpt:identifier>
  <cpt:parent>ENCPOS_1972</cpt:parent>
  <dc:title xml:lang="fre">Le bestiaire héraldique au Moyen Âge</dc:title>
  <dc:type>dts:work</dc:type>
  <cpt:members>
    <cpt:collection readable="true" path="./ENCPOS_1972_18.xml">
      <cpt:identifier>ENCPOS_1972_18</cpt:identifier>
      <cpt:parent>ENCPOS_1972</cpt:parent>
      <dc:title xml:lang="fre">Le bestiaire héraldique au Moyen Âge</dc:title>
      <dc:type>dts:edition</dc:type>
      <dc:creator>Pastoureau, Michel</dc:creator>
      <dc:date>1972</dc:date>
      <dc:publisher xml:lang="mul">École des chartes, Paris</dc:publisher>
      <dc:language>fr</dc:language>
      <dc:coverage>1000-1499</dc:coverage>
      <dc:format>application/tei+xml</dc:format>
      <cpt:structured-metadata>
        <dct:extend>143-154</dct:extend>
        <dct:creator>https://www.idref.fr/027059952</dct:creator>
        <dct:isPartOf>https://www.sudoc.fr/234764724</dct:isPartOf>
        <dct:isPartOf>https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber=125235</dct:isPartOf>
      </cpt:structured-metadata>
    </cpt:collection>
  </cpt:members>
</cpt:collection>
```


### DTS

```json
{
  "@id": "ENCPOS_1972_18",
  "@type": "Resource",
  "title": "Le bestiaire héraldique au Moyen Âge",
  "totalItems": 0,
  "dts:passage": "/dts/document?id=ENCPOS_1972_18",
  "dts:references": "/dts/navigation?id=ENCPOS_1972_18",
  "dts:extensions": {
    "ns1:publisher": [
      {
        "@value": "École nationale des chartes",
        "@language": "mul"
      }
    ],
    "ns1:language": "fr",
    "ns1:type": [
      "dts:work",
      "dts:edition"
    ],
    "ns1:creator": "Pastoureau, Michel",
    "ns1:coverage": "1000-1499",
    "ns1:date": "1972",
    "ns1:title": [
      {
        "@value": "Le bestiaire héraldique au Moyen Âge",
        "@language": "fre"
      }
    ],
    "ns1:format": "application/tei+xml"
  },
  "dts:dublincore": {
    "dct:isPartOf": [
      {
        "@id": "https://www.sudoc.fr/234764724"
      },
      "benc_number: 125235"
    ],
    "dct:creator": [
      {
        "@id": "https://www.idref.fr/027059952"
      }
    ],
    "dct:extend": "143-154"
  },
  "@context": {
    "ns1": "http://purl.org/dc/elements/1.1/",
    "dts": "https://w3id.org/dts/api#",
    "dct": "http://purl.org/dc/terms/",
    "@vocab": "https://www.w3.org/ns/hydra/core#"
  }
}
```


