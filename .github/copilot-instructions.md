# Playwright Test Generation Rules

## Locators
- Always prefer getByRole, getByTestId, and getByLabel
- Never use CSS selectors or XPath unless no semantic alternative exists
- Never use page.locator('div.some-class') style selectors

## Structure
- One test file per feature or user flow
- Use describe blocks to group related tests
- Keep individual tests under 30 lines
- Name test files as feature-name.spec.ts

## Waits and Timing
- Never use page.waitForTimeout or fixed delays
- Use auto-wait or explicit waitFor conditions
- Prefer waitForLoadState('networkidle') for page transitions

## Data
- Isolate test data per test using fixtures
- Never depend on data from a previous test
- Use beforeEach for setup, afterEach for cleanup

## Assertions
- One primary assertion per test
- Use toBeVisible, toHaveText, toHaveURL over generic expect
- Always assert the outcome, not the intermediate state

## Auth
- Use storageState for authenticated tests
- Never log in through the UI in every test

## Output
- Return a diff, not the full file
- Add a brief comment at top explaining what the test covers