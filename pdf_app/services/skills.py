from collections import defaultdict

from utils.common import convert_value_list_to_str


def get_all_skills_for_user(user_cv, value_as_str=False):
    """
    Function to get all skills for user and group by type.

    :param user_cv: Model CV
    :param value_as_str: flag (True/False) to change final values type
    :return: dict with values as list or str
    """
    skill_groups = defaultdict(set)

    experiences = user_cv.experiences.all().prefetch_related("skills")

    for experience in experiences:  # pragma: no cover
        for result in experience.skills.all():
            skill_groups[result.group].add(result.name)

    return (
        convert_value_list_to_str(skill_groups)
        if value_as_str else
        skill_groups
    )
