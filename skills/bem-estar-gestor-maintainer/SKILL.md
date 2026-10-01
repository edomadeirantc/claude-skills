---
name: bem-estar-gestor-maintainer
description: Maintain and extend the Bem-estar Gestor SaaS safely across its React/TanStack Start interface, shadcn/Tailwind design system, Supabase schema/RPCs/RLS, Lovable synchronization, student portal, billing, sales, plans, add-ons, access codes, and physical assessments. Use for any request that names Bem-estar Gestor, bem-estar-gestor, its Lovable project, its Supabase project, or asks to diagnose, implement, test, review, migrate, or redesign those workflows.
---

# Bem-estar Gestor Maintainer

Maintain the application without weakening financial, authorization, or Lovable synchronization guarantees. Prefer evidence from the repository and database over assumptions.

## Start Every Task

1. Locate the `bem-estar-gestor` repository and read its `AGENTS.md` completely.
2. Inspect `git status`, the current branch, remotes, and recent commits. Preserve unrelated user changes.
3. Never rewrite published history. Do not force-push, rebase, amend, or squash commits already synchronized with Lovable.
4. Read only the relevant project documentation and code. Search with `rg` before opening large files.
5. Inspect environment-variable names without printing their values. Redact credentials, tokens, cookies, and authorization headers from all output.

## Route the Work

- For the active student, sales, add-on, access-code, plan, due-date, and assessment improvements, read [current-improvement-scope.md](references/current-improvement-scope.md).
- For architecture, database boundaries, and verification commands, read [architecture-and-validation.md](references/architecture-and-validation.md).
- For visual or interaction changes, apply `$ui-ux-pro-max` and `$ui-styling` when available. Generate a design-system recommendation first, then preserve the application's existing semantic tokens and component language.
- For reported defects, build a red-capable regression loop before changing behavior. Prefer pure helper tests, RPC/SQL invariant tests, or focused Playwright flows at the real user-facing seam.

## Implement Safely

1. Trace each feature vertically: route/component → server function → Supabase RPC/table → portal or reporting consumers.
2. Reuse existing components and query keys. Keep student-specific actions inside the student record without duplicating full-page implementations.
3. Put fragile business logic in tested helpers or database functions, not inline JSX.
4. Add a new forward-only migration for schema or RPC changes. Never edit an already-applied migration to change production behavior.
5. Preserve RLS and role boundaries. Use narrowly scoped `SECURITY DEFINER` RPCs only when the project already follows that pattern; set a safe `search_path` and validate the caller's role and affected student.
6. Preserve historical financial snapshots unless the requirement explicitly calls for propagation. Make propagation rules transactional, auditable, and covered by tests.
7. Invalidate every affected query after mutation, including student detail, dashboard/financial summaries, portal views, and lists.
8. Use clear Brazilian Portuguese in the UI. Explain technical classifications, references, cutoffs, recalculation effects, and recovery actions in language a non-specialist can understand.

## Verify Before Delivery

1. Run the smallest relevant tests during each vertical slice.
2. Run type checking regularly and the complete unit suite at the end.
3. Run lint and a production build.
4. Exercise database migrations in a disposable/local environment when available. Before touching the linked production Supabase project, resolve the exact project reference and obtain explicit production authorization.
5. For UI changes, inspect desktop and 375 px layouts, keyboard focus, labels, empty/loading/error states, contrast, and touch targets.
6. Review the final diff against both the requested scope and repository standards. Remove debug instrumentation and temporary artifacts.
7. Commit a coherent, working change to the current branch only when the task authorizes implementation. Never push or deploy unless explicitly requested.

