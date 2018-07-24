import requests
import os

# 执行API响应并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("响应标识:", r.status_code)

# 将api响应储存在一个变量中
response_dict = r.json()
project_num = response_dict['total_count']
incomplete_results = str(response_dict['incomplete_results'])

# 返回处理的是一个字典，字典跟列表进行嵌套
print("总共处理的python项目数:\t" + str(project_num))
print("是否未处理完全：\t" + incomplete_results + "\n")
project_items = response_dict['items']
print("下面是GitHub根据stars排名前30名的Python项目信息：\n")
for i in range(0, 30):
    project_item = project_items[i]
    owner = project_item['owner']
    print("Stars排行第 " + str(i+1) + " 名：")
    print("\t项目所有人信息：")
    print("\t\t登录名：" + owner['login'])
    print("\t\tid：" + str(owner['id']))
    print("\t\t主页地址：" + owner['html_url'])
    print("\t项目id：" + str(project_item['id']))
    print("\t项目名称：" + project_item['name'])
    print("\t项目全名：" + project_item['full_name'])
    print("\t项目是否不可见：" + str(project_item['private']))
    print("\t项目地址：" + project_item['html_url'])
    print("\t创建时间：" + project_item['created_at'])
    print("\t更新时间：" + project_item['updated_at'])
    print("\tgit地址：" + project_item['git_url'])
    print("\tssh地址：" + project_item['ssh_url'])
    print("\tclone地址：" + project_item['clone_url'])
    print("\tsvn地址：" + project_item['svn_url'])
    print("\t项目主站：" + str(project_item['homepage']))
    print("\t项目大小：" + str(project_item['size']))
    print("\t关注总数：" + str(project_item["watchers_count"]))
    print("\t缓存总数：" + str(project_item['forks_count']))
    print("\t待解决的问题数：" + str(project_item['open_issues']))
    print("\t默认分支：" + project_item['default_branch'])
    print("\n")
os.system("pause")
