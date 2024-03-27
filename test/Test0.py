import torch
# 加载pth格式的模型
model = torch.load(R"F:\Project\DeepLearning\Siamese\Siamese-pytorch\model_data\word_compare.pth")
# 将模型保存为pt格式
torch.save(model, 'model.pt')