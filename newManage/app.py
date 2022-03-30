from colorama import Fore,Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsDao
from service.role_service import RoleDao
import os
import time
import sys
__user_service = UserService()
__news_service = NewsDao()
__role_service = RoleDao()
while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX,"\n\t========================")
    print(Fore.LIGHTBLUE_EX, "\n\t郭雨轩的新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t=======================")
    print(Fore.LIGHTBLUE_EX, "\n\t1.登录系统")
    print(Fore.LIGHTBLUE_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt=input("\n\t输入操作编号:")
    if opt=="1":
        username = input("\n\t用户名:")
        password = getpass("\n\t密码:")
        result = __user_service.login(username,password)
        if result==True:
            role = __user_service.search_user_role(username)
            os.system("cls")
            while True:
                if role=="管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号:")
                    if opt == "1":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一级")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号:")
                            if opt == "1":
                                while True:
                                    page = 1
                                    os.system("cls")
                                    count_page = __news_service.search_unreview_count_page()
                                    result = __news_service.search_unreview_list(page)
                                    for index in range(len(result)):
                                        one=result[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s"%(index+1,one[0],one[1],one[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d / %d"%(page,count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\tback.返回上一级")
                                    print(Fore.LIGHTBLUE_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTBLUE_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page>1:
                                        page=page-1
                                    elif opt == "next"  and  page<count_page:
                                        page=page+1
                                    elif int(opt)>=1 and int(opt)<=10:
                                        news_id = result[int(opt)-1][0]
                                        __news_service.update_unreview_news(news_id)
                            elif opt == "2":
                                while True:
                                    page = 1
                                    os.system("cls")
                                    count_page = __news_service.search_count_page()
                                    result = __news_service.search_list(page)

                                    for index in range(len(result)):
                                        one=result[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s"%(index+1,one[0],one[1],one[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d / %d"%(page,count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\tback.返回上一级")
                                    print(Fore.LIGHTBLUE_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTBLUE_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page>1:
                                        page=page-1
                                    elif opt == "next"  and  page<count_page:
                                        page=page+1
                                    elif int(opt)>=1 and int(opt)<=10:
                                        news_id = result[int(opt)-1][0]
                                        __news_service.delete_by_id(news_id)
                            elif opt == "back":
                                os.system("cls")
                                break
                    elif opt == "2":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一级")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号:")
                            if opt == "back":
                                break
                            elif opt == "1":
                                os.system("cls")
                                username=input("\n\t用户名:")
                                password = getpass("\n\t密码:")
                                repassword = getpass("\n\t重复密码:")
                                if password != repassword:
                                    print("\n\t两次密码不一致！")
                                    time.sleep(3)
                                    continue
                                email = input("\n\t邮箱：")
                                result = __role_service.search_list()
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d.%s"%(index+1,one[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\t角色编号：")
                                role_id = result[int(opt)-1][0]
                                __user_service.insert(username,password,email,role_id)
                                print("\n\t保存成功")
                                time.sleep(3)

                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
                elif role=="新闻编辑":
                    print("test")
        else:
            print("\n\t登录失败(3s后退出)")
            time.sleep(3)
    elif opt=="2":
        sys.exit(0)



