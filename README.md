# UndistortX
OpenCV를 이용한 카메라 캘리브레이션 및 렌즈 왜곡 보정 프로그램

# Camera calibration

카메라 캘리브레이션 수행 과정

![화면 캡처 2025-04-05 211815](https://github.com/user-attachments/assets/afc89d70-20e5-4dee-86c0-ab1ff99e88ba)

카메라 캘리브레이션 결과

```
## Camera Calibration Results
* The number of selected images = 11
* RMS error = 0.6689116204807904
* Camera matrix (K) =
[[627.9110147    0.         628.71703011]
 [  0.         637.91247595 405.01966982]
 [  0.           0.           1.        ]]
* Distortion coefficient (k1, k2, p1, p2, k3, ...) = [ 0.00645102  0.08530672 -0.00891972  0.00220997 -0.09186439]
```

# Lens distortion correction

correction 적용 전

![O](https://github.com/user-attachments/assets/93ed0b41-32d4-4240-889a-af9a638bec87)


correction 적용 후

![R](https://github.com/user-attachments/assets/49240692-721e-4bc6-9ad2-07d83f5f071b)

