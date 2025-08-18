import time
import random

print("Welcome to your personal roadmap generator...")
print("Tell me what you're passionate about today...\n")

skill=input("Enter a skill you want to master ").strip().lower()

roadmaps={
    "web development":[
        "1.Learn HTML, CSS and basic JavaScript",
        "2.Practice by building personal Websites",
        "3.Learn Git & GitHub for version Control",
        "4.Explore frameworks like React or Tailwind CSS",
        "5.Deploy your website using Netlify or Vercel"
    ],
    "data science":[
        "1.Master Python and Jupyter Notebooks",
        "2.Learn NumPy,Pandas and Matplotlib",
        "3.Study Statistics & Data Cleaning",
        "4.Practice Machine Learning with Scikit-Learn",
        "5.Build projects and explore Kaggle Competitions"
    ],
    "business analyst":[
        "1.Learn Excel,PowerPOint, and SQL basics",
        "2.Understand Business Processes & Requirements",
        "3.Learn tools like Tableau or Power BI",
        "4.Practice writing BRDs and use cases",
        "5.Do mock case studies & real-world projects"
    ],
    "photoshop":[
        "1.Learn the Photoshop interface & tools",
        "2.Practice with layers,masks and filters",
        "3.Create aesthetic posters, thumbnails,etc",
        "4.Explore retouching and manipulation projects",
        "5.Post your designs on Behance/Instagram"
    ]
}

quotes=[
    "One step a day is still progress",
    "Be patient.You're growing roots",
    "You're doing better than you think"
]

print("\nGenerating your roadmap...")
time.sleep(2)

if skill in roadmaps:
    print(f"Here's your roadmap to master{skill.title()}: ")
    for step in roadmaps[skill]:
        print("🤍",step)
        time.sleep(1)
else:
    print("Sorry, I don't have a roadmao for that skill yet")
    print("But you can start by researching on YouTube or Coursera!")

print("\n Motivation for today:")
print(random.choice(quotes))