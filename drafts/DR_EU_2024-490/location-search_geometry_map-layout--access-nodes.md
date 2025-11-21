---
id: location-search_geometry_map-layout--access-nodes
label: geometry/map layout structure of access nodes
definition: the minimum information required for identifying the location of specific facilities within access nodes considering the topographical structure of access nodes.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Location search (access nodes)
---

<table style="font-size: smaller; width: 100%;">
  <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td>EQUIPMENT PLACE </td>
    <td>A SITE (e.g., a STOP PLACE) COMPONENT containing EQUIPMENT.</td>
  </tr>
  <tr>
    <td>EQUIPMENT POSITION</td>
    <td>The precise position within an EQUIPMENT PLACE where particular equipment is placed.</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: left">It is also possible to relate equipment to PATH LINKs; PATH LINKs within a STOP PLACE are connecting between components. (e.g., a STOP PLACE ENTRANCE, ACCESS SPACE, QUAY, BOARDING POSITIONs, etc.), or PATH JUNCTIONs (i.e. points at which two or more PATH LINKs may connect or branch).</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: left">Equipment may be represented on a SCHEMATIC MAP:  A map representing schematically the layout of the topographic structure of PLACEs (e.g., a set of SITEs) or the public transport network (a set of LINEs), or other entity with a geometric projection (e.g., DECK PLAN for a train, vessel or aircraft). It can include a pixel projection of a set of ENTITies onto a bitmap image so as to support hyperlinked interactions.</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: left">The nature of amenities available at an access node can be specified as FACILITies and LOCAL SERVICEs. Further detailed information can be provided using EQUIPMENT of different types (e.g., LIFT EQUIPMENT, TICKET EQUIPMENT, ENTRANCE EQUIPMENT, etc.). Within an access node EQUIPMENT can be exactly located using an EQUIPMENT POSITION.</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: left">The topographical structure of an access node can be described through the spatial layout of its subcomponents and by explicit links between them, over which a trip planner may compute a route through a site. The plan of a STOP PLACE and the paths through it can be visualized on a digital map.</th>
  </tr>
</table>

>References/additional info: EN12896-2 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu); https://publications.jrc.ec.europa.eu/repository/handle/JRC118744

