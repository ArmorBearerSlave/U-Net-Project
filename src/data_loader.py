"""
Data loading utilities for U-Net project.
Handles loading and preprocessing of image data from local directories.
"""

import os
import numpy as np
from pathlib import Path
from typing import Tuple, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataLoader:
    """Handles loading of image data for U-Net training."""
    
    def __init__(self, data_root: str = "data"):
        """
        Initialize DataLoader.
        
        Args:
            data_root: Root directory containing data folders
        """
        self.data_root = Path(data_root)
        self.train_dir = self.data_root / "train"
        self.val_dir = self.data_root / "val"
        self.test_dir = self.data_root / "test"
        
        self._check_data_structure()
    
    def _check_data_structure(self):
        """Check if data directories exist and create if missing."""
        required_dirs = [self.train_dir, self.val_dir, self.test_dir]
        
        for dir_path in required_dirs:
            if not dir_path.exists():
                logger.warning(f"Directory {dir_path} not found. Creating...")
                dir_path.mkdir(parents=True, exist_ok=True)
    
    def get_data_info(self) -> dict:
        """Get information about available data."""
        info = {}
        
        for split in ["train", "val", "test"]:
            split_dir = self.data_root / split
            if split_dir.exists():
                files = list(split_dir.glob("*"))
                info[split] = {
                    "count": len(files),
                    "files": [f.name for f in files[:5]]  # Show first 5 files
                }
            else:
                info[split] = {"count": 0, "files": []}
        
        return info
    
    def load_images(self, split: str = "train") -> List[Path]:
        """
        Load image paths from specified split.
        
        Args:
            split: Data split to load ('train', 'val', 'test')
            
        Returns:
            List of image file paths
        """
        split_dir = self.data_root / split
        
        if not split_dir.exists():
            raise FileNotFoundError(f"Data directory {split_dir} not found")
        
        # Common image extensions
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.tiff', '*.bmp']
        image_files = []
        
        for ext in extensions:
            image_files.extend(split_dir.glob(ext))
            image_files.extend(split_dir.glob(ext.upper()))
        
        logger.info(f"Found {len(image_files)} images in {split} split")
        return sorted(image_files)
    
    def setup_data_from_desktop(self, desktop_path: str, copy: bool = False):
        """
        Set up data from desktop location.
        
        Args:
            desktop_path: Path to data on desktop
            copy: If True, copy files; if False, create symbolic links
        """
        desktop_path = Path(desktop_path)
        
        if not desktop_path.exists():
            raise FileNotFoundError(f"Desktop path {desktop_path} not found")
        
        if copy:
            logger.info(f"Copying data from {desktop_path} to {self.data_root}")
            # Implementation for copying files
        else:
            logger.info(f"Creating symbolic link from {desktop_path} to {self.data_root}")
            if self.data_root.exists():
                self.data_root.unlink()
            self.data_root.symlink_to(desktop_path.absolute())


def check_data_availability() -> bool:
    """Check if data is properly set up."""
    loader = DataLoader()
    info = loader.get_data_info()
    
    total_files = sum(split_info["count"] for split_info in info.values())
    
    if total_files == 0:
        logger.error("No data found! Please set up your data directory.")
        logger.info("Run the following commands to set up data:")
        logger.info("1. Create data directories: mkdir -p data/{train,val,test}")
        logger.info("2. Copy your data or create symbolic links")
        return False
    
    logger.info(f"Data found: {info}")
    return True


if __name__ == "__main__":
    # Example usage
    check_data_availability()