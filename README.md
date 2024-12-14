# grib_to_nc
# py 3.9.9版本
## python处理grib文件(如.GBR2后缀）转换格式为 .nc ；有单个转换、批量转换和批量分块转换(如果文件过大)
--- 
#### - 无论哪种转换方法，都需要修改 `grib_folder_path` 和 `nc_folder_path` 两个参数，填写自己实际的路径文件夹或者也可能是填实际的文件名（对于单个转换来说）
#### - 如果第一次运行报错不要慌，查看报错信息，将缺少的包挨个通过 `pip install xxx` 下载一下即可。
#### - 如果还报错也可能是当前版本的问题，可以用 `pip install --upgrade xxx` 命令更新软件包，查看一下版本是否已是最新。

> 如果有优化方法（尤其是批量分块转换）烦请不吝赐教（q485165007）
> 如果有需要帮助的也可以交流一下（free~）
