

### LEAN & COMPUTING IN CONSTRUCTION CONGRESS 



**3D BUILDING MODELING WITH MULTI-SOURCE DATA A STUDY OF HIGH-DENSITY URBAN AREA IN HONG KONG** 

Chen, K. **Xue, F.** Lu, W. _PhD Cand.                   RAP                   Assoc. Prof. i_ Lab, Faculty of Architecture The University of Hong Kong 







JC3-2017, 4-7 July, 2017 Heraklion, Crete, Greece 



## OUTLINE 





1 Background & Opportunity 2 A Pilot of A Multi-source Modeling Method in HK 3 Discussion & Future Research 



2 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 







## 1. BACKGROUND & OPPORTUNITY 



3 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 



## 1.1 BACKGROUND 





- 3D modeling from measurement (as-built BIM<sup>†</sup> )<sup>(Volk</sup><sup>_et al_.,2014)</sup> 

   - The digital foundation of smart city development, _e.g._ 

      - Smart construction and human-machine cooperation 

An example of photogrammetry: Kowloon Wall City (Source: patrick-@sketchfab.com) 

   - Healthy aging and accessibility development 

   - Energy consumption and waste emissions reduction 

   - Facility management & built heritage conservations, _etc._ 

- Popular (semi-)auto methods & data types 

   - Photogrammetry, point cloud-based, GIS-based, rules, _etc._ 

An example of point cloud: Pompei City (Source: MAP-Gamsau lab, CNRS, France) 

   - Image (video), point clouds, GIS data layers, knowledge, _etc._ 

- Not new, but still very challenging in scenarios of CIM<sup>‡</sup> 

   - Unsatisfactory semantic/abstraction 

      -  huge size, poor reusability, & poor details in models 

   - Obstacles: Complexity, incomplete data, noises, _etc._ 

      - Especially for high-rise high-density urban areas 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 

4 An example of GIS-based: 3D Berlin (Open Data, source: berlin.de) 

- †: Building information modeling 

‡: City information modeling 



## 1.1 BACKGROUND 







<!-- Start of picture text -->
Smart governance<br>Smart living<br>Smart environment<br>Camera<br>Matching by features;<br>Structure from Motion(SfM)<br>Data-driven<br>( many )<br>Meshing;<br>Texturing Semantically rich 3D<br>building models<br>(in CIM)<br>Model-<br>Simultaneous localization and  Driven<br>mapping (SLAM) Stitched point cloud Mesh surface ( few )<br>BIM<br>component<br>Point<br>Laser  Database<br>cloud<br>scanner<br>(Some icons from Wikipedia: CC-BY; CC-BY-NC) 5<br>Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece)  A previous study<br>(Xue  et al ., 2016)<br><!-- End of picture text -->

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 



## 1.2 PREVIOUS STUDY & LOD 





 There exist (semi-)automatic data-driven methods on single-source data 

|**Data sources**|**No. of buildings**|**Auto?**|**LoD**|**Reference**|
|---|---|---|---|---|
|Aerial images|city-scale|Yes|Between LoD1 and LoD2|Lafarge_et al._(2008)|
|Aerial images|3|No|Between LoD2 and LoD3|Singh_et al_. (2014)|
|Aerial images|city-scale|Yes|LoD2|Haala_et al_. (2015)|
|Aerial images|375|Yes|Between LoD1 and LoD2|Li_et al_. (2016)|
|Satellite images|Univ. campus|No|LoD1|Fraser_et al._(2001)|
|Satellite images|city-scale|No|LoD2|Kocaman_et al_. (2006)|
|||||Maas and Vosselman|
|LiDAR|51|Yes|Between LoD1 and LoD2|(1999)|
|LiDAR|city-scale|Yes|Between LoD1 and LoD2|Poullis and You (2009)|
|LiDAR|<20|Yes|LoD2|Sun and Salvaggio (2013)|
|LiDAR|29|No|LoD2|Heo_et al_. (2013)|
|LiDAR|39|Yes|LoD2|Yan_et al_. (2016)|



 Adopted computer vision Aerial images city-scale Yes Between LoD1 and LoD2 Lafarge methods, _e.g._ , RANSAC<sup>†</sup> , Aerial images 3 No Between LoD2 and LoD3 Singh Aerial images city-scale Yes LoD2 Haala SGM<sup>‡</sup> . Aerial images 375 Yes Between LoD1 and LoD2 Li _et al_  CityGML* defines LoD Satellite images Univ. campus No LoD1 Fraser Satellite images city-scale No LoD2 Kocaman (Level-of-Detail) LiDAR 51 Yes Between LoD1 and LoD2 (1999)  LoD0 (2.5D DTM<sup></sup> ) LiDAR city-scale Yes Between LoD1 and LoD2  LoD1 (prismatic block, LiDAR <20 Yes LoD2 LiDAR 29 No LoD2 Heo _et al_ flat roof) LiDAR 39 Yes LoD2 Yan _et al_  LoD2 (+ roof shapes, assemblies)  _where the auto single-source methods can go_  LoD3 (+ detailed outer surfaces, roof structures) 



