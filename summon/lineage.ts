import processIndex from '../config/processIndex.json'
import segments from '../config/segments.json'
import fs from 'fs'

export function updateLineage(segment: string) {
  const entry = segments[segment]
  const lineageEntry = {
    program: entry.program,
    process: entry.process,
    function: entry.function,
    pipeline: entry.pipeline,
    strand: entry.strand,
    invoked: new Date().toISOString()
  }

  processIndex[segment] = lineageEntry
  fs.writeFileSync('./config/processIndex.json', JSON.stringify(processIndex, null, 2))
}