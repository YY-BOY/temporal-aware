#!/usr/bin/env python3
"""
Script to rename PDF files with more descriptive names
"""

import os
from pathlib import Path

papers_dir = Path("papers")

# Mapping: old_filename -> new_filename
rename_map = {
    # 2024-2025 Temporal Works
    "liu2025mlrg_CVPR2025.pdf": "Liu_2025_MLRG_Enhanced_Contrastive_Learning_Multi_View_Longitudinal_CXR_CVPR.pdf",
    "wang2024hergen_ECCV2024.pdf": "Wang_2024_HERGen_History_Enhanced_Radiology_Report_Generation_Longitudinal_ECCV.pdf",
    "kim2024ehrxdiff_CHIL2025.pdf": "Kim_2024_EHRXDiff_Predicting_Temporal_Changes_CXR_from_EHR_CHIL.pdf",
    "atici2024tibix_MICCAI2024.pdf": "Atici_2024_TiBiX_Temporal_Bidirectional_XRay_Report_Generation_MICCAI.pdf",
    "xie2024cxrtft.pdf": "Xie_2024_CXR_TFT_MultiModal_Temporal_Fusion_Transformer_CXR_Trajectories.pdf",

    # Transformer Architectures
    "sriram2025gitcxr.pdf": "Sriram_2025_GIT_CXR_End_to_End_Transformer_Report_Generation.pdf",
    "dosovitskiy2020vit.pdf": "Dosovitskiy_2020_ViT_Vision_Transformer_Image_Recognition_at_Scale.pdf",

    # Vision-Language Models
    "radford2021clip.pdf": "Radford_2021_CLIP_Contrastive_Language_Image_Pretraining.pdf",

    # Contrastive Learning
    "ouyang2023comet.pdf": "Ouyang_2023_COMET_Hierarchical_Contrastive_Framework_Medical_Time_Series.pdf",
    "lotzsch2024spatiotemporal.pdf": "Lotzsch_2024_Spatiotemporal_Representation_Learning_Medical_Image_Time_Series.pdf",
    "pang2023longitudinal.pdf": "Pang_2023_Longitudinal_Data_Semantic_Similarity_Reward_CXR_Report_Generation.pdf",

    # Evaluation Metrics
    "jain2021radgraph.pdf": "Jain_2021_RadGraph_Extracting_Clinical_Entities_Relations_Radiology_Reports.pdf",
    "smit2020chexbert.pdf": "Smit_2020_CheXbert_Automatic_Labelers_Expert_Annotations_Radiology_Reports.pdf",

    # Datasets
    "boecking2022mscxrt.pdf": "Boecking_2022_MS_CXR_T_Text_Semantics_Biomedical_Vision_Language_Processing.pdf",
    "irvin2019chexpert.pdf": "Irvin_2019_CheXpert_Large_Chest_Radiograph_Dataset_Uncertainty_Labels.pdf",

    # Advanced Methods
    "yan2024llmrg4.pdf": "Yan_2024_LLM_RG4_Flexible_Factual_Radiology_Report_Generation.pdf",
}

def main():
    print("Renaming PDF files to more descriptive names...\n")

    renamed = 0
    skipped = 0

    for old_name, new_name in rename_map.items():
        old_path = papers_dir / old_name
        new_path = papers_dir / new_name

        if not old_path.exists():
            print(f"⚠ Skipping (not found): {old_name}")
            skipped += 1
            continue

        if new_path.exists():
            print(f"⚠ Skipping (target exists): {new_name}")
            skipped += 1
            continue

        try:
            os.rename(old_path, new_path)
            print(f"✓ Renamed: {old_name}")
            print(f"       -> {new_name}\n")
            renamed += 1
        except Exception as e:
            print(f"✗ Failed: {old_name} - {str(e)}\n")

    print(f"{'='*80}")
    print(f"Renaming complete!")
    print(f"Renamed: {renamed}")
    print(f"Skipped: {skipped}")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
