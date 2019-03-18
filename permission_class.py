from rest_framework.decorators import  permission_classes

class IsPostOrIsAuthenticated(permissions.BasePermission):
    """This is a IsPostOrIsAuthenticated class.

    """
    def has_permission(self, request, view):
        """
        It gives the permission for requested users.
        :returns: True/False -- the return code.
        :param name: request/view.
        :type name: object.
        """
        try:
            
            # user=request.user.users.get_user_permanent_role()
            group_name=request.user.groups.values('name')
            role_name=group_name[0].get('name')
            if  role_name in view.role:
                return Response(True)
            else:
                pass
        except Exception as e:
            print (str(e))





class testaSongs(APIView):
    role=[roles_data['role_student']]
    def get(self,request):
        response_dict = {"status": True, "message": "", "data": {}}
        data ={}
        try:
           print("u r bussiness logic")
        except Exception as e:
            response_dict=False
        return Response(response_dict)
