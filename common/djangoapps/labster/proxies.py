from lxml import etree

from django.contrib.auth.models import User

from xmodule.modulestore.django import modulestore

from labster.masters import get_problem_as_platform_xml, get_quiz_block_as_platform_xml
from labster.models import LabProxy, Lab
from labster.models import QuizBlock, Problem
from labster.parsers.problem_parsers import QuizParser
from labster.quiz_blocks import create_xblock, update_problem


USER_ID = 19  # kriwil@gmail.com


def prepare_lab(lab, location):
    user = User.objects.get(id=USER_ID)

    lab_proxy, _ = LabProxy.objects.get_or_create(
        lab=lab, location=location)

    lab_proxy.is_active = True
    lab_proxy.save()

    # quizblocks
    quiz_blocks = QuizBlock.objects.filter(lab=lab, is_active=True)
    for quiz_block in quiz_blocks:
        # create unit
        unit = create_unit_from_quiz_block(user, quiz_block, lab_proxy.location)

        problems = Problem.objects.filter(quiz_block=quiz_block, is_active=True)
        for problem in problems:

            # create component
            component = create_component_from_problem(
                user, lab_proxy, problem, unit.location)

            component = modulestore().get_item(component.location)
            modulestore().publish(component.location, user.id)

        unit = modulestore().get_item(unit.location)
        modulestore().publish(unit.location, user.id)


def prepare_lab_from_lab_id(lab_id, location):
    lab = Lab.objects.get(id=lab_id)
    return prepare_lab(lab, location)


def create_unit_from_quiz_block(user, quiz_block, location):
    name = quiz_block.element_id
    unit = create_xblock(user, 'vertical', location, name=name)
    return unit


def create_component_from_problem(user, lab_proxy, problem, location):
    name = problem.element_id
    extra_post = {'boilerplate': "multiplechoice.yaml"}
    quiz_block = problem.quiz_block

    component = create_xblock(
        user, 'problem', location.to_deprecated_string(), extra_post=extra_post)

    platform_xml = get_problem_as_platform_xml(problem)
    quiz_parser = QuizParser(platform_xml)
    edx_xml = quiz_parser.parsed_as_string

    update_problem(
        user,
        component,
        data=edx_xml,
        name=component.name,
        platform_xml=etree.tostring(platform_xml, pretty_print=True),
        correct_index=quiz_parser.correct_index,
        correct_answer=quiz_parser.correct_answer,
    )

    get_or_create_problem_proxy_from_quiz(
        lab_proxy, platform_xml, component.location, quiz_block.element_id)

    return component


def get_lab_proxy_as_platform_xml(lab_proxy):
    attrib = {'Id': str(lab_proxy.id)}
    lab_proxy_el = etree.Element('Lab', attrib)
    quizblocks_el = etree.SubElement(lab_proxy_el, 'QuizBlocks')

    quiz_blocks = QuizBlock.objects.filter(is_active=True, lab=lab_proxy.lab)
    for quiz_block in quiz_blocks:
        quiz_block_el = get_quiz_block_as_platform_xml(quiz_block)
        quizblocks_el.append(quiz_block_el)

    return lab_proxy_el
