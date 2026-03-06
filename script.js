// ==============================
// Initialize on DOM Ready
// ==============================
document.addEventListener('DOMContentLoaded', function () {
  // Initialize AOS
  AOS.init({
    duration: 800,
    once: false,
    offset: 50,
    easing: 'ease-out-cubic'
  });

  // Create floating particles
  createParticles();

  // Setup all animations
  setupMouseGlow();
  setupNavigation();
  setupCardEffects();
  setupButtonEffects();
  setupScrollProgress();
  setupThemeToggle();
  initParallaxShapes();

  // Animate hero on load
  animateHeroOnLoad();

  // Animate sidebar on load
  animateSidebar();
});

// ==============================
// Hero Load Animation
// ==============================
function animateHeroOnLoad() {
  const heroSection = document.querySelector('.hero-section');
  if (!heroSection) return;

  const elements = heroSection.querySelectorAll('p, h1, .flex');

  elements.forEach((el, index) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(50px)';

    setTimeout(() => {
      el.style.transition = 'all 1s cubic-bezier(0.16, 1, 0.3, 1)';
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    }, 200 + (index * 200));
  });
}

// ==============================
// Sidebar Animation
// ==============================
function animateSidebar() {
  const sidebar = document.querySelector('.sidebar');
  if (!sidebar) return;

  sidebar.style.opacity = '0';
  sidebar.style.transform = 'translateX(-100%)';

  setTimeout(() => {
    sidebar.style.transition = 'all 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
    sidebar.style.opacity = '1';
    sidebar.style.transform = 'translateX(0)';
  }, 100);
}

// ==============================
// Floating Particles
// ==============================
function createParticles() {
  const existing = document.querySelector('.particles');
  if (existing) existing.remove();

  const container = document.createElement('div');
  container.className = 'particles';
  container.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
  `;
  document.body.appendChild(container);

  for (let i = 0; i < 35; i++) {
    const particle = document.createElement('div');
    const size = 2 + Math.random() * 4;
    particle.style.cssText = `
      position: absolute;
      width: ${size}px;
      height: ${size}px;
      background: #7c3aed;
      border-radius: 50%;
      left: ${Math.random() * 100}%;
      top: ${Math.random() * 100}%;
      opacity: ${0.1 + Math.random() * 0.3};
      animation: floatParticle ${15 + Math.random() * 20}s linear infinite;
      animation-delay: ${-Math.random() * 20}s;
    `;
    container.appendChild(particle);
  }

  // Add particle animation
  const style = document.createElement('style');
  style.textContent = `
    @keyframes floatParticle {
      0% { transform: translateY(100vh) rotate(0deg); }
      100% { transform: translateY(-100vh) rotate(720deg); }
    }
  `;
  document.head.appendChild(style);
}

// ==============================
// Mouse Glow Effect
// ==============================
function setupMouseGlow() {
  const mouseGlow = document.getElementById('mouseGlow');
  if (!mouseGlow) return;

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let glowX = mouseX;
  let glowY = mouseY;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  function animate() {
    glowX += (mouseX - glowX) * 0.08;
    glowY += (mouseY - glowY) * 0.08;

    mouseGlow.style.left = glowX + 'px';
    mouseGlow.style.top = glowY + 'px';

    requestAnimationFrame(animate);
  }
  animate();
}

// ==============================
// Navigation
// ==============================
function setupNavigation() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  // Smooth scroll
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href');
      const targetSection = document.querySelector(targetId);

      if (targetSection) {
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Active nav on scroll
  window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
      const sectionTop = section.offsetTop - 150;
      if (window.scrollY >= sectionTop) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  });
}

// ==============================
// Card 3D Effects
// ==============================
function setupCardEffects() {
  const cards = document.querySelectorAll('.card-hover, .skill-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = (y - centerY) / 15;
      const rotateY = (centerX - x) / 15;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px) scale(1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
}

// ==============================
// Button Effects
// ==============================
function setupButtonEffects() {
  // Magnetic effect on primary buttons
  document.querySelectorAll('.btn-primary').forEach(button => {
    button.addEventListener('mousemove', (e) => {
      const rect = button.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;

      button.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
    });

    button.addEventListener('mouseleave', () => {
      button.style.transform = '';
    });
  });

  // Ripple effect on all buttons
  document.querySelectorAll('.btn-primary, .btn-secondary, .btn-accent').forEach(button => {
    button.addEventListener('click', function (e) {
      const ripple = document.createElement('span');
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height) * 2;

      ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        left: ${e.clientX - rect.left - size / 2}px;
        top: ${e.clientY - rect.top - size / 2}px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 50%;
        transform: scale(0);
        animation: rippleEffect 0.6s ease-out;
        pointer-events: none;
      `;

      this.style.position = 'relative';
      this.style.overflow = 'hidden';
      this.appendChild(ripple);

      setTimeout(() => ripple.remove(), 600);
    });
  });

  // Add ripple animation
  const style = document.createElement('style');
  style.textContent = `
    @keyframes rippleEffect {
      to { transform: scale(4); opacity: 0; }
    }
  `;
  document.head.appendChild(style);
}

