# ChatGPT handoffs

Codex's local files, repositories, file links, and conversation context are not automatically shared with ChatGPT. Prompts prepared for ChatGPT must not assume access to local information unavailable to the recipient.

Prohibited handoff patterns:

- Saving a prompt locally and treating its dependency files as already delivered to ChatGPT.
- Instructing ChatGPT to read attached files without bundling the actual required files into one deliverable.
- Providing only repository paths or local links and assuming ChatGPT can read their contents.
- Requiring many individual manual attachments without a way to detect missing attachments.
- Allowing investigation or judgment to continue from prompt fragments when required files are missing.
- Reporting the handoff ready before delivery is complete.

When preparing a ChatGPT prompt that depends on local information, choose exactly one of the following approaches at the outset and identify it in both the deliverable and completion report. Do not mix them. The prompt itself is user-facing and follows the Communication language policy.

### A. Self-contained prompt (default)

Make the prompt executable by pasting its text alone into a new ChatGPT chat. A local artifact may distribute the prompt but must not be a required ChatGPT input.

1. Reduce the required information to the minimum and include it directly in the prompt. Retain source file paths, stable IDs, and verification dates for traceability.
2. Even if distributing the prompt as a file, do not make its filename, attachment receipt, a local path, or prior conversation a condition for starting. Do not embed the same information in the prompt and also require receipt of the containing file before proceeding.
3. If using a preflight, ask for a brief restatement/check of essential targets, constraints, dates, and output requirements present in the text. Do not require a filename inventory or attachment check.

### B. Attachment-dependent prompt (exception)

Use this only when ChatGPT must actually read primary sources, images, tables, or large datasets that cannot be embedded in the prompt.

1. Minimize the required information and normally bundle it into one self-contained Markdown file or explicit archive. Retain source file paths, stable IDs, and verification dates for traceability.
2. Explain why embedding is impractical, provide a manifest of required files and the sections to read from each, and state concretely what the user should attach and what they should paste.
3. Begin the prompt with a preflight. Require an inventory of received filenames; if a required file or section is missing, do not begin the substantive investigation and report only what is missing.

### Self-containment check before delivery

For a self-contained prompt, always verify the following before delivering it:

> If this text alone is pasted into a new ChatGPT chat without attaching any files, can ChatGPT understand the research purpose, scope, constraints, required evidence, and expected output and start without clarification?

If not, copy the required information into the text or switch to the attachment-dependent approach and redesign the manifest and preflight. When reporting completion of a self-contained prompt, state that it works by copy and paste; do not present uploading as mandatory.

When using data from ChatGPT Library, Projects, connectors, or similar sources, depend on files only after confirming they can actually be found and read. Distinguish locally created files from files actually delivered to ChatGPT in the completion report. If they are not automatically shared, say so; for attachment-dependent handoffs, explain how to verify receipt after uploading.

When the user requests a prompt for asking ChatGPT a question or commissioning research or deliberation, unless they explicitly specify another output format, instruct ChatGPT to produce its final output as a self-contained, documentation-request prompt that can be handed directly to the Codex instance managing the repository. Do not ask for only an answer or research report.

Require that Codex-directed prompt to include at least:

- Research purpose, scope, reference date, and conclusion.
- Separate verified facts, inferences, and unverified matters.
- Source names, direct URLs, verification dates, and how changeable the information is.
- Relevant repository files, stable IDs, and mapping to the existing state.
- Additions, updates, and maintenance requested of Codex, and what must remain unchanged.
- Application conditions such as schemas, naming conventions, no guessing, and not marking unresolved matters resolved.
- Necessary validation such as YAML parsing, schema validation, duplicate IDs, reference integrity, and tests.
- The changed files, applied content, unresolved matters, and validation results Codex should report at completion.

ChatGPT's response must be self-contained and directly pasteable into Codex as a request to apply the repository changes, without user reconstruction, summarization, or reformatting. Do not assume ChatGPT can edit the repository or access local files.

When a requested ChatGPT prompt depends on local artifacts, the prompt text alone is not the complete deliverable. Complete the handoff only when the recipient can read the necessary evidence.

### Split long investigations into stages

When a ChatGPT investigation involves multiple independent sources, travel segments, decisions, or final deliverables, normally divide it into stages to prevent response timeouts and mixed evidence. Do not mechanically split a single short verification request.

1. The first self-contained prompt includes the overall research purpose, fixed conditions, final output requirements, and only the first step to execute now. Do not request the entire investigation or final deliverable in the first response.
2. Normally limit each step to one travel segment, facility group, issue, or primary-source family. Each response should briefly provide the conclusion, verified facts with direct URLs, unverified matters, and the next short instruction to send.
3. When the user has authorized the overall investigation and its destination, Codex should validate each stage and send the next scoped instruction in the same ChatGPT conversation without requiring the user to authorize each step again. Keep one stage per response and avoid combined re-investigation or lengthy repetition. Ask only for indispensable user-only inputs, authentication, an expansion of scope or destination, or separately required adoption/execution approval; continue independent work where possible.
4. Separate integration from research. Combine only facts verified in prior steps; do not perform new research or make assumptions during integration. Keep unverified matters unverified.
5. Produce the final Codex-directed implementation request as a separate step after integration. Retain all requirements for purpose, evidence, unverified matters, stable IDs, application conditions, validation, and completion reporting.
