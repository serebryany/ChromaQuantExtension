# ChromaQuantExtension
Extension and Analysis of ChromaQuant by Julia Hancock (JnliaH). Created for CHEME 546 Winter 2025. 

### Overview

ChromaQuantExtension is a software tool designed to empirically assess the accuracy of ChromaQuant, an automated solution for gas chromatographic peak assignment and quantification. ChromaQuant simplifies the process of integrating gas chromatography (GC) data from multiple sources, specifically when using flame ionization and thermal conductivity detectors for quantitative analysis that must be labeled using mass spectrometric data.

The primary goals of ChromaQuantExtension are:

- *Accuracy Evaluation*: Comparing the output of ChromaQuant against manually calculated product composition data to measure accuracy.

- *Machine Learning Integration*: Developing an ML-based alternative to ChromaQuant to automate product composition prediction.

### Features

Automated Comparison: Takes ChromaQuant-generated CSV outputs and manually curated product composition sheets, performing statistical analysis on the accuracy of ChromaQuant.

Customizable Metrics: Users can define their own evaluation metrics to assess ChromaQuant's performance.

Machine Learning Model Training: Enables users to train models for predicting product composition based on GC data.

User-Friendly Interface: Simplifies workflow for both experimental chemists and computational scientists.

### Developers:
- Franklin Guevara 
- Tata Serebryany
- Enisha Sehgal
- Mariya Hyrb
