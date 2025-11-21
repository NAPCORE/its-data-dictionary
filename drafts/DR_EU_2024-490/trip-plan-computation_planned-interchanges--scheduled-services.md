---
id: trip-plan-computation_planned-interchanges--scheduled-services
label: planned interchanges between guaranteed scheduled services
definition: the minimum information required for indicating the possibility for transfer of passengers from one planned transport service to another securely interconnected, essential for trip plan computation purposes.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Trip plan computation
---

>The planned transport services involved can be either scheduled transport or on demand transport.

<table style="font-size: smaller; width: 100%;">
  <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td>INTERCHANGE</td>
    <td>The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs.<br>This can be:<br>
    o SERVICE JOURNEY INTERCHANGE: the scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different SCHEDULED STOP POINTs, or<br>
    o SERVICE JOURNEY PATTERN INTERCHANGE: a recognised/organised possibility for passengers to change public transport vehicles using two SCHEDULED STOP POINTs (which may be identical) on two particular SERVICE JOURNEY PATTERNs, including the maximum wait duration allowed and the standard to be aimed at.<br> Or provided by an:<br>
    o INTERCHANGE RULE: Conditions for considering JOURNEYs<sup>10</sup> to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. </td>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;">The INTERCHANGE has the characteristic of being guaranteed (or not): i.e. the OPERATOR of the distributor service is in charge of ensuring the connection.</th>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;"><sup>10</sup> VEHICLE JOURNEYs (or SPECIAL SERVICEs: work of a vehicle that is not planned in a classical way, i.e. that is generally not based on VEHICLE JOURNEYs using JOURNEY PATTERNs). </th>
    </tr>
</table>

>BEST PRACTICES\
• For example, a guarantee is that a departing vehicle waits for a minimum amount of time for an arriving vehicle, guaranteeing an interchange for the passengers.\
• It may also describe the prioritized place of interchange between two journey legs.\
• It may also be used to describe that two journeys with different identifiers are in fact operated by the same vehicle, allowing the passenger to stay seated in the vehicle at the interchange point.\
• Interchanges connect two specific journeys at specific proximate stops, or at a single stop.\
• What is “guaranteed” must be clarified, and by whom. The interchange time provided in the booking phase by the trip planner is the responsibility of the trip planner, but the customer should know who is responsible for what in case of missed interchange, and it should be specified if the minimum interchange time is accepted by the operator(s) providing services before and after the interchange.\
• The “guaranteed” interchange time may differ according to the category of traveller (passenger with only hand luggage, passenger with registered luggage, passengers with reduced mobility, children travelling alone, etc.).

>References/additional info: EN12896-3 (see https://www.transmodel-cen.eu); CEN/TS 16614-2 (see https://netex-cen.eu); http://naptan.dft.gov.uk/transmodel/schema/doc/GoogleTransit/TransmodelForGoogle-07.pdf

