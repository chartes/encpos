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
- le manifeste IIIF : [https://iiif.chartes.psl.eu/encpos/encpos_1972_12/manifest](https://iiif.chartes.psl.eu/encpos/encpos_1972_12/manifest)


### `title_rich`

Titre de la position, avec des enrichissements typographiques

- format : HTML5
- par exemple : `<i>Ciperis de Vignevaux</i>, chanson de geste du début du <small>XV</small><sup>e</sup> siècle. Étude et édition`

Recours à 3 balises HTML5 :

- `small` : pour les petites caps, par ex. `<small>XV</small><sup>e</sup> siècle`. Permet de conserver la chaîne de caractères en MAJ, pour l’export texte brut.
- `sup`
- `i` : pour les titres, expressions en langue étrangère

NB. A partir de 2016, nous avons des titres **et des sous-titres** inscrits dans les `teiHeader` -> récupérer l’information.

NB. Des thèses ont presque le même titre. Donnée à explorer et proposer du rebond (thèse similaire).


### `title_text`

Titre de la position, sans enrichissement typographique, pour export SIGB et DTS (`title`) : export de `title_rich`, sans les balises.

**NB TODO. `title_text` doit disparaître, pour être dérivé de `title_rich`.**


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

## Réconciliation des données 
Requête SPARQL pour récupérer l'ark data.bnf et le catalogue général à partir du ppn idref:

~~~ sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT DISTINCT ?person
WHERE {
	?person skos:exactMatch <http://www.idref.fr/027059952>.
} LIMIT 100
~~~
Si on souhaite récupérer en même temps l'id wikidata et le lien wikipedia, il faut rajouter des demandes pour la requête :
~~~ sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT DISTINCT ?person ?wikidata ?wikipedia
WHERE {
	?person skos:exactMatch <http://www.idref.fr/027059952>.
  ?person skos:exactMatch ?wikidata;
          skos:exactMatch ?wikipedia.
  FILTER ( contains(str(?wikidata), "wikidata"))
  FILTER ( contains(str(?wikipedia), "wikipedia"))}
} LIMIT 100
~~~

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
2ème possibilité avec intégration des liens externes en changeant la forme de la balise author

```xml
<teiHeader>
    <fileDesc>
      <titleStmt>
        <title>{html2tei(rich_title)}</title>
        <author>
          <persName>{author_firstname} {author_name}</persName>
          <idno type="Idref">{author_idref-id}</idno>
          <idno type="dbpedia">{id_dbpedia}</idno>
          <idno type="Wikidata">{id_wikidata}</idno>
          <idno type="Wikipedia">{link_wikipedia}</idno>
          <idno type="DataBnF">{ark_databnf}</idno>
          <idno type="CatalogueBnF">{ark_cataloguebnf}</idno>   
        </author>
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

Exemple avec l'intégration des liens extérieurs en changenant la forme autour de author 

```xml
<teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Le bestiaire héraldique au Moyen_Âge</title>
        <author sameAs="https://www.idref.fr/027059952">Michel Pastoureau</author>
        <author>
          <persName>Michel Pastoureau</persName>
          <idno type="Idref">027059952</idno>
          <idno type="dbpedia">http://dbpedia.org/resource/Michel_Pastoureau</idno>
          <idno type="Wikidata">http://wikidata.org/entity/Q2497623</idno>
          <idno type="Wikipedia">http://fr.wikipedia.org/wiki/Michel_Pastoureau</idno>
          <idno type="DataBnF">http://data.bnf.fr/ark:/12148/cb119187467</idno>
          <idno type="CatalogueBnF">https://catalogue.bnf.fr/ark:/12148/cb119187467</idno>
        </author>
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
	- `title_rich
	- liages Wikidata, data.bnf, etc.
  
Tous les liens sont liées à l'auteur donc à une personne exemple de Michel Pastoureau pour son livre [*Le loup, une histoire culturelle*](https://data.bnf.fr/fr/temp-work/3c57f282f8a639ec0998784e8da7d8d5/rdf.jsonld)

Donc une solution peut être de faire le liste des liens qui concerne l'auteur dans `dct:creator`


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
        <dct:title>{title_rich}</dct:title>
        <dct:extend>{pagination}</dct:extend>
        <dct:creator>https://www.idref.fr/{author_idref-id}</dct:creator>
        <dct:creator>{ark_databnf}</dct:creator>
        <dct:creator>{ark_cataloguebnf}</dct:creator>
        <dct:creator>{id_wikidata}</dct:creator>
        <dct:creator>{link_wikipedia}</dct:creator>
        <dct:creator>{id_dbpedia}</dct:creator>
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
        <dct:creator>http://data.bnf.fr/ark:/12148/cb119187467</dct:creator>
        <dct:creator>https://catalogue.bnf.fr/ark:/12148/cb119187467</dct:creator>
        <dct:creator>http://wikidata.org/entity/Q2497623</dct:creator>
        <dct:creator>http://fr.wikipedia.org/wiki/Michel_Pastoureau</dct:creator>
        <dct:creator>http://dbpedia.org/resource/Michel_Pastoureau</dct:creator>
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
    "ns1:format": "application/tei+xml",
    "ns1:type": [
      "dts:work",
      "dts:edition"
    ],
    "ns1:date": "1972",
    "ns1:creator": [
      "Pastoureau, Michel",
      "https://www.idref.fr/027059952"
    ],
    "ns1:coverage": "1000-1499",
    "ns1:publisher": [
      {
        "@value": "École des chartes, Paris",
        "@language": "mul"
      }
    ],
    "ns1:title": [
      {
        "@value": "Le bestiaire héraldique au Moyen Âge",
        "@language": "fre"
      }
    ],
    "ns1:language": "fr"
  },
  "dts:dublincore": {
    "dct:creator": [
      {
        "@id": "http://wikidata.org/entity/Q2497623"
      },
      {
        "@id": "https://www.idref.fr/027059952"
      },
      {
        "@id": "http://dbpedia.org/resource/Michel_Pastoureau"
      },
      {
        "@id": "http://data.bnf.fr/ark:/12148/cb119187467"
      },
      {
        "@id": "https://catalogue.bnf.fr/ark:/12148/cb119187467"
      },
      {
        "@id": "http://fr.wikipedia.org/wiki/Michel_Pastoureau"
      }
    ],
    "dct:isPartOf": [
      "benc_number: 125235",
      {
        "@id": "https://www.sudoc.fr/234764724"
      }
    ],
    "dct:extend": "143-154"
  },
  "@context": {
    "dct": "http://purl.org/dc/terms/",
    "dts": "https://w3id.org/dts/api#",
    "ns1": "http://purl.org/dc/elements/1.1/",
    "@vocab": "https://www.w3.org/ns/hydra/core#"
  }
}
```

