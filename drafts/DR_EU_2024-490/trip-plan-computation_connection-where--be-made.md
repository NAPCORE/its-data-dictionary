---
id: trip-plan-computation_connection-where--be-made
label: connection where interchanges may be made
definition: the minimum information required for indicating the attributes of connection links (enabling the transfer of travellers from one vehicle to another), essential for trip plan computation purposes.
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
    <td colspan="2" style="text-align: left">TRANSFER and its specializations CONNECTION, SITE CONNECTION, and DEFAULT CONNECTION</th>
  </tr>
  <tr>
    <td>TRANSFER</td>
    <td>A couple of POINTs located sufficiently near that it may represent for a passenger a possibility to reach one of these POINTs when starting at the other one in a timescale which is realistic when carrying out a trip.</td>
  </tr>
  <tr>
    <td>CONNECTION</td>
    <td>The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip, determined by a pair of points which may be either SCHEDULED STOP POINTs or VEHICLE MEETING POINTs. Different times may be necessary to cover the link between these points, depending on the kind of passenger.</td>
  </tr>
  <tr>
    <td>SITE CONNECTION</td>
    <td>The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip, determined by physical locations, such as SITEs and/or its components and/or ENTRANCEs, in particular STOP PLACEs and/or its components. Different times may be necessary to cover the resulting distance, depending on the kind of passenger.</td>
  </tr>
  <tr>
    <td>DEFAULT CONNECTION</td>
    <td>The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip.It specifies default times to be used to change from one mode of transport to another at an area or national level as specified by a TOPOGRAPHIC PLACE, STOP AREA or SITE ELEMENT. It may be restricted to a specific MODE or OPERATOR or only apply in a particular direction of transfer, e.g., bus to rail may have a different time for rail to bus.</td>
  </tr>
</table>

>BEST PRACTICES\
• From a topological perspective, connection links serve as a means of explicitly connecting two or more places that are located sufficiently near to each other to make a transfer between the points within a reasonable timeframe.\
• From a geographical perspective, connection links can be addressed as designated paths between two places, which may be made up of ordered sequences of links within a place or between two places representing a step in a possible route for pedestrians, cyclists, or other out-of-vehicle passengers. A common point in both perspectives is that a passenger transfer shall be time- and distance-feasible to be considered valid. In this respect, the attributes of connection links encompassed by this data category should at least include the distance and time duration of each connection link, also allowing for alternative durations for different types of impaired mobility. Moreover, connection links should be mode-specific including at least (and as applies) walking and cycling modes.

>References/additional info: EN12896-2 (see https://www.transmodel-cen.eu);  CEN/TS 16614-1 (see https://netex-cen.eu); https://publications.jrc.ec.europa.eu/repository/handle/JRC118744 

