---
id: detailed-common--fare-query_common-fare-products
label: common fare products (access rights such as zone/point-to-point including daily and weekly tickets/single/return, eligibility of access, basic usage conditions such as validity period/operator/time of travel/interchanging, standard point-to-point fares prices for different point-to-point pairs including daily and weekly fares/zonal fare prices/flat fare prices)
definition: the minimum set information about common fare products required for supporting fare queries.
category: Level of service 3
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Detailed common standard and special fare query
  - for scheduled transport and transport on demand where relevant
  
---

>Provided information may be classified based on tariff offers and access rights (e.g., zone/point-to-point weekly/single/roundtrip tickets) as well as the eligibility of access and basic usage conditions (e.g., valid period/operator/time of travel interchanging, standard point-to-point fare prices for different point-to-point pairs including daily and weekly fares/zonal fare/flat fare).\
The prices may be absolute or derived from other prices.

<table style="font-size: smaller; width: 100%;">
    <tr>
        <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Parameters determining the sales offer, i.e., the set of main FARE PRODUCTs and their parameters.</td>
    </tr>
    <tr>
        <td>FARE PRODUCT</td>
        <td>An immaterial marketable element (access rights to travel or use other services, discount rights to buy products at a discount, etc.), specific to a CHARGING MOMENT<sup>14</sup>.</td>
    </tr>
    <tr>
        <td>Types of FARE PRODUCTs</td> 
        <td>Transmodel/NeTEx distinguishes different types of products:<br>
        &nbsp;&nbsp;&nbsp;o PRE-ASSIGNED FARE PRODUCT: Specific access rights to travel either on a specific trip or repeatedly on a pass.<br>
        &nbsp;&nbsp;&nbsp;o	AMOUNT OF PRICE UNIT: Stored value to travel a certain amount.<br>
        &nbsp;&nbsp;&nbsp;o	SALE DISCOUNT RIGHT: A product that gives the right to buy or consume travel at a discount.</td>
    </tr>
    <tr>
        <td>ENTITLEMENT PRODUCT</td>
        <td>A precondition to access a service or to purchase a FARE PRODUCT expressed as another product. Issued by an organisation that may not be a PT operator (e.g., military card, travel discount card).</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">The FARE PRODUCTs are characterised by a range of validity and usage limitation parameters.
    </tr>
    <tr>
        <td>TEMPORAL VALIDITY PARAMETERS</td>
        <td>Grouping of time-related parameters defining the validity of access rights.<br>
        &nbsp;&nbsp;&nbsp;o	VALIDITY CONDITION<br>
        &nbsp;&nbsp;&nbsp;o	SERVICE CALENDAR<br>
        &nbsp;&nbsp;&nbsp;o	DAY TYPE<br>
        &nbsp;&nbsp;&nbsp;o	OPERATING DAY<br>
        &nbsp;&nbsp;&nbsp;o	TIME BAND</td>
    </tr>
    <tr>
        <td>SCOPING VALIDITY PARAMETERS (ORGANISATIONAL/NETWORK/ROUTING/FARE/SERVICE VALIDITY PARAMETERS</td>
        <td>Space- and organisation-related parameters defining the validity of access rights</td>
    </tr>
    <tr>
        <td>USAGE PARAMETERS</td>
        <td>Parameters used to specify/limit the use of a SALES OFFER PACKAGE or a FARE PRODUCT:<br>
        &nbsp;&nbsp;&nbsp;o travel usage parameters, such as MINIMUM STAY, ROUND TRIP, etc;<br> 
        &nbsp;&nbsp;&nbsp;o eligibility parameters, such as USER PROFILE, GROUP TICKET, etc;<br>
        &nbsp;&nbsp;&nbsp;o entitlement parameters, such as ENTITLEMENT REQUIRED);<br>  
        &nbsp;&nbsp;&nbsp;o luggage usage parameters, such as LUGGAGE ALLOWANCE;<br> 
        &nbsp;&nbsp;&nbsp;o booking usage parameters, such as PURCHASE WINDOW, RESERVING, CANCELLING;<br> 
        &nbsp;&nbsp;&nbsp;o after sales usage parameters, such as REFUNDING, REPLACING, EXCHANGING, TRANSFERABILITY, etc;<br> 
        &nbsp;&nbsp;&nbsp;o charging usage parameters, such as PENALTY POLICY, CHARGING POLICY, SUSCRIBING.</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Some FARE PRODUCTs may be characterised by a possibility to change the normal access rights given to a passenger because of a disruption (possibility of a FARE EASEMENT).</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">The elements of a fare offer are PRICEABLE OBJECTs (element which may have a FARE PRICE i.e. price features).</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">The Price MODEL provides the necessary parameters (pricing parameters) for the calculation of the exact price of an access right (FARE PRODUCT) based on the atomic FARE PRICEs of the different parameters determining a FARE PODUCT.</td>
    </tr>
    <tr>
        <td>PRICING RULE</td>
        <td>A rule used for the calculation of FARE PRICE, determined either by a set of parameters to be applied to a reference price or by a more complex algorithm. PRICING RULEs may be chained together.</td>
    </tr>    
    <tr>
        <td colspan="2" style="text-align: left;"><sup>14</sup> A classification of FARE PRODUCTs according to the payment method and the account location: pre-payment with cancellation (throw-away), pre-payment with debit on a value card, pre-payment without consumption registration (pass), post-payment etc.</td>
    </tr>
</table>

>References/additional info: EN12896-5 (see www.transmodel-cen.eu); CEN/TS 16614-3 (see https://netex-cen.eu/)

