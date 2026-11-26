# Reproducibility

Run the exact finite checks with Python 3.11 or later. The replay needs only the standard library.

```sh
python3 -I verification/src/replay.py
```

Dijkstra's algorithm computes the least cost of single-cell pushes and adjacent swaps on one grid. Independently, all labeled token destinations are enumerated, aggregated by source and target runs, and evaluated by the transport cost. The comparison covers all binary pairs on grids with one to four cells over a unit interval, all ternary pairs on one to three unit-interval cells, and all binary pairs on one to three cells over length 3/2. The replay also tests the original half-unit grid and the attaining three moves at letter distance 1/3. [Recorded results](verification/results/replay.txt).

Open the single HTML file in the offline explorer ZIP in a browser. It computes exact rational costs on four grids and displays the chosen chain. The [visualization notes](visualization/README.md) explain the controls and GIF renderer. The [paper build instructions](paper/BUILD.md) describe compilation.
