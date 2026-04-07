keep_orig_copy：在将WSI拆分为训练集、验证集和测试集时，是移动还是复制。
        wsi_train：将创建用于存放WSI用于培训的地点。
        wsi_val：创建用于存储 WSI 以供验证的位置。
        wsi_test：创建用于存储WSI测试的地点。
        类：数据集中类的名称。
        all_wsi：WSI按类别分类的子文件夹位置。
        val_wsi_per_class：验证集中每个类别使用的WSI数量。
        test_wsi_per_class：测试集中每个类别使用的 WSI 数量。
        labels_train：用于存储培训用CSV文件标签的位置。
        labels_test：存放CSV文件标签以便测试的地方。
        labels_val：存储CSV文件标签以便验证的地方。