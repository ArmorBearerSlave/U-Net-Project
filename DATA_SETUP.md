# Data Directory Structure

This project expects data to be organized as follows:

```text
U-Net-Project/
├── data/                    # Add this folder locally (gitignored)
│   ├── raw/                 # Original images
│   ├── processed/           # Preprocessed images
│   ├── train/              # Training set
│   ├── val/                # Validation set
│   └── test/               # Test set
├── src/                    # Python source code (tracked in git)
├── notebooks/              # Jupyter notebooks (tracked in git)
├── models/                 # Saved model files
│   └── final_model.pth     # Only final model tracked
└── README.md
```

## Setting Up Your Data

1. **Create the data directory locally:**

   ```bash
   mkdir -p data/{raw,processed,train,val,test}
   ```

2. **Copy or link your dataset:**

   ```bash
   # Option A: Copy files
   cp -r /path/to/your/desktop/dataset/* data/raw/
   
   # Option B: Create symbolic link
   ln -s /path/to/your/desktop/dataset data/raw
   ```

3. **Download sample data (for other users):**
   - Provide download links or scripts for public datasets
   - Include data preparation instructions
   - Consider using sample/demo data for testing

## Data Sources

- **Training Data:** [Provide source/download link]
- **Sample Data:** Include small sample files for testing
- **Data Format:** Describe expected file formats and structure

## Note for Contributors

Large datasets are not included in this repository. Please:

1. Follow the directory structure above
2. Use the provided data loading scripts
3. Ensure your local `data/` folder matches the expected structure
