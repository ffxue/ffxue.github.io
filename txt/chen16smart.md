# **Smart Gateway for Bridging BIM and Building** 

K. Chen*, W.S. Lu, F. Xue, L.Z. Zheng and D.D. Liu 

Department of Real Estate and Construction, The University of Hong Kong, Pok Fu Lam, 

Hong Kong 

leochen@connect.hku.hk, {wilsonlu, xuef, lizzheng, liudd}@hku.hk 

This is the author’s copy of the conference paper: Chen, K., Lu, W.S., Xue, F., Zheng, L.Z., Liu, D.D. (2018). Smart Gateway for Bridging BIM and Building. In: Chau, K., Chan, I., Lu, W., Webster, C. (eds) _Proceedings of the 21st International Symposium on Advancement of Construction Management and Real Estate_ . Springer, Singapore. Full version: http://doi.org/10.1007/978-981-10-6190-5_15. 

## **Abstract** 

Building information modeling (BIM) has been emerging as a digital platform to create, exchange, and manage the information in a construction project. Over the past decades, researchers have explored various techniques, including laser scanning and sensing devices, to keep the BIM up-to-date. Their efforts have been conceptualized as bridging BIM and building (BBB). In the BBB framework, a key component is the smart gateway which is the middleware to ensure information input/out between the physical project layer and the BIM layer. The aims of this research is multifold: (1) to highlight the importance of smart gateway for BBB; (2) to generate the definition of the smart gateway based on existing gateways in other industries; and (3) to describe the essential functions of the smart gateway based on the BBB framework. Theoretically, with four major functions including device configuration and management, data filtering and processing, temporary information storage, and supplementary information input, the proposed smart gateway can significantly facilitate the integration between the physical project information with BIM. Future research will be conducted to develop and implement a prototype of the smart gateway in actual construction projects where multi data-acquisition devices are used. 

## **1 Introduction** 

The architecture, engineering, and construction (AEC)industry has long been characterized as highly fragmented and data intensive. The inadequate provision of information in a construction project has been recognized as a factor that results in poor project performance. In order to overcome such problem, building information modeling (Bl) has emerged as a digital platform to create, exchange, and manage the project relevant information. In 2016, Timetric's Construction Intelligence Center (CIC)conducted a survey of more than 100 participants in the global construction industry. The results showed that 49% of the respondents are currently using BlM, and another 10% of the respondents plan to use BIM within one year(CIC 2016). 

Across project stages, BIM should be continuously updated so that stakeholders can analyze actual against expected performance in a real-time manner (Tserng et al. 2014). 0therwise, BlM will be “blind and deaf, that cannot support decision-making. Many researchers have explored methods or technologies for synchronizing the BIM information with the project process. Their efforts have been conceptualized by Chen et al. (2015) as bridging BIM and building (BBB). In the conceptual framework of BBB, information about various aspects of a construction project is collected by advanced technologies including laser scanner, sensors, and Auto-ID devices. With the real-time information, BIM can support a series of project management practices, such as cost management, schedule management, and material management. Since it is not feasible to directly import the raw data in BIM, the smart gateway — the middleware between the physical project layer and the BIM layer — is of great importance to ensure information integration between the two layers. 

This study aims at exploring the smart gateway for BBB. It firstly reviews previous studies on information required at construction and O&M stages. Then, based on the theoretical framework of BBB, the importance of the smart gateway is highlighted. Finally, major functions of the proposed smart gateway are described in details. 

## **2 Information Requirements at Construction and O&M Stages** 

The management of a construction project involves using available information to make a web of decisions across the project life cycle (Flanagan and Lu 2008). The information needed by different stakeholders varies from stage to stage. Ndekugri and McCaffer (1988) summarized the contractors’ inputs and outputs of information for planning, estimating, cash flow forecasting, valuations, cost control, and accounting. Ergen et al. (2007) analyzed the information flow patterns for management of prefabricated components at production, construction, and O&M stages. 

Becerik-Gerber et al. (2011) summarized the data requirements for facilities management. A simplified summary of information requirements at construction and O&M stages is presented in Table 1. 

**Table 1** Information requirements 

