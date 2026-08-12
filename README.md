# Scientists Who Code: reproducible environmental data workflow

**A fully reproducible, beginner-friendly environmental data workflow: obtain openly available data, document decisions, run an analysis, interpret results, and collaborate through GitHub.**

This repository has two connected layers: a learner-friendly template you can fork for a new project, and a completed exemplar using public USGS streamflow observations from Boulder Creek, Colorado. The analysis is deliberately modest: its value is in making each decision visible and repeatable.

## What you will build

You will download one summer of daily streamflow, check and document it, summarize it, and create a transparent time-series figure. After running the notebooks, the result is saved to `outputs/figures/boulder_creek_streamflow.png`.

![Generated Boulder Creek streamflow result](outputs/figures/boulder_creek_streamflow.png)

## Who this is for

Learners new to coding, instructors running workshops, project managers coordinating data work, and community collaborators who want to see where data and decisions live. You do not need to understand every line to begin.

## Learning objectives

- Use a small Git/GitHub workflow to collaborate safely.
- Create a shared, pinned Python environment.
- Record data provenance and inspect data quality.
- Read and run notebooks, then turn repeatable work into source code.
- Create a defensible figure and summary table.
- State interpretations, limitations, and contribution expectations clearly.

## Quick start

From a fresh clone, run:

```bash
conda env create -f environment.yml
conda activate scientists-who-code
python -m pip install -e .
python src/download.py
python -m pytest
jupyter lab
```

Open the notebooks in numeric order. Alternatively, regenerate the completed exemplar without Jupyter:

```bash
python src/processing.py
python src/plotting.py
```

The downloader calls the public USGS Water Services API and records its URL, access date, and query parameters in `data/raw/provenance.json`. Raw and derived data are intentionally ignored by Git; anyone can regenerate them.

## Project map

| Location | Purpose |
| --- | --- |
| `data/raw/` | Downloaded source files; never hand-edit or commit them. |
| `data/processed/` | Reproducible intermediate tables generated from raw data. |
| `src/` | Reusable download, processing, and plotting functions. |
| `notebooks/` | The guided learning narrative, in execution order. |
| `outputs/figures/` | Regenerated figures for reports and discussion. |
| `docs/` | Governance guidance and workshop facilitation materials. |
| `tests/` | Small checks that protect the transformation rules. |

## Reproducibility checklist

- [x] Environment versions are declared in `environment.yml`.
- [x] The data source, access date, URL, and parameters are written at download time.
- [x] Raw data are downloaded rather than committed.
- [x] Processed tables and figures can be regenerated from source.
- [x] Tests cover the main cleaning rule.
- [x] The final notebook states what the data can and cannot support.

## Data governance and ethics

This is an exercise using public USGS data. “Open” does not mean every dataset is appropriate to collect, publish, or reuse without context. Do not use this template unchanged for Tribal, culturally sensitive, personally identifiable, endangered-species, or otherwise restricted data. Start with the [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/care), applicable Tribal governance, consent processes, and project-specific agreements. See [data governance guidance](docs/data-governance.md) before adapting this workflow.

## How to use it in a workshop

For a 60–90 minute session, use `00_start_here`, run the download and cleaning cells together, then have teams discuss the figure and limitations. For a multi-session series, assign one notebook per session and use a pull request to practice review. The [facilitator guide](docs/facilitator-guide.md) includes timing, roles, common sticking points, and an inclusive review activity.

## Contributing

Contributions from every skill level are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before opening an issue or pull request.

## Citation and license

See [CITATION.cff](CITATION.cff). This project is released under the [MIT License](LICENSE).
