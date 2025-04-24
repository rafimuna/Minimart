# Minimart
fullstack ecommerce website
"DjangoQuasarStore"
Project Feature:
• REST API authentication
• Django Admin এ full product management (image, video সহ)
• Quasar frontend এ registration/login, product list, search, filter, pagination
• Add to Cart system
• GSAP animation
• Component-based UI design
• Django Admin এ order management এবং navigation system
• Step-by-step logic explanation in Bangla
• Test system per step
• Clean file structure (Django dot structure সহ)
• Generate code with AI , implement in project fix error and solve.

PART 1: Backend - Django + Django REST Framework
প্রথমে Django প্রজেক্ট সেটআপ:
Project Name: shop_backend
Apps:
products – পণ্যের মডেল, API, ও admin management
orders – order tracking ও admin dashboard view
accounts – user registration/login API (JWT)
Step-by-step:
django-admin startproject shop_backend .
python manage.py startapp products, orders, accounts
Django REST Framework install
JWT authentication setup (djangorestframework-simplejwt)
Custom User Model (email-based)
Django admin customize (navigation/sidebar, logo, product upload with image/video preview)
Admin Customization:
ModelAdmin override করে list display
django-admin-interface বা jazzmin use করে dashboard UI change
Navigation menu dynamically বানানো যাবে sidebar টা fixed করে
PART 2: Frontend - Quasar Framework (Vue 3 + Pinia + Composition API)
Feature Plan:
•	Quasar SPA project (quasar create shop-frontend)
•	Global Pinia store setup (auth, product, cart)
•	Pages:
o	LoginPage.vue, RegisterPage.vue
o	ProductListPage.vue (search/filter/pagination)
o	ProductDetails.vue
o	AddCartPage.vue
o	UserProfile.vue
•	Components:
o	ProductCard.vue
o	Navbar.vue, Footer.vue, SearchBar.vue
o	Pagination.vue, FilterDropdown.vue
•	Animation:
o	GSAP for entry animation, smooth page transitions
•	Form validation + notification (Quasar Notify)
•	Loading/Error state handling
•	API call test per step (console log + component test section)
________________________________________
PART 3: Communication Between Django & Quasar
•	Django REST API endpoints:
o	/api/products/ (GET, POST for admin)
o	/api/products/<id>/ (GET single)
o	/api/cart/ (POST item, GET cart)
o	/api/orders/ (POST order, admin view)
•	Quasar থেকে axios দিয়ে fetch করা হবে
•	JWT token login system (token store in localStorage)
•	Route Guard দিয়ে user কে protect করা হবে
________________________________________
PART 4: Deployment Ready Features
•	Image & Video upload (Django FileField, ImageField + MEDIA_URL)
•	Pagination (DRF pagination + frontend pagination logic)
•	Product Search & Filter (query param + Quasar search bar)
•	Order list view Django Admin এ
•	Responsive UI with Quasar Grid System
________________________________________
File Structure (Django & Quasar Suggestion)
Django:
CopyEdit
shop_backend/
  ├── shop_backend/
  │   └── settings.py
  ├── products/
  ├── orders/
  ├── accounts/
  └── manage.py
Quasar:
css
shop-frontend/
  ├── src/
  │   ├── components/
  │   ├── pages/
  │   ├── stores/
  │   ├── router/
  │   └── App.vue
________________________________________
Demo Flow:
•	Admin Django panel থেকে প্রোডাক্ট আপলোড করবে (image/video সহ)
•	Quasar এর ProductListPage.vue এ সেই প্রোডাক্ট দেখাবে
•	User search করবে, filter করবে
•	Cart এ add করবে
•	Order করলে Django admin order dashboard এ দেখাবে

