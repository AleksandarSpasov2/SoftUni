def gather_credits(credits_needed, *args):
    courses = {}
    current_credits = 0

    for course_name, course_credits in args:
        if current_credits >= credits_needed:
            break

        if course_name not in courses:
            courses[course_name] = course_credits
            current_credits += course_credits

    if current_credits >= credits_needed:

        return f'Enrollment finished! Maximum credits: {sum(courses.values())}\n' \
               f'. Courses: {", ".join(sorted(courses))}'
    else:
        return f'You need to enroll in more courses! ' \
               f'You have to gather {credits_needed - current_credits} credits more.'


print(gather_credits(
    80,
    ("Basics", 27),
))