|Stage|Information requirements||
|---|---|---|
||Geometry information|Non-geometry<br>information|
|Construction|Site information (coordinate’s data and|Construction materials (status, quality,|
||layout)|category, manufacturer)|
||Building spaces (floor, zones, rooms,|Precast elements (quality, category,|
||openings)|manufacturer)|
||Utility lines|Equipment attributes (ID, type, status)|



2 

||Dimension of building components|Financial data<br>Location of labor, materials, and machine<br>Project performance data<br>Construction schedule<br>Construction activity status<br>Site environment|
|---|---|---|
|Operation|Building services (location,|Building services (identification number,|
|and|relationship)|manufacturer)|
|maintenance|Building spaces (floor, zones, rooms,<br>openings)|Status of mechanical, electrical, and<br>plumbing equipment|
||Utility lines|Maintenance record|
||Specification of exterior enclosure|Indoor environment|
||products|Attributes of replaced components|
||Furnishing|Maintenance status|
|||Maintenance schedule|
|||Operation records|



Most of the geometry and non-geometry information listed in Table 1 is dynamic. For example, the status of construction materials changes from “produced” to “being delivered”, and then to “arrived at the construction site”. Another example is the change in the dimension of building components (e.g. a wall or column) due to the design variations. Therefore, in a project where BIM is used, the original BIM developed at the design stage can be easily outof-date. Real-time information should be timely collected to update the original BIM, based on which, stakeholders can monitor the project performance and make adjustments when it is necessary. 

## **3 Concept of Bridging BIM and Building** 

Bridging BIM and building (BBB) is defined as connecting the information contained in BIM with physical building processes to make BIM reflecting the actual situations (Chen et al. 2015). Here, “reflecting the actual situations” does not mean that all information about a construction project must be contained in BIM. The discussion on the usefulness of an “ever more complete/complex” BIM falls beyond the theme of this study. Technically, BIM is capable of containing nearly all types of project information, while stakeholders can determine which information should be involved and updated according to their own requirements. 

Generally, BBB is performed by following procedures: (1) developing the initial BIM; (2) determining which parts of the original BIM need to be updated; (3) collecting the required information along the project process; (4) managing and processing the collected information; and (5) updating the original BIM with the processed information. Except for the first two steps, entirely relying on manual efforts to finish the remaining three steps is 

3 

time-consuming and error-prone. Thanks to advanced technologies, procedures of BBB, especially for information collection and process, can be performed with considerable efficiency and effectiveness. 

For geometry information, laser scanning and photogrammetry are two widely-used technologies to capture the as-built information. An example is given by Bosché et al. (2013) that a scan-vs-BIM method is proposed to integrate point clouds and BIM. The scanned point clouds are first aligned in the coordinate system of the model. Then, the comparison between point clouds and BIM helps to check variation and project process. Both laser scanners and cameras can be fixed on an unmanned aerial vehicle (UAV) to rapidly capture the construction site information from height. GIS is the computer system that has the potential for capturing, storing, checking, and displaying spatial data. 

Laser scanning and photogrammetry can also be used to collect the non-geometry information such as the location of construction resources (e.g. equipment, machinery, material, building components). Besides, GPS is satellite-based for getting the position and navigation of construction objects and activities (Pradhananga and Teizer 2013). Auto-ID technologies including barcode and radio frequency identification (RFID) enable rapid tracking and tracing (Lu et al. 2011; Flanagan et al. 2014). Once being attached to a construction resource, the unique ID contained in the RFID tag or barcode can help to link the information of that construction resource to its digital representation in BIM. Sensors can capture the information about the site and indoor environment. With an integration of sensing technologies, Niu et al. (2015) even proposed smart construction objects which can automatically collect and report their own information. 

## **4 Requirements for the Smart Gateway** 

Currently, after the real-life project information is collected, the most common methods for its integration with BIM are direct input, hyperlink, application programming interface (API) and schema extension. Goedert and Meadati (2008) added new shared parameters (e.g. specifications, RFI, shop drawings) to the components in BIM. The values of these parameters are hyperlinks that help stakeholders to find the documents of a specific component. Motamedi et al. (2016) extended the IFC schema to include the definition of RFID technology components in BIM. Standardized definitions for RFID components can be used to map the data to be stored in RFID memory to the associated entries in a BIM database. Solihin et al. (2016) introduced a concept of deferred references to the IFC schema, with which, partial models will remain integrated when they are inserted into federated models. 

