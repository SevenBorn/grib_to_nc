import cfgrib
import xarray as xr
import os

# 定义输入的GRIB文件路径和输出的NC文件路径
grib_file_path = 'D:/tools/PyCharm 2023.1/grib_to_nc/202410grib/202410left/Z_NWGD_C_BABJ_20241005025129_P_RFFC_SCMOC-ERH_202410050800_24003.GRB2'
nc_file_path = 'D:/tools/PyCharm 2023.1/grib_to_nc/202410grib/left_output'

try:
    # 检查输入的GRIB文件是否存在
    if not os.path.exists(grib_file_path):
        raise FileNotFoundError(f"输入的GRIB文件 {grib_file_path} 不存在，请检查文件路径是否正确。")

    # 读取GRIB文件
    grib_data = cfgrib.open_datasets(grib_file_path)[0]
    # 将数据转换为NetCDF格式并保存
    grib_data.to_netcdf(nc_file_path)
    print(f"成功将 {grib_file_path} 转换为 {nc_file_path}")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"cfgrib库解析文件时出现错误: {e}")
except Exception as e:
    print(f"转换过程中出现未知错误: {e}")