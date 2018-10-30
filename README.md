公司里用一个公用模板，填写报销内容。有的领导他只想看部分，想看的页面而且格式pdf。模板又不能删，只能一次性转成pdf。

解决 word 不能筛选哪几页筛选成一个pdf
筛选pdf中的几个页
config 配置文件
{
	"source_path":"test.pdf",
	"target_path":"target.pdf",
	"print_pages":[4,8,9]	
}

source_path   源目标文件

target_path  筛选后目标文件

print_pages  筛选的内容页