4 

Using these methods, the project information can be manually or semi-automatically “placed” in BIM environment. However, they are not sufficient for the integration of BIM and realtime project information. To fully achieve BBB, a middleware between the physical project and BM is important due to the following reasons. 

Firstly, raw data collected by data-acquisition technologies contains much irrelevant data and noise to be filtered, and its format can be various. Directly importing all raw data into BIM will not only make the model cumbersome, but also lead to troublesome preparation works (e.g. searching, filtering, and converting) when stakeholders would like to use BIM for decision making. Therefore, the raw data should be processed before being imported in BIM. 

Secondly, some collected information is related to the entire project, while others can be related to a single space or an individual building resource. Preparatory works are needed to link the physical project and its components with the right part (s) in BIM. Without a preidentified link, manually searching among the collected information and then selecting the corresponding part(s) of BIM for information update is very likely to be time-consuming and error-prone. 

Thirdly, researchers have noted that single technologies may not able to collect all types of information required for BIM update (Akanmu et al 2014; Akanmu and Anumba 2015). Some technologies should be configured with the right set of API for information retrieve. Besides, the working status of the data-acquisition technologies should be monitored to ensure information collection. 

Fourthly, the communication network may not be always available at the dynamic construction site. When a large amount of information is transferred to BIM along with the project process, a more stable channel is essential to decrease information loss. 

## **5 Definition of the Smart Gateway: An Analogy** 

The smart gateway for BBB is inspired by gateways in many other industries. Generally, a gateway is a link between two programs or systems for information sharing. In telecommunication, gateway is a piece of hardware such as protocol translators and signal translators to provide interoperability (Chen et al. 2010). In network, gateway is a node on a TCP/IP network that serves as an access point to another network. In the field of Internet of Thing (IoT) and smart building/housing, gateway provides the bridge between devices in the physical world, the cloud, where data is collected, stored and manipulated by enterprise applications and the user equipment. In manufacturing, Huang et al. (2011) proposed a gateway as the sandwiched layer between enterprise information system (EIS) and smart object services. Their proposed gateway is used to: (1) connect and host a set of RFID- 

5 

enabled objects; (2) communicate and interact with EIS and decision support system; (3) process and exchange real-time data; (4) provide facilities for service definition and configuration. 

It can be seen that even though the definitions of gateways in various industries are not completely the same, the key function is to ensure the information flow among different protocols and devices. In the context of bridging BIM and building, we define the smart gateway as “the middleware platform that centrally connects the data acquisition technologies and provides mechanisms for processing the collected information to facilitate information integration between the physical project and BIM”. As shown in Fig. 115.1, gateway communicates with data acquisitions technologies and the digital databases by wired or wireless networks. The smart gateway can be stationary and mobile. The stationary gateway is placed at a designated place, while the mobile gateway can be held by stakeholders to perform its function. These two types of smart gateway can be corporate with different data acquisition technologies. For example, the stationary gateway can be permanently linked with sensors placed at a fixed location; the mobile gateway is suitable to work with hand-held Auto-ID readers. 



<!-- Start of picture text -->
= = => a<br>_—a lz —a 1<br>3 = = ae oR ih.<br>n_ _ a noe<br>Digital databases<br>| Wired/wireless networks<br>Stationary and mobile smart gateway<br>| Wired/wireless networks<br>Laser Auto-ID LJ Sensor ky _ Photo- OL!<br>scanner (RFD, barca, QR} agg | (OPS, Tenet, grammetry<br>Data acquisition technologies<br><!-- End of picture text -->

**Figure 1** Architecture of smart gateway 

If we consider the database as a reservoir, the data/information will be the water stored in that reservoir. There are many tubes for water input/output (I/O). The role of smart gateway will 

6 

be managing all the tubes and administrating the water input/output. When the water enters the reservoir through the input tube, it should be clarified and classified so that it can be stored in the right place. When the water needs to be exported, the output tube should point to the correct destination. Besides, the working status of individual tubes should also be monitored to maintain the water flow. 

## **6 Functions of the Smart Gateway** 

Basically, the smart gateway has the following four functions: (1) device configuration and management; (2) data filtering and processing; (3) temporary information storage; and (4) additional information input. As shown in Fig. 115.2, some of these functions are interrelated with each other. 



<!-- Start of picture text -->
API Software<br>Algorithm User<br>Device configuration and<br>management Data filtering and processing<br>Gateway) | time | |Material i a<br>Identifier | .<br>r ) rp a | Cache2 |<br>v Y | Lb<br>oe Temporary information<br>Information input storage<br>Smart Gateway<br><!-- End of picture text -->

