export const Jin = {
  order: (segment: string) => stageSegment(segment),
  command: (segment: string, action: string) => executeSegment(segment, action),
  demand: (segment: string, action: string) => overrideSegment(segment, action)
};
