# Copilot Instructions for LearningHubMonolith (VueSchool)

## Workspace Context

This workspace is part of the **LearningHubMonolith** monorepo. The purpose of this repository is to facilitate active study and experimentation with coding languages, frameworks, packages, plugins, and related technologies.

## VueSchool Workspace Structure

- Each subfolder in this workspace represents a separate course from [VueSchool](https://vueschool.io/).
- Every course subfolder contains a `README.md` file.
  - The `README.md` summarizes the key takeaways and lessons learned from the course.
  - Takeaways are written in a general way, focusing on concepts and best practices, not on project-specific details.
- Subfolders may also include:
  - Projects or code snippets used as playgrounds for hands-on learning during the course.
  - Example implementations, experiments, or exercises related to the course content.

## Copilot Guidance

- When generating code or explanations, prefer general best practices and concepts over project-specific solutions, unless the user requests otherwise.
- Reference the relevant course subfolder and its `README.md` for lesson summaries and conceptual guidance.
- When suggesting code, ensure it is suitable for learning and experimentation, and aligns with the VueSchool course context.
- If referencing files or symbols, use fully qualified paths and names for clarity.
- Maintain a focus on clarity, reusability, and educational value in all suggestions.

## Summarizing Lesson Transcripts (.vtt files)

- When a `.vtt` file (lesson transcript) is pasted in chat and the user requests a summary:
  - Summarize the new learnings as bullet points, focusing on general concepts and best practices related to Vue, Nuxt, and plugins/packages in that ecosystem.
  - If helpful, include short, general code examples to illustrate concepts. Do not tie examples to a larger project or specific context from the transcript.
  - Keep all summaries and examples general, educational, and suitable for experimentation or learning, not project-specific.
  - Do not reference or assume any broader example or project unless explicitly instructed by the user.
