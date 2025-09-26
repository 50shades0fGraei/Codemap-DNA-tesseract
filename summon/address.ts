import segments from '../config/segments.json'

export function resolveAddress(segment: string, strand: string): string {
  const entry = segments[segment]
  if (!entry || entry.strand !== strand) {
    throw new Error(`Invalid segment or strand: ${segment} / ${strand}`)
  }
  return `../strands/${strand}/${entry.function}`
}