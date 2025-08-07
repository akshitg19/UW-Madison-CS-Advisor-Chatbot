'''
Akshit Ganesh
8/3/25
'''
cs_bs_description_data = {
    "description": """Our graduates discover the field of computer science helps open up a world of possibilities.
Computer scientists enjoy exceptional career opportunities, in settings ranging from large, established companies to adventurous new start-ups. They are also well qualified to pursue graduate study in a number of fields.
Our students are creative, analytical problem-solvers. Computer science is a rich, collaborative, and varied field that you will find challenging, no matter where your individual interests lie.
And there is more to computer science than programming. While software engineering is an important skill, computer scientists also work with robots and other physical devices, design hardware that runs faster and more efficiently, and apply machine learning techniques to gain insight from large data sets—to name just a few examples.
Because computer science has become highly interconnected with medicine, business, and many other fields, it is a great fit with other interests you may have. You will enjoy a strong career outlook while having an impact on society."""
}

cs_bs_how_to_get_in_data = {
    "how_to_get_in": {
        "summary": "To declare the computer sciences major, students must meet course, grade, and GPA requirements.",
        "course_credit_requirement": "Credit for COMP SCI 300 and MATH 222.",
        "grade_requirement": "Grade of BC or higher in one of these introductory programming courses, taken at UW-Madison: COMP SCI 300, COMP SCI/E C E 354 or COMP SCI 400.",
        "gpa_requirement": "2.250 GPA or higher among major declaration eligible coursework.",
        "gpa_calculation_rules": [
            "UW-Madison courses only.",
            "All attempts up to the first passed attempt of a course. A passed attempt is a grade of D or higher.",
            "All eligible major declaration coursework completed at the time of submitting a major declaration request."
        ],
        "additional_gpa_courses": "If a student needs additional coursework to meet the 2.250 GPA requirement, COMP SCI/MATH 240, COMP SCI/E C E 354, and/or COMP SCI 400 Programming III may also be used.",
        "advising_note": "It is advisable to submit a Computer Sciences major declaration request as soon as a student meets all three declaration requirements. Students having difficulties meeting the above requirements should schedule a meeting with a computer sciences advisor.",
        "declaration_instructions_source": "For instructions on declaring the major, see the Department of Computer Sciences website."
    }
}

university_general_education_requirements_data = {
    "requirement_type": "University General Education Requirements",
    "description": "All undergraduate students at the University of Wisconsin-Madison are required to fulfill a minimum set of common university general education requirements to ensure that every graduate acquires the essential core of an undergraduate education.",
    "requirements": {
        "breadth_humanities_literature_arts": "6 credits",
        "breadth_natural_science": "4 to 6 credits, consisting of one 4- or 5-credit course with a laboratory component; or two courses providing a total of 6 credits",
        "breadth_social_studies": "3 credits",
        "communication_part_a": "Required",
        "communication_part_b": "Required",
        "ethnic_studies": "Required",
        "quantitative_reasoning_part_a": "Required",
        "quantitative_reasoning_part_b": "Required"
    },
    "note": "The mortarboard symbol appears before the title of any course that fulfills one of the Communication Part A or Part B, Ethnic Studies, or Quantitative Reasoning Part A or Part B requirements."
}

ls_bs_degree_requirements_data = {
    "requirement_type": "College of Letters & Science Degree Requirements: Bachelor of Science (BS)",
    "description": "Students pursuing a Bachelor of Science degree in the College of Letters & Science must complete all of the requirements below.",
    "requirements": {
        "mathematics": "Complete two courses of 3+ credits at the Intermediate or Advanced level in MATH, COMP SCI, or STAT subjects. A maximum of one course in each of COMP SCI and STAT subjects counts toward this requirement.",
        "language": "Complete the third unit of a language other than English.",
        "ls_breadth": {
            "humanities": "12 credits of Humanities, which must include at least 6 credits of Literature.",
            "social_science": "12 credits of Social Science.",
            "natural_science": "12 credits of Natural Science, which must include 6 credits of Biological Science and 6 credits of Physical Science."
        },
        "liberal_arts_and_science_coursework": "Complete at least 108 credits.",
        "depth_of_intermediate_advanced_coursework": "Complete at least 60 credits at the Intermediate or Advanced level.",
        "major": "Declare and complete at least one major.",
        "total_credits": "Complete at least 120 credits.",
        "uw_madison_experience": "Complete both: 30 credits in residence, overall, and 30 credits in residence after the 86th credit.",
        "quality_of_work": [
            "2.000 in all coursework at UW–Madison",
            "2.000 in Intermediate/Advanced level coursework at UW–Madison"
        ]
    },
    "note_for_non_ls_students": "Non–L&S students who have permission from their school/college to pursue an additional major within L&S only need to fulfill the major requirements. They do not need to complete the L&S Degree Requirements above."
}

