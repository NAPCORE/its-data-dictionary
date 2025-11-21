---
id: location-search_topographic-places
label: topographic places (city, town, village, suburb, administrative unit)
definition: the minimum information required for matching wider locations (e.g., areas, regions, localities, cities, suburbs, towns, administrative units, or settlements) as trip origins and destinations based on their name.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Location search (origin_destination)
---

>The names of settlements, counties, etc., are of importance for locating trip endpoints, namely for the distinction of place names that are not globally unique.

>The following data needs to be provided for topographic places:\
• Identifier (must be globally unique)\
• Name\
• Coordinates (Centroid)\
• Topographic or address identifiers\
• Category or classification

>The following data is optional for an address:\
• External identifiers (e.g., for OSM) (KeyList)\
• Area\
• Validity

<table style="font-size: smaller; width: 100%;">
  <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td>TOPOGRAPHIC PLACE</td>
    <td>A type of PLACE providing the topographical context when searching for or presenting travel information, for example as the origin or destination of a trip. It may be of any size (e.g., County, City, Town, Village) and of different specificity (e.g., Greater London, London, West End, Westminster, St James’s). Based on the Transmodel/NeTEx data specification, TOPOGRAPHIC PLACEs may be located within one single country, may intersect one or more countries, and may be contained inside other topographic places. TOPOGRAPHIC PLACEs can include disambiguation information to ensure that different places with the same name can be distinguished when searching for place names.</td>
  </tr>
</table>

>References/additional info: EN12896-1 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu); https://publications.jrc.ec.europa.eu/repository/handle/JRC118744

