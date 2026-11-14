"""Small line icons (24 x 24, stroke = currentColor), drawn for this site.

icon(name, size=24, cls="") -> inline <svg>.
paths(name) -> the raw SVG elements, for use inside the diagrams (wrap them in a <g transform=...>).
"""

P = {
    # domains
    "industries": '<path d="M3 21V10l5 3V10l5 3V6h3l1-3h2l1 3v15z"/><path d="M7 17h2M12 17h2M17 17h1"/>',
    "stations": '<rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M9 20l-2 2M15 20l2 2M8 16l-1 4M16 16l1 4"/>'
                '<circle cx="9" cy="13" r=".6"/><circle cx="15" cy="13" r=".6"/>',
    "warehouses": '<path d="M3 21V9l9-5 9 5v12"/><path d="M7 21v-8h10v8M7 17h10"/>',
    "towns": '<path d="M3 21V11l5-4 5 4v10M13 21V5h8v16M3 21h18"/><path d="M16 9h2M16 13h2M16 17h2M7 15h2"/>',
    "economy": '<path d="M3 7h13l5 5-5 5H3z"/><circle cx="8" cy="12" r="2"/>',
    "company": '<rect x="4" y="7" width="16" height="14" rx="2"/><path d="M9 7V4h6v3M4 13h16"/>',
    "finance": '<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .8-3 2s1.3 1.7 3 2 3 .8 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5M12 6v2M12 16v2"/>',
    "subsidies": '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>',
    "emission": '<path d="M4 15a4 4 0 0 1 3-6.5A5 5 0 0 1 17 8a4 4 0 0 1 2 7.5"/><path d="M8 19h8M10 22h4"/>',
    "vehicles": '<rect x="3" y="6" width="18" height="10" rx="2"/><path d="M3 11h18M7 16v2M17 16v2"/><circle cx="7" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
    "infrastructure": '<path d="M7 3 5 21M17 3l2 18M6 7h12M5.6 12h12.8M5 17h14"/>',
    "time": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "notifications": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>',
    "landmarks": '<path d="M12 3v3M5 21h14M7 21V10l5-4 5 4v11M10 21v-5h4v5"/>',
    "achievements": '<path d="M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M7 6H4a3 3 0 0 0 3 4M17 6h3a3 3 0 0 1-3 4M12 14v4M8 21h8"/>',
    "map": '<path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15M15 6v15"/>',
    "missions": '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
    "interface": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 9h18M8 22h8M12 18v4"/>',
    # page and diagram symbols
    "person": '<circle cx="12" cy="7" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v11h14V10M10 21v-6h4v6"/>',
    "bus": '<rect x="4" y="3" width="16" height="15" rx="3"/><path d="M4 11h16M8 18v3M16 18v3"/><circle cx="8" cy="14.5" r=".8"/><circle cx="16" cy="14.5" r=".8"/>',
    "walk_no": '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "cross": '<path d="M6 6l12 12M18 6 6 18"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "scale": '<path d="M12 3v18M6 21h12M5 7h14"/><path d="M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
    "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    "book": '<path d="M4 4h6a2 2 0 0 1 2 2v15a2 2 0 0 0-2-2H4zM20 4h-6a2 2 0 0 0-2 2v15a2 2 0 0 1 2-2h6z"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "back": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "flask": '<path d="M9 3h6M10 3v6L4 19a1.5 1.5 0 0 0 1.3 2h13.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7 15h10"/>',
    "truck": '<path d="M2 6h11v10H2zM13 10h4l4 4v2h-8z"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "train": '<rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M8 20l-2 2M16 20l2 2"/><circle cx="9" cy="13" r=".6"/><circle cx="15" cy="13" r=".6"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    "lightbulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.8.8 1 1.5 1 2.5h6c0-1 .2-1.7 1-2.5A6 6 0 0 0 12 3z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="18" r="1"/>',
}


def paths(name):
    return P[name]


def icon(name, size=24, cls="", stroke=2):
    return (f'<svg class="ic {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>')


def place(name, x, y, size, color, stroke=2):
    """Icon inside a diagram, top-left corner at (x, y)."""
    k = size / 24
    return (f'<g transform="translate({x},{y}) scale({k})" fill="none" stroke="{color}" stroke-width="{stroke / k * k}" '
            f'stroke-linecap="round" stroke-linejoin="round">{P[name]}</g>')
