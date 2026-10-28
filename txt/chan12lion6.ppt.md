

###### - Pearl Hunter: An Inspired Hyper Pearl Hunter: An Inspired Hyperheuristic heuristic 

16th January 2012, Paris 16th January 2012, Paris 

CY Chan, Fan Xue, WH CY Chan, Fan Xue, WH Ip Ip, , CF Cheung CF Cheung _Department of Industrial & Systems Engineering_ De partment of Industrial<sup>&Systems</sup> Engineering _Hong Kong Polytechnic University_ Hong Kong Polytechnic University 



<!-- Start of picture text -->
LeeaN THEPOLYTECHNIC HONG KONG  UNIVERSITY<br>Yo AEM LAS<br><!-- End of picture text -->



<!-- Start of picture text -->
5<br><!-- End of picture text -->

Department of Industrial and Systems Engineering 

工業及系統工程學系 

### **Outline** & ~~Outline~~ 

**1 Pearl Hunting** 

**2 The Pearl Hunter** 

**3 Training and Validation on HyFlex** 

**4 Conclusions** 

2 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 



###### **Pearl Diving** 

- _Pearl diving_ is an out-of-date 

- diving activity of retrieving pearls from oysters. 

- Can still be found in: 

   - Some Asian tourist sites, 

 Virtual games. 



In Australia (screenshot of “Introduction to pearls and Australian Pearl Divers”, © by Australian Opal Cutter youtube.com/watch?v=V6vuBvglndw) 



Pearl diver in Japan (from Wikimedia Commons, public  copyright) 



In Qatar (screenshot of “Pearling”, © Qatar Pavilion, World EXPO 2010) 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 

3 



###### **Pearl Diving and Simulation** 

- In a search perspective, pearl hunting consists of repeated 

   - _diversification_ (surface and change target area) 

   - _intensification_ (dive and find pearl oysters). 

- In the paradigm of Iterated Local Search (Lourenço et al, 2003). 

- Simulated operations 

   - _move_ ( _diversification_ , 1 source or multiple sources) 

   - _dive_ ( _intensification_ ) 

      - _snorkeling_ (quick, low level local search, stops after any improvements) 

      - _deep dive_ (scuba; slow, high level local search, till no further improvements) 

4 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 



###### **Correlations Between Snorkeling and Deep Dive** 

Table 1: Pearson correlations between improvements by snorkeling (10% maximum <u>depth of search) and deep dive (maximum depth of search) in 3 domains of CHeSC</u> 

|**Diversification**|**by LLH**|**Max-SAT**|**Bin Packing**|**Flow Shop**|
|---|---|---|---|---|
|Crossover|Pearson Cor.|0.82*|0.47^|0.88*|
||Sig. (2-tailed)|0.00|0.00|0.00|
||N|466|143|317|
|Mutation|Pearson Cor.|0.61^|0.11|0.83*|
||Sig. (2-tailed)|0.00|0.00|0.00|
||N|112|1405|752|
|Ruin-recreate|Pearson Cor.|0.08|0.07|0.58^|
|(extra)|Sig. (2-tailed)|0.51|0.11|0.00|
||N|70|551|328|



###### Correlations: 

 Strong (*) or moderate (^) positive coefficient with a significant level 0.01 

 1≤ _N_ snorkeling/ _N_ deepdive ≤ 10, choose best of snorkeling in practice 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 

5 

###### **-** LQ» **Pearl Hunter: A HyperImitation** Pearl Hunter: A Hyper-heuristic **heuristic** RS ~~Imitation~~ 

Obj Value 

“Environment”: 



<!-- Start of picture text -->
_ —<br><!-- End of picture text -->

 _Shallow water_ , where deep dive always returns the same as snorkeling 

- _Sea trench_ , where deep dives cost too much 

- time at maximum depth-of-search 

Trail 

 _Default, otherwise_ 

Preparation of Low Level Heuristics(LLHs) 

 Selective scheme (CHeSC2011) 

 Choose {A, B} from {A, B, C} 

 Constructive scheme 

Time 



<!-- Start of picture text -->
(<br><!-- End of picture text -->

Iterated move-snorkeling-dive 

Perceiving the environment and preparing LLHs 

 Pre-trained 

 Online trained 

6 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 

#### **Pearl Hunter** GOQ ~~Pearl Hunter~~ 

- Pearl Hunter can drop a Buoy at the depth of first deep dive, to escape from local optimum by mutations (SIs). 

- Four running modes (portfolios) of selected LLHs:  **A** : all moves averagely, with a _Buoy_ mark  **B** : _crossover_ with a _Buoy_ mark (triggering a few mutations)  **C** : _crossover_ only, no mutation, no _Buoy_ 

 **D** : Sea trench mode, all surface moves averagely, no _Buoy._ Moves are subject to online pruning. 

C B D A ~~<u>Y | | ’</u>~~ Crossover ~~ESE Dil!~~ Anchors of the modes Other tricks: 

Mutation 

 tabu lists (memory), “mission restarts” (go to new areas) 

7 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 



###### **HyFlex and CHeSC** 

HyFlex (Hyper-heuristics Flexible framework) is a java cross-domain platform (Burke et al, 2011) 

- 6 domains, 4 public (training domain) and 2 hidden 

 “Black-box” low-level heuristics in 4 categories: 

 Crossover, Mutation, Ruin-recreate, and Local search 

- Parameters to control low-level heuristics : 

   - “Intensity" of mutations, and “depth of local search” 

CHeSC 2011 is the first Cross-domain Heuristic Search Challenge on HyFlex. (http://www.asap.cs.nott.ac.uk/chesc2011/) Pearl Hunter was ranked in CHeSC: 

- 4th out of 20 entries overall, 

 1st out of 20 entries in the hidden domains. 

8 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 

##### **-** LQ» **HyFlexb** HyFlex **<u>y Offline Learnin</u>** and **and** CHeSC: **CHeSC: BFg** BF-Tree **<u>(byTree Obtained Weka</u>** Obtained **v3.5)** RS ~~by Offline Learning~~ ~~<mark>(by</mark> Weka v3.5)~~ 



<!-- Start of picture text -->
Pmu > = 18.9% © Pmu < 18.9% (>)<br>vePere n 1 59% O dPaet ve Pdir > = 34.5% O) pair <34.5%<br>Mco < 14.5 © Mco > = 14.5<br>(3) Dmurr > = 9 O) pmmurr <9<br>N> =7 8 ©) N<78<br>(8)<br><!-- End of picture text -->

