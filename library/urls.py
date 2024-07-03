from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("view_students/", views.view_students, name="view_students"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    path("student_issued_books/", views.student_issued_books, name="student_issued_books"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
   
    path("student_registration/", views.student_registration, name="student_registration"),
    path("change_password/", views.change_password, name="change_password"),
    
    path("student_login/", views.student_login, name="student_login"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),
    path("Book List/",views.book_list,name="Book List"),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('contact/', views.contact, name='contact'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("delete_student/<int:myid>/", views.delete_student, name="delete_student"),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('feedback/', views.feedback, name='feedback'),
    path('view_feedbacks/', views.view_feedbacks, name='view_feedbacks'),
    path('sentiment_analyse/', views.sentiment_analysis, name='sentiment_analysis')
    
   
    
    

   ]