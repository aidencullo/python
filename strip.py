text = """
Remote
The Wikimedia Foundation is seeking an experienced and mission-driven Engineering Manager to lead our new Tools Platform Team—a group dedicated to building and evolving Toolforge, the backbone platform that powers over 3,300 community-built tools responsible for nearly 30% of all edits across Wikipedia and its sister projects. This is a critical leadership role at the intersection of infrastructure and contributor experience. You will guide a team focused on transforming Toolforge into a production-grade platform that is not only reliable and scalable, but also intuitive, inclusive, and empowering for technical contributors at every level of expertise.

PLEASE NOTE: We will only be considering hiring within UTC-3 to UTC+3 due to the geographical location of the team.
"""

non_empty_lines = [line for line in text.splitlines() if line.strip()]
# print(non_empty_lines)




strings = ['adf  ads', '   dasf   ', 'dddd     ', 's', '     ']
stripped = list(map(str.rstrip, strings))
# print(stripped)

strings = ['adf  ads', '   dasf   ', 'dddd     ', 's', '     ']
stripped = list(map(str.lstrip, strings))
# print(stripped)

strings = ['adf  ads', '   dasf   ', 'dddd     ', 's', '     ']
stripped = list(map(str.lstrip, map(str.rstrip, strings)))
# print(stripped)

maps = [str.lstrip, str.rstrip]
data = strings
from functools import reduce
stripped = list(reduce(lambda d, m: map(m, d), maps, data))
print(stripped)

from functools import reduce
# result = reduce(print, [1,2])
# print(result)
