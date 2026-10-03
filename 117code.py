def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info(
    "Python",
    "AI",
    name="Om",
    age=25
)

student_info(student_info)