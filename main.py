from glob import glob
from pathlib import Path

import numpy as np
import open3d as o3d

SAMPLE_PATH = Path("D:/datasets/mes-lidar-test1/lidar")
TARGET_PATH = Path("D:/datasets/mes-lidar-test1/cad")

# =========================
# LiDAR NPZ
# =========================
sample_paths = glob(str(SAMPLE_PATH / "*.npz"))
for sample_path in sample_paths:
    print("LiDAR:", sample_path)
    sample = np.load(sample_path)

    # print(sample.files)
    # for key in sample.files:
    #     print(key, sample[key].shape, sample[key].dtype)

    points = sample["lidar03"]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    o3d.visualization.draw([pcd])
    break

# =========================
# CAD FBX
# =========================
target_paths = glob(str(TARGET_PATH / "*.fbx"))
for target_path in target_paths:
    print("FBX:", target_path)
    mesh = o3d.io.read_triangle_mesh(target_path)

    mesh.compute_vertex_normals()
    
    o3d.visualization.draw([mesh])
    break
