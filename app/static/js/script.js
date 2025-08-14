// Sample articles data
const articles = [
    {
        id: 1,
        title: "The Evolution of Web Design in 2023",
        excerpt: "How modern CSS and JavaScript frameworks are pushing the boundaries of what's possible in web design.",
        category: "Design",
        date: "June 12, 2023",
        readTime: "5 min read",
        image: "https://images.unsplash.com/photo-1547658719-da2b51169166?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1364&q=80"
    },
    {
        id: 2,
        title: "Building Scalable Microservices with Node.js",
        excerpt: "Best practices for architecting your Node.js applications to handle millions of requests.",
        category: "Development",
        date: "June 8, 2023",
        readTime: "7 min read",
        image: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80"
    },
    {
        id: 3,
        title: "The Rise of No-Code Development Platforms",
        excerpt: "How no-code tools are democratizing software development and what it means for professional developers.",
        category: "Technology",
        date: "June 5, 2023",
        readTime: "4 min read",
        image: "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80"
    },
    {
        id: 4,
        title: "UX Psychology: Principles Every Designer Should Know",
        excerpt: "Leveraging cognitive psychology to create more intuitive and engaging user experiences.",
        category: "Design",
        date: "May 29, 2023",
        readTime: "6 min read",
        image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
    },
    {
        id: 5,
        title: "React 18: New Features and Performance Improvements",
        excerpt: "Exploring concurrent rendering, automatic batching, and other enhancements in the latest React release.",
        category: "Development",
        date: "May 22, 2023",
        readTime: "8 min read",
        image: "https://images.unsplash.com/photo-1633356122544-f134324a6cee?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
    },
    {
        id: 6,
        title: "The Future of Remote Work in Tech",
        excerpt: "How distributed teams are reshaping company cultures and productivity in the tech industry.",
        category: "Business",
        date: "May 18, 2023",
        readTime: "5 min read",
        image: "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
    }
];

// DOM Elements
const gridContainer = document.querySelector('.grid-container');
const loadMoreBtn = document.getElementById('load-more');
const themeToggle = document.getElementById('theme-toggle');
const backToTop = document.getElementById('back-to-top');
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const mainNav = document.querySelector('.main-nav');

// Initial load
let visibleArticles = 3;
renderArticles();

// Render articles
function renderArticles() {
    gridContainer.innerHTML = '';
    
    articles.slice(0, visibleArticles).forEach(article => {
        const articleEl = document.createElement('article');
        articleEl.className = 'article-card';
        articleEl.innerHTML = `
            <div class="card-image">
                <img src="${article.image}" alt="${article.title}">
            </div>
            <div class="card-content">
                <span class="card-category">${article.category}</span>
                <h3 class="card-title">${article.title}</h3>
                <p class="card-excerpt">${article.excerpt}</p>
                <div class="card-footer">
                    <span>${article.date}</span>
                    <span>${article.readTime}</span>
                </div>
            </div>
        `;
        
        gridContainer.appendChild(articleEl);
    });
    
    // Hide load more button if all articles are visible
    if (visibleArticles >= articles.length) {
        loadMoreBtn.style.display = 'none';
    }
}

// Load more articles
loadMoreBtn.addEventListener('click', () => {
    visibleArticles += 3;
    renderArticles();
    
    // Smooth scroll to bottom of new articles
    setTimeout(() => {
        gridContainer.scrollIntoView({
            behavior: 'smooth',
            block: 'end'
        });
    }, 100);
});

// Theme toggle
themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    themeToggle.innerHTML = newTheme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    
    // Save preference to localStorage
    localStorage.setItem('theme', newTheme);
});

// Check for saved theme preference
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
    themeToggle.innerHTML = savedTheme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
}

// Back to top button
backToTop.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Show/hide back to top button based on scroll position
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTop.style.opacity = '1';
        backToTop.style.visibility = 'visible';
    } else {
        backToTop.style.opacity = '0';
        backToTop.style.visibility = 'hidden';
    }
});

// Mobile menu toggle
mobileMenuBtn.addEventListener('click', () => {
    mainNav.classList.toggle('show');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        mainNav.classList.remove('show');
    });
});

// Form submission
document.querySelector('.newsletter-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const email = e.target.querySelector('input').value;
    
    // In a real app, you would send this to your backend
    console.log('Subscribed with email:', email);
    alert('Thanks for subscribing!');
    e.target.reset();
});

// Animation on scroll
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.featured-post, .article-card, .newsletter');
    
    elements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.2;
        
        if (elementPosition < screenPosition) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
};

// Set initial styles for animation
document.querySelectorAll('.featured-post, .article-card, .newsletter').forEach(element => {
    element.style.opacity = '0';
    element.style.transform = 'translateY(20px)';
    element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
});

window.addEventListener('scroll', animateOnScroll);
window.addEventListener('load', animateOnScroll);