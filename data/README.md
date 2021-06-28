Métadonnées des positions de thèses
===

**Documentation en cours de rédaction**

L’application est pilotée par le tableau `encpos.tsv` :

- les métadonnées sont injectées dans les fichiers `__capitains__.xml` grâce à un [Capitainizer](https://github.com/chartes/capitainizer).
- les métadonnées sont ensuite exposées via le *endpoint* DTS `Collections`, par ex. : [https://dev.chartes.psl.eu/dts/collections?id=ENCPOS_1972_18](https://dev.chartes.psl.eu/dts/collections?id=ENCPOS_1972_18)

Une position de thèse et un résumé d’une thèse d’École des chartes publié dans le volume annuel des positions des thèses.


## Métadonnées de référence : `encpos.tsv`

### `id`

Identifiant de la position

- format : `ENCPOS_{AAAA}_{NN}` (`AAAA` : année de publication ;  `NN` : numéro d’ordre dans le volume).
- par exemple : `ENCPOS_1972_18`

Cet identifiant permet de désigner :

- la source XML/TEI : `ENCPOS_1972_18.xml`
- le fichier PDF : `ENCPOS_1972_18.pdf`
- le manifeste IIIF : [`https://iiif.chartes.psl.eu/encpos/encpos_1972_12/manifest`](https://iiif.chartes.psl.eu/encpos/encpos_1972_12/manifest)


### `title_rich`

Titre de la position, avec des enrichissements typographiques.

Pour les exports SIGB et DTS (`dc:title`), le titre de la position sans enrichissement typographique, est généré par la simple suppression de ces balises.

- format : HTML5
- par exemple : `<i>Ciperis de Vignevaux</i>, chanson de geste du début du <small>XV</small><sup>e</sup> siècle. Étude et édition`

3 balises HTML5 autorisées :

- `small` : chaîne **en capitales**, rendue en petites capitales. On conserve ainsi les capitales, pour l’export texte brut. Par ex. `<small>XV</small><sup>e</sup> siècle` → `XVe siècle` (et non `xve siècle`).
- `sup` : exposant.
- `i` : titre cité ou expression en langue étrangère.


### `promotion_year`

Année de publication du volume de la position (et donc de la promotion qui soutient sa thèse).


### `author_name`

Nom standardisé de l’auteur (minuscules et majuscules initiales), pour les tris.

- `Bastard, De`
- `Delisle`
- `La Borderie, De`


### `author_firstname`

Prénom de l’auteur, en minuscules avec majuscules initiales, pour les tris (utile notamment pour rechercher une autrice).


### `author_fullname_label`

Nom complet de l’auteur (Prenom Nom) pour affichage.


### `author_idref_ppn`

Le [`PPN`](https://data.idref.fr/) IdRef de l’auteur : identifiant à 9 caractères (NB. peut commencer par un `0`).

- Pour l’identification des auteurs et le liage Sudoc.
- Donnée de référence utile à différents liages (data.bnf, Wikidata, etc.).
- L’ABES s’engage à fournir un PPN pour **tous** les auteurs du corpus. Dialogue avec la bibliothèque en cours : 187 PPN manquant (le 18/06/2021).


### `author_bnf_ark`

Liage : identifiant ark BnF de l’auteur. Utile pour le liage data.bnf.fr et le lien à la notice auteur du catalogue général de la BnF.

par ex., pour `ark:/12148/cb119187467` :

- lien data.bnf.fr : [https://data.bnf.fr/ark:/12148/cb119187467](https://data.bnf.fr/ark:/12148/cb119187467)
- lien catalogue général : [https://catalogue.bnf.fr/ark:/12148/cb119187467](https://catalogue.bnf.fr/ark:/12148/cb119187467)


### `author_wikidata_id`

Liage : identifiant (`Q`) Wikidata de l’auteur. Donnée pivot essentielle (liage Wikipedia) et l’appel à différentes ressources (portrait de l’auteur, etc.).


### `author_wikipedia_url`

URL de la page Wikipedia (fr) de l’auteur.

TODO. Revoir l’encodage des URL?


### `author_dbpedia_id`

Liage : identifiant (`string`) DBpedia de l’auteur.


### `author_gender`

Genre de l’auteur :

- `1` : masculin
- `2` : féminin

Permet d’observer l’équilibre des genres sur 150 ans.


### `author_is_enc_teacher`

Booléen pour déterminer si l’auteur de la position a par la suite été professeur à l’École des chartes.

- `1` : futur professeur de l’École des chartes
- `O` : sinon


### `pagination`

Pagination de la position dans le volume annuel : `startPage-endPage`.


### `topic_notBefore` et `topic_notAfter`

Indexation sujet : bornes chronologiques du sujet traité, inscrites en [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601).  
Pour les millésimes avant notre ère : `-AAAA`.


### `thenca_these-record_id`

L’identifiant numérique ThENC@ de la notice de la thèse correspondante. Par ex., pour `47536`, la notice est accessible : [http://bibnum.chartes.psl.eu/s/thenca/item/47536](http://bibnum.chartes.psl.eu/s/thenca/item/47536)


### `benc_these-record_id`

L’identifiant de la notice de la thèse correspondante dans le SIGB de la bibliothèque de l’ENC. Par ex., pour `125235`, la notice est accessible : [https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber=125235](https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber=125235)


### `sudoc_these-record_ppn`

Identifiant de la notice de la thèse correspondante dans le Sudoc. Par ex., pour `234764724`, la notice est accessible : [https://www.sudoc.fr/234764724](https://www.sudoc.fr/234764724)

NB. Donnée essentielle pour reconstruire de nombreux liages.


### `hal_these-record_id`

Identifiant de la notice de la thèse correspondante dans [HAL-SHS](https://halshs.archives-ouvertes.fr/). Par ex., pour `tel-01116805v1`, la notice est accessible : [https://halshs.archives-ouvertes.fr/tel-01116805v1](https://halshs.archives-ouvertes.fr/tel-01116805v1)

NB. La thèse numérisée peut-être accessible sur le portail HAL-SHS.


### Identifiants abandonnés de la bibliothèque

Ces identifiants ont pu être utilisés au cours du projet, à la bibliothèque. Abandonnés, ils ne sont pas inscrits dans le tableau des métadonnées. Nous les documentons pour mémoire :

- `site:id` : concaténation `{AAAA}{numéro-ordre}`, par ex. `197218` pour `ENCPOS_1972_18`. Ajout des M2TNAH ? Quelle utilité ? Supprimer ?
- `these_id` : `{AAAA}THESE{numéro-ordre}`, par ex. `1972THESE18`. Cote BENC : toujours utilisé ? on garde ?


## CapiTains

Les métadonnées inscrites dans `encpos.tsv` sont injectées dans les fichiers `__capitains__.xml` grâce à un [Capitainizer](https://github.com/chartes/capitainizer).

Cette sérialisation XML des métadonnées doit se conformer aux [recommandations CapiTains](http://capitains.org/pages/guidelines). Un [schéma Relax-NG](https://raw.githubusercontent.com/Capitains/guidelines/master/capitains.rng) est disponible pour la validation.


### Template

```xml
<?xml-model
  href="https://raw.githubusercontent.com/Capitains/guidelines/master/capitains.rng"
  schematypens="http://relaxng.org/ns/structure/1.0"
?>
<cpt:collection
  xmlns:dts="https://w3id.org/dts/api#"
  xmlns:html="http://www.w3.org/1999/xhtml/"
  xmlns:dct="http://purl.org/dc/terms/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:cpt="http://purl.org/capitains/ns/1.0#"
  >
  <cpt:identifier>{id}</cpt:identifier>
  <dc:type>dts:work ???</dc:type><!-- Requis, mal documenté : on attend quoi ici ? -->
  <dc:title xml:lang="fre">{html2string(title_rich)}</dc:title>
  <cpt:parent>ENCPOS_{promotion_year}</cpt:parent>
  <cpt:members>
    <cpt:collection readable="true" path="./{id}.xml">
      <cpt:identifier>{id}</cpt:identifier>
      <dc:type>dts:edition ???</dc:type><!-- Requis, mal documenté : on attend quoi ici ? -->
      <dc:title xml:lang="fre">{html2string(title_rich)}</dc:title><!-- Requis, mais redondant. cf //cpt:structured-metadata/dct:title -->
      <dc:language>fre</dc:language><!-- Requis, mais redondant. cf //cpt:structured-metadata/dct:language -->
      <cpt:parent>ENCPOS_{promotion_year}</cpt:parent>
      <cpt:structured-metadata>
        <dct:title xml:lang="fre">{html2string(title_rich)}</dct:title>
        <html:h1>{title_rich}</html:h1>
        <dct:creator>{author_fullname_label}</dct:creator>
        <dct:creator>https://www.idref.fr/{author_idref_ppn}</dct:creator>
        <dct:creator>https://catalogue.bnf.fr/{author_bnf_ark}</dct:creator>
        <dct:creator>https://data.bnf.fr/{author_bnf_ark}</dct:creator>
        <dct:creator>https://wikidata.org/entity/{author_wikidata_id}</dct:creator>
        <dct:creator>{author_wikipedia_url}</dct:creator>
        <dct:creator>https://dbpedia.org/resource/{author_dbpedia_id}</dct:creator>
        <dct:date>{promotion_year}</dct:date>
        <dct:extend>{pagination}</dct:extend>
        <dct:publisher xml:lang="mul">École des chartes, Paris</dct:publisher>
        <dct:language>fre</dct:language>
        <dct:coverage>{iso8601(topic_notBefore, topic_notBefore)}</dct:coverage>
        <dct:format>application/tei+xml</dct:format>
        <dct:rights>https://creativecommons.org/licenses/by-nc-nd/3.0/fr/</dct:rights>
        <dct:isVersionOf>https://www.sudoc.fr/{sudoc_these-record_ppn}</dct:isVersionOf>
        <dct:isVersionOf>https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber={benc_these-record_id}</dct:isVersionOf>
        <dct:source>https://iiif.chartes.psl.eu/encpos/{id.lower()}/manifest</dct:source>
        <dts:download>https://github.com/chartes/encpos/raw/metadata/data/ENCPOS_{promotion_year}/{id}.xml</dts:download>
        <dts:download>https://github.com/chartes/encpos/raw/metadata/data/ENCPOS_{promotion_year}/{id}.PDF</dts:download>
      </cpt:structured-metadata>
    </cpt:collection>
  </cpt:members>
</cpt:collection>
```

### Exemple

```xml
<?xml-model
  href="https://raw.githubusercontent.com/Capitains/guidelines/master/capitains.rng"
  schematypens="http://relaxng.org/ns/structure/1.0"
?>
<cpt:collection
  xmlns:dts="https://w3id.org/dts/api#"
  xmlns:html="http://www.w3.org/1999/xhtml/"
  xmlns:dct="http://purl.org/dc/terms/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:cpt="http://purl.org/capitains/ns/1.0#">
  <cpt:identifier>ENCPOS_1972_18</cpt:identifier>
  <dc:type>dts:work ???</dc:type><!-- Requis, mal documenté : on attend quoi ici ? -->
  <dc:title xml:lang="fre">Le bestiaire héraldique au Moyen Âge</dc:title>
  <cpt:parent>ENCPOS_1972</cpt:parent>
  <cpt:members>
    <cpt:collection readable="true" path="./ENCPOS_1972_18.xml">
      <cpt:identifier>ENCPOS_1972_18</cpt:identifier>
      <dc:type>dts:edition ???</dc:type><!-- Requis, mal documenté : on attend quoi ici ? -->
      <dc:title xml:lang="fre">Le bestiaire héraldique au Moyen Âge</dc:title><!-- Requis, mais redondant. cf //cpt:structured-metadata/dct:title -->
      <dc:language>fre</dc:language><!-- Requis, mais redondant. cf //cpt:structured-metadata/dct:language -->
      <cpt:parent>ENCPOS_1972</cpt:parent>
      <cpt:structured-metadata>
        <dct:title xml:lang="fre">Le bestiaire héraldique au Moyen Âge</dct:title>
        <html:h1>Le bestiaire héraldique au Moyen Âge</html:h1>
        <dct:creator>Michel Pastoureau</dct:creator>
        <dct:creator>https://www.idref.fr/027059952</dct:creator>
        <dct:creator>https://catalogue.bnf.fr/ark:/12148/cb119187467</dct:creator>
        <dct:creator>https://data.bnf.fr/ark:/12148/cb119187467</dct:creator>
        <dct:creator>https://wikidata.org/entity/Q2497623</dct:creator>
        <dct:creator>https://fr.wikipedia.org/wiki/Michel_Pastoureau</dct:creator>
        <dct:creator>https://dbpedia.org/resource/Michel_Pastoureau</dct:creator>
        <dct:date>1972</dct:date>
        <dct:extend>143-154</dct:extend>
        <dct:publisher xml:lang="mul">École des chartes, Paris</dct:publisher>
        <dct:language>fr</dct:language>
        <dct:coverage>1000/1499</dct:coverage>
        <dct:format>application/tei+xml</dct:format>
        <dct:rights>https://creativecommons.org/licenses/by-nc-nd/3.0/fr/</dct:rights>
        <dct:isVersionOf>https://www.sudoc.fr/234764724</dct:isVersionOf>
        <dct:isVersionOf>https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber=125235</dct:isVersionOf>
        <dct:source>https://iiif.chartes.psl.eu/encpos/encpos_1972_18/manifest</dct:source>
        <dts:download>https://github.com/chartes/encpos/raw/metadata/data/ENCPOS_1972/ENCPOS_1972_18.xml</dts:download>
        <dts:download>https://github.com/chartes/encpos/raw/metadata/data/ENCPOS_1972/ENCPOS_1972_18.PDF</dts:download>
      </cpt:structured-metadata>
    </cpt:collection>
  </cpt:members>
</cpt:collection>
```


## DTS

### Template

```json
  "@id": "{id}",
  "@type": "Resource",
  "title": "{html2string(title_rich)}",
  "totalItems": 0,
  "dts:totalParents": 1,
  "dts:totalChildren": 0,
  "dts:passage": "/dts/document?id={id}",
  "dts:references": "/dts/navigation?id={id}",
  "dts:download": [
    "https://github.com/chartes/encpos/raw/master/data/{path-to-xml-file.xml}",
    "https://github.com/chartes/encpos/raw/master/data/{path-to-pdf-file.pdf}"
  ],
  "dts:citeDepth": "1",
  "dts:citeStructure": [
    {
      "dts:citeType": "position"
    }
  ],
  "dts:extensions": {
    "html:h1": "{title_rich}"
  },
  "dts:dublincore": {
    "dc:date": "{promotion_year}",
    "dc:creator": [
      "{author_fullname_label}",
      "https://www.idref.fr/{author_idref-ppn}",
      "http://data.bnf.fr/{author_bnf_ark}",
      "https://catalogue.bnf.fr/{author_bnf_ark}",
      "http://wikidata.org/entity/{author_wikidata_id}",
      "{author_wikipedia_url}",
      "http://dbpedia.org/resource/{author_dbpedia_id}"
    ],
    "dc:title": [
      {
        "@value": "{html2string(title_rich)}",
        "@language": "fre"
      }
    ],
    "dc:language": [
      "fre"
    ],
    "dc:format": "application/tei+xml",
    "dc:coverage": "{iso8601(topic_notBefore, topic_notBefore)}",
    "dc:publisher": [
      "École nationale des chartes",
      "https://www.wikidata.org/wiki/Q273570"
    ],
    "dc:source": [
      {
        "@id": "https://catalogue.bnf.fr/ark:/12148/cb344683389",
        "@type": "text",
        "dc:title": "Positions des thèses soutenues par les élèves de la promotion de ... pour obtenir le diplôme d'archiviste paléographe",
        "dc:date": "{promotion_year}",
        "dc:extent": "p. {pagination}"
      },
      {
        "@id": "https://iiif.chartes.psl.eu/encpos/{id.lower()}/manifest",
        "@type": "sc:Manifest",
        "dc:title": "{author_fullname_label}, {html2string(title_rich)}"
      }
    ],
    "dc:isVersionOf": [
      "http://bibnum.chartes.psl.eu/s/thenca/item/{thenca_these-record_id}",
      "https://catalogue.chartes.psl.eu/cgi-bin/koha/opac-detail.pl?biblionumber={benc_these-record_id}",
      "https://www.sudoc.fr/{sudoc_these-record_ppn}",
      "https://halshs.archives-ouvertes.fr/{hal_these-record_id}"
    ]
  },
  "@context": {
    "dc": "http://purl.org/dc/terms/",
    "dts": "https://w3id.org/dts/api#",
    "html": "http://www.w3.org/1999/xhtml",
    "@vocab": "https://www.w3.org/ns/hydra/core#"
  }
}
```

### Exemple

[`https://dev.chartes.psl.eu/dts/collections?id=ENCPOS_1972_18`](https://dev.chartes.psl.eu/dts/collections?id=ENCPOS_1972_18)



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


