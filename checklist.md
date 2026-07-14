# BookShelf CMS – Complete User Checklist (Chapters 1‑5)
## 📚 1. Catalogue (Book Listing & Detail)

- [ ] **Book List Page**  
  - Visit `/catalog/` (or the home page).  
  - ✔️ Page loads with a grid of published books, newest first.  
  - ✔️ Each card shows title, tags, description snippet, added_by, publish date.  
  - ✔️ Cards have hover effect (subtle lift).  
  - ✔️ Responsive layout on mobile/tablet.

- [ ] **Pagination**  
  - Ensure you have enough published books (≥ 10) and `PAGINATE_BY` is set low (e.g., 3) for testing.  
  - ✔️ Pagination controls appear at the bottom.  
  - ✔️ Clicking page numbers works; active page is highlighted.  
  - ✔️ First/Last/Previous/Next buttons function correctly.  
  - ✔️ Entering an out‑of‑range page number (e.g., `?page=99`) shows the last page.  
  - ✔️ Entering a non‑numeric page number (e.g., `?page=abc`) shows the first page.

- [ ] **Tag Filtering**  
  - Click a tag pill on a book card.  
  - ✔️ URL changes to `/catalog/tag/<slug>/`.  
  - ✔️ Page shows a banner “Books tagged with ‘tagname’”.  
  - ✔️ Only books with that tag appear.  
  - ✔️ A “Clear filter” link returns to the full catalogue.

- [ ] **Book Detail Page**  
  - Click a book title to go to `/catalog/<slug>/`.  
  - ✔️ Page shows title, all tags, metadata (added by, publish date, status, last updated).  
  - ✔️ Full synopsis rendered (Markdown if used).  
  - ✔️ “Share” and “Back to catalog” buttons visible.  
  - ✔️ “Similar books” section appears (if there are books sharing tags).  
  - ✔️ Review section shows existing reviews (name, date, body) or an empty state.  
  - ✔️ Review form is present.

- [ ] **Similar Books**  
  - Tag two books with the same tags.  
  - ✔️ On each book's detail page, the other appears under “Similar books”.  
  - ✔️ Books are ordered by number of shared tags, then by publish date.

---

## 🔍 2. Full‑Text Search

- [ ] **Search Page**  
  - Visit `/catalog/search/`.  
  - ✔️ Search input and “Search” button are visible.

- [ ] **Search Execution**  
  - Type a word present in a book's title or synopsis.  
  - ✔️ Results page shows “Books matching ‘query’”.  
  - ✔️ Matching books appear with title, tags, snippet.  
  - ✔️ Clicking a result goes to the book detail.

- [ ] **Empty Results**  
  - Search for a nonsensical string (e.g., `xyznope`).  
  - ✔️ Shows “No books match your search” and a “Browse all books” link.

- [ ] **Fuzzy Matching (Trigram)**  
  - Search for a misspelled title (e.g., “Django” → “Djagno”).  
  - ✔️ If full‑text search returns no results, the trigram fallback finds the book.  
  - ✔️ A note may indicate fuzzy matching was used.

- [ ] **New Search**  
  - After a search, click “Search again”.  
  - ✔️ Returns to the empty search form.

---

## ✍️ 3. Reviews

- [ ] **Submit a Review**  
  - On a book detail page, fill in the review form (name, body).  
  - ✔️ Form validates required fields.  
  - ✔️ After submission, redirects to the review success page (or back to detail with success message).  
  - ✔️ The new review appears in the reviews list with correct name, date, body.

- [ ] **Multiple Reviews**  
  - Submit a second review.  
  - ✔️ Review count updates (“2 reviews”).  
  - ✔️ Reviews display in chronological order (newest first?).

- [ ] **Review Form on Separate Page**  
  - Access `/catalog/<slug>/review/` directly.  
  - ✔️ Form is displayed; submission works.

---

## ✉️ 4. Share via Email

- [ ] **Share Form**  
  - Click “Share” on a book detail page.  
  - ✔️ Page shows “Share ‘Book Title’”, form fields (to, comments optional).

- [ ] **Send Share Email**  
  - Fill recipient email, add a message, click “Send Email”.  
  - ✔️ Success message “Email sent!” appears.  
  - ✔️ Email is delivered (or printed to console if console backend).  

- [ ] **Validation**  
  - Submit with empty “To” field.  
  - ✔️ Validation error shown.  
  - ✔️ “Back to book” link works.

---

## 📡 5. RSS Feed & Sitemap

- [ ] **RSS Feed**  
  - Visit `/catalog/feed/`.  
  - ✔️ Browser renders raw XML (or shows feed preview).  
  - ✔️ Feed contains latest 5 published books with title, link, description.  

