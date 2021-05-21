# https://github.com/wkentaro/gdown

# pip install gdown

import gdown

phase1 = "https://drive.google.com/uc?id=1Y-aDWNMfvgYUb-u-_cqzibZ6ePFOOLGj"
phase2_1 = "https://drive.google.com/u/0/uc?id=1KTV9dmqkv0xrheIOEkPXbqeg36_rXJ_E"
phase2_2 = "https://drive.google.com/u/0/uc?id=1cAcnyBTO5JeB2zSaEoGBWf0Jd-jAnguS"

output1 = "phase1"
output2_1 = "phase2_1"
output2_2 = "phase2_2"

gdown.download(phase1, output1, quiet=False)
gdown.download(phase2_1, output2_1, quiet=False)
gdown.download(phase2_2, output2_2, quiet=False)