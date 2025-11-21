---
id: trip-plan-computation_transport-operators
label: transport operators
definition: the minimum information about the public transport companies providing scheduled transport or transport on demand services necessary to provide correct contact information to the travellers.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Trip plan computation
---

>Such information may encompass the name and identification code of transport operators.

<table style="font-size: smaller; width: 100%;">
  <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td>OPERATOR</td>
    <td>A company providing public transport services. An OPERATOR may be associated with each scheduled SERVICE JOURNEY to indicate the organization advertised as responsible for its operation.</td>
  </tr>    
</table>

>BEST PRACTICES\
A distinction should be made between two types of OPERATORS:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• the Transport Service Provider (TSP) responsible for the contract with the customer;\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• the Transport Service Carrier (TSC) responsible for running the vehicle.\
Take the typical case of code-sharing for flights. A customer purchases a ticket from a given Airline (the TSP), and the flight is operated by another one (the TSC).\
In case of incident prior to the travel (e.g. flight cancelled or delayed), the contact point for the customer is the TSP. In case of incident during the travel (e.g. missed connection due to a delay in the arrival of the first flight or due to a cancellation of the connecting flight) the contact point for the customer is first the relevant TSC, but if no alternative is found the customer the liable company is the TSP.

>References/additional info: EN12896-1 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu)

