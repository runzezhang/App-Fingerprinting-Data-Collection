Team Members
-----------

- Binhan Wang
- Menghua Liu
- Wenjie Li
- Runze Zhang
- Hafez Eslami Manoochehri

Project Structure
-----------

    Group9_Final_Project
    ├── README.md               # Current readme file.
    ├── Group9Presentation.pptx # PPT for presentation.
    ├── pcap_parser.py          # model to extract features from a single pcap file
    ├── data_parser.py          # model to parse all the pcap files and generate input data file
    ├── training.py             # train model using input data and get accuracy  
    └── app_data                # some data for running the code
        ├── communication       # pcap files with label communication
        ├── finance             # pcap files with label finance
        └── social              # pcap files with label social

Requirement
-----------

1. Install tshark (https://www.wireshark.org/docs/man-pages/tshark.html)
2. Python 3.6.2
3. pip3
    - pyshark
    - numpy
    - sklearn

Running instruction
-----------

Feature extractions and generate input file for ML

    python3 data_parser.py --input app_data --output output.csv

Training with svm

    python3 training.py --input output.csv

Sample output

    Round 1 - kernel='rbf', probability=True
    Accuracy: 0.93 (+/- 0.04)
    Round 2 - kernel='sigmoid', probability=True
    Accuracy: 0.74 (+/- 0.10)
    Round 3 - kernel='poly', probability=True, degree=3
    Accuracy: 0.87 (+/- 0.06)
    Round 4 - kernel='poly', probability=True, degree=8
    Accuracy: 0.80 (+/- 0.08)
    Round 5 - kernel='poly', C=10, probability=True, degree=8
    Accuracy: 0.84 (+/- 0.08)    
