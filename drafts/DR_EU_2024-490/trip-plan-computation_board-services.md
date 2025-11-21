---
id: trip-plan-computation_board-services
label: board services (such as toilets)
definition: the minimum information required for indicating the accessibility conditions of scheduled or on demand transport services’ vehicles (incl. their on-board amenities), essential for trip plan computation purposes.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Trip plan computation
---

>EXAMPLES\
• A specific train has a lower floor option for people traveling in wheelchairs.\
• A bus has guidance amenities for visually impaired travellers (e.g., handrail to board a bus and reach a seat, tactile and high contrast design).\
• A tramway has a screen with a continuous display of the next stop name for hearing-impaired travellers.\

<table style="font-size: smaller; width: 100%;">
      <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
    <tr>
        <td>ACTUAL VEHICLE EQUIPMENT</td>
        <td>An item of equipment of a particular type in an individual VEHICLE.</td>
    </tr>
    <tr>
        <td>PASSENGER EQUIPMENT</td>
        <td>An item of equipment of a particular type actually available at a location within a PLACE or a VEHICLE</td>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;">Both equipment types are characterised by accessibility-related features.</th>
    </tr>
    <tr>
        <td>ACCESSIBILITY ASSESSMENT</td>
        <td>The accessibility characteristics of an entity used by passengers such as a STOP PLACE, STOP PLACE COMPONENT, EQUIPMENT or DECK COMPONENT -to indicate its usability by passengers with specific needs, for example, those needing wheelchair access, step-free access or wanting to avoid confined spaces such as lifts. An ACCESSIBILITY ASSESSMENT comprises one or more ACCESSIBILITY LIMITATIONs.</td>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;">ACCESSIBILITY LIMITATION provides the following characteristics (some of them may be used to characterise accessibility of a vehicle as well):<br>
o Wheelchair access<br>
o Step-free access<br>
o Escalator-free access<br>
o Lift-free access<br>
o Audible signs available<br>
o Virtual signs available</th>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;">Accessibility features can be described in summary using FACILITIEs, or in detail using an appropriate specialisation of EQUIPMENT. For instance, ASSISTANCE FACILITY names support services such as boarding assistance, while ACCESSIBILITY INFO FACILITY names the available facilities for the visually and hearing impaired.  WHEELCHAIR VEHICLE EQUIPMENT describes physical properties of wheelchair spaces, ACCESS EQUIPMENT Describes ramps, hoists etc. LIFT EQUIPMENT describes lifts.</th>
    </tr>
</table>

>BEST PRACTICES\
• The above information can be used to find suitable routes and guide travellers with impaired mobility by assessing the suitability of the vehicles used on each service.\
• An important note: the classification of the accessibility services to describe the vehicles uses the same data model as the stations/stop facilities.\
• The number of places available for wheelchair, prams, bicycle, e-scooters… may be limited on-board a vehicle, and/or subject to allowed periods of the days (peak or off-peak periods).\
• The characteristics of the traveller may depend on specific categories according to the age, physical conditions, etc.\
• The traveller may have to cope with some technical requirements like: size and weight of wheelchairs, of prams, of luggage, conditions of travel for accompanying pets, conditions of travel for children, etc.

>References/additional info: EN12896-1&2 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu)

