## Example MLflow project
这篇教程展示了如何：

1. 训练一个线性回归模型.   
2. 将训练代码打包成一个可复用可复现的模型格式.   
3. 将模型部署成一个简单的HTTP服务用于进行预测.    
这篇教程使用的数据来自UCI的红酒质量数据集，主要用于根据红酒的PH值，酸度，残糖量等指标来评估红酒的质量。

### Model Training
我们要训练的线性回归模型包含两个超参数:alpha和l1_ratio。

使用 train.py 代码进行训练

这个例子用pandas，numpy，sklearn的API构建了一个简单的机器学习模型。通过MLflow tracking APIs来记录每次训练的信息，比如模型超参数和模型的评价指标。这个例子还将模型进行了序列化以便后续部署。

每次运行完训练脚本，MLflow都会将信息保存在目录mlruns中。

### Compare Models
在mlruns目录的上级目录中运行下边的命令：     
`mlflow ui`; 然后就可以通过 `http://localhost:5000` 来查看每个版本的模型了。我们可以通过搜索功能快速筛选感兴趣的模型，比如搜索条件设置为metrics.rmse<0.8可以将rmse小于0.8的模型找出来，如果更复杂的搜索条件，可以下载CSV文件并用其他软件进行分析。


### Create Package
我们已经写好了训练代码，可以将其打包提供给其他的数据科学家来复用，或者可以进行远程训练。

我们根据MLflow Projects的惯例来指定代码的依赖和代码的入口。比如创建一个sklearn_elasticnet_wine目录，在这个目录下创建一个MLproject文件来指定项目的conda依赖和包含两个参数alpha/l1_ratio的入口文件。`conda.yaml`文件列举了所有依赖：

通过执行mlflow run examples/sklearn_elasticnet_wine -P alpha=0.42可以运行这个项目，MLflow会根据conda.yaml的配置在指定的conda环境中训练模型。

如果代码仓库的根目录有MLproject文件，也可以直接通过Github来运行，比如代码仓库：`https://github.com/mlflow/mlflow-example。` 我们可以执行这个命令`mlflow run git@github.com:mlflow/mlflow-example.git -P alpha=0.42`来训练模型。
