// Gerryk — shared header, footer, tweaks panel (light theme, Innovative-style)
(function () {
  const PAGE = document.body.dataset.page || 'home';

  const SERVICES_MENU = [
    { label: 'Landscape Design', href: 'services.html#design' },
    { label: 'Landscape Construction', href: 'services.html#construction' },
    { label: 'Hardscaping Services', href: 'services.html#hardscape' },
    { label: 'Landscape Maintenance', href: 'services.html#maintenance' },
    { label: 'Irrigation Systems', href: 'services.html#irrigation' },
    { label: 'Outdoor Living Spaces', href: 'services.html#outdoor' },
    { label: 'Tree Trimming', href: 'services.html#tree' },
    { label: 'Fencing', href: 'services.html#fencing' },
    { label: 'Artificial Turf', href: 'services.html#turf' },
    { label: 'Outdoor Lighting', href: 'services.html#lighting' },
  ];

  const AREAS_MENU = [
    { label: 'Atherton', href: 'areas.html#atherton' },
    { label: 'Belmont', href: 'areas.html#belmont' },
    { label: 'Hillsborough', href: 'areas.html#hillsborough' },
    { label: 'Los Altos', href: 'areas.html#losaltos' },
    { label: 'Los Altos Hills', href: 'areas.html#losaltoshills' },
    { label: 'Menlo Park', href: 'areas.html#menlopark' },
    { label: 'Palo Alto', href: 'areas.html#paloalto' },
    { label: 'Redwood City', href: 'areas.html#redwoodcity' },
    { label: 'Woodside', href: 'areas.html#woodside' },
  ];

  const NAV_ITEMS = [
    { href: 'index.html', label: 'Home', key: 'home' },
    { href: 'about.html', label: 'About', key: 'about' },
    { href: 'services.html', label: 'Services', key: 'services', menu: SERVICES_MENU },
    { href: 'areas.html', label: 'Locations', key: 'areas', menu: AREAS_MENU },
    { href: 'gallery.html', label: 'Gallery', key: 'gallery' },
    { href: 'contact.html', label: 'Reviews', key: 'reviews' },
  ];

  const caret = `<svg class="nav-caret" width="10" height="6" viewBox="0 0 10 6" fill="none"><path d="M1 1 L5 5 L9 1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>`;

  const LOGO = `
    <a href="index.html" class="logo logo-badge" aria-label="Gerryk Landscaping home">
      <svg class="logo-svg" width="88" height="88" viewBox="0 0 120 120" fill="none" aria-hidden="true">
        <!-- Circular badge -->
        <circle cx="60" cy="60" r="58" fill="currentColor"/>
        <circle cx="60" cy="60" r="54" fill="none" stroke="#fff" stroke-width="1" opacity="0.35"/>

        <defs>
          <!-- Top arc for GERRYK -->
          <path id="logo-top-arc" d="M 30 60 A 30 30 0 0 1 90 60" fill="none"/>
          <!-- Bottom arc for LANDSCAPING (flipped so text reads upright L-to-R) -->
          <path id="logo-bot-arc" d="M 32 78 A 28 28 0 0 0 88 78" fill="none"/>
        </defs>

        <!-- GERRYK arched along top -->
        <text fill="#fff" font-family="Montserrat, sans-serif" font-weight="800"
              font-size="10" letter-spacing="2.2">
          <textPath href="#logo-top-arc" startOffset="50%" text-anchor="middle">GERRYK</textPath>
        </text>
        <!-- LANDSCAPING arched along bottom -->
        <text fill="#fff" font-family="Montserrat, sans-serif" font-weight="600"
              font-size="6" letter-spacing="1.4" opacity="0.9">
          <textPath href="#logo-bot-arc" startOffset="50%" text-anchor="middle">LANDSCAPING</textPath>
        </text>
        <!-- Little dot separators flanking LANDSCAPING -->
        <circle cx="32" cy="72" r="1.2" fill="#fff" opacity="0.7"/>
        <circle cx="88" cy="72" r="1.2" fill="#fff" opacity="0.7"/>

        <!-- Classic push mower silhouette -->
        <g transform="translate(60 66)">
          <!-- Grass tufts -->
          <path d="M-28 10 Q -26 3 -24 10 Q -22 4 -20 10 Z" fill="#fff" opacity="0.55"/>
          <path d="M18 10 Q 20 4 22 10 Q 24 3 26 10 Q 28 4 30 10 Z" fill="#fff" opacity="0.55"/>

          <!-- Handle -->
          <path d="M12 -4 L 26 -20" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
          <path d="M23 -23 L 29 -17" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>

          <!-- Deck body -->
          <path d="M-16 -4 L -12 -10 L 8 -10 L 14 -4 L 14 6 L -16 6 Z" fill="#fff"/>
          <!-- Engine -->
          <rect x="-6" y="-15" width="10" height="7" rx="1.2" fill="#fff"/>
          <circle cx="1" cy="-12" r="1.2" fill="currentColor"/>

          <!-- Wheels -->
          <circle cx="-11" cy="8" r="4" fill="#fff"/>
          <circle cx="-11" cy="8" r="1.8" fill="currentColor"/>
          <circle cx="9" cy="8" r="4" fill="#fff"/>
          <circle cx="9" cy="8" r="1.8" fill="currentColor"/>

          <!-- Ground line -->
          <rect x="-30" y="12" width="60" height="1.6" rx="0.8" fill="#fff" opacity="0.7"/>
        </g>
      </svg>
    </a>
  `;

  function renderNavItem(i) {
    if (!i.menu) {
      return `<a href="${i.href}" class="${i.key === PAGE ? 'active' : ''}">${i.label}</a>`;
    }
    const menuHTML = i.menu.map(m => `<a href="${m.href}">${m.label}</a>`).join('');
    return `
      <div class="nav-item has-menu">
        <a href="${i.href}" class="${i.key === PAGE ? 'active' : ''}">${i.label}${caret}</a>
        <div class="nav-dropdown">
          <div class="nav-dropdown-inner">
            <div class="nav-dropdown-grid">${menuHTML}</div>
          </div>
        </div>
      </div>
    `;
  }

  const NAV = `
    <nav class="nav">
      ${NAV_ITEMS.map(renderNavItem).join('')}
    </nav>
  `;

  const TOPBAR = `
    <div class="topbar">
      <div class="container topbar-inner">
        <div class="topbar-left">
          <span class="topbar-item">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M7 12.5 C 3.5 8.5, 2 6.5, 2 5 A 5 5 0 1 1 12 5 C 12 6.5, 10.5 8.5, 7 12.5 Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/><circle cx="7" cy="5" r="1.6" stroke="currentColor" stroke-width="1.3"/></svg>
            Redwood City, CA 94063
          </span>
          <span class="topbar-item hide-sm">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="7" cy="7" r="5.5" stroke="currentColor" stroke-width="1.3"/><path d="M7 4 V7 L9 8.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
            Accepting inquiries 24/7
          </span>
        </div>
        <div class="topbar-right">
          <div class="topbar-socials">
            <a href="#" aria-label="Instagram"><svg width="12" height="12" viewBox="0 0 14 14" fill="none"><rect x="2" y="2" width="10" height="10" rx="3" stroke="currentColor" stroke-width="1.2"/><circle cx="7" cy="7" r="2.3" stroke="currentColor" stroke-width="1.2"/><circle cx="10" cy="4" r="0.6" fill="currentColor"/></svg></a>
            <a href="#" aria-label="Facebook"><svg width="12" height="12" viewBox="0 0 14 14" fill="none"><path d="M9 3 H8 A2 2 0 0 0 6 5 V7 H4 V9 H6 V13 H8 V9 H10 L10.5 7 H8 V5.5 C 8 5.2 8.2 5 8.5 5 H10 V3 Z" fill="currentColor"/></svg></a>
            <a href="#" aria-label="Google"><svg width="12" height="12" viewBox="0 0 14 14" fill="none"><path d="M7 6.5 V8 H10 C 9.7 9.2 8.5 10 7 10 A 3 3 0 1 1 9 4.8 L 10.3 3.5 A 5 5 0 1 0 12 7.5 C 12 7 12 6.7 12 6.5 Z" fill="currentColor"/></svg></a>
          </div>
        </div>
      </div>
    </div>
  `;

  const HEADER = `
    ${TOPBAR}
    <header class="header">
      <div class="container header-inner">
        ${LOGO}
        ${NAV}
        <div class="header-cta">
          <a href="contact.html" class="btn btn-primary">Get A Quote</a>
        </div>
      </div>
    </header>
  `;

  const FOOTER = `
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div>
            ${LOGO}
            <p class="footer-tag">A modern Bay Area landscaping company — design, construction, hardscape, and maintenance — built to bring whatever you picture to life.</p>
          </div>
          <div>
            <h5>Service Area</h5>
            <ul>
              ${AREAS_MENU.map(i => `<li><a href="${i.href}">${i.label}</a></li>`).join('')}
            </ul>
          </div>
          <div>
            <h5>Services</h5>
            <ul>
              ${SERVICES_MENU.map(i => `<li><a href="${i.href}">${i.label}</a></li>`).join('')}
            </ul>
          </div>
          <div>
            <h5>Contact</h5>
            <ul>
              <li class="footer-contact-item"><svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="7" cy="7" r="5.5" stroke="currentColor" stroke-width="1.3"/><path d="M7 4 V7 L9 8.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg><span>Accepting inquiries 24/7</span></li>
              <li class="footer-contact-item"><svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M2 3 L 3 2 L 5 2 L 6 4 L 5 5 C 5.5 7, 7 8.5, 9 9 L 10 8 L 12 9 L 12 11 L 11 12 C 7 12, 2 7, 2 3 Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg><span>(650) 716-7231</span></li>
              <li class="footer-contact-item"><svg width="14" height="14" viewBox="0 0 14 14" fill="none"><rect x="1.5" y="3" width="11" height="8" rx="1" stroke="currentColor" stroke-width="1.3"/><path d="M1.5 4 L 7 8 L 12.5 4" stroke="currentColor" stroke-width="1.3"/></svg><span>gerryklandscapingco@gmail.com</span></li>
              <li class="footer-contact-item"><svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M7 12.5 C 3.5 8.5, 2 6.5, 2 5 A 5 5 0 1 1 12 5 C 12 6.5, 10.5 8.5, 7 12.5 Z" stroke="currentColor" stroke-width="1.3"/></svg><span>Redwood City, CA 94063</span></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <div class="footer-nav">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="services.html">Services</a>
            <a href="gallery.html">Gallery</a>
            <a href="contact.html">Contact</a>
          </div>
          <span class="footer-license">Licensed · Bonded · Insured · CA Lic. #C-27 1098432</span>
          <span>© 2026 Gerryk Landscaping — Designed, Built, and Ranked by Contractor Growth</span>
        </div>
      </div>
    </footer>
  `;

  const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
    "accent": "green",
    "darkTone": "forest"
  }/*EDITMODE-END*/;

  const ACCENTS = {
    green: { bright: '#28A745', dark: '#004225', deep: '#002E1A' },
    emerald: { bright: '#10B981', dark: '#064E3B', deep: '#04372A' },
    olive: { bright: '#84A84F', dark: '#3D5220', deep: '#293816' }
  };

  function applyTweaks(t) {
    const a = ACCENTS[t.accent] || ACCENTS.green;
    document.documentElement.style.setProperty('--bright-green', a.bright);
    document.documentElement.style.setProperty('--bright-green-hover', a.bright);
    document.documentElement.style.setProperty('--dark-green', a.dark);
    document.documentElement.style.setProperty('--dark-green-deep', a.deep);
  }

  let currentTweaks = { ...TWEAK_DEFAULTS };
  applyTweaks(currentTweaks);

  function buildTweaksPanel() {
    const panel = document.createElement('div');
    panel.className = 'tweaks-panel';
    panel.id = 'tweaks-panel';
    panel.innerHTML = `
      <h6>Tweaks</h6>
      <div class="tweak-row">
        <label>Accent Palette</label>
        <div class="tweak-options" data-key="accent">
          <button data-val="green">Forest Green</button>
          <button data-val="emerald">Emerald</button>
          <button data-val="olive">Olive</button>
        </div>
      </div>
    `;
    document.body.appendChild(panel);

    function refresh() {
      panel.querySelectorAll('.tweak-options').forEach(group => {
        const key = group.dataset.key;
        group.querySelectorAll('button').forEach(b => {
          b.classList.toggle('active', b.dataset.val === currentTweaks[key]);
        });
      });
    }
    refresh();

    panel.querySelectorAll('.tweak-options button').forEach(b => {
      b.addEventListener('click', () => {
        const key = b.parentElement.dataset.key;
        const val = b.dataset.val;
        currentTweaks[key] = val;
        applyTweaks(currentTweaks);
        refresh();
        try { window.parent.postMessage({ type: '__edit_mode_set_keys', edits: { [key]: val } }, '*'); } catch (e) {}
      });
    });
  }

  function init() {
    const headerSlot = document.getElementById('header-slot');
    const footerSlot = document.getElementById('footer-slot');
    if (headerSlot) headerSlot.outerHTML = HEADER;
    if (footerSlot) footerSlot.outerHTML = FOOTER;

    buildTweaksPanel();

    window.addEventListener('message', (e) => {
      const d = e.data;
      if (!d || !d.type) return;
      if (d.type === '__activate_edit_mode') document.getElementById('tweaks-panel').classList.add('visible');
      else if (d.type === '__deactivate_edit_mode') document.getElementById('tweaks-panel').classList.remove('visible');
    });
    try { window.parent.postMessage({ type: '__edit_mode_available' }, '*'); } catch (e) {}

    // FAQ accordion
    document.querySelectorAll('.faq-item').forEach(item => {
      const q = item.querySelector('.faq-q');
      if (q) q.addEventListener('click', () => item.classList.toggle('open'));
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
