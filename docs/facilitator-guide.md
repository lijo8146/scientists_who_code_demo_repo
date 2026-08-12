# Facilitator guide

## Timing and prerequisites

For a 60–90 minute workshop, ask learners to install Conda and Git beforehand (or provide a cloud notebook environment), then spend 10 minutes orienting, 20 downloading and cleaning, 20 plotting, 15 interpreting, and 10–25 reviewing a small pull request. For a longer series, use one notebook per meeting with time between sessions for reflection and contribution.

Learners commonly get stuck at environment activation, finding the terminal, distinguishing a notebook from a script, and interpreting missing values. Normalize this: pair people up, offer copy/paste commands, and say explicitly that reading code line-by-line is not the goal of the first run.

## Mixed-skill team roles

- **Facilitator:** protects time, participation, and shared understanding.
- **Data steward:** checks source, provenance, permissions, and data dictionary.
- **Analyst:** runs and explains the transformations and figure.
- **Documentarian:** records decisions, questions, and limitations in plain language.
- **Reviewer:** checks that a fresh reader can reproduce the claimed result.

Rotate roles; none is a lesser technical contribution.

## Inclusive pull-request activity

Give each team a tiny change (a clearer label, provenance note, or limitation). Have one person open a pull request, another leave one question and one appreciation, and the author make a revision. Model comments such as “Could we name the unit here so a future reader does not have to infer it?” Avoid using review as a test of belonging. Merge only after the group can explain what changed and why.

## When governance requirements differ

Stop before moving data into the template. Invite the appropriate data authority or community partner to define access, attribution, retention, and publication rules. Adapt the folder structure, Git permissions, and documentation to those decisions; a public GitHub repository may not be an appropriate workspace.