**Figure 2** Functions of smart gateway 

## **_115.6.1 Device Configuration and Management_** 

The Auto-ID device and sensors entail different software drivers and invoking 

standards/protocols provided by their vendors. Taking RFID devices as an example, the same reading function of RFID readers may require different APIs (Fang et al. 2013). The APIs of different devices are stored at the gateway, where they are grouped by their brands. When 

7 

different brands of Auto-ID technologies are used in a single project, they can be connected with the smart gateway, and the right set of API will be called to enable the reading and writing functions. 

When sensing devices such as the GPS sensor and the temperature sensor are fixed on construction resources or building components, they are configurated by the smart gateway for two purposes: (1) users can set the interval for each time of data collection; (2) users can monitor their working status and check whether there is information collected. 

## **_115.6.2 Data Filtering and Processing_** 

Even to the same type of data-acquisition devices, their collected data could have distinct messaging protocol and format if their brands are different. Before transferring the data into the database, the smart gateway will filter and process the raw data. These mechanisms guarantee that the collected data can be presented in the required form. The raw point cloud generated by laser scanning and photogrammetry can be hundred megabytes to gigabytes with many noisy data. Directly importing it into the database could be a waste of resources for transfer and storage. The raw point cloud should be filtered, and be arranged into a predefined coordinate system in order to keep the coordinate system of all scanned data consistent. For RFID technologies, the tag could contain diverse types of information. When a tag attached to the construction resource is scanned to record relevant information of that resource, the reader will send several types of information to the gateway. Among the retrieved data, the EPC code is usually needed since it is the unique ID for identification, while other information could be filtered to avoid information redundancy. 

## **_6.3 Temporary Information Storage_** 

Regardless of being stationary or mobile, caches can be provided in the smart gateway for temporary information storage. The data-acquisition devices and smart gateway are communicated by cable, USB, and Bluetooth at a near distance. Therefore, it is relatively stable for the smart gateway to receive the collected raw data. However, it is possible that there is no communication network for the smart gateway to access the database for information upload. For example, the worker takes a RFID reader that is connected to a mobile smart gateway to check the installation of a prefabricated façade. After confirmation, installation information should be transferred to the database in order to update the status of the digital component in BIM. However, the network signal is too weak to transfer the information. The smart gateway will hold that information until the network signal becomes strong enough. The provision of temporary information storage helps to decrease the chance of information loss. 

8 

## **_6.4 Information Input_** 

As mentioned in Sect. 115.4, the collected information can be related to the whole project or individual construction resources. In the smart gateway, the received information will be virtually linked with a pre-defined ID which represents the different part(s) of BIM (e.g. individual components, space, and entire project) before it is transferred to the database. This helps to group relevant information throughout the project process. 

Additionally, the smart gateway provides a user-interface for stakeholders to input supplementary information. For laser scanning and photogrammetry, information such as the time of each scan or photo-taking and the responsible person can be recorded. For Auto-ID technologies, along with the project process, the scan of Auto-ID tag will show its attached resource in the user-interface of the smart gateway where the stakeholder can input relevant information about that resource. 

## **7 Conclusion** 

Building information modeling (BIM) would be an ideal platform to support decision making if it synchronized with the physical project to reflect the actual situation. Considerable efforts have been taken to use advanced data-acquisition technologies to collect the real-time project information and update the original BIM. This process has been conceptualized as bridging BIM and building (BBB). The BBB framework consists of physical project layer, smart gateway, database, and BIM layer. Compared with the other three layers, less attention has been paid to the smart gateway. This paper provides the concept of smart gateway, and comprehensively discusses functions of the smart gateway for BBB. 

