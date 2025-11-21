---
id: detailed-common--fare-query_special-fare-products
label: special fare products (offers with additional special conditions such as promotional fares, group fares, season passes, aggregated products combining different products, and add-on products such as parking and travel, minimum stay)
definition: the minimum set of information about special fare products required for supporting fare queries.
category: Level of service 3
language: en
status: under review
source: DR_EU_2024-490
subcategory:
  - Detailed common standard and special fare query
  - for scheduled transport and transport on demand where relevant
---

>Special fare products are based on offers with additional special conditions, such as promotional fares, group fares, season passes, aggregated products combining different products and add on products (e.g., parking and travel, minimum stay).

<table style="font-size: smaller; width: 100%;">
    <tr>
        <th colspan="2" style="text-align: left;">Correspondence with Transmodel/NeTEx Concepts</th>
    </tr>
    <tr>
        <th colspan="2" style="text-align: left;">Special fare products</th>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">The different validity and usage limitation parameters are presented above. In particular, the usage limiting parameters (USAGE PARAMETERS) express specificities of certain access rights (FARE PRODUCTS).</td>
    </tr>
    <tr>
        <td>USAGE PARAMETERS</td>
        <td>Allow detailed limitations on use to be specified:<br>
        o RESIDENTIAL QUALIFICATION: A parameter providing an authorisation to consider a user as being characterised by a USER PROFILE.<br>
        o COMPANION PROFILE: The number and characteristics of the persons entitled to travel in a group or as companions to another USER PROFILE.<br>
        o GROUP TICKET: The number and characteristics of persons entitled to travel in addition to the holder of an access right.</td>
    </tr>
    <tr>
        <th colspan="2" style="text-align: left;">Combined products</th>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">Combined access rights: several different access rights may be combined into a single access right, for example a smartcard that providing the right to travel in a specific zone and a discounted travel using value stored on the card for other zones. Another typical example is the access to a parking for a certain time followed by the access to a transport network. Such combined FARE PRODUCTs are considered a FARE PRODUCTs in their own right. Transmodel/NeTEx expresses the combination of the parameters determining the validity of such combined FARE PRODUCTs. Such combinations are often resulting from contracts between product owners/operators and allow for a special price (when used as combinations and not separately). The combined access rights are considered as FARE PRODUCTs in their own right an have to be validated in one go (as one single access right).</td>
    </tr>
    <tr>
        <td>VALIDABLE ELEMENT</td>
        <td>A sequence or set of FARE STRUCTURE ELEMENTs, grouped together to be validated in one go.</td>
    </tr>
    <tr>
    <tr>
        <th colspan="2" style="text-align: left;">Offer packages</th>
    </tr>
    </tr>
    <tr>
        <td>SALES OFFER PACKAGEs</td>
        <td>Combine one or more FARE PRODUCTs with information on the materialisation (as paper ticket, electronic ticket, etc.) and distribution:<br>
        o A TYPE OF TRAVEL DOCUMENT specifies the media used (paper, app, smartcard, etc.)<br>
        o Where to purchase and collect a product can be specified using DISTRIBUTION CHANNELs, FULFILMENT METHODS<br>
        o Means of payment (cash, credit card) can be specified as a TYPE OF PAYMENT METHOD<br> 
        o FARE PRODUCTs can also be used to define add-on products such as seat reservations, cycle tickets, parking, etc. Such FARE PRODUCTs can be sold separately or bundled into a SALES OFFER PACKAGE with other access rights.</td>
    </tr>
    <tr>
        <th colspan="2" style="text-align: left;">Pricing</th>
    </tr>
    <tr>
        <td colspan="2" style="text-align: left;">The Price MODEL provides the necessary parameters (pricing parameters) for the calculation of the exact price of an access right (FARE PRODUCT) based on the atomic FARE PRICEs of the different parameters determining a FARE PODUCT.</td>
    </tr>
    <tr>
        <td>PRICE GROUPs</td>
        <td>Allow for a grouping of prices, allowing the grouping of numerous possible consumption elements into a limited number of price references, or to apply grouped increase, in value or percentage.</td>
    </tr>
    <tr>
        <td>PRICING RULE</td>
        <td>A rule used for the calculation of FARE PRICE, determined either by a set of parameters to be applied to a reference price or by a more complex algorithm. PRICING RULEs may be chained together.</td>
    </tr>    
</table>

>References/additional info: EN12896-5 (see www.transmodel-cen.eu); CEN/TS 16614-3 (see https://netex-cen.eu/)

