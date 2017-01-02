from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.urls import reverse


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose pub_date is in the future
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose pub_date is older than 1 day
        :return: False
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose pub_date is within the last day
        :return: True
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    """
    Creates a question with the given `question_text` and published the given number of `days`
    offset to now (negative for questions published in the past, positive for questions that have yet to be published)
    :param days:
    :return:
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exists, an appropriate message should be displayed.
        :return:
        """
        response = self.client.get(reverse('pools:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Question with a pub_date in the past should be displayed on the index page.
        :return:
        """
        create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Questoin: Past question.>']
        )

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questoins exist, only past questions should be displayed.
        :return:
        """
        create_question(question_text="Past", days=-30)
        create_question(question_text="Future", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        :return:
        """
        create_question(question_text="Past1", days=-30)
        create_question(question_text="Past2", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past2.>', '<Question: Past1.>']

        )

class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """The detail view of a question with a pub_date in the future should return a 404 not found"""
        future_question = create_question("Future", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """The detail view of a question with a pub_date in the past should display the question's text"""
        past_question = create_question(question_text="Past", days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

