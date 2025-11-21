---
id: trip-plan-computation_road-network
label: road network (including segregated lanes for bus/taxi)
definition: the minimum information required for describing the link and node structure of a (linear) road network used for the transportation of vehicles.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Trip plan computation
---

<table style="font-size: smaller; width: 100%;">
    <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</tr>
    <tr>
    <td colspan="2" style="text-align: left;">The road network is represented by ROAD (RAILWAY) ELEMENTs and ROAD (RAILWAY) JUNCTIONs.  Such elements are part of the physical transport infrastructure. Transmodel/NeTEx describe in detail the service infrastructure using for example ROUTEs:  ordered lists of located POINTs defining one single path through the road (or rail) network). ROUTEs (defined through ROUTE LINKs and ROUTE POINTs) are schematic representations of vehicle paths. In order to integrate/link the road network data with transport service data sets, the elements of the service network (e.g., ROUTEs) may be projected on the infrastructure network. The Transmodel/NeTEx PROJECTION mechanism allows this association.</th>
    </tr>
        <tr>
        <td>PROJECTION</td>
        <td>An oriented correspondence from an element in one layer, onto an entity in a target layer.</td>
    </tr>
</table>

>BEST PRACTICES\
The primary dimensions modelled for road network elements include (INSPIRE – reference):\
• Spatial dimension: Geometric (point, line, and area (topographic)) representation of various elements that are parts of a road network. Typically, the road network is handled as a network of connected linear elements (links) with points (nodes) at the ends of the lines (at junctions, road ends, etc.). Real objects with a function in a network may also be represented in a dataset. Network connectivity within the roads network is essential but between elements in the other networks is an optional spatial aspect.\
• Temporal dimension: All elements in a network may have a temporal validity (i.e., description of when a network element exists or is available in the real world). Optional meta-information on when information about a network element was entered, modified, or deleted may also be included in a dataset.\
• Thematic dimension: The road schema can be thematically displayed via several of the attributes defined within the specification.\
The three dimensions mentioned above are relevant to the physical infrastructure representing the road network.

>References/additional info: EN12896-1 (see www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu/);
https://publications.jrc.ec.europa.eu/repository/handle/JRC118744

