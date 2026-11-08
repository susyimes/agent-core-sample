# Excalidraw CLAUDE.md (concise high-star exemplar)

Source-URL: https://raw.githubusercontent.com/excalidraw/excalidraw/master/CLAUDE.md
Source-Repo-or-Site: excalidraw/excalidraw
Original-Path: CLAUDE.md
Category: CLAUDE.md / web app
Tags: claude-md, excalidraw, concise
Retrieved: 2026-11-07
Value-Note: Short high-star (100k+) CLAUDE.md: folder-to-change map plus exact commands, no fluff.

--- ORIGINAL ---

# CLAUDE.md

## Project Structure

Excalidraw is a **monorepo** with a clear separation between the core library and the application:

- **`packages/excalidraw/`** - Main React component library published to npm as `@excalidraw/excalidraw`
- **`excalidraw-app/`** - Full-featured web application (excalidraw.com) that uses the library
- **`packages/`** - Core packages: `@excalidraw/common`, `@excalidraw/element`, `@excalidraw/math`, `@excalidraw/utils`
- **`examples/`** - Integration examples (NextJS, browser script)

## Development Workflow

1. **Package Development**: Work in `packages/*` for editor features
2. **App Development**: Work in `excalidraw-app/` for app-specific features
3. **Testing**: Always run `yarn test:update` before committing
4. **Type Safety**: Use `yarn test:typecheck` to verify TypeScript

## Development Commands

```bash
yarn test:typecheck  # TypeScript type checking
yarn test:update     # Run all tests (with snapshot updates)
yarn fix             # Auto-fix formatting and linting issues
```

## Architecture Notes

### Package System

- Uses Yarn workspaces for monorepo management
- Internal packages use path aliases (see `vitest.config.mts`)
- Build system uses esbuild for packages, Vite for the app
- TypeScript throughout with strict configuration
