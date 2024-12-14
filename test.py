import gc

import cfgrib
import xarray as xr
import os

# 定义输入的GRIB文件所在文件夹路径和输出的NC文件保存文件夹路径
grib_folder_path = 'D:/tools/PyCharm 2023.1/grib_to_nc/202410grib/test'
nc_folder_path = 'D:/tools/PyCharm 2023.1/grib_to_nc/202410grib/test_output'

# 检查输入的GRIB文件夹是否存在，如果不存在则创建
if not os.path.exists(grib_folder_path):
    raise FileNotFoundError(f"输入的GRIB文件所在文件夹 {grib_folder_path} 不存在，请检查文件夹路径是否正确。")

# 检查输出的NC文件夹是否存在，如果不存在则创建
if not os.path.exists(nc_folder_path):
    os.makedirs(nc_folder_path)

# 遍历GRIB文件夹下的所有文件
for file_name in os.listdir(grib_folder_path):
    if file_name.endswith('.GRB2'):
        # 构建完整的GRIB文件路径和对应的NC文件路径
        grib_file_path = os.path.join(grib_folder_path, file_name)
        nc_file_name = os.path.splitext(file_name)[0] + '.nc'
        nc_file_path = os.path.join(nc_folder_path, nc_file_name)

        try:
            # 读取GRIB文件
            grib_data = cfgrib.open_datasets(grib_file_path)[0]
            # 将数据转换为NetCDF格式并保存
            grib_data.to_netcdf(nc_file_path)
            # 手动释放内存，将数据对象引用设为None
            grib_data = None
            # 运行垃圾回收，强制立即回收内存（可选，Python会自动进行垃圾回收，但可以主动触发）
            gc.collect()
            print(f"成功将 {grib_file_path} 转换为 {nc_file_path}")
        except Exception as e:
            print(f"cfgrib库解析 {grib_file_path} 文件时出现错误: {e}")
        except Exception as e:
            print(f"转换 {grib_file_path} 文件过程中出现未知错误: {e}")

