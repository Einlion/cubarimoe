from django.http import HttpResponsePermanentRedirect


async def home_redirect(request, chapter=None, page=None):
    if chapter is not None and page is None:
        page = 1
    if chapter is None or page is None:
        return HttpResponsePermanentRedirect(f"/read/manga/The-Classroom-of-a-Black-Cat-and-a-Witch")
    else:
        return HttpResponsePermanentRedirect(f"/read/manga/The-Classroom-of-a-Black-Cat-and-a-Witch/{chapter}/{page}")