<!-- Start of picture text -->
6<br><!-- End of picture text -->

†: Random sampling consensus 

‡: Semi-global matching *: See Kolbe _et al_ . (2005) : Digital terrain model 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 

## 1.2 PREVIOUS STUDY & LOD 





 Capability of multi-source methods was still limited to generating LoD2 models 



 If not involving manual work 

|**Data sources**|**No. of buildings**<br>**A**|**uto? **|**LoD**|**Reference**|
|---|---|---|---|---|
|Satellite images; LiDAR|170|Yes|LoD1|Sohn and Dowman (2007)|
|Aerial images; LiDAR|<30|Yes|Between LoD1 and LoD2|Rottensteiner and Jansa (2002)|
|LiDAR; Camera|city-scale|No|Between LoD2 and LoD3|Frueh and Zakhor (2003)|
|Aerial images; LiDAR|<50|Yes|LoD2|Cheng et al. (2011)|
|Aerial images; LiDAR|88|No|N/A (Roof only)|Awrangjeb et al. (2013)|
|Aerial images; LiDAR|107|No|LoD2|Siddiqui et al. (2016)|
|Aerial images; LiDAR; 2D vector map|170|No|Between LoD2 and LoD3|Zhang et al. (2005)|
|LiDAR; Building footprints|529|N.A.|LoD2|Alexander et al. (2009)|
|OpenStreetMap; Shuttle radar mission|city-scale|No|LoD1|Over et al. (2010)|
|OpenStreetMap; Aerial images|>700|Yes|LoD2|Rumpler et al. (2012)|
|Laser scanner; Ground plans|83|Yes|LoD2|Vosselman and Dijkman (2001)|
|LiDAR; Building footprints|370|No|LoD1|Ledoux and Meijers (2011)|
|LiDAR; Topographic map|109|Yes|LoD2|~~7~~<br>You and Lin (2011)|
|Chen, Xue, Lu: Multi-source 3D building modeling (JC3<br>LiDAR; Land cadaster maps; Topographic map; Digital<br>orthophotos; Building footprints; Non-spatial data|-2017, Heraklion, Gre<br>~2,300|ece)<br>No|LoD2|Agugiaro (2014)|











## 1.3 OPPORTUNITY 

- LiDAR and digital maps are extensively available, **but** 

   - Unsatisfactory semantic/abstraction discovery 

   - “For-profit” models ( _e.g._ , Google) are not open 

   - Existing LoD2 methods still have some flaws 

      - many methods only illustrated in low-density areas 

- Opportunity of a multi-source method 

#### Yan _et al._ (2016)’s space-cutting method 

- Object recognition from point clouds ( **LiDAR data** ) 

   - Facilitated by **topographic map** 

- Some _a priori_ rules about alignment (horizontal, parallel, perpendicular, _etc._ ) as architectural **knowledge** 

   - _E.g.,_ parallel to the major edges of footprints (existing in **topographic map** ) 

LiDAR: 1 p/m<sup>2</sup> 16 p/m<sup>2</sup> 40p/m<sup>2</sup> Alexander _et al._ (2009)’s aspect regulation 

8 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 







## 2. A PILOT OF A MULTI-SOURCE MODELING METHOD IN HK 



9 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 







## 2.1 THE PILOT PROBLEM 

- The pilot area 

   - A 4 km<sup>2</sup> square area in Central & Western District, Hong Kong 

   - 1,819 prisms (1,361 blocks) of densely distributed buildings 

- Three inputs 

   - Point clouds from LiDAR ( 4 p/m<sup>2</sup> , format: _.las_ ) 

   - Building footprints & heights from topographic map (format: . _json_ ) 

   - A list of architectural knowledge about rooftop elements from literature reviews (hard coded rules with parameters) 

- One output 

   - All building models in LoD2 in the area (format: . _dae_ & . _json_ ) 

The pilot area (Source: OpenStreetMap) 



#### Airborne LiDAR data (.las format) 



The _ib1000_ topographic 10 map & data layers (ArcGIS format) 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 







## 2.2 A CLOSE LOOK 

- LoD1 building models can be quickly generated in ArcGIS based on the topographic map 

   - Extrusion of footprint 

- LiDAR data contains geometric measurements of rooftop elements 

#### LoD1 models in ArcGIS 

   - It fits well onto the map (both in HK1980 grid system) 

- The topographic map can export all necessary data in GeoJSON 

   - Easy for in-house program development 

- Knowledge-based rectification of rooftop elements 

#### LiDAR point clouds are able to bring 

#### rooftop elements 

- Must be in parallel or perpendicular (0°, 90°, 180°, 270°) with one or more directions of major edges of footprint 

11 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 

Extracting information from the map 



2.3 THE PROCESS (STEPS 1~2) 





 Step 1: Filter the points of rooftop of each building with its footprint and roof level  Reduce the size of point cloud from ~10<sup>7</sup> (urban-scale) to ~10<sup>3</sup> (building-scale)  Step 2: Cluster the directions of the longest edges in footprint 

 Find one, or more if there are more clusters, direction for each building 



