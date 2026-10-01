# Architecture and Validation

## Project shape

- Frontend/server: React 19, TanStack Start/Router, TypeScript, Vite.
- UI: shadcn/Radix primitives, Tailwind CSS v4, Lucide icons.
- Data/auth: Supabase client plus server functions and forward-only SQL migrations.
- Hosting/editor synchronization: Lovable connected to the published Git branch.
- Tests: Bun unit tests and Playwright end-to-end tests, with SQL invariant and operational scripts under `scripts/sql-tests`.

## Trace points

- Student routes: `src/routes/_authenticated/alunos.*.tsx`.
- Student record components: `src/components/alunos/detalhe/`.
- Assessment UI and presentation: `src/components/avaliacao/`, `src/lib/avaliacao/`, `src/lib/api/avaliacoes.functions.ts`.
- Sales: `src/routes/_authenticated/vendas.tsx`, `src/components/vendas/`, `src/lib/api/vendas.functions.ts`, `src/lib/vendas/`.
- Add-ons: `src/components/alunos/detalhe/adicionais/`, `src/lib/api/adicionais.functions.ts`.
- Portal access: `src/components/alunos/detalhe/AcessoAlunoSection.tsx`, `src/routes/portal.tsx`, `src/lib/api/portal*.functions.ts`.
- Plans and billing: `src/routes/_authenticated/_admin/planos.tsx`, `src/components/alunos/detalhe/plano/`, `src/components/alunos/detalhe/mensalidades/`, and related API modules.
- Database contracts: `supabase/migrations/` and generated `src/integrations/supabase/types.ts`.

## Test seams

- Pure business rules: colocate `*.test.ts` beside helpers.
- Server contracts: validate input and error translation at exported server-function boundaries.
- Database invariants: add SQL tests for authorization, transactional propagation, snapshot totals, and revocation/regeneration.
- User journeys: add focused Playwright coverage for registration, sale from student record, add-on quantity, portal login persistence, and assessment preview.

## Validation order

Use the project's installed runtime and scripts. Resolve the exact runtime path if `bun`, `node`, or `supabase` is not on `PATH`.

1. Run the changed helper/test file.
2. Run `typecheck`.
3. Run the complete unit suite.
4. Run `lint`.
5. Run the production `build`.
6. Run focused Playwright flows when credentials and a safe test environment are available.
7. Validate new SQL against a disposable Supabase/Postgres instance before production.