- [ ] **Sitemap**  
  - Visit `/sitemap.xml`.  
  - ✔️ Returns an XML sitemap index linking to `/sitemap-books.xml`.  
  - Visit that link.  
  - ✔️ Lists all published books with correct last‑modified dates.

---

## 🛡️ 6. Admin Interface

- [ ] **Book Admin**  
  - Log into `/admin/` as superuser.  
  - ✔️ Book list shows filters (by status, added_by), search, date hierarchy.  
  - ✔️ Adding/editing a book prepopulates slug from title.  
  - ✔️ Can set status (Draft/Published).  

- [ ] **Review Admin**  
  - ✔️ Review list allows filtering by active/inactive, search by name.  
  - ✔️ Can toggle `active` to hide a review from the site.

- [ ] **Email OTP Admin**  
  - ✔️ List of OTPs with user, purpose, code, used status (read‑only).  
  - ✔️ Searchable by username/email.

- [ ] **Profile Admin**  
  - ✔️ Manage user bios, phone numbers, avatars.

---

## 👤 7. User Registration & Email Verification

> Use `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` for testing; emails appear in the terminal.

- [ ] **Registration Form**  
  - Visit `/accounts/register/`.  
  - ✔️ Fields: username, email, password, confirm password.  
  - ✔️ Validation errors for mismatched passwords, duplicate email, weak password.  
  - ✔️ Valid submission redirects to `/accounts/register/done/`.

- [ ] **Registration Done Page**  
  - ✔️ Displays “Check your email” and a link to enter verification code.  
  - ✔️ In the console, a verification email appears with a 6‑digit code and a magic link.

- [ ] **OTP Verification (manual code entry)**  
  - Go to `/accounts/register/confirm/`.  
  - ✔️ Enter the 6‑digit code from the console.  
  - ✔️ Click “Verify”.  
  - ✔️ Automatically logged in, redirected to profile. Account is now active.

- [ ] **Magic‑Link Verification**  
  - Register a second account.  
  - Instead of entering the code, copy the magic link from the console (`/register/confirm/<uidb64>/<token>/`).  
  - ✔️ Paste in browser → instant verification, logged in, profile page.

- [ ] **Invalid Code / Expiry**  
  - Attempt to verify with a wrong code.  
  - ✔️ Error message “That code is invalid or has expired.”  
  - After too many wrong attempts (5 default), a lockout warning appears.

- [ ] **Resend Code**  
  - On verification page, click “Resend code”.  
  - ✔️ New email sent, old code invalidated.  
  - ✔️ Rapid repeated clicks show a cooldown message.

---

## 🔑 8. Login & Logout

- [ ] **Email‑Based Login**  
  - Log out, visit `/accounts/login/`.  
  - ✔️ Form asks for email and password.  
  - ✔️ Login with verified email + password → redirect to profile.  
  - ✔️ Wrong credentials show “Invalid email or password.”  
  - ✔️ Too many failed attempts triggers lockout.

- [ ] **Inactive User Cannot Log In**  
  - Try logging in with an unverified account.  
  - ✔️ Error: “Please verify your email before signing in.”

- [ ] **Redirect After Login**  
  - While logged out, try to access `/accounts/profile/edit/`.  
  - ✔️ Redirected to login; after login you land on the originally requested page.  

- [ ] **Logout**  
  - Click “Sign out”.  
  - ✔️ See “You have been signed out” with a link to sign in again.  
  - ✔️ Visiting a protected page after logout redirects to login.

---

## 🔐 9. Password Change & Reset

- [ ] **Change Password (authenticated)**  
  - Navigate to `/accounts/password-change/`.  
  - ✔️ Enter old password, new password twice.  
  - ✔️ Submit → success message “Password changed”.  
  - ✔️ Log out, log in with new password – works.

- [ ] **Password Reset (forgotten password)**  
  - Log out, click “Forgot your password?” on login page.  
  - ✔️ Enter email → submit.  
  - ✔️ See “Check your inbox” page.  
  - ✔️ Console prints an email with a reset link.

- [ ] **Reset Confirm**  
  - Copy the reset link from console (the one with `/password-reset/<uidb64>/<token>/`).  
  - ✔️ Paste in browser, see “Set a new password” form.  
  - ✔️ Enter new password twice → success message “Password set”.  
  - ✔️ Log in with the new password.

- [ ] **Invalid Reset Link**  
  - Use a wrong or expired token.  
  - ✔️ Page shows “The password reset link was invalid” and offers to request a new one.

