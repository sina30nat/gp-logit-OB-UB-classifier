# OB/UB Classification Tool

This repository contains a **Streamlit-based GUI prototype** for classifying underground drillholes as:

- **Balanced**
- **Overbreak-Prone**
- **Underbreak-Prone**

using a trained **Optimised LR** , developed from operational, geotechnical, and design data.

---

## How to Run

> These instructions assume Python is installed. Use [python.org](https://www.python.org/downloads/) if needed.

### 1. Clone the Repository

```bash
git clone https://github.com/sina30nat/OB-UB-classifier.git
cd OB-UB-classifier


2. Install Requirements:
pip install -r requirements.txt

3. Launch the App
streamlit run gui_classifier.py
It will open automatically in your default browser at: http://localhost:8501

Features
Input Form: Enter 16 drill and blast design parameters

Real-time Prediction: Uses a pre-trained Tuned Logistic Regression model

Design Warnings: Examples (e.g., excessive DFE, short holes, primer location)

Lightweight GUI: Built with Streamlit for accessibility

 Repository Structure
gp-logit-classifier/
│
├── gui_classifier.py             # Streamlit app script
├── requirements.txt              # List of required Python packages
├── models/
│   └── logistic_regression_tuned_fitted.joblib  # Trained model
└── README.md                     # this file


Model Info
Base model: Logistic Regression (sklearn)

Tuned via: GridSearchCV with cross-validation

Features: 16 operational, design, and geotechnical parameters

Use case: Supports prediction of OB UB classification for stope design evaluation in underground mining

Citation
If used in academic work, please cite the associated publication
GitHub repository: https://github.com/sina30nat/gp-logit-OB-UB-classifier

This prototype is provided for research and demonstration purposes. It is not intended for direct production use without further validation.

more information about different features in the GUI can be found below:

Variable Number	Parameter	Symbol	Explanation
1	Powder Factor	PF
Amount of explosive used per volume of rock (Kg/tonne)

2	Explosive Type	ET	3 types:
Density of 0.8 g/cc, 1.0 g/cc and 1.2g/cc

3	Distance from end of drillhole to stope shape	DFE
The distance from the end of the drillhole to the designed/planned stope shape (m)

4	Spacing/ Burden ratio SB	
Burden: Distance from point of blast to the free face (m)
Spacing: Distance between adjacent blastholes (m)

5	Primer Location	PL	
Distance from the last primer to the end of the drillhole (m)

6	Void Raio	VR	
Ratio of void in relation to the blasted rock (%) (Chandrakar, Paul, & Sawmliana, 2021)

7	Drillhole Blast/Firing Sequence	HFS	Blasting sequence for each drillhole within a ring

8	Ring Blast/Firing Sequence	RFS	
Blasting sequence for each ring within a blast

9	Blasthole Angle	ANG	
Angle between blasthole and stope wall (degree)

10	Drillhole Type	HT	
Type of Drillhole: HW, FW, Main or Easer drillhole (FW holes: 2, Main holes:3, HW holes:4, Easer holes:5)

11	Hole Length	HL	
Designed Length of Drillhole

12	Breakthrough or non-breakthrough drillhole	BT
Whether is drillhole breakthrough into the drift or level above or not (value of 1 for breakthrough and 0 for non-breakthrough)


13	Fracture Frequency	FF	
Number of fractures, joints, or discontinuities per unit length (O'Hara, Jacobi, & Sheets, 2017)

			
14	Effective Radius Factor 1 ERF
Distance from the centre point in stope to the stope wall (m)
			


15	Rock Quality Designation2 RQD	
RQD %=((Sum of lengths of core pieces ≥10 cm)/(Total length of core run))×100

16	Stress Ratio3	SR	
SR=((S1))/((S3))

			

