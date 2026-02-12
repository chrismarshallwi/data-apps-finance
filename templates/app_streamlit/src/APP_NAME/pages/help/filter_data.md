## Filtering Data

Use the controls at the top of the page to narrow the dataset before interacting with charts or tables.

### Controls (left to right)
- Search / Free text: Type any text to perform a live substring match across primary fields (titles, descriptions, IDs).
- Date range picker: Select a start and end date to show rows whose timestamp falls within the range.
- Category dropdown: Choose one or more categories. Multi-selects combine with OR; selecting none leaves category unfiltered.
- Status / Toggle chips: Click one or multiple status chips (Active, Archived, Pending) to include those states.
- Numeric slider(s): Adjust min/max sliders to filter on numeric fields (amount, score).
- Advanced filters (gear icon): Opens modal with field-level filters (contains, equals, greater/less than).
- Apply / Reset buttons: Apply runs the current set of controls; Reset clears all controls to defaults.

### Quick steps
1. Enter a search term to quickly reduce results by text.
2. Narrow by date using the range picker.
3. Further refine with category and status chips.
4. If needed, open Advanced filters for precise numeric or exact-match criteria.
5. Click Apply to update the view; click Reset to start over.

### Examples
- Find recent invoices: set date range to last 30 days, category = "Invoices", status = Active.
- High-value items: set numeric slider min to 10,000 and status = Active.
- Troubleshoot an item: search its ID, then open Advanced filters to match exact fields.

### Tips
- Filters are cumulative: all active filters are combined before displaying results.
- Use Reset when filters seem to conflict.
- When results are unexpectedly empty, widen the date range or remove one filter at a time to isolate the blocker.

### Accessibility
- All controls support keyboard navigation and can be cleared with the Reset button.
- Hover tooltips describe each control and expected input format.
