from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters

# CFG = 'sim_HToAATo4Tau_RunIISummer20UL18_00066_1_cfg'

# To submit to crab:
# crab submit -c crabConfig_data.py
# To check job status:
# crab status -d <config.General.workArea>/<config.General.requestName>
# To resubmit jobs:
# crab resubmit -d <config.General.workArea>/<config.General.requestName>
Mass = '14' #3p7,4,5,6,8,10,12,14
# Local job directory will be created in:
# <config.General.workArea>/<config.General.requestName>

dataset_ = {
'3p7': "/GEN_PreMix_HToAATo4Tau_M_3p7_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_3p7-4e990a3bd75cc61aab762cd20dddf671/USER"
, '4': "/GEN_SIM_HToAATo4Tau_M_4_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_4-318a03a6d743bbb30a2617ad206a1575/USER"
, '5': "/GEN_SIM_HToAATo4Tau_M_5_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_5-8fa7a4d2e9279767e7302e4e174f6332/USER"
, '6': "/GEN_SIM_HToAATo4Tau_M_6_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_6-91790617a59effd666a23a2f9dd67a4c/USER"
, '8': "/GEN_SIM_HToAATo4Tau_M_8_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_8-19c81b84dd8b2be31307b38aeae9b67b/USER"
, '10': "/GEN_SIM_HToAATo4Tau_M_10_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_10-42ad5a215a78c4406436425f9d78c168/USER"
, '12': "/GEN_SIM_HToAATo4Tau_M_12_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_12-8ed0cbfc169db886a58f99f03c10db34/USER"
, '14': "/GEN_SIM_HToAATo4Tau_M_14_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_M_14-847331e38606cd3b58a750303c3593fc/USER"
}.get(Mass, None)

config.General.workArea        = 'crab_MC'
config.General.requestName     = 'digi_premix_HToAATo4Tau_M_%s'%Mass
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis' # mass > 8 use this

config.JobType.psetName    = 'HToAA4Tau_DIGIPremix_cfg.py' # cms cfg file for generating events
# config.JobType.maxMemoryMB = 5000 #5000
# config.JobType.numCores = 4

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:

config.Data.inputDataset = dataset_
# config.Data.userInputFiles = open('MLAnalyzer/list_gen_sim_aToTauTau_m3p6To15.txt').readlines()

# for m >8 use this to process all events.
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 10 # units: as defined by config.Data.splitting
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
