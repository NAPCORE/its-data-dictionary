---
id: auxiliary-information_standard-fare-structures
label: standard fare structures (point to point including daily and weekly fares, zonal fares, flat fares)
definition: the minimum information required to describe how users of public transport services are charged (i.e., data objects and elements needed to support the definition of fare products and their parameters).
category: Level of service 2
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Auxiliary information
  - for scheduled transport and transport on demand where relevant
  - basic common standard fares
---

>Fare structures can be broadly discerned into:\
• Space-based structures: flat or progressive, zonal- or interval-based, point-to-point, etc. Interval-based fares may be based on simple distances, numbers of zones, border points, etc.\
• Time-based structures: flat or progressive depending upon time intervals.\
• Combination of the two (e.g., fare products based on both zones and time intervals).

<table style="font-size: smaller; width: 100%;">
    <tr>
        <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Point to point fares may be described with DISTANCE MATRIX ELEMENTs</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Zonal fares may be described with DISTANCE MATRIX ELEMENTs</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Fares based on unit counts, such as number of zones or number of stops may be described using GEOGRAPHIC INTERVALs</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Fares that are progressive on distance may be described using GEOGRAPHIC INTERVALs</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Fares that are progressive on time may be described using TIME INTERVALs</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Other pricing factors can be represented using QUALITY STRUCTURE FACTORs (factors influencing access rights definition or calculation of prices, based on the quality: traffic congestion threshold, early/late reservation etc.</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Complex combinations of all the above (such as distance and time combinations) can be specified using GENERIC PARAMETER assignments</td>
    </tr>    
</table>

>References/additional info: https://www.transmodel-cen.eu/wp-content/uploads/2019/10/TUTORIAL_Part5_v2.3-1.pdf;
EN 12896-1,5 & 10 (see www.transmodel-cen.eu); CEN/TS 16614-1, 3 & 5 (see https://netex-cen.eu/)

