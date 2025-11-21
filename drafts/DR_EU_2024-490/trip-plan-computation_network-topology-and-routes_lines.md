---
id: trip-plan-computation_network-topology-and-routes_lines
label: network topology and routes/lines (topology)
definition: the minimum information required for indicating the topology of the service network of scheduled transport or transport on demand modes, essential for trip plan computation purposes.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Trip plan computation
---

>This data category assists the indication of the pattern of stops that makes up the timetables.

<table style="font-size: smaller; width: 100%;">
  <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td>ROUTE</td>
    <td>An ordered list of located POINTs defining one single path through the road (or rail) network. A ROUTE may pass through the same POINT more than once.</td>
  </tr>
  <tr>
    <td>FLEXIBLE ROUTE</td>
    <td>Specialisation of ROUTE for flexible services.</td>
  </tr>
  <tr>
    <td>LINE</td>
    <td>A group of ROUTEs which is generally known to the public by a similar name or number.</td>
  </tr>
  <tr>
    <td>FLEXIBLE LINE</td>
    <td>Specialisation of LINE for flexible service.</td>
  </tr>
    <tr>
    <td>SERVICE PATTERN</td>
    <td>An ordered list of SCHEDULED STOP POINTs on a single ROUTE, sequentially connected by SERVICE LINKs, describing the pattern of working for public transport vehicles.</td>
  </tr>
      <tr>
    <td>FLEXIBLE STOP PLACE</td>
    <td>A specialisation of the STOP PLACE describing a stop of a FLEXIBLE SERVICE. It may be composed of FLEXIBLE AREAs or HAIL AND RIDE AREAs identifying the catchment areas for flexible services (when they use areas or flexible quays). Some FLEXIBLE SERVICE also uses regular STOP PLACEs for their stops.</td>
  </tr>
</table>

>BEST PRACTICES\
The topology of service networks is defined by routes, lines, and service patterns.

>References/additional info: EN12896-2 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu); https://publications.jrc.ec.europa.eu/repository/handle/JRC118744

