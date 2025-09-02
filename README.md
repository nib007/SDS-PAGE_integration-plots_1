In this repository are a python code where you paste in Band %, Lane % of a protein detected with total protein stain e.g. commassie, silver. The results can be many lane results integrated in for example Image Lab at different pH, salt and a additive e.g. Urea. Program then computes plots of the combined effect as the three variables (if any).

Summary: Python code where you paste in Band %, Lane % of a protein detected, plots of the combined effect as the three variable

Example input (is "^t" tab-separated) for 4 lanes exported data from Image Lab. The lanes was annotated as TEV-protein, Enz His-Enz. Enz=cleaved protein, and His-Enz=Uncleaved protein.
Lane	Band No.	Band-Lane	Condition	pH	Salt	Urea	Protein	Protein Mol. Wt. (KDa)	Abs. Quant. (ug)	Rel. Quant.	Band %	Lane %
2	1	2-1	Not treated His-Enz	-	-	-		79.7	N/A	0.2	5.1	2.6
2	2	2-2	Not treated His-Enz	-	-	-	TEV protease	28.3	2.1	1.2	29.1	14.8
2	3	2-3	Not treated His-Enz	-	-	-		23.6	N/A	0.4	10.0	5.1
2	4	2-4	Not treated His-Enz	-	-	-	His-Enz	16.6	5.1	1.8	44.6	22.8
2	5	2-5	Not treated His-Enz	-	-	-	Enz	14.7	N/A	0.5	11.2	5.7
3	1	3-1	Test condition	6.0	0.1	0.0		79.7	N/A	0.2	3.8	2.2
3	2	3-2	Test condition	6.0	0.1	0.0	TEV protease	27.9	2.8	1.4	32.9	19.0
3	3	3-3	Test condition	6.0	0.1	0.0		23.3	N/A	0.4	9.8	5.7
3	4	3-4	Test condition	6.0	0.1	0.0	His-Enz	16.4	4.4	1.7	41.1	23.7
3	5	3-5	Test condition	6.0	0.1	0.0	Enz	14.6	N/A	0.5	12.4	7.2
4	1	4-1	Test condition	6.0	0.1	0.5		79.7	N/A	0.2	3.7	2.1
4	2	4-2	Test condition	6.0	0.1	0.5	TEV protease	28.0	3.0	1.4	34.1	19.1
4	3	4-3	Test condition	6.0	0.1	0.5		23.3	N/A	0.4	9.7	5.4
4	4	4-4	Test condition	6.0	0.1	0.5	His-Enz	16.5	4.8	1.8	43.4	24.3
4	5	4-5	Test condition	6.0	0.1	0.5	Enz	14.6	N/A	0.4	9.1	5.1
