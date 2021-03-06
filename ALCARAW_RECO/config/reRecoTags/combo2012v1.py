import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
                               globaltag = cms.string('GR_R_52_V7::All'),
                               toGet = cms.VPSet(
                                 cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
                                     tag = cms.string("EcalLaserAPDPNRatios_data_20120516_190380_193761_P_p1_tbc"),
                                     connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_42X_ECAL_LAS")
                                     )
                                 ,cms.PSet(record = cms.string('EcalLaserAlphasRcd'),
                                           tag = cms.string('EcalLaserAlphas_EB_sic1_btcp152_EE_sic1_btcp116'),
                                           connect = cms.untracked.string('frontier://FrontierPrep/CMS_COND_ECAL')
                                           )
                                 ,cms.PSet(record = cms.string('ESIntercalibConstantsRcd'),
                                           tag = cms.string('ESIntercalibConstants_V02_offline'),
                                           connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PRESHOWER')
                                           ),
                                 ),
                               BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
                               )