- Dmurr: Depth of the mission in the Mutation and Ruin-recreate test, 

- Mco: Number of missions completed in the Crossover test, 

- N: Number of sub-optimal solutions found in total, 

- Pdir: Percent of sub-optimal solutions found right after some moves (before any dive), 

- Pmu: Percent of sub-optimal solutions found in iterations started with Mutation moves, 

- Prr: Percent of sub-optimal solutions found in iterations started with Ruin-recreate moves, 

9 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 

## **Tests on Personnel Scheduling: Beyond the 600s Time Limit of CHeSC** ~~>~~ 

- On large-scale personnel scheduling problems,  Running time was increased to 10 hours (normalized to P4 3GHz), 

   - Same decision tree and algorithm codes 

|New best<br><br>|known sol<br>  <br>|utions:<br> <br>||<br>|<br>|
|---|---|---|---|---|---|
|**Instance**<br>~~a~~|**Men| days**<br> ~~es~~|**Time(h)**<br>~~ee~~|**Result**<br>~~ee~~|**Prev BK***<br>|**% improved**<br>~~ee~~|
|CHILD-2A<br>|41|42<br>|10<br>|_1,095_<br>|1,111<br>|1.4<br>|
|ERRVH-A|51|42|10|_2,142_|2,197|2.5|
|ERRVH-B|51|42|10|_3,121_|6,859|54.5|



* Best known values were collected from http://www.cs.nott.ac.uk/~tec/NRP/misc/NRP_Results.xls 

A possible reason 

 A new “vertical” swap concept first implemented in low-level heuristics on HyFlex 

10 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 

# **Conclusion** We present a hyper-heuristic  Imitates pearl hunting  Perceives “environment” of search  Determines a perturbation mode by offline learning  Generates different modes of ILS We find the results of tests encouragingWe find the results of tests encouraging Possible future works  Hunters can generate new LLHs besides a selection  branch-and-bound and local search (2-Opt, 5-Opt) (Xue 2012). | <u>Conclusion</u> 

   - Perceives “environment” of search 

   - Determines a perturbation mode by offline learning 

   - Generates different modes of ILS 

- We find the results of tests encouragingWe find the results of tests encouraging 

   - Hunters can generate new LLHs besides a selection 

      - (Custom designed for TSP) Generated an association-rules-based weighting hyper-heuristic to determine candidate set, and facilitated branch-and-bound and local search (2-Opt, 5-Opt) (Xue _et al_ , 2010, 2012). 

11 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 

- **References** 

- GO ~~References~~  Burke E.K., Curtois T., Qu R., Vanden Berghe G. (2007) A Time Pre-defined Variable Depth Search for Nurse Rostering. Technical Report No. NOTTCS-TR-2007-6. University of Nottingham 

   - Burke, E. K., Hyde, M., Kendall, G., Ochoa, G., Ozcan, E., and Qu, R. (2010) Hyperheuristics: A Survey of the State of the Art, University of Nottingham. Technical Report No. NOTTCS-TR-SUB-0906241418-2747. 

   - Burke, E., Curtois, T., Hyde, M., Ochoa, G., Vazquez-Rodriguez J. A. (2011) HyFlex: A Benchmark Framework for Crossdomain Heuristic Search, ArXiv e-prints, arXiv:1107.5462v1 

   - Lourenço, H., Martin, O., St�ützle, T. (2003) Iterated Local Search. In Glover, F., Kochenberger, G. (eds.) Handbook of Lourengo, H., Martin, O., Stiiitzle, T. (2003) Iterated Local Search. In Glover, F., Kochenberger, G. (eds.) Handbook of Metaheuristics. Springer New York. 320-353. 

   - Xue F., Chan, C.Y., Ip, W.H., Cheung, C.F. (2010) Towards a learning-based heuristic searching reform scheme, XXIV European Conference on Operational Research (EURO), Lisbon, Portugal. 

   - Xue F., Chan, C.Y., Ip, W.H., Cheung, C.F. (2012) A learning-based variable assignment weighting scheme for heuristic and exact searching in Euclidean traveling salesman problems, NETNOMICS, (to appear). 

12 

Chan et al: Pearl Hunter: An Inspired Hyper-heuristic 



Thank you for your attention! Thank you for your attention! - E E-mail mail addr addr.: .: mffxue@inet.polyu.edu.hk mffxue@inet.polyu.edu.hk dewolf_matri_x@msn.com dewolf_matri_x@msn.com 



<!-- Start of picture text -->
Yo Avew LAKE<br><!-- End of picture text -->



Department of Industrial and Systems Engineering 工業及系統工程學系 