cs_bs_requirements_data = {
    "requirements_for_the_major": {
        "basic_computer_sciences": {
            "summary": "Complete the following 5 courses.",
            "courses": [
                {"code": "COMP SCI/MATH 240", "title": "Introduction to Discrete Mathematics", "credits": 3},
                {"code": "COMP SCI/E C E 252", "title": "Introduction to Computer Engineering", "credits": 3},
                {"code": "COMP SCI 300", "title": "Programming II", "credits": 3},
                {"code": "COMP SCI/E C E 354", "title": "Machine Organization and Programming", "credits": 3},
                {"code": "COMP SCI 400", "title": "Programming III", "credits": 3}
            ],
            "total_credits": 15
        },
        "basic_calculus": {
            "summary": "Complete one of the following two sequences.",
            "sequences": [
                {"name": "Sequence 1", "courses": ["MATH 221", "MATH 222"]},
                {"name": "Sequence 2", "courses": ["MATH 171", "MATH 217", "MATH 222"]}
            ],
            "total_credits": "9-14"
        },
        "additional_mathematics": {
            "summary": "Complete one course from Linear Algebra and one course from Probability or Statistics.",
            "linear_algebra": {
                "requirement": "Complete one of the following courses.",
                "options": ["MATH 320", "MATH 340", "MATH 345", "MATH 341", "MATH 375"]
            },
            "probability_or_statistics": {
                "requirement": "Complete one of the following courses.",
                "options": ["STAT/MATH 309", "STAT 311", "STAT 324", "MATH 331", "STAT 333", "STAT 340", "STAT 371", "STAT/MATH 431", "MATH 531"]
            }
        }
    }
}

cs_bs_advanced_requirements_data = {
    "requirements_for_the_major": {
        "advanced_computer_science_courses": {
            "summary": "Complete a total of four courses: one from Theory, two from Software & Hardware, and one from Applications.",
            "theory": {
                "requirement": "Complete one course.",
                "options": ["COMP SCI 577", "COMP SCI 520"]
            },
            "software_and_hardware": {
                "requirement": "Complete two courses.",
                "note": "COMP SCI 536 or COMP SCI 538 may be used to satisfy this requirement.",
                "options": [
                    "COMP SCI 407", "COMP SCI/E C E 506", "COMP SCI 536", "COMP SCI 538",
                    "COMP SCI 537", "COMP SCI 542", "COMP SCI 544", "COMP SCI/E C E 552",
                    "COMP SCI 557", "COMP SCI 564", "COMP SCI 640", "COMP SCI 642"
                ]
            },
            "applications": {
                "requirement": "Complete one course.",
                "options": [
                    "COMP SCI 412", "COMP SCI/I SY E/MATH 425", "COMP SCI/MATH 513",
                    "COMP SCI/MATH 514", "COMP SCI/E C E/I SY E 524", "COMP SCI/I SY E/MATH/STAT 525",
                    "COMP SCI 534", "COMP SCI 540", "COMP SCI 541", "COMP SCI 559",
                    "COMP SCI 565", "COMP SCI 566", "COMP SCI 570", "COMP SCI 571"
                ]
            }
        },
        "electives": {
            "requirement": "Complete two additional courses for 6-8 credits.",
            "options": [
                "COMP SCI 407", "COMP SCI 412", "COMP SCI/I SY E/MATH 425", "COMP SCI/E C E/MATH 435",
                "COMP SCI/STAT 471", "COMP SCI/MATH/STAT 475", "COMP SCI/E C E 506", "COMP SCI/MATH 513",
                "COMP SCI/MATH 514", "COMP SCI/DS/I SY E 518", "COMP SCI 520", "COMP SCI/E C E/I SY E 524",
                "COMP SCI/I SY E/MATH/STAT 525", "COMP SCI/I SY E 526", "COMP SCI/E C E/M E 532",
                "COMP SCI/E C E 533", "COMP SCI 534", "COMP SCI 536", "COMP SCI 537", "COMP SCI 538",
                "COMP SCI/E C E/M E 539", "COMP SCI 540", "COMP SCI 541", "COMP SCI 542", "COMP SCI 544",
                "COMP SCI/E C E 552", "COMP SCI 557", "COMP SCI 559", "COMP SCI/E C E 561", "COMP SCI 564",
                "COMP SCI 565", "COMP SCI 566", "COMP SCI/B M I 567", "COMP SCI 570", "COMP SCI 571",
                "COMP SCI/B M I 576", "COMP SCI 577", "COMP SCI/DS 579", "COMP SCI 620", "COMP SCI 640",
                "COMP SCI 642", "COMP SCI 639"
            ]
        }
    }
}

cs_bs_residence_honors_data = {
    "residence_and_quality_of_work": {
        "major_gpa": "2.000 GPA in all COMP SCI courses and courses counting toward the major.",
        "upper_level_major_gpa_in_residence": "2.000 GPA on 15 upper-level credits, taken in residence.",
        "on_campus_credits": "15 credits in COMP SCI, taken on campus."
    },
    "honors_in_the_major": {
        "summary": "Students may declare Honors in the Computer Sciences Major in consultation with the Computer Sciences undergraduate coordinator(s). To earn Honors in the Major, students must satisfy both the requirements for the major and the following additional requirements.",
        "requirements": [
            "Earn a minimum 3.300 University GPA.",
            "Earn a minimum 3.500 GPA for all COMP SCI and major courses.",
            "Complete one COMP SCI course numbered 500 through 699, taken for Honors with a grade of B or higher.",
            "Complete COMP SCI 681 and COMP SCI 682 for a total of 6 credits."
        ]
    },
    "footnotes": {
        "course_fulfillment_rule": "COMP SCI courses may only fulfill one COMP SCI major requirement area. For example, if a course taken for the Applications requirement cannot also apply to the Elective requirement.",
        "upper_level_definition": "COMP SCI courses numbered 400 through 699 count as Upper Level.",
        "senior_honors_thesis_details": "Senior Honors Thesis proposal must be approved by the thesis/project advisor and student must be declared as Honors in the Major before enrollment in COMP SCI 681. A final thesis or project must be completed before a final grade for COMP SCI 682 can be awarded."
    }
}

