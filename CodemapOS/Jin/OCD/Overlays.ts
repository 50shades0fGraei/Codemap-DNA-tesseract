export function validateEmotion(segment: string, biometric: BiometricData): boolean {
  // Check typing rhythm, pressure, mistake handling, proofreading
  return biometric.traits.includes("discernment") && biometric.rhythm === "reflective";
}
