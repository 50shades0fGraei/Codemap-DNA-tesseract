export function logInvocation(segment: string, mode: string, biometric: BiometricData) {
  const echo = {
    segment,
    mode,
    timestamp: Date.now(),
    emotionalState: biometric.state,
    lineage: "CodemapDNA → Jin → Graei"
  };
  saveToVault(echo);
}
