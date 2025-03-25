from django.shortcuts import render
import os
import markdown2

def home_page(request):
    return render(request, "home.html")
def view_blog(request):
    blog_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output_blog.md")

    if not os.path.exists(blog_file):
        return render(request, "blog_template.html", {"blog_content": "<h2>Blog content not available</h2>"})

    with open(blog_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return render(request, "blog_template.html", {"blog_content": "<h2>Blog content is empty</h2>"})

    html_content = markdown2.markdown(content)
    return render(request, "blog_template.html", {"blog_content": html_content})
