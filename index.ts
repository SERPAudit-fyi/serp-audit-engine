#!/usr/bin/env node

interface SERPAuditInput {
  domain: string;
  auditType: string;
  seoScore: number;
  technicalSEO: number;
  geoScore: number;
  aiVisibility: number;
  contentScore: number;
  auditCoverage: number;
}

interface SERPAuditOutput {
  domain: string;
  auditType: string;
  seoScore: number;
  technicalSEOScore: number;
  geoScore: number;
  aiVisibilityScore: number;
  contentScore: number;
  auditCoverageScore: number;
  overallAuditIndex: number;
  priorityAction: string;
  visibilityPlatforms: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    seo: "SEO",
    technicalSEO: "Technical SEO",
    geo: "GEO",
    aiVisibility: "AI Visibility",
    content: "Content",
    auditCoverage: "Audit Coverage",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getVisibilityPlatforms(seo: number, ai: number): Record<string, number> {
  return {
    "Google Search": Math.min(100, Math.round(seo * 1.0)),
    "ChatGPT": Math.min(100, Math.round(ai * 1.0)),
    "Gemini": Math.min(100, Math.round(ai * 1.0)),
    "Perplexity": Math.min(100, Math.round(ai * 1.0)),
  };
}

export function runSERPAudit(input: SERPAuditInput): SERPAuditOutput {
  const scores = {
    seo: input.seoScore,
    technicalSEO: input.technicalSEO,
    geo: input.geoScore,
    aiVisibility: input.aiVisibility,
    content: input.contentScore,
    auditCoverage: input.auditCoverage,
  };
  const overallAuditIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    domain: input.domain,
    auditType: input.auditType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" "),
    seoScore: input.seoScore,
    technicalSEOScore: input.technicalSEO,
    geoScore: input.geoScore,
    aiVisibilityScore: input.aiVisibility,
    contentScore: input.contentScore,
    auditCoverageScore: input.auditCoverage,
    overallAuditIndex,
    priorityAction: getPriorityAction(scores),
    visibilityPlatforms: getVisibilityPlatforms(input.seoScore, input.aiVisibility),
  };
}

const args = process.argv.slice(2);
const domain = args[0] || "domain.com";
const auditType = args[1] || "technical-seo";
const seoScore = parseInt(args[2]) || 88;
const technicalSEO = parseInt(args[3]) || 82;
const geoScore = parseInt(args[4]) || 85;
const aiVisibility = parseInt(args[5]) || 78;
const contentScore = parseInt(args[6]) || 90;
const auditCoverage = parseInt(args[7]) || 84;

const result = runSERPAudit({
  domain, auditType, seoScore, technicalSEO,
  geoScore, aiVisibility, contentScore, auditCoverage,
});

console.log(`Domain: ${result.domain}`);
console.log(`Audit Type: ${result.auditType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`SEO Score:                     ${result.seoScore}/100  [${getStatus(result.seoScore)}]`);
console.log(`Technical SEO Score:           ${result.technicalSEOScore}/100  [${getStatus(result.technicalSEOScore)}]`);
console.log(`GEO Score:                     ${result.geoScore}/100  [${getStatus(result.geoScore)}]`);
console.log(`AI Visibility Score:           ${result.aiVisibilityScore}/100  [${getStatus(result.aiVisibilityScore)}]`);
console.log(`Content Score:                 ${result.contentScore}/100  [${getStatus(result.contentScore)}]`);
console.log(`Audit Coverage Score:          ${result.auditCoverageScore}/100  [${getStatus(result.auditCoverageScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Audit Index:           ${result.overallAuditIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nVisibility Platforms:");
Object.entries(result.visibilityPlatforms).forEach(([platform, score]) => {
  console.log(`  ${platform.padEnd(22)} ${score}/100`);
});
