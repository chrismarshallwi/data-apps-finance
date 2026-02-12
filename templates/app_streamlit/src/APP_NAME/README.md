# UX Guidelines

## Structure

This repository contains several example pages that demonstrate good UX practices using Streamlit components. Each page is designed to showcase specific layout and interaction techniques that enhance user experience.

### Files and Folders

Sample folder structure:

```bash
streamlit_app/
├── .streamlit/
│   ├── config.toml              # Streamlit server and UI configuration
│   └── secrets.toml             # Sensitive credentials (add to .gitignore)
├── data/
│   ├── __init__.py
│   ├── lakehouse.py             # Databricks unity Catalog connection and session management
│   ├── models.py                # SQLAlchemy ORM models
│   └── repositories/
│       ├── __init__.py
│       ├── base_repository.py   # Base repository pattern for CRUD operations
│       └── user_repository.py   # User-specific data operations
├── services/
│   ├── __init__.py
│   ├── auth.py                  # Authentication and authorization services
│   ├── config.py                # Application configuration management
│   └── databricks.py            # Databricks-specific API services
├── utils/
│   ├── __init__.py
│   ├── helpers.py               # Common utility functions
│   ├── validators.py            # Input validation functions
│   ├── formatters.py            # Data formatting utilities
│   └── decorators.py            # Custom decorators (caching, auth checks)
├── ui/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── sidebar.py           # Reusable sidebar components
│   │   ├── header.py            # Common header elements
│   │   └── widgets.py           # Custom widget wrappers
│   └── custom_css.py            # Custom CSS styling
├── pages/
│   ├── dashboard.py             # Main dashboard (numbered for order)
│   ├── analytics.py             # Analytics page
│   ├── settings.py              # User settings page
│   └── admin.py                 # Admin panel (role-restricted)
├── tests/
│   ├── __init__.py
│   ├── test_auth.py              # Authentication tests
│   ├── test_data.py              # Data layer tests
│   ├── test_services.py          # Service layer tests
│   └── test_utils.py             # Utility function tests
├── app.py                        # Main application entrypoint
├── .gitignore                    # Git ignore patterns
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

### Application layers

The application is structured into several layers to promote separation of concerns and maintainability:
1. **Data Layer**: Manages database connections, ORM models, and data repositories for CRUD operations.
2. **Service Layer**: Contains business logic, authentication, and external API interactions.
3. **Utility Layer**: Provides common helper functions, input validation, data formatting, and decorators.
4. **UI Layer**: Houses reusable Streamlit components, custom widgets, and CSS styling.

The dependency flow between these layers is as follows:
:::mermaid
graph LR;
    A[Data Layer] --> B[Service Layer]
    C[Utility Layer] --> D[UI Layer]
    A --> D
    B --> D
:::

### DOs and DON'Ts
- **DO** break down complex pages into smaller, reusable components.
- **DO** keep business logic and data access in separate layers from UI code.
- **DON'T** access `st.session_state` directly from other components; use functions to encapsulate state management.
- **DON'T** create circular dependencies between layers; maintain a clear flow of data and control.

## Pages

### Home page
1. First thing to notice is the use of Material font for icons. They look consistent, clear and professional
   - You can search for icons in the [Google Material font's website](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded&icon.size=24&icon.color=%23e3e3e3&icon.platform=web
   )
2. We changed the size of the font (from 16 to 14) to make more space in the screen
3. We added global config to the sidebar, for apps that need configuration across all pages
4. The page elements are laid out consistently and automatically:
   - A `st.header` element
   - A `st.caption` element
   - The `page` content
5. In the `home` page, you want to give the user some basic info to get started, and maybe a button to take action

### User page
1. Related information is grouped in `st.container`, with borders for clear delimitation.
2. Sometimes, the user wants special meaning (or visual cue) about the data. The `st.badge` is a way to represent that outside a table.
3. We use `st.columns` to layout components that are shorter than the page (use Chrome's `inspect` feature to see the columns)

### Search data 1
1. Pages with a help document will show the `help` button automatically
2. Pages can add more options to the `st.sidebar`. Here, there is a selection to highlight the data
3. Avoid showing intense colors in your table. See the effects of enabling `lime` color in highlights. A list of named columns can be [found here](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color#examples).
4. This page intentionally hides the filters in a `st.popover` so the user can focus on the table. When doing that, call out the selections so the user knows what filters are applied. It should work nicely along with the global filters and the page options as well.
5. Use `help` icons when available. The user will forget what the UI elements mean

### Search data 2
1. When the user want the filters to be inline and visible, group them together and craft the layout so they will occupy the least ammount of space in your page
2. In this case, see how the chart that appears after selection is visible and does not require scroll down.


## Best Practices

### Show the minimal visual elements necessary to complete the task

Keep the interface clean and focused by displaying only the essential components required for the user to complete their task. Avoid cluttering the screen with unnecessary widgets, charts, or text. This improves usability and reduces cognitive load. Consider the following:

- Use conditional rendering to show elements only when needed.
- Group related inputs using `st.expander` or `st.tabs` to keep the layout tidy.
- Hide advanced options behind toggles or expandable sections.
- Use concise labels and tooltips to reduce visual noise.

**Goal:** Help users stay focused and avoid distractions by presenting a streamlined interface.

### Drive the focus of attention to the task

Design the layout and flow of your app to guide users toward the primary action or decision. Use visual hierarchy and layout strategies to emphasize what matters most:

- Place the most important widgets (e.g., inputs, buttons) at the top of the page.
- Use `st.markdown` with headers and spacing to create clear sections.
- Highlight key actions with color (e.g., `st.button` with a distinct `type`).
- Use progress indicators or status messages to keep users informed and engaged.

**Goal:** Ensure users intuitively understand what they need to do and where to focus their attention.

### Avoid scrolling

Minimize the need for vertical scrolling by designing compact, responsive layouts. Excessive scrolling can disrupt the user experience and make it harder to compare or interact with elements. Strategies include:

- Use `st.columns` to place widgets side-by-side when appropriate.
- Collapse long content into `st.expander` sections.
- Paginate large datasets or visualizations using tabs or dropdowns.
- Dynamically show/hide content based on user interaction to keep the layout concise.

**Goal:** Keep the entire task visible and accessible without requiring users to scroll through long pages.

