from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="serp-audit-engine",
    version="1.0.0",
    author="SERPAudit.fyi",
    author_email="info@serpaudit.fyi",
    description="SERP Audit Engine is an AI-powered SEO and search visibility audit framework that helps businesses identify website issues and improve their visibility across traditional search and AI platforms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://serpaudit.fyi",
    project_urls={
        "Homepage": "https://serpaudit.fyi",
        "GitHub": "https://github.com/SERPAudit-fyi/serp-audit-engine",
        "Documentation": "https://serp-audit-engine.readthedocs.io",
        "PyPI": "https://pypi.org/project/serp-audit-engine",
    },
    py_modules=["serp_audit"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    ],
    keywords=[
        "serp-audit",
        "seo-audit",
        "technical-seo",
        "geo-audit",
        "ai-search-visibility",
        "ai-visibility-scoring",
        "website-audit",
        "chatgpt-visibility",
        "gemini-visibility",
        "serpaudit",
    ],
    entry_points={
        "console_scripts": [
            "serp-audit=serp_audit:main",
        ],
    },
)
