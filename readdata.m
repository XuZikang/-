%% 读取目标文件夹下的所有文件名单
fileList = dir(['F:\2018暑假工作\人体平衡性\', '*.csv']);
len = length(fileList);
nameList = ["open" "close" "noise" "left" "right" "count" "finger" "sponge" "rotate"];
%% 新建结构体，用于存储数据
wholeDataset = struct('open', {}, 'close', {}, 'noise', {}, 'left', {}, 'right', {}, 'count', {}, 'finger', {}, 'sponge', {}, 'rotate', {});

for i =1:len
    eval('wholeDataset(1).'+ nameList(i) + '=csvread(fileList(i).name, 6, 0, [6, 0, 30004, 2])');
end
