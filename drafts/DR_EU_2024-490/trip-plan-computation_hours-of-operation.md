---
id: trip-plan-computation_hours-of-operation
label: hours of operation
definition: the minimum information required for indicating the time validity – hours of operation of scheduled or on demand transport services, essential for trip plan computation purposes.
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
    <td>AVAILABILITY CONDITION</td>
    <td>A VALIDITY CONDITION expressed in terms of temporal parameters and referring to DAY TYPEs. </td>
  </tr>
      <tr>
    <td colspan="2" style="text-align: left;">The use of DAY TYPEs (which may include TIMEBANDs) allows the time validity to be characterized precisely. This can be resolved in a precise calendar date and time by means of a DAY TYPE ASSIGNMENT.</th>
    </tr>
</table>

>BEST PRACTICES\
• Each scheduled journey has a precise date and time of operation.\
• Hours of operations may refer to:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o The time of starting services and time of closing services (e.g. for local public transport which may propose timetables, but also only headways per period of the day).\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o They may refer to DAY TYPEs for long distance bus and rail services.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o They may refer to long periods in case of air travel (low-cost airlines may operate only part of the year).\
• For on-demand transport it is necessary to provide information on the time between ordering a trip and the time of actual start of the trip, and the trip time computation in itself is a two steps process. 

>References/additional info: EN12896-1 (see https://www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu)

