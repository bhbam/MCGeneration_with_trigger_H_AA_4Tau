from CRABClient.UserUtilities import config
config = config()
# Process = 'DYTauTau'
# Process = 'QCD'
# Process = 'WJets'
Process = 'TTbar'

inputDataset_ ={
        'DYTauTau': "/DYToTauTau_M-50_13TeV-powheg_pythia8/lpcml-DYTauTau_DIGI-Premix-a4b16f3a529872f5497e88f7f4b0cfae/USER",
        'QCD': "/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/lpcml-QCD_DIGI-Premix-a4b16f3a529872f5497e88f7f4b0cfae/USER",
        'WJets': "/WJetsToLNu_TuneCP5_13TeV_madgraphMLM-pythia8/lpcml-WJets_DIGI-Premix-a4b16f3a529872f5497e88f7f4b0cfae/USER",
        'TTbar': "/TTToHadronic_TuneCP5_13TeV_powheg-pythia8/lpcml-TTbar_DIGI-Premix-a4b16f3a529872f5497e88f7f4b0cfae/USER"
        }.get(Process, None)

outputDataset_ = {
        'DYTauTau':'DYToTauTau_M-50_13TeV-powheg_pythia8',
        'QCD':'QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8',
        'WJets':'WJetsToLNu_TuneCP5_13TeV_madgraphMLM-pythia8',
        'TTbar':'TTToHadronic_TuneCP5_13TeV_powheg-pythia8'
        }.get(Process, None)

#config.section_('General')
config.General.requestName = '%s_HLT'%Process
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_HLT_cfg.py'
#config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset = inputDataset_
#config.Data.userInputFiles = open('%s'%inputProcess_).readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.outputPrimaryDataset = outputDataset_

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
config.Data.publication = True
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
