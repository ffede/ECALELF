import FWCore.ParameterSet.Config as cms

elPFIsoValueCharged03PFIdRecalib = cms.EDProducer('ValueMapTraslator',
                                                  inputCollection = cms.InputTag('elPFIsoValueCharged03PFIdPFIso'),
                                                  outputCollection = cms.string(''),
                                                  referenceCollection = cms.InputTag('electronRecalibSCAssociator')
                                                  )

elPFIsoValueGamma03PFIdRecalib = cms.EDProducer('ValueMapTraslator',
                                                inputCollection = cms.InputTag('elPFIsoValueGamma03PFIdPFIso'),
                                                outputCollection = cms.string(''),
                                                referenceCollection = cms.InputTag('electronRecalibSCAssociator')
                                                )

elPFIsoValueNeutral03PFIdRecalib = cms.EDProducer('ValueMapTraslator',
                                                inputCollection = cms.InputTag('elPFIsoValueNeutral03PFIdPFIso'),
                                                outputCollection = cms.string(''),
                                                referenceCollection = cms.InputTag('electronRecalibSCAssociator')
                                                )
