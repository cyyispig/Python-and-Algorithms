from db.mysql_db import pool
class NewsDao:
    def search_unreview_list(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql="select n.id,n.title,t.type,u.username " \
                "from t_news n join t_type t " \
                "on n.type_id=t.id join t_user" \
                " u on n.editor_id=u.id where" \
                " n.state=%s order by n.create_time desc limit %s,%s"
            cursor.execute(sql,("待审批",(page-1)*10,10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql="select ceil(count(*)/10) from t_news where state=%s"
            cursor.execute(sql,["待审批"])
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update_unreview_news(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()

            sql="update t_news set state=%s where id=%s"
            cursor.execute(sql,("已审批",id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
                print(e)
        finally:
            if "con" in dir():
                con.close()


    def search_list(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id,n.title,t.type,u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                  "join t_user u on n.editor_id=u.id " \
                  "order by n.create_time desc " \
                  "limit %s,%s"
            cursor.execute(sql,((page-1)*10,10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql="select ceil(count(*)/10) from t_news"
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def delete_by_id(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql="delete from t_news where id=%s"
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
                print(e)
        finally:
            if "con" in dir():
                con.close()