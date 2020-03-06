# tcb-heatmap
Heatmaps of Transverse Cirrus bands for a year's worth of data. Data downloaded from Phenomena Detection Portal.

## What does this code do?
seasonal.py takes a JSON or multiple JSON files from the data folder as inputs.

Each JSON file has longitude/latitude polygon information.

The code calculates the centerpoint of each polygon and visualizes the density of detections for each square lat/long.

## Visualization Outputs

### Seasonal
3 month intervals for a year.
![seasonal_combined](https://user-images.githubusercontent.com/46700480/76041169-f9051300-5f16-11ea-9bfd-63e39f23642d.png)

### Hurricane Season
From June 1st to November 30th.
![hurricane](https://user-images.githubusercontent.com/46700480/76041137-f0144180-5f16-11ea-92de-89c626d0e142.png)

### Ocean Detections during Hurricane Season
From June 1st to November 30th.
![hurricane_oceans](https://user-images.githubusercontent.com/46700480/76041161-f6a2b900-5f16-11ea-9085-68921887bbdb.png)