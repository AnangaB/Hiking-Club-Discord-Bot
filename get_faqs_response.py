from thefuzz import fuzz

# Define the FAQ dictionary, with questions and answers to it, alongside related phrasings that lead to the same answer
faq = {
    "Do I need to officially join the SFU Hikers Club to participate in hikes?": {
        "answer": "Nope! You don’t need to officially join the club to participate in our hikes. Just sign up for the hikes you’re interested in. If you do want to officially join our club, you can do so here: [SFU Hikers Official Club Page](https://go.sfss.ca/clubs/622/info).",
        "related_questions": [
            "Do I need to be a member of the club to join hikes?",
            "Can I join hikes without officially being a member?",
            "Is membership required to participate in hikes?"
        ]
    },
    "Is this club active?": {
        "answer": "Yes, we are super active and typically host hikes every week!",
        "related_questions": [
            "Is the club active?",
            "Do you still host hikes?",
            "How often do you run hikes?",
            "Are y'all here active?",
            "Are y'all active or nah?"
        ]
    },
    "Where can I find information about upcoming hikes?": {
        "answer": "Check out the **#events** channel! We post RSVP forms for each hike there. A few days before the hike, you'll might receive an invite with all the details about that hike and meeting place address, as long as hike capacity isn't full. Please just get a Happy Hikers role from here: https://discord.com/channels/944042280820539462/944105985230909480/1092242659415957555 to be notified, whenever we post a new hike.",
        "related_questions": [
            "How can I sign up for hikes?",
            "Where can I find RSVP forms for hikes?",
            "How do I find out about upcoming hikes?",
            "How can I join the next hike?"
        ]
    },
    "Who can join your hikes?": {
        "answer": "Our hikes are open to everyone! However, they’re primarily targeted toward SFU undergraduates. Whether you’re a student, alumni, or just a hiking enthusiast, you’re welcome to join us on the trails!",
        "related_questions": [
            "Who is allowed to join the hikes?",
            "Can anyone join your hikes?",
            "Are your hikes open to non-SFU members?"
        ]
    },
    "Do you host any events besides hikes?": {
        "answer": "Yes! In addition to hikes, we occasionally organize other social events. Keep an eye on the **#events** channel for announcements about these fun gatherings!",
        "related_questions": [
            "Do you organize other activities besides hikes?",
            "What other events do you host?",
            "Are there non-hike events?"
        ]
    },
    "Do you have other social media accounts?": {
        "answer": "Yes, we’re on Instagram! Follow us here: [@sfuhikers](https://www.instagram.com/sfuhikers/)",
        "related_questions": [
            "Where can I find your social media?",
            "Do you have Instagram?",
            "Can I follow you on social media?",
            "Is your club on Instagram?",
            "Where can I follow you on Instagram?",
            "Y'all have Ig?",
            "Do y'all have insta?"
        ]
    }
}


def is_msg_a_faq(msg, threshold=80):
    msg_lower = msg.lower()

    # Loop through each FAQ question and related questions
    for question, data in faq.items():
        # Check if the main question matches
        if fuzz.partial_ratio(msg_lower, question.lower()) >= threshold:
            #print(fuzz.partial_ratio(msg_lower, question.lower()))
            #print(question)
            return data['answer']

        # Check if any related questions match
        for related_question in data['related_questions']:
            if fuzz.partial_ratio(msg_lower, related_question.lower()) >= threshold:
                #print(fuzz.partial_ratio(msg_lower, question.lower()))
                #print(related_question)
                return data['answer']

    return None
