from django.core.management.base import BaseCommand
from faker import Faker
from polls_project.models import Question

class Command(BaseCommand):

    help = 'Add new questions'

    def add_arguments(self, parser):

        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):

        fake = Faker()

        self.stdout.write('Start generate Questions')

        for _ in range(options['len']):
            self.stdout.write('Generate Questions')
            question = Question()
            question.question_text = fake.sentence().replace(".", "?")
            question.save()
        self.stdout.write(self.style.SUCCESS(f"Successfully generate {options['len']} questions"))
