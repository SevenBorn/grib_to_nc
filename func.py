import gc
import cfgrib
import psutil
import xarray as xr
import os

# 获取当前Python进程对象
process = psutil.Process()

# 定义输入的GRIB文件所在文件夹路径和输出的NC文件保存文件夹路径
grib_folder_path = 'D:/tools/PyCharm 2023.1/grib_to_nc/202410grib/202410left'
nc_folder_path = 'D:/tools/PyCharm 2023.1/grib_to_nc/202410grib/left_output'

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

        chunk_list = []
        try:
            # 分块读取GRIB文件，此处分块大小可根据实际情况调整，这里示例为latitude和longitude维度各80
            grib_data_chunks = cfgrib.open_datasets(grib_file_path, chunks={'latitude': 80, 'longitude': 80})
            for index, chunk in enumerate(grib_data_chunks):
                # 在这里可以对每个分块数据进行进一步处理，如果不需要额外处理可直接添加到列表
                processed_chunk = chunk  # 示例中简单将分块数据添加，实际可按需添加处理逻辑
                chunk_list.append(processed_chunk)
                # 每处理5个分块后，检查内存使用情况并进行垃圾回收，可调整数值
                if (index + 1) % 5 == 0:
                    mem_usage = process.memory_info().rss / 1024 / 1024  # 获取内存使用量（单位：MB）
                    print(f"正在处理文件 {grib_file_path}，已处理 {index + 1} 个分块，当前内存占用: {mem_usage} MB")
                    gc.collect()
            # 拼接分块数据为一个完整的数据集
            merged_data = xr.concat(chunk_list, dim='latitude')

            # 将拼接后的数据转换为NetCDF格式并保存
            merged_data.to_netcdf(nc_file_path)

            # 手动释放内存，将数据对象引用设为None
            merged_data = None
            # 运行垃圾回收，强制立即回收内存（可选，Python会自动进行垃圾回收，但可以主动触发）
            gc.collect()
            print(f"成功将 {grib_file_path} 转换为 {nc_file_path}")
        except Exception as e:
            print(f"cfgrib库解析 {grib_file_path} 文件时出现错误: {e}")
        except Exception as e:
            print(f"转换 {grib_file_path} 文件过程中出现未知错误: {e}")