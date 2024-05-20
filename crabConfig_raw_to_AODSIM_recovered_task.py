from CRABClient.UserUtilities import config, getLumiListInValidFiles
from FWCore.PythonUtilities.LumiList import LumiList
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters

# CFG = 'sim_HToAATo4Tau_RunIISummer20UL18_00066_1_cfg'

# To submit to crab:
# crab submit -c crabConfig_data.py
# To check job status:
# crab status -d <config.General.workArea>/<config.General.requestName>
# To resubmit jobs:
# crab resubmit -d <config.General.workArea>/<config.General.requestName>
Mass = '4' #3p7,4,5,6,8,10,12,14
# Local job directory will be created in:
# <config.General.workArea>/<config.General.requestName>

dataset_ = {
'3p7': "/GEN_PreMix_HToAATo4Tau_M_3p7_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_3p7-b403a189a2d057e62e59ed092120c7f4/USER"
, '4': "/GEN_SIM_HToAATo4Tau_M_4_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_4-b403a189a2d057e62e59ed092120c7f4/USER"
, '5': "/GEN_SIM_HToAATo4Tau_M_5_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_5-b403a189a2d057e62e59ed092120c7f4/USER"
,'6': "/GEN_SIM_HToAATo4Tau_M_6_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_6-b403a189a2d057e62e59ed092120c7f4/USER"
, '8': "/GEN_SIM_HToAATo4Tau_M_8_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_8-b403a189a2d057e62e59ed092120c7f4/USER"
, '10': "/GEN_SIM_HToAATo4Tau_M_10_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_10-b403a189a2d057e62e59ed092120c7f4/USER"
, '12': "/GEN_SIM_HToAATo4Tau_M_12_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_12-b403a189a2d057e62e59ed092120c7f4/USER"
, '14': "/GEN_SIM_HToAATo4Tau_M_14_pythia8_2018UL/lpcml-HLT_HToAATo4Tau_M_14-b403a189a2d057e62e59ed092120c7f4/USER"
}.get(Mass, None)

all_taskLumis = getLumiListInValidFiles(dataset=dataset_, dbsurl='phys03')

final_dataset = {
'4': "/GEN_SIM_HToAATo4Tau_M_4_pythia8_2018UL/lpcml-raw_to_AODSIM_HToAATo4Tau_M_4-ce2d8483a217bdee138ad6a78c69df45/USER"
, '8': "/GEN_SIM_HToAATo4Tau_M_8_pythia8_2018UL/lpcml-raw_to_AODSIM_HToAATo4Tau_M_8-ce2d8483a217bdee138ad6a78c69df45/USER"
, '10': "/GEN_SIM_HToAATo4Tau_M_10_pythia8_2018UL/lpcml-raw_to_AODSIM_HToAATo4Tau_M_10-ce2d8483a217bdee138ad6a78c69df45/USER"
, '12': "/GEN_SIM_HToAATo4Tau_M_12_pythia8_2018UL/lpcml-raw_to_AODSIM_HToAATo4Tau_M_12-ce2d8483a217bdee138ad6a78c69df45/USER"
}.get(Mass, None)

finished_taskLumis = getLumiListInValidFiles(dataset=final_dataset, dbsurl='phys03')

newLumiMask = all_taskLumis - finished_taskLumis
newLumiMask.writeJSON('my_lumi_mask_M_%s.json'%Mass)

config.General.workArea        = 'crab_MC_recovered_task'
config.General.requestName     = 'raw_to_AODSIM_HToAATo4Tau_M_%s'%Mass
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis' # mass > 8 use this

config.JobType.psetName    = 'raw_to_AODSIM_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 2500 #5000
# config.JobType.numCores = 4

config.Data.inputDBS = 'phys03'
config.Data.lumiMask = 'my_lumi_mask_M_%s.json'%Mass
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:

config.Data.inputDataset = dataset_
# config.Data.userInputFiles = open('MLAnalyzer/list_gen_sim_aToTauTau_m3p6To15.txt').readlines()

# for m >8 use this to process all events.
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1  # units: as defined by config.Data.splitting
config.Data.totalUnits     = -1 # -1: all inputs. total jobs submitted = totalUnits / unitsPerJob. cap of 10k jobs per submission

config.Data.publication    = True


# # for m < 10 use this but you have final number of events.
# config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 1
# NJOBS = 2
# config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
# config.Data.totalUnits = -1
# config.Data.outputPrimaryDataset = 'sim_HToAATo4Tau_Hadronic_tauDR0p4_M%s_ctau0To3_eta0To2p4_pythia8_2018UL'%Mass

# Output files will be stored in config.Site.storageSite at directory:
# <config.Data.outLFNDirBase>/<config.Data.outputPrimaryDataset>/<config.Data.outputDatasetTag>/
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration/signal_withTrigger'
# config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
