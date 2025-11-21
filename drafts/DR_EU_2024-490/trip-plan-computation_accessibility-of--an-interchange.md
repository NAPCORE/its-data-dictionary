---
id: trip-plan-computation_accessibility-of--an-interchange
label: accessibility of access nodes, and paths within an interchange (such as existence of lifts, escalators)
definition: the minimum information required for indicating the accessibility conditions of access nodes as well as the conditions for transferring between vehicles, essential for trip plan computation purposes.
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
    <tr>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;">Transmodel explicitly represents ENTRANCEs, platforms (QUAYS) of a STOP PLACE, as well as and designated positions within platforms (BOARDING POINTs) so that precise directions can be given as to where to access a service journey, and/or from where to exit the access node. Intermediate places where facilities may also be located, such as ticket halls, waiting rooms, restaurants are described as ACCESS SPACEs. Any of the specific places may further be assigned EQUIPMENT to describe detailed characteristics such as the nature and dimensions of entrance barriers, lifts, ramps, and FACILITIEs to summarise available amenities and services such as boarding assistance.</th>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;">The components of a STOP PLACE including PATH LINKs, QUAYs, ENTRANCEs, etc., may be assigned ACCESSIBILITY LIMITATIONs with the following characteristics:<br>
•	Wheelchair access<br>
•	Step-free access<br>
•	Escalator-free access<br>
•	Lift-free access<br>
•	Audible signs available<br>
•	Virtual signs available</th>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;">Accessibility may be further described in detail with different types of ACCESS EQUIPMENT: an item of equipment of a particular type actually available at a location within a PLACE and dedicated to access (e.g., lifts, entrances, stairs, ramps, etc.). This can include physical dimensions and usability restrictions (e.g., ENTRANCE EQUIPMENT gives door dimensions and opening mechanisms).</th>
    </tr>    
</table>

>BEST PRACTICES\
The above conditions may encompass access through lifts, escalators, or navigations stairs.

>References/additional info: EN12896-2 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu) ; CEN/TS 16614-6 (EPIAP)

