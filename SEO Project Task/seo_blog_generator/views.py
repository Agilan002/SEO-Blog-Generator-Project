from django.shortcuts import render
import markdown2
import os

def view_blog(request):
    """Renders the blog content from a markdown file"""
    blog_file_path = os.path.join(os.path.dirname(__file__), "..", "output_blog.md")

    if os.path.exists(blog_file_path):
        with open(blog_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        html_content = markdown2.markdown(content)
    else:
        html_content = "<h2>Blog content not available</h2>"

    return render(request, "blog_template.html", {"blog_content": html_content})


def generate_blog():
    """Generates an SEO-optimized blog post and saves it as Markdown"""
    blog_content = """
# The Future of Remote Work in HR

## Introduction
Remote work has transformed the corporate landscape, especially in **Human Resources (HR)**. Companies worldwide are rethinking policies, employee engagement, and recruitment strategies to adapt to the remote-first culture. But what does the future hold for HR in a remote work environment?

## The Shift to Remote HR Operations
With companies embracing hybrid and fully remote work models, HR departments are leveraging technology to ensure seamless operations. **Cloud-based HR management systems**, virtual collaboration tools, and AI-driven recruitment processes are streamlining HR tasks.

### Key Trends Shaping Remote Work in HR
1. **AI-Powered Recruitment** – Automated resume screening, chatbots for candidate interactions, and predictive analytics are making hiring smarter.
2. **Virtual Onboarding & Training** – Companies are investing in **e-learning platforms** to enhance employee experience.
3. **Employee Engagement & Well-being** – HR is focusing on mental health support, virtual team-building activities, and work-life balance programs.
4. **Data-Driven Decision Making** – HR analytics is helping companies measure employee productivity and satisfaction in remote settings.
5. **Compliance & Cybersecurity** – As remote work grows, ensuring **GDPR compliance** and **data security** is crucial.

## Advantages of Remote Work in HR
✔ **Cost Reduction** – Less office space, travel expenses, and operational costs.  
✔ **Access to Global Talent** – Companies can hire skilled professionals regardless of location.  
✔ **Increased Productivity** – Studies show remote workers often perform better with flexible schedules.

## Challenges & How to Overcome Them
❌ **Communication Barriers** → Use Slack, Microsoft Teams, or Zoom for seamless collaboration.  
❌ **Tracking Performance** → Implement OKRs (Objectives & Key Results) and time-tracking tools.  
❌ **Maintaining Company Culture** → Conduct virtual meetups, town halls, and mentorship programs.  

## SEO Optimization Strategies Used
- **Primary Keyword**: Future of Remote Work in HR
- **Secondary Keywords**: Remote HR strategies, virtual hiring, employee engagement
- **Meta Description**: Learn how HR is adapting to remote work with AI, virtual onboarding, and HR analytics.
- **Optimized Headings & Readability**

## Conclusion
The future of remote work in HR is **technology-driven, flexible, and employee-focused**. By embracing digital transformation, companies can build a resilient, future-proof workforce.
    """

    blog_file_path = os.path.join(os.path.dirname(__file__), "..", "output_blog.md")
    
    with open(blog_file_path, "w", encoding="utf-8") as f:
        f.write(blog_content)
