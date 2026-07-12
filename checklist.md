Here’s a comprehensive checklist to manually test every feature of BookShelf CMS (Chapters 1‑4). Work through each section step by step.

---

## 🧪 BookShelf CMS – Full User Acceptance Checklist

### 📚 1. Catalogue (Book Listing & Detail)

- [ ] **Book List Page**  
  - Visit `/catalog/` (or `/` if that's the home).  
  - ✔️ Page loads with a grid of published books, newest first.  
  - ✔️ Each card shows title, tags, description snippet, author, publish date.  
  - ✔️ Hovering a card lifts it slightly (hover effect).  
  - ✔️ Responsive layout on mobile/tablet.

- [ ] **Pagination**  
  - Create enough books (≥ 10) and set `PAGINATE_BY` low (e.g., 3) in settings.  
  - ✔️ Pagination controls appear at the bottom.  
  - ✔️ Clicking page numbers works; active page is highlighted.  
  - ✔️ First/Last/Previous/Next buttons work correctly.  
  - ✔️ Directly entering a huge page number shows the last page, not an error.

- [ ] **Tag Filtering**  
  - Click a tag pill on a book card.  
  - ✔️ URL changes to `/catalog/tag/<slug>/`.  
  - ✔️ Page shows a banner with “Books tagged ‘tagname’” and a “Clear filter” link.  
  - ✔️ Only books with that tag appear.  
  - ✔️ Clicking “Clear filter” returns to the full catalogue.

- [ ] **Book Detail Page**  
  - Click a book title to go to `/catalog/<slug>/`.  
  - ✔️ Page shows title, all tags, metadata (added by, publish date, status, last updated).  
  - ✔️ Full synopsis rendered (Markdown if used).  
  - ✔️ “Share” and “Back to catalog” buttons visible.  
  - ✔️ “Similar books” carousel appears (if there are books sharing tags).  
  - ✔️ Review section shows existing reviews (with name, date, body) and an empty state if none.  
  - ✔️ Review form is present.

- [ ] **Similar Books**  
  - Tag two books with the same tags.  
  - ✔️ On each book's detail page, the other appears under “Similar books”.  
  - ✔️ The badge shows “1 shared tag” (or more).  
  - ✔️ Clicking a similar book navigates to its detail page.

---

### 🔍 2. Full‑Text Search

- [ ] **Search Page**  
  - Visit `/catalog/search/`.  
  - ✔️ Large search input and “Search” button visible.

- [ ] **Search Execution**  
  - Type a word present in a book's title or synopsis.  
  - ✔️ Results page shows “Results for ‘word’”.  
  - ✔️ Matching books appear with title, tags, snippet.  
  - ✔️ Clicking a result goes to the book detail.

- [ ] **Empty Results**  
  - Search for a nonsensical string (e.g., `xyznope`).  
  - ✔️ Shows “No books match your search” with a friendly illustration and a “Browse all books” button.

- [ ] **Fuzzy Matching (Trigram)**  
  - Search for a misspelled title (e.g., “Django” → “Djagno”).  
  - ✔️ If full‑text search returns nothing, the fallback still finds the book (requires PostgreSQL with `pg_trgm` enabled).  
  - ✔️ A note “(using fuzzy title matching)” may appear.

- [ ] **“New search” Button**  
  - After a search, click the “New search” button.  
  - ✔️ Returns to the empty search form.

---

### ✍️ 3. Reviews

- [ ] **Submit a Review**  
  - On a book detail page, fill in the review form (name, body).  
  - ✔️ Form validates (required fields).  
  - ✔️ After submission, redirects to the review success page (or back to detail with a success message).  
  - ✔️ The new review appears in the reviews list with correct name, date, body.  
  - ✔️ Empty state is replaced by the review.

- [ ] **Duplicate/Multiple Reviews**  
  - Submit a second review.  
  - ✔️ The counter updates (“2 reviews”).  
  - ✔️ Both reviews appear in chronological order (newest first, depending on your view sorting).  

- [ ] **Review Form on Separate Page**  
  - Access `/catalog/<slug>/review/` directly.  
  - ✔️ Form is displayed; submitting works the same way.

---

### ✉️ 4. Share via Email

- [ ] **Share Form**  
  - Click “Share” on a book detail page.  
  - ✔️ Page shows a card with “Share ‘Book Title’”, form fields (to, comments optional).

- [ ] **Send Share Email**  
  - Fill recipient email, add a message.  
  - ✔️ Click “Send Email”.  
  - ✔️ Success message “Email sent!” appears.  
  - ✔️ The email is actually delivered (or visible in the console if using console backend).  

- [ ] **Validation**  
  - Submit with empty “To” field.  
  - ✔️ Validation error shown.  
  - ✔️ “Back to book” link works.

---

### 📡 5. RSS Feed & Sitemap

- [ ] **RSS Feed**  
  - Visit `/catalog/feed/`.  
  - ✔️ Browser renders raw XML (or shows feed preview).  
  - ✔️ Feed contains latest 5 published books with title, link, description.  

- [ ] **Sitemap**  
  - Visit `/sitemap.xml`.  
  - ✔️ Returns an XML sitemap index with a link to `/sitemap-books.xml`.  
  - Visit that link.  
  - ✔️ Lists all published books with correct last‑modified dates.

---

### 🛡️ 6. Admin Interface

- [ ] **Book Admin**  
  - Log into `/admin/` as superuser.  
  - ✔️ Book list shows filters (by status, added_by), search fields, date hierarchy.  
  - ✔️ Adding/editing a book prepopulates slug from title.  
  - ✔️ You can set status (Draft/Published).  

- [ ] **Review Admin**  
  - ✔️ Review list allows filtering by active/inactive, search by name.  
  - ✔️ Can toggle `active` to hide a review from the site.

- [ ] **Email OTP Admin (read‑only)**  
  - ✔️ See a list of OTPs with user, purpose, code, used status.  
  - ✔️ Searchable by username/email.

- [ ] **Profile Admin**  
  - ✔️ Manage user bios, phone numbers, avatars.

---

### 👤 7. User Registration & Email Verification

> **Prerequisite:** Set `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` for development, or use real SMTP. The console backend prints emails to the terminal.

- [ ] **Registration Form**  
  - Visit `/accounts/register/`.  
  - ✔️ Form shows fields: username, email, password, confirm password.  
  - ✔️ Validation: mismatched passwords, duplicate email, weak password all show errors.  
  - ✔️ Submitting with valid data redirects to `/accounts/register/done/`.

- [ ] **Registration Done Page**  
  - ✔️ Displays a message: “Check your email”, and a link to “Enter verification code”.  
  - ✔️ In the console output, you see the verification email with a 6‑digit code and a magic link.

- [ ] **OTP Verification (manual code entry)**  
  - Click “Enter verification code” (or go to `/accounts/register/confirm/`).  
  - ✔️ Enter the 6‑digit code from the console.  
  - ✔️ Click “Verify”.  
  - ✔️ You are logged in automatically and redirected to `/accounts/profile/`.  
  - ✔️ The account is now active.

- [ ] **Magic‑Link Verification**  
  - Register a second account.  
  - Instead of entering the code, copy the full verification URL from the console (the one containing `/register/confirm/<uidb64>/<token>/`).  
  - ✔️ Paste it into the browser.  
  - ✔️ Instant verification – logged in and redirected to profile.

- [ ] **Verification Expiry / Invalid Code**  
  - Attempt to verify with a wrong code.  
  - ✔️ Error message “That code is invalid or has expired.”  
  - After too many wrong attempts (5 by default), you get a lockout warning.

- [ ] **Resend Code**  
  - On the verification page, click “Resend code”.  
  - ✔️ A new email is sent, old code invalidated.  
  - ✔️ Rapid repeated clicks show a cooldown message.

---

### 🔑 8. Login & Logout

- [ ] **Email‑Based Login**  
  - Log out if you're in. Visit `/accounts/login/`.  
  - ✔️ Form asks for email and password.  
  - ✔️ Enter email (not username) + password of a verified user.  
  - ✔️ Successful login → redirected to profile (or `next` parameter if provided).  
  - ✔️ Login with wrong credentials shows “Invalid email or password.”  
  - ✔️ Too many failed attempts triggers a lockout message.

- [ ] **Inactive User Cannot Log In**  
  - Try to log in with an unverified (still inactive) account.  
  - ✔️ Error message: “Please verify your email before signing in.”

- [ ] **Redirect after Login**  
  - While logged out, try to access `/accounts/profile/edit/`.  
  - ✔️ You're redirected to the login page. After login, you land on the originally requested page.  

- [ ] **Logout**  
  - Click “Sign out” (from profile or user dropdown).  
  - ✔️ You see “You have been signed out” with a link to sign in again.  
  - ✔️ Visiting a protected page after logout sends you to login.

---

### 🔐 9. Password Change & Reset

- [ ] **Change Password (authenticated)**  
  - Navigate to `/accounts/password-change/` (link on profile page).  
  - ✔️ Enter old password, new password twice.  
  - ✔️ Submit → success message “Password changed”.  
  - ✔️ Log out, log in with new password – works.

- [ ] **Password Reset (forgotten password)**  
  - Log out. Click “Forgot your password?” on login page.  
  - ✔️ Enter email address → submit.  
  - ✔️ See “Check your inbox” page.  
  - ✔️ Console prints an email with a reset link.  

- [ ] **Reset Confirm**  
  - Copy the reset link from the console (the one with `/password-reset/<uidb64>/<token>/`).  
  - ✔️ Paste in browser, see “Set a new password” form.  
  - ✔️ Enter new password twice → success message “Password set”.  
  - ✔️ Log in with the new password.

- [ ] **Invalid Reset Link**  
  - Use a wrong or expired token.  
  - ✔️ Page shows “The password reset link was invalid” and offers to request a new one.

---

### 🧑‍💼 10. Profile & Avatar

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

### 🎨 11. UI & Cross‑Cutting Concerns

- [ ] **Dark Mode Toggle**  
  - Click the sun/moon icon in the navbar.  
  - ✔️ Site theme toggles between light and dark.  
  - ✔️ Preference persists across page reloads.  

- [ ] **Mobile Responsiveness**  
  - Resize browser to mobile width.  
  - ✔️ Hamburger menu appears; menu items clickable.  
  - ✔️ All pages scroll vertically without overflow.  
  - ✔️ Cards stack in a single column.  
  - ✔️ Footer columns stack properly.

- [ ] **Flash Messages**  
  - Perform actions that trigger success/error messages (login, verification, profile save).  
  - ✔️ Colored alert banners appear at the top with icons.  
  - ✔️ They automatically disappear? (If you added that) or remain until dismissed.

- [ ] **Navigation Consistency**  
  - All navbar links (Home, Books, Search, Feed, Login/Profile dropdown) work.  
  - ✔️ “BookShelf” logo links to catalogue.

- [ ] **404 Page**  
  - Visit a non‑existent URL like `/catalog/this-book-does-not-exist/`.  
  - ✔️ Friendly 404 page with “Page not found” and a “Go to Catalog” button.

---

## 🧰 Testing Tools & Notes

- Use the **Django console email backend** to inspect all emails without a real SMTP server.  
- For full‑text search tests, ensure PostgreSQL is running and `pg_trgm` extension is installed (`SELECT * FROM pg_extension;`).  
- If you switch between SQLite and PostgreSQL, re‑run migrations and load data as described in the README.  
- Tailwind CDN is used; ensure internet connectivity for styling.  
- Media files (avatars) will be stored in `media/avatars/` – confirm that directory exists and is writable.

---
