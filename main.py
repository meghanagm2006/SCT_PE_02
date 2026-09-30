print("=" * 60)
print("SKILLCRAFT TECHNOLOGY - TASK 02")
print("PROMPTING FOR CREATIVITY")
print("=" * 60)


# EXPERIMENT 1
print("\nEXPERIMENT 1 - BASE PROMPT")
print("-" * 60)

prompt1 = """
Generate 5 innovative startup ideas for college students.
For each idea provide:
Startup Name, Problem, Solution, Target Users, Unique Feature.
Keep ideas practical, creative and suitable for students.
"""

print("PROMPT:")
print(prompt1)

print("SAMPLE OUTPUT:")
print("""
1. StudyBuddy
Problem: Students find it difficult to maintain a study schedule.
Solution: An app that creates personalized study plans.
Target Users: College students
Unique Feature: Smart study reminders

2. CampusCycle
Problem: Students need affordable transportation.
Solution: A college-based ride sharing platform.
Target Users: College students
Unique Feature: Verified college users

3. SkillSwap
Problem: Students want to learn skills from other students.
Solution: A platform for students to exchange skills.
Target Users: College students
Unique Feature: Skill exchange points

4. FoodSave
Problem: Extra food from college events gets wasted.
Solution: A platform to share extra food with students.
Target Users: Students and colleges
Unique Feature: Real-time food alerts

5. NoteShare
Problem: Students may miss important class notes.
Solution: A platform to share and organize notes.
Target Users: College students
Unique Feature: Subject-wise note collection
""")


# EXPERIMENT 2
print("\nEXPERIMENT 2 - PROFESSIONAL TONE")
print("-" * 60)

prompt2 = """
Generate 5 innovative startup ideas for college students
using a professional and business-oriented tone.
For each idea provide Startup Name, Problem, Solution,
Target Users and Unique Feature.
Make the ideas practical and useful.
"""

print("PROMPT:")
print(prompt2)

print("SAMPLE OUTPUT:")
print("""
1. CampusConnect
Problem: Students have difficulty finding campus services.
Solution: A centralized digital campus service platform.
Target Users: College students
Unique Feature: All campus services in one platform

2. InternLink
Problem: Students struggle to find relevant internships.
Solution: A platform connecting students with internship opportunities.
Target Users: College students and companies
Unique Feature: Skill-based internship matching

3. EduMarket
Problem: Students spend too much on academic materials.
Solution: A platform for buying and selling used study materials.
Target Users: Students
Unique Feature: Verified student marketplace

4. EventHub
Problem: Students miss information about college events.
Solution: A centralized college event management platform.
Target Users: Students and colleges
Unique Feature: Personalized event notifications

5. CareerTrack
Problem: Students find it difficult to monitor career progress.
Solution: A platform for tracking skills, projects and internships.
Target Users: College students
Unique Feature: Personal career dashboard
""")


# EXPERIMENT 3
print("\nEXPERIMENT 3 - FUN AND CREATIVE TONE")
print("-" * 60)

prompt3 = """
Generate 5 startup ideas for college students using a fun,
exciting and highly creative tone.
Make ideas interesting, unique and easy to understand.
Include startup name, problem, solution and unique feature.
"""

print("PROMPT:")
print(prompt3)

print("SAMPLE OUTPUT:")
print("""
1. SnackAttack
Problem: Students get hungry between classes.
Solution: Quick snack delivery around campus.
Unique Feature: 10-minute campus delivery

2. ChillZone
Problem: Students need short breaks from academic stress.
Solution: A platform for fun campus activities.
Unique Feature: Daily mini challenges

3. BookBuddy
Problem: Students cannot find textbooks quickly.
Solution: Students can lend and borrow books.
Unique Feature: Book matching based on subjects

4. CampusQuest
Problem: College life can become repetitive.
Solution: Fun challenges and activities around campus.
Unique Feature: Reward points for completing challenges

5. FriendFinder
Problem: New students find it difficult to make friends.
Solution: Connect students with similar interests.
Unique Feature: Interest-based matching
""")


# EXPERIMENT 4
print("\nEXPERIMENT 4 - FEW-SHOT PROMPTING")
print("-" * 60)

prompt4 = """
Example 1:
Startup Name: StudyBuddy
Problem: Students struggle to study consistently.
Solution: Personalized study schedules.
Unique Feature: AI-based study reminders.

Example 2:
Startup Name: CampusCycle
Problem: Students need affordable transportation.
Solution: Student ride-sharing.
Unique Feature: College-only verified users.

Task:
Generate 5 NEW startup ideas in the same format.
Do not repeat the examples.
Keep the ideas creative and practical.
"""

print("PROMPT:")
print(prompt4)

print("SAMPLE OUTPUT:")
print("""
1. CampusChef
Problem: Students struggle to find affordable healthy meals.
Solution: A student-focused meal planning platform.
Unique Feature: Budget-based meal suggestions

2. SkillBridge
Problem: Students need practical skills for careers.
Solution: Connect students with peer skill mentors.
Unique Feature: Skill-based mentor matching

3. LostLink
Problem: Students often lose personal items on campus.
Solution: A digital campus lost-and-found platform.
Unique Feature: Location-based item alerts

4. ProjectPartner
Problem: Students find it difficult to find project teammates.
Solution: Connect students based on skills and interests.
Unique Feature: Skill-based team matching

5. ClubConnect
Problem: Students do not know about suitable college clubs.
Solution: A platform to discover and join student clubs.
Unique Feature: Interest-based club recommendations
""")


# COMPARISON
print("\n" + "=" * 60)
print("COMPARISON OF EXPERIMENTS")
print("=" * 60)

print("""
1. Base Prompt:
   Produces practical and balanced startup ideas.

2. Professional Tone:
   Produces business-oriented and formal ideas.

3. Fun and Creative Tone:
   Produces more exciting, playful and engaging ideas.

4. Few-Shot Prompting:
   Helps the model follow the format and style shown
   in the examples.
""")


# OBSERVATION
print("\nOBSERVATION")
print("-" * 60)
print("""
Prompt structure, tone and examples can influence the style,
format and creativity of generated responses.
Few-shot examples help guide the expected output format.
""")


# CONCLUSION
print("\nCONCLUSION")
print("-" * 60)
print("""
Different prompting techniques can produce different types
of creative outputs. Clear instructions, suitable tone and
examples help guide the desired response.
""")

print("=" * 60)
print("TASK 02 COMPLETED SUCCESSFULLY")
print("=" * 60)