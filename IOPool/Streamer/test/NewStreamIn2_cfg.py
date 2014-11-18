import FWCore.ParameterSet.Config as cms

process = cms.Process("TRANSFER")

import FWCore.Framework.test.cmsExceptionsFatal_cff
process.options = FWCore.Framework.test.cmsExceptionsFatal_cff.options

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('file:teststreamfile.dat'),
    inputFileTransitionsEachEvent = cms.untracked.bool(True)
)

process.a1 = cms.EDAnalyzer("StreamThingAnalyzer",
    product_to_get = cms.string('m1')
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myout11.root')
)

process.end = cms.EndPath(process.a1*process.out)
