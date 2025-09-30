#!/usr/bin/env python3
"""
Script to download PDFs from arXiv and other sources based on reference.bib
"""

import os
import re
import time
import urllib.request
from pathlib import Path

# Create papers directory
papers_dir = Path("papers")
papers_dir.mkdir(exist_ok=True)

# List of arXiv IDs extracted from reference.bib
arxiv_papers = [
    ("2502.20056", "liu2025mlrg_CVPR2025"),
    ("2407.15158", "wang2024hergen_ECCV2024"),
    ("2409.07012", "kim2024ehrxdiff_CHIL2025"),
    ("2403.13343", "atici2024tibix_MICCAI2024"),
    ("2507.14766", "xie2024cxrtft"),
    ("2501.02598", "sriram2025gitcxr"),
    ("2010.11929", "dosovitskiy2020vit"),
    ("2103.00020", "radford2021clip"),
    ("2310.14017", "ouyang2023comet"),
    ("2403.07513", "lotzsch2024spatiotemporal"),
    ("2307.09758", "pang2023longitudinal"),
    ("2106.14463", "jain2021radgraph"),
    ("2004.09167", "smit2020chexbert"),
    ("2412.12001", "yan2024llmrg4"),
    ("2204.09817", "boecking2022mscxrt"),
    ("1901.07031", "irvin2019chexpert"),
]

def download_arxiv_pdf(arxiv_id, filename):
    """Download PDF from arXiv"""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    output_path = papers_dir / f"{filename}.pdf"

    if output_path.exists():
        print(f"✓ Already exists: {filename}.pdf")
        return True

    try:
        print(f"Downloading {arxiv_id} -> {filename}.pdf ...")

        # Set user agent to avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=30) as response:
            with open(output_path, 'wb') as out_file:
                out_file.write(response.read())

        print(f"✓ Downloaded: {filename}.pdf")
        return True

    except Exception as e:
        print(f"✗ Failed to download {arxiv_id}: {str(e)}")
        return False

def main():
    print(f"Starting download of {len(arxiv_papers)} arXiv papers...")
    print(f"Output directory: {papers_dir.absolute()}\n")

    successful = 0
    failed = 0

    for arxiv_id, filename in arxiv_papers:
        if download_arxiv_pdf(arxiv_id, filename):
            successful += 1
        else:
            failed += 1

        # Be polite to arXiv servers
        time.sleep(3)

    print(f"\n{'='*60}")
    print(f"Download complete!")
    print(f"Successful: {successful}/{len(arxiv_papers)}")
    print(f"Failed: {failed}/{len(arxiv_papers)}")
    print(f"Papers saved to: {papers_dir.absolute()}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()