cs_bs_learning_outcomes_data = {
    "learning_outcomes": [
        "Recognize and apply the core principles of Computing (abstractions and algorithms) to solve real-world problems.",
        "Describe and apply the theoretical foundations of Computer Science (e.g., complexity analysis) in practical settings.",
        "Demonstrate knowledge of key elements of computer systems, e.g., hardware, operating systems, networks.",
        "Use fundamental and detailed knowledge, skills, and tools (e.g., specific algorithms, techniques methods, etc.) of computer science and develop the ability to acquire new knowledge, skills, and tools.",
        "Design, implement, and evaluate software in multiple programming paradigms and languages.",
        "Develop a substantial piece of software, and recognize the challenges of designing and developing software.",
        "Exhibit technical (designing, implementing, and testing) and teamwork (communication, collaboration, and professional practice) skills in order to develop solutions as a computer science practitioner.",
        "Can solve problems by applying a broad toolbox of knowledge and techniques."
    ]
}

cs_bs_four_year_plan_data = {
    "four_year_plan": {
        "disclaimer": "This Four-Year Plan is only one way a student may complete an L&S degree with this major. Many factors can affect student degree planning, including placement scores, credit for transferred courses, credits earned by examination, and individual scholarly interests.",
        "first_year": {
            "fall": {
                "courses": ["COMP SCI 200", "MATH 221", "Communications Part A", "First-Semester Language"],
                "credits": 15
            },
            "spring": {
                "courses": ["COMP SCI 300", "MATH 222", "Ethnic Studies", "Second Semester Language"],
                "credits": 14
            }
        },
        "second_year": {
            "fall": {
                "courses": ["COMP SCI 400", "COMP SCI/E C E 252", "Linear Algebra", "Third Semester Language", "Social Science Breadth"],
                "credits": 16
            },
            "spring": {
                "courses": ["COMP SCI/E C E 354", "COMP SCI/MATH 240", "INTER-LS 210 (Optional)", "Communication Part B", "Fourth Semester Language"],
                "credits": 14
            }
        },
        "third_year": {
            "fall": {
                "courses": ["COMP SCI Theory (COMP SCI 577 recommended)", "Probability or Statistics", "COMP SCI 368 (Optional)", "Humanities Breadth", "Social Science Breadth", "Elective"],
                "credits": 16
            },
            "spring": {
                "courses": ["COMP SCI Software/Hardware", "COMP SCI Applications", "Literature Breadth", "Biological Science Breadth", "Elective"],
                "credits": 15
            }
        },
        "fourth_year": {
            "fall": {
                "courses": ["COMP SCI Software/Hardware", "COMP SCI Elective", "Humanities Breadth", "Social Science Breadth", "Elective"],
                "credits": 15
            },
            "spring": {
                "courses": ["COMP SCI Elective", "Physical Science Breadth", "Literature Breadth", "Social Science Breadth", "Elective"],
                "credits": 15
            }
        },
        "total_credits": 120
    }
}

cs_bs_advising_careers_data = {
    "advising_and_careers": {
        "advising": {
            "summary": "The undergraduate coordinators in the Department of Computer Sciences assist students with questions about the major, L&S degree requirements and policy, and course selection.",
            "resource": "Information on academic advising for students interested or declared in the computer sciences major is posted on the Computer Sciences advising page."
        },
        "careers": {
            "outlook": "Demand for those with a computer sciences education is exceptionally strong. According to figures from the U.S. Bureau of Labor Statistics, the vast majority of growth in STEM occupations will occur within computing fields.",
            "recommendation": "Computer Sciences students are encouraged to begin working on their career exploration and preparation soon after arriving on campus to explore different career paths, participate in co-ops or summer internships, and prepare for job searches or graduate school applications.",
            "resources": [
                "Department of Computer Sciences: hosts one major career fair per year, in the fall, as well as other opportunities to connect with employers, such as technical talks and information sessions.",
                "SuccessWorks at the College of Letters & Science: Offers two major career fairs per year, assists with resume writing and interviewing skills, and offers individual career advising appointments for L&S students."
            ]
        },
        "successworks_details": {
            "summary": "SuccessWorks at the College of Letters & Science helps you turn the academic skills learned in your classes into a fulfilling life, guiding you every step of the way to securing jobs, internships, or admission to graduate school.",
            "services": [
                "One-on-one career advising",
                "Events, and resources",
                "Build valuable internship and research experience",
                "Connect with supportive alumni and employers"
            ],
            "links": [
                "What you can do with your major (Major Skills & Outcomes Sheets)",
                "Make a career advising appointment",
                "Learn about internships and internship funding",
                "Try 'Jobs, Internships, & How to Get Them,' an interactive guide in Canvas"
            ]
        }
    }
}

cs_bs_scholarships_data = {
    "resources_and_scholarships": {
        "summary": "Students can find and apply for scholarships through university-wide and department-specific resources.",
        "resources": [
            {
                "name": "Wisconsin Scholarship Hub",
                "description": "Visit the Wisconsin Scholarship Hub to find UW–Madison scholarships and apply online."
            },
            {
                "name": "Department of Computer Sciences Scholarships Page",
                "description": "Visit the scholarships page on the Department of Computer Sciences website for a compendium of opportunities available to students studying computer sciences."
            }
        ]
    }
}

