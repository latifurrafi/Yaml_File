# project (key)
# └─ team (key)
#    ├─ item 1 (dictionary)
#    │   ├─ name: Maven
#    │   ├─ role: Backend Developer
#    │   └─ skills (list)
#    │       ├─ Python
#    │       ├─ Golang
#    │       └─ DevOps
#    └─ item 2 (dictionary)
#        ├─ name: Alex
#        ├─ role: DevOps Engineer
#        └─ skills (list)
#            ├─ Kubernetes
#            ├─ Docker
#            └─ CI/CD



# 🔹 Basic Rules of YAML

# 1. File extension: .yaml or .yml (both valid).

# 2. Indentation matters: Use spaces only (not tabs). Usually 2 spaces.

# 3. Key–Value pairs: Written as key: value.

# 4. Lists: Use - followed by a space.

# 5. Nested values: Indented under their parent key.

# 6. Strings: No quotes needed unless the value has special characters.

# 7. Comments: Start with #.


📘 YAML Project Example

This project demonstrates how to structure YAML files with nested dictionaries, lists, and key–value pairs. YAML is widely used for configuration files, CI/CD pipelines, Kubernetes manifests and more.


🗂 Example Structure

Here’s a sample YAML file representing a project team:

project:
  team:
    - name: Maven
      role: Backend Developer
      skills:
        - Python
        - Golang
        - DevOps

    - name: Alex
      role: DevOps Engineer
      skills:
        - Kubernetes
        - Docker
        - CI/CD


🔹 Key Concepts in YAML
1. File Extension

Use .yaml or .yml (both are valid).

Prefer .yaml in modern projects for clarity.



2. Indentation

Spaces only (no tabs).

Standard: 2 spaces per level.

✅ Good:

key:
  child: value


❌ Bad:

key:
	child: value   # (tab used — invalid)



3. Key–Value Pairs
name: Maven
role: Backend Developer


Keys are always strings.

Values can be strings, numbers, booleans, lists, or dictionaries.



4. Lists

Use - followed by a space:

skills:
  - Python
  - Golang
  - DevOps



5. Nested Structures

Indent to show hierarchy:

project:
  team:
    - name: Alex
      role: DevOps Engineer



6. Strings

Quotes not required for simple strings.

Use quotes if the value includes:

Special characters (:, {}, [], #)

Leading/trailing spaces.

Examples:

title: "Hello: World"
description: "This string contains special characters."



7. Comments

Start with # and place anywhere.

# This is a comment
name: "Maven"  # inline comment



⚠️ Common Mistakes to Avoid

Mixing tabs and spaces.

Forgetting - for list items.

Misalignment in indentation.

Using unsupported data types (e.g., functions).



✅ Best Practices

Always validate YAML using a linter (e.g., yamllint
).

Keep indentation consistent (2 spaces).

Use comments generously for clarity.

Break long YAML files into smaller, modular files when possible.

Stick to lowercase keys unless domain-specific (e.g., APIKey).



📌 Real-World Uses of YAML

Kubernetes manifests (deployment.yaml, service.yaml).

CI/CD pipelines (.gitlab-ci.yml, .github/workflows/*.yml).

Docker Compose (docker-compose.yml).

Infrastructure as Code (Terraform, Ansible, etc.).



🔧 Tools for YAML

Validator: YAML Lint

Editor plugins: VS Code, PyCharm, IntelliJ (with YAML support).

CLI tools: yq for YAML querying.

✨ With this guide, you’re ready to create clean and valid YAML files for any project!
