---
id: auxiliary-information_fare-network-data
label: fare network data (fare zones/stops and fare stages)
definition: the minimum information required for describing the layout of a fare network, such as the zones of which it is comprised.
category: Level of service 2
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Auxiliary information
  - for scheduled transport and transport on demand where relevant
  - basic common standard fares
---

>Fare or tariff zones are used to group different sections of a public transport journey for which a set charge is made. They constitute two-dimensional elements within the service area of a public transport operator. The individual one-dimensional elements within the service are of a public transport operator. The individual one-dimensional sections of a fare network are defined as the consecutive fare or border points of a public transport journey that fall within the same fare or tariff zone. For fare structures that are based on the number of fare stages passed, the fare stages passed, the fare stages can be demarcated.

<table style="font-size: smaller; width: 100%;">
    <tr>
        <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
    </tr>
    <tr>
        <td>TARIFF ZONE</td>
        <td>A ZONE used to define a zonal fare structure in a zone-counting or zone-matrix system.</td>
    </tr>
    <tr>
        <td>FARE ZONE</td>
        <td>A specialization of TARIFF ZONE to include FARE SECTIONs.</td>
    </tr>
    <tr>
        <td>FARE SECTION</td>
        <td>A subdivision of a JOURNEY PATTERN<sup>13</sup> consisting of consecutive POINTs IN JOURNEY PATTERN, used to define an element of the fare structure. FARE SECTIONs can be used to indicate fare stages.</td>
    </tr>
    <tr>
        <td>ZONE</td>
        <td>A two-dimensional location.  NOTE: may have global coordinates or relative to an encompassing space.</td>
    </tr>    
    <tr>
        <td colspan="2" style="text-align: left;"><sup>13</sup> An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles.</td>
    </tr>
</table>

>References/additional info: EN 12896-1, 2 & 10 (see www.transmodel-cen.eu); CEN/TS 16614-1 & 5 (see https://netex-cen.eu/)

