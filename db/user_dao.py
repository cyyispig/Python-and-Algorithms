from db.mysql_db import pool
class UserDao:
    def login(self,username,password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql="select count(*) from t_user where username=%s and " \
                "AES_DECRYPT(UNHEX(password),'我爱学习')=%s"
            cursor.execute(sql,(username,password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()


    def search_user_role(self,username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql="select r.role from t_user u join" \
                " t_role r on u.role_id=r.id where u.username=%s"
            cursor.execute(sql,[username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def insert(self,username,password,email,role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql="insert into t_user(username,password,email,role_id) values (%s,hex(aes_encrypt(%s,'我爱学习')),%s,%s)"
            cursor.execute(sql,(username,password,email,role_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
                print(e)
        finally:
            if "con" in dir():
                con.close()


