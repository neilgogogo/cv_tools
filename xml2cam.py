import os
import cv2
import numpy as np

def load_params(Calibration_Data, factor=1):
    extlist = []
    dislist = []
    intlist = []
    for cam in range(1,105):
        extrinsics_xmlfile = os.path.join(Calibration_Data, str(cam), 'extrinsics.xml')
        intrinsic_xmlfile = os.path.join(Calibration_Data, str(cam), 'intrinsic.xml')

        extrinsics_fs = cv2.FileStorage(extrinsics_xmlfile, cv2.FileStorage_READ)
        R = extrinsics_fs.getNode('R').mat()
        T = extrinsics_fs.getNode('T').mat()
        intrinsic_fs = cv2.FileStorage(intrinsic_xmlfile, cv2.FileStorage_READ)
        K = intrinsic_fs.getNode('M').mat()
        D = intrinsic_fs.getNode('D').mat()

        if factor != 1:
            K[0:2, 0:3] = K[0:2, 0:3] * 1.0 / factor

        extlist.append(np.concatenate((R, T), axis=1))
        dislist.append(D)
        intlist.append(K)

    extlist = np.stack(extlist, 0)
    dislist = np.stack(dislist, 0)
    intlist = np.stack(intlist, 0)
    return extlist, dislist, intlist

Calibration_Data = 'dataset/tencent-mocap/Calibration_Data/Calib_20211216_0.9'
load_params(Calibration_Data)

