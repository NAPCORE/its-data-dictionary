---
id: trip-plan-computation_timetables
label: timetables
definition: (_scheduled transport modes_) the minimum information required for indicating the planned passing times of scheduled transport services’ vehicles, essential for trip plan computation purposes; (_on-demand transport_)<sup id="fn4">[4](#ref4)</sup> the minimum information required for indicating the operation times, hours of operation, geographical extend (zones, flexible stops), and further limitations of “dial-a-ride services”; (_vehicle pooling_) the minimum information required for indicating the scheduled transportation times, routes/lines (topology), and further limitations of vehicle-pooling.
category: Level of Service 1
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Trip plan computation
---

><u>For scheduled transport modes</u>: It is an aggregation of vehicle journeys (defined for specific day types) and passing times at stops for the concerned vehicle journeys.

><span id="ref4">[4]</span> The data category “demand-responsive”/ “transport on-demand” as per DR (EU) 2017/1926 (p. 11)/ DR (EU) 2024/490 (p. 10) covers more modes of transportation than Transmodel would address as demand responsive. E.g. vehicle-pooling (not only car) is not addressed as a part of demand responsive modes, but a separate category.  [↩](#fn4)

<table style="font-size: smaller; width: 100%;">
    <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
    </tr>
    <tr>
    <td>TIMETABLED PASSING TIME</td>
    <td>Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN<sup>5</sup> on a specified VEHICLE JOURNEY<sup>6</sup> for a certain DAY TYPE.</td>
    </tr>  
    <tr>
    <td>DATED PASSING TIME</td>
    <td>Time data concerning public transport vehicles passing a particular POINT, e.g., arrival time, departure time, waiting time on a particular OPERATING DAY and for a DATED VEHICLE JOURNEY<sup>7</sup>.</td>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;"><sup>5</sup> A SCHEDULED STOP POINT or TIMING POINT in a JOURNEY PATTERN (pattern of working for public transport vehicles) with its order in that JOURNEY PATTERN.</th>
    </tr>
    <tr>
    <td colspan="2" style="text-align: left;"><sup>6</sup> The planned movement of a public transport vehicle on a DAY TYPE from the start point to the end point of a JOURNEY PATTERN on a specified ROUTE.</th>
    <tr>
    <td colspan="2" style="text-align: left;"><sup>7</sup> A particular journey of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff.</th>
    </tr>
</table>

>BEST PRACTICES\
<u>For scheduled transport modes</u>, timetables must be provided in NeTEx format (part 1 and 2). To allow for European interoperability, they must adhere to the European Passenger Information Profile (EPIP; part 4) and/or to the European Passenger Information Accessibility Profile (EPIAP; part 6, under definition).\
In addition, to facilitate international/worldwide adoption, timetables should be provided in an aggregated form in GTFS format as well by the national access point. The main reason is that GTFS covers many use cases and is a lot simpler to consume than NeTEx.\
• In the context of this data category, vehicles are assumed to carry out specified vehicle journeys conforming to the schedule of availability conditions (specified as bitfields), including modifications possibly decided by the control staff of a transport operator. Based on the public transport reference data model (Transmodel), passing time information encompasses expected departure times, expected waiting times, and in some cases (partially on demand) earliest departure times, and latest arrival times.\
• The time horizon of the timetable is of importance. In some cases, booking occurs up to 120 days in advance.  So having a prospective time horizon of timetables of those 120 days would be idea and should be aspired to. However, the information must also be known in advance. The time horizon can be different according to the mode. For long distance trips 3 information can be obtained up to 3 months in advance, but other local-operated services can provide only 1 month in advance.\
• Coverage: timetable datasets should be as complete as possible for a given country or region. The degree of coverage/completeness should be declared per geographical region (e.g. country) in terms of percentages/fractions (e.g. “100 % of trains in country A are covered” and a description which modes, operators are missing.\
• Partitioning of files: if necessary (for data size or operational reasons), timetables of a country/region may be partitioned onto several files. It must be pointed out, that full XSD validation can’t be done in some of the following cases (reference-id checks). It is also very important, that merging the files is not necessarily easy (e.g. mixed lines, service journeys that exist in more than one file). The following divisions have been seen and ordered in the simplicity of parsing. Usually this creates redundancy or size problems. As the redundancy can’t always be avoided, importers must be able to identify identical copies (e.g. replicated stop place information when dealing with a line-oriented approach):\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o One file (network approach)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o Complete lines\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o Complete operators (and sometimes regions, but this might cause integration problems)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o Complete groups based on modes or mode groups\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o Site frame and lines without site in separate files\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o Files per (NeTEx) frame and multiple timetable frames.\
• File organization: within datasets, the data (XML files) should be organized in a simple and practicable way, with a moderate file size if feasible, allowing for handling in standard XML or text editors.\
• Datasets should be published in compressed form (ZIP archives).\
• File sizes: ZIP archives and files contained therein should have sizes smaller than 2 GB each.\
• Datasets should be provided via HTTPS (TLS) under permalinks, so that they may be retrieved easily and securely by automated scripts.\
• Cross-border services (e.g. international trains) may be included in datasets end-to-end but using whenever possible internationally harmonized/aligned identifiers.\
• Quality checks: datasets should be checked for well-formedness and validity (schema conformance) by the national access points. In the future, specific tools (converters/adaptors/validators) need to be available.\
• In addition to NeTEx (EPIP and/or EPIAP profiles), GTFS versions of the timetables may be provided as well. IDs in GTFS are equal to IDs in NeTEx, so data consumers can use the data best suited to the purpose of need.\
• Interchanges shall be used and supported. Remain seated must be supported. Transregional travel should use interchanges when multiple control systems are involved.\
• The data of each national access point should support the collating of transregional travel by interchanges, id for lines/journeys. Either artificial border points can be introduced, or the data should cover the first commercial stop abroad for outgoing journeys and last commercial stop for incoming journeys. It is better to be able to reference the other parts of the journey than to have to map it with timing information on stops.\
• Splitting, joining of trains should be supported. The splitting can be based on operational information (where there is always only one train on a block) or from the passengers’ point of view. One journey for each composition they can remain in it which is coupled on some blocks.\
• Direct carriages should be supported as well.\
• Equipment and equipment places are modelled. Facilities are shown.\
• Accessibility assessments are provided.\
• Leaving out the physical sites (STOP PLACE/QUAY) is possible, but not recommended. SCHEDULED STOP POINTs should refer to the physical model.  Modelling should be done on the Quay or sector level and not on the STOP PLACE level. Only then foot paths can be modelled correctly.\
• The data should support transfers based on time and paths.\
• The transport operators and their contact data should be up to date.\
• Notices and FacilitySets must be available for stops, parts of a service journey and a service journey.\
\
<u>For transport on demand</u>, offers must be provided in NeTEx format (part 1+2). Unfortunately, neither EPIP nor EPIAP currently deal with demand responsive traffic yet. An indication of how to implement can be found in the technical description used in Switzerland<sup id="fn8">[8](#ref8)</sup> (unfortunately currently only available in German).\
From a business perspective we point to the recent work in Switzerland referenced in further reading, which extends the previous work done in the VDV 462 standard.\
• For area services the areas should be clearly defined, and stops should be within those areas.\
• Booking conditions should be clearly defined.\
• No overlapping areas should exist. For complex spatial layouts multi-polygons should be used.\
• Simple, and clear offers from a user perspective that can be easily combined with other modes of transportation should be preferred.\
\
<u>For vehicle pooling</u>, offers must be provided in NeTEx format (part 5). Unfortunately, neither EPIP nor EPIAP deal with vehicle pooling.  A possible indication on how to do it (especially in GTFS) could be the analysis done in Switzerland<sup id="fn9">[9](#ref9)</sup>.\
• The mode of operation of operators should be clear.\
• Offers and demands should be provided to allow open matchmaking and thus an improved spatio-temporal coverage.\

><span id="ref8">[8]</span> See https://www.oev-info.ch/sites/default/files/2023-04/technisches_konzept_on-demand_v2.0.pdf [↩](#fn8)\
<span id="ref9">[9]</span> See https://www.xn--v-info-vxa.ch/sites/default/files/2024-01/vehicle_pooling_switzerland_v1.0.pdf [↩](#fn9)

>PROCEDURES\
<u>For all</u>:\
•	Timetable datasets (ZIP archives) should be generated on a regular periodic basis, at least weekly.\
•	Datasets must be quality-controlled (see best practices above).\
•	The data is aggregated.\
•	The id has to match the id in the real-time data.\
•	The interchanges in the real-time data should match the interchanges in the timetable data.

>DATA STRUCTURE\
<u>For scheduled transport</u>:\
Usually in this section the core data elements are listed. Timetables are a complex structure and EPIP/EPIAP as profiles cover most of it. But still EPIP and EPIAP have some flexibility in their implementation. Therefore, the following implementation restrictions should apply (the list is intended for readers that already studied EPIP and EPIAP):\
•	Use AvailabilityCondition with Bitfields.\
•	Use ResponsibilitySet for Authority and Operator at least.\
•	LineRef should be filled.\
•	Don’t rely on Route.\
As far as possible the concepts should be copied over to GTFS.\
<u>For on-demand transport</u>:\
The data structure for on demand can be taken from the NeTEx standard (part 5), which is no reiterated here. The same holds true for the GTFS-Flex and the VDV 462 standards.\
The previous work on business aspects of on demand done in Switzerland (see further reading) extends on the VDV 462 standard and content-wise constitutes a superset of GTFS Flex.\
<u>For vehicle-pooling</u>:\
As for on demand we do not reiterate the work in the NeTEx standard. Note the previous work in Switzerland which summarizes the unsuccessful approaches to modelling pooling, as well as the suggested extension to GTFS named GTFS pool to accommodate particularly for the smaller companies wanting exchange their offers and demands in a standardized manner.

>EXAMPLES\
<u>For scheduled transport</u>:\
• As valid examples use the EPIP and EPIAP examples on github: https://github.com/NeTEx-CEN/NeTEx/tree/master/examples/standards \
<u>For on-demand transport</u>:\
• As valid examples use the NeTEx examples on github: https://github.com/NeTEx-CEN/NeTEx/tree/master/examples/functions/timetable (e.g., zones)\
• Further examples can be found in the Swiss technical guide: https://www.öv-info.ch/sites/default/files/2023-04/technisches_konzept_on-demand_v2.0.pdf \
<u>For vehicle-pooling</u>:\
• As valid examples use the NeTEx examples on github: https://github.com/NeTEx-CEN/NeTEx/tree/master/examples/functions/newModes \
• Swiss concept for vehicle pooling: https://www.öv-info.ch/sites/default/files/2024-01/vehicle_pooling_switzerland_v1.0.pdf

>IMPLEMENTING SERVICES\
<u>For all</u>:\
•	Trip planners\
•	Ticket sales systems\
•	Station boards

>RELEVANT STANDARDS & LEGISLATION\
<u>For all</u>:\
• EU/1926/2017\
• NeTEx Parts 2 and 5\
<u>For scheduled transport</u>:\
• GTFS Schedule: https://gtfs.org/de/schedule/ \
<u>For on-demand transport</u>:\
• GTFS Flex: https://gtfs.org/extensions/flex/

>References/additional info: (_for scheduled transport_) EN12896-3 (see https://www.transmodel-cen.eu); CEN/TS 16614-2 (see https://netex-cen.eu); (_for on-demand transport_) CEN/TS 16614-5 (see https://netex-cen.eu); VDV 462 (see https://www.vdv.de/vdv-462-netex-schrift-v00-26d.pdfx?forced=true); Swiss business concept for On-Demand (see https://www.öv-info.ch/sites/default/files/2024-02/fachkonzept_on-demand_v2.0_en.pdf); (_for vehicle-pooling_) CEN/TS 16614-5, page 10 ff (see https://netex-cen.eu); Swiss concept for vehicle pooling: https://www.öv-info.ch/sites/default/files/2024-01/vehicle_pooling_switzerland_v1.0.pdf)

