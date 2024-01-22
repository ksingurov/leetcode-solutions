WITH
    attended_exams AS (
        SELECT
            student_id
            , subject_name
            , COUNT(*) AS attended_exams
        FROM Examinations
        GROUP BY student_id, subject_name
    )
    , all_students_and_subjects AS (
        SELECT
            stud.student_id
            , stud.student_name
            , subj.subject_name
        FROM Students stud
        CROSS JOIN Subjects subj
    )

SELECT
    all_.student_id
    , all_.student_name
    , all_.subject_name
    , COALESCE(exams.attended_exams, 0) AS attended_exams
FROM all_students_and_subjects AS all_
LEFT JOIN attended_exams exams
    ON all_.student_id = exams.student_id AND all_.subject_name = exams.subject_name
ORDER BY all_.student_id, all_.subject_name
