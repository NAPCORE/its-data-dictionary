---
id: location-search_addresses
label: addresses (building number, street name, postcode)
definition: the minimum information required for matching specific locations (mainly properties) as trip origins and destinations based on their address.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Location search (origin_destination)
---

>The following data needs to be provided for an address:\
• Identifier (must be globally unique)\
• Name\
• Coordinates (Centroid)\
• Topographic or address identifiers\
• Category of classification

>The following data is optional for an address:\
• External identifiers (e.g., for OpenStreetMap (KeyList)\
• Additional coordinates (access)\
• Area\
• Validity

<table style="font-size: smaller; width: 100%;">
  <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td>ROAD ADDRESS</td>
    <td>Specialization of ADDRESS using conventional characteristics such as road number and name for identification of a location along a road.</td>
  </tr>
  <tr>
    <td>NeTEx POSTAL ADDRESS</td>
    <td>A specification of ADDRESS refining it by using the attributes used for conventional identification for mail. Comprises variously a building Identifier, Street name, Post code, and other descriptors.</td>
  </tr>
</table>

>BEST PRACTICES\
• Addresses that appear in this data type are mostly relevant to the postal address.\
• Examples of this are: building numbers, street numbers, postcodes linked with coordinates or other location references (coordinates will be supplied according to WGS84).\
• When talking of the origin and destination of a trip, it should be made clear if the reference for origin and destination is the physical location of the departure or arrival of the customer’s trip (e.g. from home and to a shopping mall), or the public transport point of origin and destination. In the latter case you need to add information about an access and egress trip leg which is most often not done by public transport (except if you order a taxi or an Uber-like service or some on-demand shuttles).\
• Based on INSPIRE data specification, the postal address constitutes a hierarchy consisting of components with an increasing level of detail, e.g., town, street name, and house number or house name. It may also include a post code or other postal descriptors.\
>Both types of addresses may be used:\
o The reference for postal address format is INSPIRE.\
o The reference for road address is NeTEx.

>References/additional info: EN12896-1 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu); https://publications.jrc.ec.europa.eu/repository/handle/JRC118744

