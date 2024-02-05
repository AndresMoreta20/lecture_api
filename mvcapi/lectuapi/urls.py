from django.urls import path
from .views import LecturespaceList, FlashcardList, TagList, StartStudySession, FlashcardFeedback, EndStudySession

urlpatterns = [
    path('lecturespaces/', LecturespaceList.as_view(), name='lecturespace-list'),
    path('flashcards/', FlashcardList.as_view(), name='flashcard-list'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('study-session/start/', StartStudySession.as_view(), name='start-study-session'),
    path('study-session/<int:session_id>/feedback/', FlashcardFeedback.as_view(), name='flashcard-feedback'),
    path('study-session/<int:session_id>/end/', EndStudySession.as_view(), name='end-study-session'),
]
