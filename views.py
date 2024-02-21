from django.shortcuts import render
from django.http import HttpResponse

def mission_view(request):
    mission_essay = "The Manuel S. Enverga University Foundation is a private, non-stock, non-profit, non-sectarian educational foundation with a three-fold function – instruction, research and community service – offering responsive and alternative programs supportive of national development goals and standards of global excellence."
    return HttpResponse(mission_essay)

def vision_view(request):
    vision_essay = "In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentrations of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration."
    return HttpResponse(vision_essay)

def objectives_view(request):
    objectives_essay = "The core values of Manuel S. Enverga University Foundation (MSEUF) are grounded in a commitment to fostering a holistic, transformative, and student-centered educational experience. These values guide our approach to teaching and learning and serve as a compass for our students as they navigate their academic and personal journeys."
    return HttpResponse(objectives_essay)
