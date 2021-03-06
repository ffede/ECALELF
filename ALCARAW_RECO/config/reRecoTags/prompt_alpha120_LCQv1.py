import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
                               globaltag = cms.string('GR_P_V32::All'),
                               toGet = cms.VPSet(
                                 cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
                                     tag = cms.string("EcalLaserAPDPNRatios_data_20120512_190262_193774_tbc"),
                                     connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_42X_ECAL_LAS")
                                     )
                                 ,cms.PSet(
                                     record = cms.string('EcalLaserAlphasRcd'),
                                     tag = cms.string('EcalLaserAlphas_EB_sic_btcp154_EE_sic1_btcp120'),
                                     connect = cms.untracked.string('frontier://FrontierPrep/CMS_COND_ECAL')
                                     )
                                 ),
                               BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
                               )
