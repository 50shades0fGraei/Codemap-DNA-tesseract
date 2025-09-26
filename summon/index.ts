// summon/index.ts
import { resolveAddress } from './address'
import { validateGlyph } from './glyph'

export function summon({ segment, strand, traits, cyclone }) {
  const address = resolveAddress(segment, strand)
  const isValid = validateGlyph({ segment, traits, cyclone })

  if (!isValid) throw new Error('Invocation rejected: trait or cyclone mismatch')

  return require(address).default()
}