Après lecture de l'issue 42 projet DTS sur github dans dct:creator, on ne devrait avoir qu'une liste d'URIRef et ne pas avoir des dictionnaires. Voir l'issue [https://github.com/distributed-text-services/specifications/issues/42](https://github.com/distributed-text-services/specifications/issues/42). Le problème semble être dans le fichier _json_ld.py de MyCapitain qui considère qu'un URIRef doit être dans un dictionnaire avec une id [https://github.com/Capitains/MyCapytain/blob/dev/MyCapytain/common/utils/_json_ld.py](https://github.com/Capitains/MyCapytain/blob/dev/MyCapytain/common/utils/_json_ld.py)


```json
{
  "@id": "ENCPOS_1972_18",
  "@type": "Resource",
  "title": "Le bestiaire héraldique au Moyen Âge",
  "totalItems": 0,
  "dts:passage": "/dts/document?id=ENCPOS_1972_18",
  "dts:references": "/dts/navigation?id=ENCPOS_1972_18",
  "dts:extensions": {
    "ns1:format": "application/tei+xml",
    "ns1:type": [
      "dts:work",
      "dts:edition"
    ],
    "ns1:date": "1972",
    "ns1:creator": [
      "Pastoureau, Michel",
      "https://www.idref.fr/027059952"
    ],
    "ns1:coverage": "1000-1499",
    "ns1:publisher": [
      {
        "@value": "École des chartes, Paris",
        "@language": "mul"
      }
    ],
    "ns1:title": [
      {
        "@value": "Le bestiaire héraldique au Moyen Âge",
        "@language": "fre"
      }
    ],
    "ns1:language": "fr"
  },
  "dts:dublincore": {
    "dct:creator": [
      "http://wikidata.org/entity/Q2497623",
      "https://www.idref.fr/027059952",
      "http://dbpedia.org/resource/Michel_Pastoureau",
      "http://data.bnf.fr/ark:/12148/cb119187467",
      "https://catalogue.bnf.fr/ark:/12148/cb119187467",
      "http://fr.wikipedia.org/wiki/Michel_Pastoureau"
    ],
    "dct:isPartOf": [
      "benc_number: 125235",
      {
        "@id": "https://www.sudoc.fr/234764724"
      }
    ],
    "dct:extend": "143-154"
  },
  "@context": {
    "dct": "http://purl.org/dc/terms/",
    "dts": "https://w3id.org/dts/api#",
    "ns1": "http://purl.org/dc/elements/1.1/",
    "@vocab": "https://www.w3.org/ns/hydra/core#"
  }
}
```