// ==============================
// Scroll Progress Bar
// ==============================
function setupScrollProgress() {
  const progressBar = document.createElement('div');
  progressBar.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    width: 0%;
    background: linear-gradient(90deg, #7c3aed, #a78bfa);
    z-index: 9999;
    transition: width 0.1s;
    box-shadow: 0 0 10px rgba(124, 58, 237, 0.5);
  `;
  document.body.appendChild(progressBar);

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    progressBar.style.width = scrollPercent + '%';
  });
}

// ==============================
// Parallax on Scroll
// ==============================
window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;

  // Hero parallax
  const hero = document.querySelector('.hero-section');
  if (hero && scrolled < window.innerHeight) {
    hero.style.transform = `translateY(${scrolled * 0.4}px)`;
    hero.style.opacity = 1 - (scrolled / window.innerHeight);
  }
});

// ==============================
// Console
// ==============================
console.log('%c🚀 Portfolio Lyes Mouhoun', 'font-size: 20px; color: #7c3aed; font-weight: bold;');

// ==============================
// Theme Toggle (Animated Rising Sun/Moon)
// ==============================
function setupThemeToggle() {
  const toggleBtn = document.getElementById('themeToggle');
  const transitionOverlay = document.getElementById('themeTransition');
  console.log('setupThemeToggle init', toggleBtn, transitionOverlay);
  if (!toggleBtn || !transitionOverlay) return;

  const toggleIcon = toggleBtn.querySelector('.toggle-icon');
  const toggleText = toggleBtn.querySelector('.toggle-text');
  let isAnimating = false;

  // Load saved theme
  const savedTheme = localStorage.getItem('portfolio-theme');
  if (savedTheme === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
    updateToggleButton(true);
  }

  // Toggle on click
  toggleBtn.addEventListener('click', (e) => {
    console.log('themeToggle clicked! isAnimating:', isAnimating);
    if (isAnimating) return;
    isAnimating = true;

    const isLight = document.documentElement.getAttribute('data-theme') === 'light';
    const targetTheme = isLight ? 'dark' : 'light';
    const btnRect = toggleBtn.getBoundingClientRect();
    const centerX = btnRect.left + btnRect.width / 2;
    const centerY = btnRect.top + btnRect.height / 2;

    console.log('Switching to targetTheme:', targetTheme, 'from isLight:', isLight);

    // Create celestial body (Sun or Moon)
    const celestial = document.createElement('div');
    celestial.className = 'theme-celestial';
    celestial.textContent = isLight ? '🌙' : '☀️';
    celestial.style.top = `${centerY}px`;
    celestial.style.left = `${centerX}px`;
    transitionOverlay.appendChild(celestial);

    // Initial state
    celestial.style.transform = `translate(-50%, 0) scale(0)`;
    celestial.style.opacity = '0';
    celestial.style.transition = 'all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)';

    // Trigger rise animation
    requestAnimationFrame(() => {
      celestial.style.transform = `translate(-50%, -60vh) scale(3)`;
      celestial.style.opacity = '1';
    });

    // Theme switch & Lightwave ripple
    setTimeout(() => {
      // Apply theme
      if (targetTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
      } else {
        document.documentElement.removeAttribute('data-theme');
      }
      localStorage.setItem('portfolio-theme', targetTheme);
      updateToggleButton(targetTheme === 'light');

      // Create ripple effect
      const ripple = document.createElement('div');
      ripple.style.position = 'absolute';
      ripple.style.top = celestial.style.top;
      ripple.style.left = celestial.style.left;
      ripple.style.width = '10px';
      ripple.style.height = '10px';
      ripple.style.background = targetTheme === 'light' ? '#faf8f5' : '#09090b';
      ripple.style.borderRadius = '50%';
      ripple.style.transform = 'translate(-50%, -50%) scale(1)';
      ripple.style.transition = 'transform 0.8s ease-in-out';
      ripple.style.zIndex = '99998';
      transitionOverlay.appendChild(ripple);

      requestAnimationFrame(() => {
        ripple.style.transform = 'translate(-50%, -50%) scale(500)';
      });

      // Cleanup
      setTimeout(() => {
        celestial.style.opacity = '0';
        celestial.style.transform = `translate(-50%, -100vh) scale(1)`;
        setTimeout(() => {
          transitionOverlay.innerHTML = '';
          isAnimating = false;
        }, 500);
      }, 700);

    }, 600);
  });

  function updateToggleButton(isLight) {
    if (isLight) {
      toggleIcon.textContent = '🌙';
      toggleText.textContent = 'Mode sombre';
    } else {
      toggleIcon.textContent = '☀️';
      toggleText.textContent = 'Mode clair';
    }
  }
}

// ==============================
// Floating Parallax Shapes
// ==============================
function initParallaxShapes() {
  const container = document.getElementById('parallaxContainer');
  if (!container) return;

  const shapes = [];
  const numShapes = 20;

  // Generate shapes
  for (let i = 0; i < numShapes; i++) {
    const shape = document.createElement('div');
    shape.className = 'parallax-shape';

    // Randomize properties
    const size = Math.random() * 150 + 50; // 50px to 200px
    const isCircle = Math.random() > 0.5;

    shape.style.width = `${size}px`;
    shape.style.height = `${size}px`;
    shape.style.borderRadius = isCircle ? '50%' : '15%';
    shape.style.background = Math.random() > 0.5 ? 'var(--accent)' : 'var(--accent-light)';

    // Initial position
    const x = Math.random() * window.innerWidth;
    const y = Math.random() * window.innerHeight;
    shape.style.left = `${x}px`;
    shape.style.top = `${y}px`;

    // Custom animation constraints
    shape.dataset.speed = Math.random() * 0.5 + 0.1;
    shape.dataset.offsetX = 0;
    shape.dataset.offsetY = 0;
    shape.dataset.baseX = x;
    shape.dataset.baseY = y;

    container.appendChild(shape);
    shapes.push(shape);
  }

  // Mouse move inverse parallax
  window.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX / window.innerWidth - 0.5;
    const mouseY = e.clientY / window.innerHeight - 0.5;

    shapes.forEach(shape => {
      const speed = parseFloat(shape.dataset.speed);
      const moveX = mouseX * -100 * speed;
      const moveY = mouseY * -100 * speed;

      shape.style.transform = `translate(${moveX}px, ${moveY}px)`;
    });
  });

  // Slow natural float
  let time = 0;
  function animateFloat() {
    time += 0.005;
    shapes.forEach((shape, index) => {
      const speed = parseFloat(shape.dataset.speed);
      const floatX = Math.sin(time + index) * 20 * speed;
      const floatY = Math.cos(time + index) * 20 * speed;

      // Combine mouse transform with float transform using matrix or just adjusting base positions
      const currentTransform = shape.style.transform;
      if (currentTransform) {
        // Simple hack to add independent movement
        shape.style.marginLeft = `${floatX}px`;
        shape.style.marginTop = `${floatY}px`;
      }
    });
    requestAnimationFrame(animateFloat);
  }
  animateFloat();
}
