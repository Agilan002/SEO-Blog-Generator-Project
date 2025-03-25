from agents.research_agent import ResearchAgent
from agents.content_planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.seo_optimization_agent import SEOOptimizationAgent
from agents.review_agent import ReviewAgent

API_KEY = "your-openai-api-key"

# Initialize agents
research_agent = ResearchAgent()
planning_agent = ContentPlanningAgent()
generation_agent = ContentGenerationAgent(API_KEY)
seo_agent = SEOOptimizationAgent(["remote work", "HR trends"])
review_agent = ReviewAgent()

# Step 1: Get trending topics
topics = research_agent.fetch_trending_topics()
selected_topic = topics[0] if topics else "The Future of HR"

# Step 2: Generate outline
outline = planning_agent.generate_outline(selected_topic)

# Step 3: Generate content
content = generation_agent.generate_content(outline)

# Step 4: Optimize SEO
optimized_content = seo_agent.optimize_content(content)

# Step 5: Review content
readability_score = review_agent.check_readability(optimized_content)

# Save blog post to markdown
with open("output_blog.md", "w") as f:
    f.write(optimized_content)

# Output
print(f"Blog Post:\n{optimized_content}")
print(f"Readability Score: {readability_score}")