As the middleware between physical project layer and BIM layer, the smart gateway guarantees the information flow between these two layers by its four main functions, namely, configuring different data-acquisition technologies, filtering and processing the collected raw data, temporarily storing information when the communication network between the smart gateway and the database is interrupted, and allowing information input by users. 

In future research, a prototype of the smart gateway will be developed and implemented in actual construction projects where multi data-acquisition devices are used. Such case study will validate the ability of smart gateway to deal with the heterogeneous BBB technologies before the information is stored in the database and transferred to BIM. 

9 

## **Acknowledgements** 

This study is supported by the General Research Fund (Project No.: 17205614) of the Hong Kong Research Grant Council (RGC). 

## **References** 

- Akanmu A, Anumba CJ (2015) Cyber-physical systems integration of building information models and the physical construction. Eng Constr Archit Manage 22(5):516–535 

- Akanmu A, Anumba C, Messner J (2014) Critical review of approaches to integrating virtual models and the physical construction. Int J Constr Manage 14(4):267–282 

- Becerik-Gerber B, Jazizadeh F, Li N, Calis G (2011) Application areas and data requirements for BIM-enabled facilities management. J Constr Eng Manage 138(3):431-442 

- Bosché F, Guillemet A, Turkan Y, Haas CT, Haas R (2013) Tracking the built status of MEP works: assessing the value of a scan-vs-BIM system. J Comput Civ Eng 28(4):05014004 

- Chen K, Lu W, Peng Y, Rowlinson S, Huang GQ (2015) Bridging BIM and building: from a literature review to an integrated conceptual framework. Int J Proj Manage 33(6):1405– 1416 

- Chen Y, Shen W, Huo H, Xu Y (2010) A smart gateway for health care system using wireless sensor network. In: 2010 Fourth international conference on sensor technologies and applications (SENSORCOMM), IEEE, pp 545–550 

- Construction Intelligence Center (CIC) (2016) Building information modeling to become future of construction industry. http://www.construction-ic.com/pressrelease/buildinginformation-modeling-to-become-future-of-construction-industry-4941964. Accessed 16 July 2016 

- Ergen E, Akinci B, Sacks R (2007) Life-cycle data management of engineered-to-order components using radio frequency identification. Adv Eng Inform 21(4):356–366 

- Fang J, Qu T, Li Z, Xu G, Huang GQ (2013) Agent-based gateway operating system for RFID-enabled ubiquitous manufacturing enterprise. Robot Comput Integr Manuf 29(4):222–231 

- Flanagan R, Lu WS (2008) Making informed decisions in product-service systems. In: IMechE conference, knowledge and information management through-life, Institute of Mechanical Engineers 

- Flanagan R, Jewell C, Lu W, Pekericli K (2014) Auto-ID—bridging the physical and the digital on construction projects. Chartered Institute of Building. ISBN 1853800191 

- Goedert JD, Meadati P (2008) Integrating construction process documentation into building information modeling. J Constr Eng Manage 134(7):509–516 

- Huang GQ, Qu T, Fang MJ, Bramley AN (2011) RFID-enabled gateway product service system for collaborative manufacturing alliances. CIRP Ann Manuf Technol 60(1):465468 

10 

- Lu W, Huang GQ, Li H (2011) Scenarios for applying RFID technology in construction project management. Autom Constr 20(2):101–106 

- Motamedi A, Soltani MM, Setayeshgar S, Hammad A (2016) Extending IFC to incorporate information of RFID tags attached to building elements. Adv Eng Inform 30(1):39–53 

- Ndekugri IE, McCaffer R (1988) Management information flow in construction companies. Constr Manage Econ 6(4):273–294 

- Niu Y, Lu W, Chen K, Huang GG, Anumba C (2015) Smart construction objects. J Comput Civ Eng 04015070 

- Pradhananga N, Teizer J (2013) Automatic spatio-temporal analysis of construction site equipment operations using GPS data. Autom Constr 29:107–122 

- Solihin W, Eastman C, Lee YC (2016) A framework for fully integrated building information models in a federated environment. Adv Eng Inform 30(2):168–189 

- Tserng HP, Ho SP, Jan SH (2014) Developing BIM-assisted as-built schedule management system for general contractors. J Civ Eng Manage 20(1):47–58 

11 

