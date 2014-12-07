import csv

from django.core.management.base import BaseCommand
from django.utils import timezone

from labster.models import Scale, Category, Problem, Answer, QuizBlock
from labster.utils import get_hashed_text


"""
Item Number,Type,Number of Destractors,Question,Content,Responses,Difficulty,FeedBack text,Scales,Station,Time (sek.),SD Time,Discrimination,Guessing
https://s3-us-west-2.amazonaws.com/labster/adaptive/item_bank.csv
"""

class Command(BaseCommand):

    def handle(self, *args, **options):
        path = args[0]

        # Order,ID,ItemID,Question,Correct Answer,Possible Answer 1,Possible Answer 2,Possible Answer 3,Possible Answer 4,Possible Answer 5,Image,Categories,Category
        with open(path, 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for row in list(reader)[1:]:
                order = row[0].strip()
                _ = row[1] # id not used
                item_number = row[2].strip()
                question = row[3].strip()
                correct_answer = row[4].strip()
                possible_answer_1 = row[5].strip()
                possible_answer_2 = row[6].strip()
                possible_answer_3 = row[7].strip()
                possible_answer_4 = row[8].strip()
                possible_answer_5 = row[9].strip()
                image_url = row[10].strip()
                _ = row[11] # categories not used
                category = row[12].strip()

                lab_id = 35
                if category == 'Cyto-Pre-Test': category = 'QuizblockPreTest'
                if category == 'Cyto-Post-Test': category = 'QuizblockPostTest'

                quiz_block = QuizBlock.objects.get(lab__id=lab_id, element_id=category)
                problem = Problem.objects.get(element_id=item_number, quiz_block=quiz_block)
                problem.image_url = image_url
                problem.save()

                Answer.objects.filter(problem=problem).update(is_active=False)

                def create_answer(problem, text, correct_answer, order):
                    if not text:
                        return

                    hashed_text = get_hashed_text(text)
                    is_correct = False
                    if correct_answer != 'N/A':
                        if correct_answer == text:
                            is_correct = True

                    answer = Answer.objects.get(problem=problem, hashed_text=hashed_text)

                    answer.text = text
                    answer.hashed_text = hashed_text
                    answer.is_correct = is_correct
                    answer.is_active = True
                    answer.order = order
                    answer.save()

                create_answer(problem, possible_answer_1, correct_answer, 1)
                create_answer(problem, possible_answer_2, correct_answer, 2)
                create_answer(problem, possible_answer_3, correct_answer, 3)
                create_answer(problem, possible_answer_4, correct_answer, 4)
                create_answer(problem, possible_answer_5, correct_answer, 5)

                category, _ = Category.objects.get_or_create(name=category)
                problem.categories.add(category)

            self.stdout.write('done!\n')

    def import_item_back(self):
        with open('item_bank.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for each in list(reader)[1:]:

                item_number = each[0]
                answer_type = each[1]
                number_of_destractors = each[2]
                question = each[3]
                content = each[4]
                responses = each[5]
                difficulties = each[6]
                feedback = each[7]
                scales = each[8]
                stations = each[9]
                problem_time = each[10]
                sd_time = each[11]
                discrimination = each[12]
                guessing = each[13]

                response_list = responses.split(';')
                difficulty_list = difficulties.split(';')

                try:
                    problem = Problem.objects.get(item_number=item_number)
                except:
                    problem = Problem(item_number=item_number)

                problem.answer_type = answer_type
                problem.number_of_destractors = number_of_destractors
                problem.question = question
                problem.content = content
                problem.feedback = feedback
                problem.time = problem_time
                problem.sd_time = sd_time
                problem.discrimination = discrimination
                problem.guessing = guessing
                problem.modified_at = timezone.now()
                problem.save()

                for scale in scales.split(','):
                    scale = scale.strip()
                    try:
                        scale_obj = Scale.objects.get(id=scale)
                    except Scale.DoesNotExist:
                        scale_obj = Scale.objects.create(id=scale, name=scale)

                    problem.scales.add(scale_obj)

                for category in stations.split(','):
                    category = category.strip()
                    try:
                        category_obj = Category.objects.get(id=category)
                    except category.DoesNotExist:
                        category_obj = Category.objects.create(id=category, name=category)

                    problem.categories.add(category_obj)

                Answer.objects.filter(problem=problem).update(is_active=False)
                for index, response in enumerate(response_list):
                    difficulty = None
                    if len(response_list) == len(difficulty_list):
                        difficulty = difficulty_list[index]

                    try:
                        answer = Answer.objects.get(
                            problem=problem,
                            answer=response,
                        )
                    except Answer.DoesNotExist:
                        answer = Answer(
                            problem=problem,
                            answer=response,
                        )

                    answer.is_correct = index == 0
                    answer.difficulty = difficulty
                    answer.is_active = True
                    answer.save()