---

## 🧑‍💼 10. Profile & Avatar

- [ ] **View Profile**  
  - After login, visit `/accounts/profile/`.  
  - ✔️ Shows username, email, full name, bio, phone (or “Not set”), avatar (initials if no image).  

- [ ] **Edit Profile**  
  - Click “Edit profile”.  
  - ✔️ Form pre‑populated with current data.  
  - ✔️ Update first/last name, bio, phone.  
  - ✔️ Upload an avatar (image).  
  - ✔️ Click “Save changes” → redirected to profile, new data visible.  
  - ✔️ Avatar now displays the uploaded image instead of initials.

- [ ] **Profile Security**  
  - Log out, try to directly access `/accounts/profile/`.  
  - ✔️ Redirected to login.

---

## 🎨 11. UI & Cross‑Cutting Concerns

- [ ] **Dark Mode Toggle**  
  - Click the sun/moon icon in the navbar.  
  - ✔️ Site theme toggles between light and dark.  
  - ✔️ Preference persists across page reloads.  

- [ ] **Mobile Responsiveness**  
  - Resize browser to mobile width.  
  - ✔️ Hamburger menu appears; menu items clickable.  
  - ✔️ All pages scroll vertically without overflow.  
  - ✔️ Cards stack in a single column.  

- [ ] **Flash Messages**  
  - Perform actions that trigger success/error messages (login, verification, profile save).  
  - ✔️ Colored alert banners appear at the top with icons.  
  - ✔️ They can be dismissed.

- [ ] **Navigation Consistency**  
  - All navbar links (Home, Books, Search, Feed, Login/Profile dropdown) work.  
  - ✔️ “BookShelf” logo links to catalogue.

- [ ] **404 Page**  
  - Visit a non‑existent URL (e.g., `/catalog/nope`).  
  - ✔️ Friendly 404 page with “Page not found” and a link back.

---

## 🔵 12. Google Social Authentication (OAuth2)

> Prerequisite: Google OAuth2 credentials configured in `.env`; HTTPS dev server running via `runserver_plus` (or appropriate setup). Use a test Google account.

- [ ] **Button Visibility**  
  - Visit `/accounts/login/` and `/accounts/register/`.  
  - ✔️ Both pages show a “Continue with Google” button below the password form.

- [ ] **First‑time Google sign‑in (new user)**  
  - Click “Continue with Google” on either page.  
  - ✔️ Redirected to Google’s consent screen.  
  - ✔️ After granting permission, returned to site and automatically logged in.  
  - ✔️ A new `User` and a `Profile` are created.  
  - ✔️ You are redirected to the profile page (or the originally requested page).

- [ ] **Returning Google sign‑in (existing association)**  
  - Log out, then click “Continue with Google” again.  
  - ✔️ Logged in immediately without extra consent.  
  - ✔️ No duplicate user or profile created.

- [ ] **Conflict with verified local account**  
  - Ensure you have a local account with email `test@example.com` (verified).  
  - Log out. Click “Continue with Google” using a Google account with the exact same email.  
  - ✔️ Sign‑in is **blocked** – you see a warning message: “An account with this email already exists. Sign in with your password instead…”  
  - ✔️ You are redirected to the login page (not logged in).

- [ ] **Conflict with unverified local account**  
  - Create an account via the normal registration form but **do not verify** the email (leave `is_active=False`).  
  - Log out. Click “Continue with Google” using a Google account with the same email.  
  - ✔️ The stale (inactive) local account is automatically deleted.  
  - ✔️ A new verified user is created from the Google data and logged in seamlessly (no error, no warning).

- [ ] **Profile after social sign‑in**  
  - After any successful Google sign‑in, visit `/accounts/profile/`.  
  - ✔️ Profile page shows the user’s name (from Google), email, and a default avatar (initials).  
  - ✔️ The “Edit profile” page works normally; avatar can be changed.

- [ ] **Session & logout**  
  - After Google login, click “Sign out”.  
  - ✔️ You are logged out completely; revisiting the site does **not** automatically log you back in via Google (you must click the button again).

---

## 🧰 Testing Notes

- Use the **Django console email backend** to inspect all emails without a real SMTP server.  
- For full‑text search tests, ensure PostgreSQL is running and `pg_trgm` extension is installed.  
- For social auth tests, either run the development server with `runserver_plus` (HTTPS) or use a real HTTPS setup; Google OAuth2 requires secure origins.  
- Media files (avatars) are stored in `media/avatars/` – confirm that directory exists and is writable.  
- When switching between SQLite and PostgreSQL, remember to re‑run migrations and reload data.

---