cs_courses_batch_1 = [
    {
        "course_code": "COMP SCI/L I S 102",
        "title": "INTRODUCTION TO COMPUTING",
        "credits": 3,
        "description": "Provides a broad, introductory overview of computing concepts like security, robotics, and AI, without a focus on intensive programming.",
        "requisites": "MATH 96 or placement into MATH 141. MATH 118 does not fulfill the prerequisite. Not open to students with credit for COMP SCI 300 or 320.",
        "designation": {
            "gen_ed": "Quantitative Reasoning Part A",
            "breadth": "Natural Science",
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 200",
        "title": "PROGRAMMING I",
        "credits": 3,
        "description": "Introduces fundamental computer science topics and the process of incrementally developing small programs for students with no prior programming experience.",
        "requisites": "Satisfied Quantitative Reasoning (QR) A requirement or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "gen_ed": "Quantitative Reasoning Part B",
            "breadth": "Natural Science",
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 220",
        "title": "DATA SCIENCE PROGRAMMING I",
        "credits": 4,
        "description": "An introduction to Data Science programming using Python with an emphasis on analyzing real datasets and visual communication.",
        "requisites": "Satisfied Quantitative Reasoning (QR) A requirement or declared in the Professional Capstone Program in Computer Sciences. Not open to students with credit for COMP SCI 301.",
        "designation": {
            "gen_ed": "Quantitative Reasoning Part B",
            "breadth": "Natural Science",
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/MATH 240",
        "title": "INTRODUCTION TO DISCRETE MATHEMATICS",
        "credits": 3,
        "description": "Covers basic concepts of logic, sets, functions, and relations with a focus on discrete structures like integers, strings, trees, and graphs.",
        "requisites": "MATH 217 or 221.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E 252",
        "title": "INTRODUCTION TO COMPUTER ENGINEERING",
        "credits": 3,
        "description": "Introduces logic components, Boolean algebra, combinational and sequential logic design, computer organization, and machine/assembly-language programming.",
        "requisites": "None",
        "designation": {
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 272",
        "title": "INTRODUCTION TO WEB DEVELOPMENT",
        "credits": 3,
        "description": "Introduces methods and tools for creating secure and interactive web content using popular scripting languages, frameworks, and content management systems.",
        "requisites": "Not open to students with credit for L I S/COMP SCI 472.",
        "designation": {
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 298",
        "title": "DIRECTED STUDY IN COMPUTER SCIENCE",
        "credits": "1-3",
        "description": "Provides an opportunity for undergraduate directed study in computer sciences.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 300",
        "title": "PROGRAMMING II",
        "credits": 3,
        "description": "Introduces Object-Oriented Programming, array-based and linked data structures, searching and sorting, and complexity analysis.",
        "requisites": "Satisfied QR-A and (COMP SCI 200, 220, 302, 310, 301, or placement into COMP SCI 300) or (E C E/COMP SCI 252 and E C E 203); graduate/professional standing; declared in Capstone Certificate in COMP SCI. Not open to students with credit for COMP SCI 367.",
        "designation": {
            "gen_ed": "Quantitative Reasoning Part B",
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 304",
        "title": "PEER COLLABORATION IN COMPUTER SCIENCES (WES-CS)",
        "credits": 1,
        "description": "An interactive opportunity to discuss basic computer science concepts in a smaller setting with peers.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 310",
        "title": "PROBLEM SOLVING USING COMPUTERS",
        "credits": 3,
        "description": "Introduces computer and analytical skills for problem-solving, including elementary programming, symbolic manipulation languages, and software packages.",
        "requisites": "MATH 222, graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Elementary",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    }
]

cs_courses_batch_2 = [
    {
        "course_code": "COMP SCI 319",
        "title": "DATA SCIENCE PROGRAMMING I FOR RESEARCH",
        "credits": 3,
        "description": "An introduction to Data Science programming in Python for graduate students, covering basics, web scraping, database queries, and tabular analysis.",
        "requisites": "Graduate/professional standing.",
        "designation": {}
    },
    {
        "course_code": "COMP SCI 320",
        "title": "DATA SCIENCE PROGRAMMING II",
        "credits": 4,
        "description": "An intermediate approach to Data Science programming in Python, covering data structures, software engineering tools, and basic classification and clustering techniques.",
        "requisites": "COMP SCI 220 (or COMP SCI 301 prior to Spring 2020), COMP SCI 300, 319, graduate/professional standing, or declared in the Computer Sciences for Professionals Capstone Certificate.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E 352",
        "title": "DIGITAL SYSTEM FUNDAMENTALS",
        "credits": 3,
        "description": "Covers logic components, Boolean algebra, combinational and sequential logic analysis and synthesis, digital subsystems, and computer organization.",
        "requisites": "Satisfied Quantitative Reasoning (QR) A requirement and E C E/COMP SCI 252.",
        "designation": {
            "gen_ed": "Quantitative Reasoning Part B",
            "breadth": "Physical Sci. Counts toward the Natural Sci req",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E 354",
        "title": "MACHINE ORGANIZATION AND PROGRAMMING",
        "credits": 3,
        "description": "An introduction to fundamental computer system structures and the C programming language, focusing on low-level interrelationships and performance.",
        "requisites": "E C E/COMP SCI 252 and (COMP SCI 300 or 302) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "gen_ed": "Quantitative Reasoning Part B",
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 368",
        "title": "LEARNING A PROGRAMMING LANGUAGE",
        "credits": 1,
        "description": "A course for students interested in learning a particular programming language, offered at beginner, intermediate, and advanced levels.",
        "requisites": "None",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 400",
        "title": "PROGRAMMING III",
        "credits": 3,
        "description": "The third course in the programming fundamentals sequence, introducing balanced search trees, graphs, hash tables, and complexity analysis.",
        "requisites": "COMP SCI 300, graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/L I S/STAT 401",
        "title": "UNDERGRADUATE COOPERATIVE EDUCATION",
        "credits": 1,
        "description": "A course for full-time work experience which combines classroom theory with practical knowledge related to Computer Sciences, Data Science, Statistics, or Information Science.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "workplace": "Workplace Experience Course"
        }
    },
    {
        "course_code": "COMP SCI 402",
        "title": "INTRODUCING COMPUTER SCIENCE TO K-12 STUDENTS",
        "credits": 2,
        "description": "Students work in teams to design and lead Computer Science clubs and workshops for K-12 students, teaching computational thinking and programming.",
        "requisites": "COMP SCI 200, 220, 300, 301, 302, 310, 367, placement into COMP SCI 300, or L I S/COMP SCI 102 (COMP SCI 202 prior to Fall 2023), graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/STAT 403",
        "title": "INTERNSHIP COURSE IN COMP SCI AND DATA SCIENCE",
        "credits": 1,
        "description": "Enables students with outside internships to earn academic credit connected to their work experience related to the Computer Sciences or Data Science programs.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 407",
        "title": "FOUNDATIONS OF MOBILE SYSTEMS AND APPLICATIONS",
        "credits": 3,
        "description": "Focuses on the design and implementation of applications, systems, and services for mobile platforms with their unique constraints and features.",
        "requisites": "COMP SCI 400 or graduate/professional standing.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    }
]

cs_courses_batch_3 = [
    {
        "course_code": "COMP SCI 412",
        "title": "INTRODUCTION TO NUMERICAL METHODS",
        "credits": 3,
        "description": "Covers interpolation, solution of linear and nonlinear systems of equations, approximate integration, numerical differentiation, and data fitting.",
        "requisites": "MATH 222 and (MATH/COMP SCI 240 or MATH 234) and (COMP SCI 200, 300, 301, 302, 310, or placement into COMP SCI 300) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/I SY E/MATH 425",
        "title": "INTRODUCTION TO COMBINATORIAL OPTIMIZATION",
        "credits": 3,
        "description": "Focuses on optimization problems over discrete structures, such as shortest paths, spanning trees, flows, matchings, and the traveling salesman problem.",
        "requisites": "(MATH 320, 340, 341, or 375) or graduate/professional standing or member of the Pre-Masters Mathematics (Visiting International) Program.",
        "designation": {
            "breadth": "Physical Sci. Counts toward the Natural Sci req",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E/MATH 435",
        "title": "INTRODUCTION TO CRYPTOGRAPHY",
        "credits": 3,
        "description": "An introduction to the technical aspects of cryptography, the art and science of transmitting digital information in a secure manner.",
        "requisites": "(MATH 320, 340, 341, or 375) or graduate/professional standing or member of the Pre-Masters Mathematics (Visiting International) Program.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/STAT 471",
        "title": "INTRODUCTION TO COMPUTATIONAL STATISTICS",
        "credits": 3,
        "description": "Develops modern statistical inference principles for complex data structures, covering topics from numerical linear algebra, optimization, and Monte Carlo methods.",
        "requisites": "STAT/MATH 310 and (STAT 333 or 340), graduate/professional standing, or declared in Statistics VISP.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/L I S 472",
        "title": "INTRODUCTION TO WEB DEVELOPMENT",
        "credits": 3,
        "description": "Applied web development that introduces methods and tools for creating and maintaining secure, interactive web content, including programming fundamentals and content management systems.",
        "requisites": "Junior standing, declared in Library and Information Studies MA, Information MS, or Capstone Certificate in Computer Sciences for Professionals. Not open to students with credit for COMP SCI 272.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI/MATH/STAT 475",
        "title": "INTRODUCTION TO COMBINATORICS",
        "credits": 3,
        "description": "Covers problems of enumeration, distribution, and arrangement, including the inclusion-exclusion principle, generating functions, and graph coloring problems.",
        "requisites": "(MATH 320, 340, 341, or 375) or graduate/professional standing or member of the Pre-Masters Mathematics (Visiting International) Program.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/CURRIC 502",
        "title": "THEORY AND PRACTICE IN COMPUTER SCIENCE EDUCATION",
        "credits": 1,
        "description": "Explores computer science educational pedagogy and general teaching practices, with practical experience gained through tutoring students.",
        "requisites": "COMP SCI 300 or 302 or declared in Computer Science graduate program.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E 506",
        "title": "SOFTWARE ENGINEERING",
        "credits": 3,
        "description": "Covers ideas and techniques for designing, developing, and modifying large software systems, including processes, requirements, project management, and architectures.",
        "requisites": "(COMP SCI 367 or 400) and (COMP SCI 407, 536, 537, 545, 559, 564, 570, 679 or E C E/COMP SCI 552) or graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/MATH 513",
        "title": "NUMERICAL LINEAR ALGEBRA",
        "credits": 3,
        "description": "Covers direct and iterative solutions of linear and nonlinear systems and of eigenproblems, including LU and QR factorizations, complexity, and stability.",
        "requisites": "(MATH 340, 341, or 375) and (COMP SCI 200, 300, 301, 302, 310, or placement into COMP SCI 300) or graduate/professional standing or member of the Pre-Masters Mathematics (Visiting International) program.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI/MATH 514",
        "title": "NUMERICAL ANALYSIS",
        "credits": 3,
        "description": "Examines polynomial forms, interpolation, and approximation; numerical differentiation and integration; splines; and numerical methods for solving ordinary differential equations.",
        "requisites": "(MATH 320, 340, 341, or 375), (MATH 322, 376, 421, or 521), and (COMP SCI 200, 220, 300, 310, or 301 prior to Spring 2020, or placement into COMP SCI 300); grad/professional standing; member of the Pre-Masters Mathematics (Visiting International) Program.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    }
]

cs_courses_final_batch = [
    {
        "course_code": "COMP SCI/DS/I SY E 518",
        "title": "WEARABLE TECHNOLOGY",
        "credits": 3,
        "description": "Provides hands-on experience in building wearable computing platforms, covering fundamental knowledge of electronic circuitry, programming, and maker skills.",
        "requisites": "Sophomore standing.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI 520",
        "title": "INTRODUCTION TO THEORY OF COMPUTING",
        "credits": 3,
        "description": "Covers the basics of computation, capabilities, and limitations, including finite automata, computability theory, and computational complexity theory.",
        "requisites": "(MATH/COMP SCI 240 or STAT/COMP SCI/MATH 475) and (COMP SCI 367 or 400), or graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E/I SY E 524",
        "title": "INTRODUCTION TO OPTIMIZATION",
        "credits": 3,
        "description": "An introduction to mathematical optimization from a modeling and solution perspective, covering discrete and continuous optimization problems.",
        "requisites": "(COMP SCI 200, 220, 300, 301, 302, 310, or placement into COMP SCI 300) and (MATH 320, 340, 341, or 375) or graduate/professional standing.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/I SY E/MATH/STAT 525",
        "title": "LINEAR OPTIMIZATION",
        "credits": 3,
        "description": "Introduces optimization problems with linear inequality constraints, developing geometric and algebraic insights and presenting the theory behind the simplex method.",
        "requisites": "MATH 320, 340, 341, 375, or 443 or graduate/professional standing or member of the Pre-Masters Mathematics (Visiting International) Program.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI/I SY E 526",
        "title": "ADVANCED LINEAR PROGRAMMING",
        "credits": 3,
        "description": "Covers polynomial time methods for linear programming, quadratic programs, linear complementarity problems, and parallel algorithms.",
        "requisites": "STAT/COMP SCI/I SY E/MATH 525 and (COMP SCI 200, 220, 300, 301, 302, 310, or placement into COMP SCI 300) or graduate/professional standing.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E/M E 532",
        "title": "MATRIX METHODS IN MACHINE LEARNING",
        "credits": 3,
        "description": "Covers linear algebraic foundations of machine learning, including topics like regression, regularization, SVD, and iterative algorithms for applications like classification and clustering.",
        "requisites": "(MATH 234, 320, 340, 341, or 375) and (E C E 203, COMP SCI 200, 220, 300, 301, 302, 310, 320, or placement into COMP SCI 300), graduate/professional standing, or declared in Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Physical Sci. Counts toward the Natural Sci req",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI/E C E 533",
        "title": "IMAGE PROCESSING",
        "credits": 3,
        "description": "Explores the mathematical representation of images, models of image degradation, and methods for picture enhancement, restoration, segmentation, and coding.",
        "requisites": "E C E 330 and (MATH 320 or 340), graduate/professional standing, or member of Engineering Guest Students.",
        "designation": {
            "breadth": "Physical Sci. Counts toward the Natural Sci req",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI 534",
        "title": "COMPUTATIONAL PHOTOGRAPHY",
        "credits": 3,
        "description": "A study of sensing and computational techniques that enhance or extend the capabilities of digital photography using methods from computer vision and graphics.",
        "requisites": "(COMP SCI 300 or 367) and (MATH 217 or 221) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 536",
        "title": "INTRODUCTION TO PROGRAMMING LANGUAGES AND COMPILERS",
        "credits": 3,
        "description": "An introduction to the theory and practice of compiler design, including a comparison of programming language features and implementation techniques.",
        "requisites": "E C E/COMP SCI 354 and (COMP SCI 367 or 400) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 537",
        "title": "INTRODUCTION TO OPERATING SYSTEMS",
        "credits": 4,
        "description": "Covers input-output hardware, interrupt handling, memory management, virtual address translation, batch processing, time sharing, scheduling, and resource allocation.",
        "requisites": "E C E/COMP SCI 354 and (COMP SCI 367 or 400) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 538",
        "title": "INTRODUCTION TO THE THEORY AND DESIGN OF PROGRAMMING LANGUAGES",
        "credits": 3,
        "description": "Explores the design and theory of programming languages, covering procedural, object-oriented, functional, and logic paradigms, as well as execution models.",
        "requisites": "E C E/COMP SCI 354 and (COMP SCI 367 or 400) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E/M E 539",
        "title": "INTRODUCTION TO ARTIFICIAL NEURAL NETWORKS",
        "credits": 3,
        "description": "Covers the theory and applications of artificial neural networks, including multi-layer perceptrons, deep neural networks, support vector machines, and genetic algorithms.",
        "requisites": "COMP SCI 200, 220, 300, 301, 302, 310, placement into COMP SCI 300, or graduate/professional standing.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 540",
        "title": "INTRODUCTION TO ARTIFICIAL INTELLIGENCE",
        "credits": 3,
        "description": "Introduces principles of knowledge-based search, automatic deduction, knowledge representation, machine learning, and probabilistic reasoning.",
        "requisites": "(COMP SCI 300, 320 or 367) and (MATH 211, 217, 221, or 275) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 541",
        "title": "THEORY & ALGORITHMS FOR DATA SCIENCE",
        "credits": 3,
        "description": "Covers theoretical methods for data science, including concentration inequalities, high dimensional geometry, estimation, optimization, and PAC learning.",
        "requisites": "(COMP SCI 200, 220, placement into COMP SCI 300, or STAT 340), (MATH 320, 340, 341, 345, or 375), and (STAT 311, 333, 340, MATH/STAT 309, 431, MATH 331, 531, or I SY E 210), or graduate/professional standing.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 542",
        "title": "INTRODUCTION TO SOFTWARE SECURITY",
        "credits": 3,
        "description": "Teaches security considerations during the software development life cycle, including secure design, programming techniques, and vulnerability assessment.",
        "requisites": "COMP SCI 400 or 320, graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 544",
        "title": "INTRODUCTION TO BIG DATA SYSTEMS",
        "credits": 3,
        "description": "Focuses on deploying and using distributed systems to store and analyze large datasets, covering query languages, streaming data, and machine learning models.",
        "requisites": "COMP SCI 320, 400, or Graduate/Professional Standing.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E 552",
        "title": "INTRODUCTION TO COMPUTER ARCHITECTURE",
        "credits": 3,
        "description": "Covers the design of computer systems and components, including processor design, instruction sets, memory management, caches, and I/O structures.",
        "requisites": "(E C E/COMP SCI 352 and E C E/COMP SCI 354) or graduate/professional standing.",
        "designation": {
            "breadth": "Physical Sci. Counts toward the Natural Sci req",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 557",
        "title": "PARALLEL & THROUGHPUT- OPTIMIZED PROGRAMMING",
        "credits": 3,
        "description": "An introduction to high-performance computing practices, emphasizing shared-memory systems, multithreaded programming, vectorization, and memory hierarchy.",
        "requisites": "E C E/COMP SCI 354 and (MATH 320, 340, 341, or 375), or graduate/professional standing.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 559",
        "title": "COMPUTER GRAPHICS",
        "credits": 3,
        "description": "A survey of computer graphics, including image representation, modeling, transformation, and display of geometric objects in two and three dimensions.",
        "requisites": "MATH 222 and (COMP SCI 367 or 400) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/E C E 561",
        "title": "PROBABILITY AND INFORMATION THEORY IN MACHINE LEARNING",
        "credits": 3,
        "description": "Covers probabilistic tools for machine learning and analysis of real-world datasets, including classification, regression, probability theory, and decision theory.",
        "requisites": "(MATH 320, 340, 341, 375, or M E/COMP SCI/E C E 532 or concurrent enrollment) and (E C E 331, STAT/MATH 309, 431, STAT 311, 324, M E/STAT 424 or MATH 531) or grad/profsnl standing or declared in Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI 564",
        "title": "DATABASE MANAGEMENT SYSTEMS: DESIGN AND IMPLEMENTATION",
        "credits": 4,
        "description": "Covers data models, file organization, query processing, concurrency control, and recovery in database management systems.",
        "requisites": "E C E/COMP SCI 354 and (COMP SCI 367 or 400) or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Physical Sci. Counts toward the Natural Sci req",
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 565",
        "title": "INTRODUCTION TO DATA VISUALIZATION",
        "credits": 3,
        "description": "An introduction to topics such as perception, cognition, communication, design, and implementation in data visualization.",
        "requisites": "COMP SCI 320, 400, or Graduate/Professional Standing.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 566",
        "title": "INTRODUCTION TO COMPUTER VISION",
        "credits": 3,
        "description": "A broad overview of computer vision, including image formation, feature detection, motion estimation, 3D shape reconstruction, and object recognition.",
        "requisites": "COMP SCI 400 and (MATH 320, 340, 341, 345 or 375) and (STAT 311, 324, 333, 340, 371, STAT/MATH 309, 431, MATH 331 or 531) or graduate/professional standing.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/B M I 567",
        "title": "BIOMEDICAL IMAGE ANALYSIS",
        "credits": 3,
        "description": "A hands-on introduction to biological and medical image analysis techniques, including segmentation, registration, and quantification.",
        "requisites": "(MATH 320, 340, 341, 345, or 375) and (STAT 511, 541, POP HLTH/B M I 551, MATH 331, MATH/STAT 431, 309, STAT 240, 301, 311, 324, 371, or STAT/F&W ECOL 571) or graduate/professional standing.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 570",
        "title": "INTRODUCTION TO HUMAN-COMPUTER INTERACTION",
        "credits": 3,
        "description": "Focuses on user-centered software design, including methods for understanding user needs, designing and prototyping interfaces, and evaluating their usability.",
        "requisites": "Junior standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 571",
        "title": "BUILDING USER INTERFACES",
        "credits": 3,
        "description": "Introduces the software development of user interfaces (UIs), covering UI paradigms, methods for handling user input, and platform-specific development tools.",
        "requisites": "COMP SCI 400.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/B M I 576",
        "title": "INTRODUCTION TO BIOINFORMATICS",
        "credits": 3,
        "description": "Studies algorithms for computational problems in molecular biology, such as genome sequencing, sequence alignment, and phylogenetic tree construction.",
        "requisites": "(COMP SCI 320 or 400) and MATH 222, graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 577",
        "title": "INTRODUCTION TO ALGORITHMS",
        "credits": 4,
        "description": "Covers basic paradigms for the design and analysis of efficient algorithms, including greed, divide-and-conquer, dynamic programming, and computational intractability.",
        "requisites": "(MATH/COMP SCI 240 or STAT/COMP SCI/MATH 475) and (COMP SCI 367 or 400), or graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 578",
        "title": "CONTEST-LEVEL PROGRAMMING",
        "credits": 1,
        "description": "Provides training in computer programming for competitions, focusing on assessing problem difficulty, recognizing algorithms, and fast coding.",
        "requisites": "(COMP SCI 300 or 367), graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/DS 579",
        "title": "VIRTUAL REALITY",
        "credits": 3,
        "description": "Introduces the field of virtual reality, focusing on creating immersive, interactive virtual experiences, and surveying topics from computer graphics to human perception.",
        "requisites": "Sophomore standing.",
        "designation": {
            "level": "Intermediate",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI/L I S 611",
        "title": "USER EXPERIENCE DESIGN 1",
        "credits": 3,
        "description": "An introduction to user experience design including the design process, ethics, methods, and tools, with a focus on formative research.",
        "requisites": "Declared in Information MS, Design + Innovation MS , or Capstone Certificate in User Experience Design.",
        "designation": {
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI/L I S 612",
        "title": "USER EXPERIENCE DESIGN 2",
        "credits": 3,
        "description": "An advanced study of UX design, introducing processes of ideation, visual design, and low- and high-resolution prototyping.",
        "requisites": "COMP SCI/L I S 611 and Declared in Information MS, Design + Innovation MS, or Capstone Certificate in User Experience Design.",
        "designation": {
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI/L I S 613",
        "title": "USER EXPERIENCE DESIGN 3",
        "credits": 3,
        "description": "Focuses on conducting formal evaluations of the user experience (UX) or usability of a digital system, covering the entire research process.",
        "requisites": "COMP SCI/L I S 612 and Declared in Information MS, Design + Innovation MS, or Capstone Certificate in User Experience Design.",
        "designation": {
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI/L I S 614",
        "title": "USER EXPERIENCE DESIGN CAPSTONE",
        "credits": 1,
        "description": "Applies a design studio critique approach to produce a learning environment of collaborative and interdisciplinary peer critique and learning.",
        "requisites": "COMP SCI/L I S 613 and declared in Design + Innovation MS, or the Capstone Certificate in User Experience Design.",
        "designation": {
            "grad_50_percent": "Counts toward 50% graduate coursework requirement"
        }
    },
    {
        "course_code": "COMP SCI 620",
        "title": "COMPUTER SCIENCES CAPSTONE",
        "credits": 3,
        "description": "Students build a meaningful product from start to finish with a corporate client, learning and using new technologies and agile software development techniques.",
        "requisites": "COMP SCI 400, senior standing, and declared in an undergraduate Computer Sciences major.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 638",
        "title": "UNDERGRADUATE TOPICS IN COMPUTING",
        "credits": "1-4",
        "description": "Covers selected topics in computing, with each offering of the course covering a topic selected by the instructor.",
        "requisites": "COMP SCI 200, 300, 301, 302, 310, 367, placement into COMP SCI 300, or L I S/COMP SCI 102 (COMP SCI 202 prior to Fall 2023), graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "breadth": "Natural Science",
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 639",
        "title": "UNDERGRADUATE ELECTIVE TOPICS IN COMPUTING",
        "credits": "3-4",
        "description": "Covers selected topics in computing with sufficient depth to count as electives for the CS Major requirements.",
        "requisites": "None",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 640",
        "title": "INTRODUCTION TO COMPUTER NETWORKS",
        "credits": 3,
        "description": "Covers the architecture of computer networks and protocols, including layering, reliable transmission, congestion control, routing, and security.",
        "requisites": "(COMP SCI/E C E 354 and COMP SCI 400) or graduate/professional standing.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 642",
        "title": "INTRODUCTION TO INFORMATION SECURITY",
        "credits": 3,
        "description": "A senior level course covering various topics on information security, such as cryptographic primitives, security protocols, and system security.",
        "requisites": "COMP SCI 537 or graduate/professional standing or declared in the Capstone Certificate in Computer Sciences for Professionals.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 681",
        "title": "SENIOR HONORS THESIS",
        "credits": 3,
        "description": "Individual study for seniors completing theses for honors in the Computer Sciences major as arranged with a faculty member.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "honors": "Honors Only Courses (H)"
        }
    },
    {
        "course_code": "COMP SCI 682",
        "title": "SENIOR HONORS THESIS",
        "credits": 3,
        "description": "A continuation of COMP SCI 681 for seniors completing theses for honors in the Computer Sciences major.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S",
            "honors": "Honors Only Courses (H)"
        }
    },
    {
        "course_code": "COMP SCI 691",
        "title": "SENIOR THESIS",
        "credits": "2-3",
        "description": "Individual study for seniors completing theses as arranged with a faculty member.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 692",
        "title": "SENIOR THESIS",
        "credits": "2-3",
        "description": "A continuation of COMP SCI 691 for seniors completing theses as arranged with a faculty member.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 698",
        "title": "DIRECTED STUDY",
        "credits": "1-6",
        "description": "Directed study projects for juniors and seniors as arranged with a faculty member.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    },
    {
        "course_code": "COMP SCI 699",
        "title": "DIRECTED STUDY",
        "credits": "1-6",
        "description": "Directed study projects for juniors and seniors as arranged with a faculty member.",
        "requisites": "Consent of instructor.",
        "designation": {
            "level": "Advanced",
            "ls_credit": "Counts as Liberal Arts and Science credit in L&S"
        }
    }
]

all_course_data = cs_courses_batch_1 + cs_courses_batch_2 + cs_courses_batch_3 + cs_courses_final_batch