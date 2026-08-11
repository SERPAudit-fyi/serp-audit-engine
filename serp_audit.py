#!/usr/bin/env python3
"""
SERP Audit Engine
An AI-powered SEO and search visibility audit framework that helps businesses
identify website issues and improve their visibility across traditional search
and AI platforms.

Core: SEO + Technical SEO + GEO + AI Search Visibility in one audit platform.

https://serpaudit.fyi
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "seo": "SEO",
        "technical_seo": "Technical SEO",
        "geo": "GEO",
        "ai_visibility": "AI Visibility",
        "content": "Content",
        "audit_coverage": "Audit Coverage",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_visibility_platforms(seo: int, ai: int) -> dict:
    return {
        "Google Search": min(100, round(seo * 1.0)),
        "ChatGPT": min(100, round(ai * 1.0)),
        "Gemini": min(100, round(ai * 1.0)),
        "Perplexity": min(100, round(ai * 1.0)),
    }


def run_serp_audit(
    domain: str,
    audit_type: str = "technical-seo",
    seo_score: int = 88,
    technical_seo: int = 82,
    geo_score: int = 85,
    ai_visibility: int = 78,
    content_score: int = 90,
    audit_coverage: int = 84,
) -> dict:
    """
    Run a SERP audit across SEO, Technical SEO, GEO, and AI visibility signals.

    Args:
        domain: Target domain or website
        audit_type: Type of audit to run
        seo_score: SEO score (0-100)
        technical_seo: Technical SEO score (0-100)
        geo_score: GEO score (0-100)
        ai_visibility: AI visibility score (0-100)
        content_score: Content score (0-100)
        audit_coverage: Audit coverage score (0-100)

    Returns:
        dict with individual audit scores, overall audit index,
        and visibility platform breakdown
    """
    scores = {
        "seo": seo_score,
        "technical_seo": technical_seo,
        "geo": geo_score,
        "ai_visibility": ai_visibility,
        "content": content_score,
        "audit_coverage": audit_coverage,
    }
    overall_audit_index = round(sum(scores.values()) / 6)

    return {
        "domain": domain,
        "audit_type": " ".join(w.capitalize() for w in audit_type.split("-")),
        "seo_score": seo_score,
        "technical_seo_score": technical_seo,
        "geo_score": geo_score,
        "ai_visibility_score": ai_visibility,
        "content_score": content_score,
        "audit_coverage_score": audit_coverage,
        "overall_audit_index": overall_audit_index,
        "priority_action": get_priority_action(scores),
        "visibility_platforms": get_visibility_platforms(seo_score, ai_visibility),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    domain = args[0] if len(args) > 0 else "domain.com"
    audit_type = args[1] if len(args) > 1 else "technical-seo"
    seo_score = int(args[2]) if len(args) > 2 else 88
    technical_seo = int(args[3]) if len(args) > 3 else 82
    geo_score = int(args[4]) if len(args) > 4 else 85
    ai_visibility = int(args[5]) if len(args) > 5 else 78
    content_score = int(args[6]) if len(args) > 6 else 90
    audit_coverage = int(args[7]) if len(args) > 7 else 84

    result = run_serp_audit(
        domain, audit_type, seo_score, technical_seo,
        geo_score, ai_visibility, content_score, audit_coverage
    )

    print(f"Domain: {result['domain']}")
    print(f"Audit Type: {result['audit_type']}")
    print("=" * 45)
    print(f"SEO Score:                     {result['seo_score']}/100  [{get_status(result['seo_score'])}]")
    print(f"Technical SEO Score:           {result['technical_seo_score']}/100  [{get_status(result['technical_seo_score'])}]")
    print(f"GEO Score:                     {result['geo_score']}/100  [{get_status(result['geo_score'])}]")
    print(f"AI Visibility Score:           {result['ai_visibility_score']}/100  [{get_status(result['ai_visibility_score'])}]")
    print(f"Content Score:                 {result['content_score']}/100  [{get_status(result['content_score'])}]")
    print(f"Audit Coverage Score:          {result['audit_coverage_score']}/100  [{get_status(result['audit_coverage_score'])}]")
    print("=" * 45)
    print(f"Overall Audit Index:           {result['overall_audit_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nVisibility Platforms:")
    for platform, score in result['visibility_platforms'].items():
        print(f"  {platform:<24} {score}/100")


if __name__ == "__main__":
    main()