An example at HKU campus (Source: Google) 







Step 1: Filtering LiDAR points, computing normal 

Step 2: Clustering guiding directions from footprints (in 12 dashed lines) 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 



2.3 THE PROCESS (STEPS 3~5) 



 Step 3: Planar primitives discovery by RANSAC 



   - May contains a few unrealistic shapes 

- Step 4: Rectification of the primitives with respect to the guiding directions of each building ( _summarized from observations_ ) 



- If there are more than one guiding directions, the closest one is used 

 Step 5: Create 3D rooftop elements from those are close to 

 ( _i_ ) guiding directions and ( _ii_ ) the horizontal plane for each building 











Reference image 13 (Source: Google) 

Step 5: Create 3D rooftop elements 

An example building from Step 1,2 

Step 4: Rectification 

Step 3: RANSAC (Schnabel _et al_ ., 2007) 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 



## 2.4 RESULT OF THE PILOT TEST 





 Pilot test 

 The 1,361 blocks of buildings in 4 km<sup>2</sup> 

 By an in-house plugin for _CloudCompare 2.9_ (single thread) 

- (Available soon) 

Result of the example area of HKU (dark=LoD1; light=rooftop in LoD2; photo source: dragageshk.com) 

 On a notebook computer, i7 2.6GHz mobile CPU 



- Time cost 

   - Clustered guiding directions of all buildings: < 1.0 s 

   - Generated 1,114 out of 1,361 building models: 319.7 s 

 Manual processing time: 0.0 s (geo-referencing by aircraft’s GPS) 

- Quality 

   - Information richness: LoD2 in general 

The area in Google Map/Earth 

- Geometric error (RMSE): 0.06~0.20m for segmented points 

 Acceptable, since the accuracy of LiDAR is 0.30 m (horizontal) and 0.10 m (vertical) Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 

14 







## 3. DISCUSSION & FUTURE RESEARCH 



15 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 



## 3.1 DISCUSSION 



- Pros: 



- The proposed method is efficient 

   - ~0.3 s per building, **linear increasing** overall time when scaling up to a district or a city 

   - Should be attributing to the efficiency of the nested RANSAC 



   - The error is acceptable 

      - Because odd shapes were dropped by the rules and the guiding directions 

- Cons: 

   - Limited to planar primitives temporarily, not fitting precisely for curve shaped roofs 

   - The airborne LiDAR contains little data of facades in high-density areas 

      - There can be more inputs to fuse, _e.g_ ., point clouds from synthetic aperture radar (SAR), freely online photos, SLAM prototype models, _etc_ . 

- Limitation: The pilot result is only visually tested yet 

16 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 



## 3.2 FUTURE RESEARCH 



 Advancing LoD2 models to LoD3 with dense point clouds 



 E.g., unmanned aerial vehicles (UAVs), Simultaneous localization and mapping (SLAM) 

 With more architectural/construction knowledge to explore 

 Semantic enrichment for applications, _e.g._ 

 Thermal properties  energy saving 

 A/C units, satellite dish, pipes, and green  facility management 



Albedo (reflectance) map, green roof map, _etc._ 

Regression / Rules / Supervised learning 



17 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 







## REFERENCES 

- Alexander, C., Smith-Voysey, S., Jarvis, C., and Tansey, K. (2009). Integrating building footprints and LiDAR elevation data to classify roof structures and visualise buildings. _Computers, Environment and Urban Systems_ , _33_ (4), 285-292. 

- Kolbe, T. H., Gröger, G., and Plümer, L. (2005). CityGML: Interoperable access to 3D city models. In: P. van Oosterom, S. Zlatanova, E. M. Fendel, ed., Geo-information for Disaster Management. Springer Berlin Heidelberg, pp. 883–899, doi: 10.1007/3-540-27468- 



- Schnabel, R., Wahl, R., and Klein, R. (2007). Efficient RANSAC for point ‐ cloud shape detection. _Comput. Graph. Forum_ , 26(2), pp. 214–226, doi: 10.1111/j.1467-8659.2007.01016.x, 214-226. 

- Volk, R., Stengel, J., and Schultmann, F. (2014). Building Information Modeling (BIM) for existing buildings— Literature review and future needs. Automation in Construction, 38: 109-127. 

- Xue, F., Chen, K., Liu, D., Niu, Y., and Lu, W. (2016). An optimization-based semantic building model generation method with a pilot case of a demolished construction. In International Conference on Advancement of Construction Management & Real Estate, CRIOCM 2016. (proceedings in press) 

- Yan, J., Jiang, W., and Shan, J. (2016). A global solution to topological reconstruction of building roof models from airborne LiDAR point clouds. _ISPRS Annals of Photogrammetry, Remote Sensing and Spatial Information Sciences_ , 379-386. 

18 

Chen, Xue, Lu: Multi-source 3D building modeling (JC3-2017, Heraklion, Greece) 



### LEAN & COMPUTING IN CONSTRUCTION CONGRESS 



# THANK YOU! 







