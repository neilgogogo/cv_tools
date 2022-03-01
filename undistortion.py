def undistort_images_1(Calibration_Data, image_Data):
    os.makedirs(os.path.join(os.path.split(image_Data)[0], 'Images'), exist_ok=True)
    for cam in range(1,105):
        intrinsic_xmlfile = os.path.join(Calibration_Data, str(cam), 'intrinsic.xml')
        intrinsic_fs = cv2.FileStorage(intrinsic_xmlfile, cv2.FileStorage_READ)
        K = intrinsic_fs.getNode('M').mat()
        D = intrinsic_fs.getNode('D').mat()
        
        srcImag_dir = os.path.join(image_Data, f'image.cam{str(cam).zfill(2)}_000000.jpg')
        dstImag_dir = os.path.join(os.path.split(image_Data)[0], 'Images', f'cam{str(cam).zfill(2)}.jpg')
        srcImg = cv2.imread(srcImag_dir)
        dstImg = cv2.undistort(srcImg, K, D, None, K)
        cv2.imwrite(dstImag_dir, dstImg)
    print("undistort直接对图像去畸变!")

    
    
# Calibration_Data = 'dataset/tencent-mocap/Calibration_Data/Calib_20211216_0.9'
# image_Data = 'dataset/tencent-mocap/Rebuild_Data/20220110/0'
# undistort_images_1(Calibration_Data, image_Data) # use this--- 可能有黑边
