import datetime

# 1. Configuration: Define your current state
data = {
    "CURRENT_TASK": "Developing YT-Music-Dashboard",
    "MOD_STATUS": "Harmony/Luau Patches [RUNNING]",
    "BLAZIN_STATUS": "v1.2.0 [DEPLOYED]",
    "LATEST_ACTIVITY": "Refining Vercel Integration",
    "CONTRIBUTION_GRAPH": "█▓▒░ [||||||||||] 100% SUCCESS" # You can replace this with logic to pull real commits
}

def generate_readme():
    with open("README.template.md", "r") as f:
        template = f.read()

    # Replace placeholders
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", value)

    # Save to final README.md
    with open("README.md", "w") as f:
        f.write(template)

if __name__ == "__main__":
    generate_readme()
