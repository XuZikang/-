%% ��ȡĿ���ļ����µ������ļ�����
fileList = dir(['F:\2018��ٹ���\����ƽ����\', '*.csv']);
len = length(fileList);
nameList = ["open" "close" "noise" "left" "right" "count" "finger" "sponge" "rotate"];
%% �½��ṹ�壬���ڴ洢����
wholeDataset = struct('open', {}, 'close', {}, 'noise', {}, 'left', {}, 'right', {}, 'count', {}, 'finger', {}, 'sponge', {}, 'rotate', {});

for i =1:len
    eval('wholeDataset(1).'+ nameList(i) + '=csvread(fileList(i).name, 6, 0, [6, 0, 30004, 2])');
end
