---
id: location-search_points-of--to-travel
label: points of interest (related to transport information) to which people may wish to travel
definition: the minimum information required for matching specific locations of interest (e.g., amenities, landmarks, tourist attractions) as trip origins and destinations (covers DR(EU)1926/2017 1.b.c).
category: Level of Service 1
language: en
status: finalised
source: DR_EU_2024-490
subcategory:
  - Location search (origin_destination)
---

## NOTES

The coordinates and/or address identifiers of any point of interest (POI) that are relevant to travellers. For example, a museum, a theatre, or a shopping mall. The following POI should be (at least) provided: 

- Administrative buildings 
- Airports 
- Amenities (such as shopping mall, restaurants) 
- Hospitals 
- Museums, tourist attractions 
- Pharmacies 
- Police stations 
- Ports 
- Protected sites 
- Rental stations (unless they are car-sharing and/or bike-sharing stations which would be out of the scope of this data type and taken into their own data types described under level of service 2). 
- Universities, schools 

<table style="font-size: smaller; width: 100%;">
  <tr>
    <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
  </tr>
  <tr>
    <td>POINT OF INTEREST</td>
    <td>A type of PLACE to or through which passengers may wish to navigate as part of their journey and which is modelled in detail by journey planners.</td>
  <tr>
    <td colspan="2" style="text-align: left">Transmodel/NeTEx provides a model for a generalized classification system that allows a point of interested to be assigned to one or more categories (POINT OF INTEREST CLASSIFICATIONs) and the categories themselves to be organized into hierarchies (POINT OF INTEREST CLASSIFICATION HIERARCHY).</th>
  </tr>
</table>

## BEST PRACTICES

Be aware that there might exist temporary POI as well (e.g. a circus). 
Be aware that some locations are considered as input to trip planners but are not POI in the narrower sense. They are also not modelled as POI, but should still contain the relevant information in their respective data types (e.g. stations, charging stations, parking): 
 
- Parking (see section on parking) 
- Park & Ride (all vehicles), kiss & ride: covered under “location search – for transport on demand and personal transport: Park & Ride stops” 
- Heavy vehicle parking: covered under DR EU 885/2013 “provision of information services for safe and secure parking places for trucks and commercial vehicles” 
- Charging stations, gas stations (personal operated vehicles): covered under DR EU 2022/670 “provision of EU-wide real-time traffic information services” 
- Public transport stops (see section on stops) 

### PROCEDURES 

- The data must follow NeTEx Part 4 (EN 12896-4, European Passenger Information Profile, EPIP) in the structure for the data export. 
- An export as Open Journey Planner (OJP) Location Information is also possible (TS17118, version 2). 
- The data must be actualized at least once a year. In the ideal case any update to a POI (content, existence, coordinates) should be available on the following day. 
- The POI are synchronized with the ones in readily available geobases (e.g. OpenStreetMap) and the national geobases. 

### DATA STRUCTURE 

The following data define a point of Interest: 

- Mandatory:
  - Identifier (must be globally unique): The identifier that is used afterwards in all other data. 
  - Name 
  - Coordinates (Centroids): A version in WGS84 is mandatory. A local projection can be added. 
  - Category or classification: There can be multiple classification systems used. It is recommended that at least the OSM map feature [classification][1] is supported.
- Recommended: 
  - External references (e.g., for OSM or a national GeoBase): This helps in using the POI in the diverse world we have. 
  - Source: A reference to the source of the data. 
  - Topographic or address identifiers: If such id exist, they should be provided. 
  - Access and egress points to the road network (doors and gates) – with coordinates: For bigger structures they are needed.
- Optional: 
  - Area: Some POIs are big and the area covered is of importance. 
  - Validity: If a POI is valid only for a given period. This data can be provided. 
  - Opening hours 

[1]: https://wiki.openstreetmap.org/wiki/Map_features

### EXAMPLE: NeTEx - [tour d’Eiffel][2]

```xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.netex.org.uk/netex file:///C:/Users/ue71603/MG_Daten/github/NeTEx1/xsd/netex_publication.xsd">
  <PublicationTimestamp>2024-05-18T18:12:00</PublicationTimestamp>
  <ParticipantRef>MMTIS-Test</ParticipantRef>
  <dataObjects>
    <CompositeFrame id="cf" version="1.0">
      <frames>
        <SiteFrame id="sf" version="1.0">
          <pointsOfInterest>
            <PointOfInterest id="fr:PointOfInterest:1881-12-122-9" version="1.0">
              <keyList>
                <KeyValue>
                  <Key>OSM</Key>
                  <Value>5013364</Value>
                </KeyValue>
              </keyList>            
              <privateCodes>
                <PrivateCode>fr:monuments:1831812</PrivateCode> <!--main identifier -->
              </privateCodes>
              <Name>Tour d'Eiffel</Name>
              <Centroid>
                <Location>
                  <Longitude>48.85822</Longitude>
                  <Latitude>2.2945</Latitude>
                </Location>
              </Centroid>
              <AccessibilityAssessment id="fr:AccessibilityAssessment:181-31-31-221" version="1.0">
                <MobilityImpairedAccess>true</MobilityImpairedAccess>
              </AccessibilityAssessment>
              <Landmark>true</Landmark>
              <PublicUse>all</PublicUse>
              <AllAreasWheelchairAccessible>true</AllAreasWheelchairAccessible>
              <TopographicPlaceRef ref="fr:TP:183819-1231"/>
              <AuthorityRef ref="CityOfParis"/>
              <entrances>
                <EntranceRef ref="fr:Entrance:12312319871"/>
              </entrances>
              <localServices>
                <AssistanceServiceRef ref="fr:AssistanceService:18381923191-123"/>
              </localServices>
              <classifications>
                <PointOfInterestClassificationRef ref="fr:PoIC:monument" version="1.0"/>
              </classifications>
            </PointOfInterest>  
          </pointsOfInterest>
          <pointOfInterestClassifications>
            <PointOfInterestClassification id="fr:PoIC:monument" version="1.0">
              <privateCodes>
                <PrivateCode type="OSM">historic:monument</PrivateCode>
              </privateCodes>
              <Name>National Monument</Name>
              <Description>National monument</Description>
            </PointOfInterestClassification>
          </pointOfInterestClassifications>
        </SiteFrame>
      </frames>
    </CompositeFrame>
  </dataObjects>
</PublicationDelivery>
```

[2]: https://www.openstreetmap.org/way/5013364#map=19/48.85826/2.29451

### IMPLEMENTING SERVICES 

- Journey Planners 
- Geocoders 

### RELEVANT STANDARDS & LEGISLATION 

- EU/1926/2017 
- EU/885/2013 
- EU/40/2010 

## References/additional info

EN12896-2 (see see www.transmodel-cen.eu); CEN/TS 16614-1 (see https://netex-cen.eu); https://publications.jrc.ec.europa.eu/repository/handle/JRC118744 This report clarifies that INSPIRE can be considered as reference standard only for a limited set of POI categories (Utilities and Governmental Services (US), Buildings (BU), and Protected Sites (PS)), each of which has its own specific data model.

[View Code Sample](../assets/code/location-search_points-of--to-travel_snippet_1.xml)
