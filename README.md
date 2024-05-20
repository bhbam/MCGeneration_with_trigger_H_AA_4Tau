Step 1:

Generated and simulate the required events in CMSSW_10_6_20 (Filters applied here)
cmsRun  HToAA4Tau_M_*_GEN_SIM_cfg.py

Step 2:
digitization and premixing  events in CMSSW_10_6_20 (pileup applied here)
cmsRun HToAA4Tau_DIGIPremix_cfg.py

Step 3:

Add HLT information in CMSSW_10_2_16_UL using generated events in step 2 because HLT menu is not available in 10_6_20
cmsRun HLT_H_AA_4Tau_RunIISummer20UL18HLT-00003_1_cfg.py

Step 4:

Convert raw to AODSIM back into CMSSW_10_6_20 using generated events in step 3
cmsRun raw_to_AODSIM_cfg.py
