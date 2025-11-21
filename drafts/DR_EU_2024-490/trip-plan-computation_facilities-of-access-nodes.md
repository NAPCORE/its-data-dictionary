---
id: trip-plan-computation_facilities-of-access-nodes
label: facilities of access nodes (including platform information, help desk/information points, ticket booths, lifts_stairs, entrances and exit locations)
definition: the minimum information required for describing the fixed equipment/facilities of the access nodes of scheduled or on demand transport services, essential for trip plan computation purposes.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Trip plan computation
---

<table style="font-size: smaller; width: 100%;">
   <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: left;">Transmodel explicitly represents ENTRANCEs, platforms (QUAYS) of a STOP PLACE, as well as designated positions within platforms (BOARDING POINTs) so that precise directions can be given as to where to access a service journey, and/or from where to exit the access node. Intermediate places where facilities may also be located, such as ticket halls, waiting rooms, restaurants are described as ACCESS SPACEs. Any of the specific places may further be assigned EQUIPMENT to describe detailed characteristics such as the nature and dimensions of entrance barriers, lifts, ramps, and FACILITIEs to summarize available amenities and services such as boarding assistance.<br>
    NOTE: The above information may be used for providing guidance to travellers planning or making a trip, e.g., where to request for information, where to validate tickets, from where to access a service journey, and/or from where to exit the access node. Transmodel describes amenities and support services at two different levels of detail. </th>
  </tr>
  <tr>
        <td>FACILITY</td>
        <td>A named amenity available to the public at a SITE or on a SERVICE.</td>
  </tr>
  <tr>
        <td>EQUIPMENT</td>
        <td>An item of equipment installed either at a fixed point (PLACE EQUIPMENT) or on-board vehicles (VEHICLE EQUIPMENT).</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: left;">A service (LOCAL SERVICE such as LEFT LUGGAGE, TICKETING SERVICE) available at a SITE is considered immaterial EQUIPMENT. EQUIPMENT and LOCAL SERVICE are specialised to create many different types of equipment and services with detailed properties, for example LIFT EQUIPMENT, STAIR EQUIPMENT, WAITING EQUIPMMENT, SIGN EQUIPMENT, RETAIL SERVICE, CATERING SERVICE, ASSISTANCE SERVICE, etc., etc. </th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: left;">Information about the location of entrances and exits is provided by the STOP PLACE ENTRANCE components of a STOP PLACE and their relationship to the boarding and alighting points (QUAYS) is given by PATH LINKs. These can be used by a trip planner to create trip specific directions. The location of signage to direct the passenger (and that the passenger will see if following a particular route) can be described using SIGN EQUIPMENT.</th>
  </tr>    
</table>

>References/additional info: EN12896-2 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu)
https://publications.jrc.ec.europa.eu/repository/handle/JRC118744

