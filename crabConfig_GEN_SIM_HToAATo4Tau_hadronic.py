from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
Mass = '14' # Mass of A is generally integer but put as string if need decimal.
N = {'3p7': 200, '4': 180, '5':175,'6':170, '8':160, '10':150, '12':150, '14':150}.get(Mass, None)
# Local job directory will be created in:
config.General.requestName = 'gen_HToAATo4Tau_M_%s'%Mass
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'HToAA4Tau_M_%s_GEN_SIM_cfg.py'%Mass
config.Data.outputPrimaryDataset = 'GEN_SIM_HToAATo4Tau_M_%s_pythia8_2018UL'%Mass

# config.JobType.maxMemoryMB = 5000

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=500
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = N
NJOBS = 999
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

# Output files will be stored in config.Site.storageSite at directory:
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration/signal_withTrigger'
config.Site.storageSite = 'T3_US_FNALLPC'
