# SentimentTrajectory

**Tracking changes in sentiment across patient feedback using transformer-based natural language processing.**

SentimentTrajectory is a Jupyter Notebook project that analyzes written patient feedback, assigns sentiment labels and confidence scores, and visualizes how sentiment varies across feedback records for individual patients. It combines a pretrained RoBERTa sentiment classifier with pandas-based data processing and Matplotlib plots.

## Overview

A single sentiment label provides a snapshot of one comment. This project adds a longitudinal perspective by grouping comments by patient identifier and plotting sentiment across ordered feedback records. The resulting trajectories can help researchers explore patterns, changes, and potentially important shifts in patient experience.

The notebook demonstrates how to:

- Load patient feedback from a CSV file.
- Apply a pretrained Hugging Face transformer to each comment.
- Calculate class probabilities with softmax and select a sentiment label.
- Record the predicted sentiment and associated score for each feedback entry.
- Join sentiment results to patient identifiers and plot patient-specific sentiment trajectories.
- Annotate chart points with model scores to help interpret predictions.

## Technology stack

| Technology | Purpose |
| --- | --- |
| Python / Jupyter Notebook | Interactive analysis |
| Hugging Face `transformers` | Model and tokenizer loading, inference |
| PyTorch | Transformer model execution |
| `cardiffnlp/twitter-roberta-large-topic-sentiment-latest` | Pretrained sentiment classification model |
| pandas | CSV ingestion and tabular processing |
| NumPy | Score ranking and numerical operations |
| SciPy | Softmax probability calculation |
| Matplotlib | Sentiment trajectory visualization |

## Repository structure

```text
SentimentTrajectory/
├── MNSVsentiment.ipynb    # Sentiment analysis and visualization notebook
├── patientfeedback.csv    # Required input file (provide locally)
└── README.md              # Project documentation
```

**Note:** `patientfeedback.csv` is referenced by the notebook. Supply it locally before running the analysis; it is not guaranteed to be included in the repository.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Mnsvxi/SentimentTrajectory.git
cd SentimentTrajectory
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
```

On Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install notebook pandas numpy scipy matplotlib transformers torch
```

The first notebook run downloads model files from Hugging Face, so an internet connection and adequate disk space are needed.

### 4. Prepare input data

Place a CSV file named `patientfeedback.csv` in the notebook's working directory. The notebook expects these columns:

| Column | Description |
| --- | --- |
| `ID` | Feedback record identifier, used for plotting order |
| `PID` | Patient identifier, used to group feedback records |
| `Comments` | Feedback text to classify |

Example **synthetic** data:

```csv
ID,PID,Comments
101,1132,"The staff were kind and helpful."
102,1132,"I waited much longer than expected."
103,1073,"The appointment went smoothly."
104,1073,"Communication about follow-up was unclear."
```

Use de-identified or synthetic data; do not commit patient-identifying information or protected health information to a public repository.

### 5. Run the notebook

```bash
jupyter notebook MNSVsentiment.ipynb
```

Run cells from top to bottom. The notebook's trajectory visualization currently uses the example patient IDs `1132`, `1073`, `537`, and `312`. Change the `pids` list in the plotting cell to match the identifiers in your dataset.

## How it works

```text
Patient feedback CSV
        |
        v
Load records (ID, PID, Comments)
        |
        v
Tokenize each comment
        |
        v
RoBERTa sentiment inference
        |
        v
Softmax probabilities + label selection
        |
        v
Results table (ID, Sentiment, Score)
        |
        v
Join with patient identifiers
        |
        v
Plot sentiment by ordered feedback ID
```

The notebook loads `cardiffnlp/twitter-roberta-large-topic-sentiment-latest` using `AutoTokenizer`, `AutoConfig`, and `AutoModelForSequenceClassification`. For each comment, it computes class probabilities and selects the highest-scoring label. A custom rule can instead choose the second-ranked label when the top label is `negative or neutral` and the second-ranked score exceeds `0.3`.

**Interpretation:** The `Score` field is the model's probability-like softmax output for the selected label, not a validated clinical confidence measure. The custom override is a heuristic and should be evaluated before use in decision-making.

## Visualizing sentiment trajectories

The notebook maps sentiment categories to an ordered numerical scale:

1. Strongly negative
2. Negative
3. Negative or neutral
4. Positive
5. Strongly positive

For each selected patient, it plots sentiment against feedback `ID` and annotates points with the selected label's score as a percentage. The example visualization uses a 2 × 2 grid of patient-level plots.

**Important:** Ordering by `ID` is not necessarily the same as ordering by time. For a true chronological trajectory, include a timestamp column and sort records by timestamp. The plotted category positions are ordinal and should not be interpreted as equally spaced clinical measurements.

## Outputs

- **Sentiment results DataFrame:** `ID`, `Sentiment`, and `Score` for each processed comment.
- **Patient-level plots:** sentiment categories over ordered feedback records, with score annotations.

The notebook displays results interactively; it does not currently establish a packaged command-line interface or automated export pipeline.

## Limitations and responsible use

- The pretrained model is not specifically validated for clinical patient feedback. Domain-specific language, sarcasm, ambiguous comments, and mixed emotions can reduce accuracy.
- Predictions may vary across model/library versions; record versions for reproducibility.
- The notebook processes comments individually and may need batching and text-length handling for larger datasets.
- Hard-coded patient IDs must be adapted to the input data.
- Sentiment is not a measure of clinical outcomes, quality of care, or patient safety.
- Human review and evaluation against representative, labeled examples are recommended before operational use.
- Patient privacy requirements apply even to exploratory analyses.

## Potential enhancements

- Support chronological timestamps and time-aware trajectory charts.
- Add configurable input paths and patient selection.
- Batch inference for improved performance.
- Add missing-value validation and long-comment handling.
- Export sentiment results and figures.
- Evaluate performance against human-labeled healthcare feedback.
- Add tests, dependency pinning, and reproducible experiment settings.

## Project notebook

Explore the implementation in [MNSVsentiment.ipynb](./MNSVsentiment.ipynb).

## Model attribution

This project uses the pretrained Hugging Face model [`cardiffnlp/twitter-roberta-large-topic-sentiment-latest`](https://huggingface.co/cardiffnlp/twitter-roberta-large-topic-sentiment-latest). Consult its model card for intended use, limitations, and licensing information.

## License

No project license is asserted in this README. Add a `LICENSE` file if you intend to specify terms for reuse or contribution.
