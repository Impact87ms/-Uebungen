# * Example 1
meetings1 = [[0, 30], [5, 10], [15, 20]]

"""meetingA = meetings1[0]
meetingB = meetings1[1]
meetingC = meetings1[2]
print("Die 3 Meetingzeiten:", meetingA, meetingB, meetingC)"""


def meeting(meetings):
    sorted_meetings = meetings
    sorted_meetings.sort()
    if len(sorted_meetings) <= 1:
        return True
    for index in range(1, len(sorted_meetings)):
        if sorted_meetings[index][0] < sorted_meetings[index - 1][1]:
            return False
    return True


print(meeting(meetings1))

# * Example 2
print("----")
meetings2 = [[7, 10], [2, 4]]

print(meeting(meetings2))
