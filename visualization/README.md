# The two-run transport example

The animation turns a 3D diagram of the optimal plan from AB to BA at letter distance 1/3. Each word has two half-unit runs. Green strands retain their letters, reverse order and contribute the inversion cost. Orange strands contribute the relabeling cost. Strand widths indicate the transported lengths.

Open the self-contained HTML file in the explorer ZIP. Select a cell width, then select a crossing length. The site computes exact fractions, displays the legal moves, and marks the grid that attains the analytical optimum. Rotate with the button, by dragging, or via the arrow keys when the canvas has focus. The transfer table conveys all values independently of the diagram.

Run the GIF renderer with Python and Pillow 13.0. The renderer uses Arial when available and Pillow's bundled font otherwise.
