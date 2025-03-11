# Online Localization - Server

## Introduction
**Online Localization** is a library for managing multilingual applications online. This section is the server-side component of the library, while client-side libraries are available in other repositories of this account.

With this library, you can add new languages to your software without writing any new code or rebuilding the application.

## Features
<ul>
  <li>Add new languages without modifying code or rebuilding the application.</li>
  <li>Manage and edit languages via the server.</li>
  <li>Customize the server for specific needs.</li>
  <li>Fully compatible with client libraries.</li>
</ul>

## Customization
If needed, you can modify this server according to your requirements and apply the corresponding changes in the client libraries to ensure proper functionality.

## Adding New Languages and Words

To take advantage of the multilingual features, you need to first add the desired language to the system and then upload the relevant words for that language to the server.

### Steps to Add a Language:
<ol>
  <li>To add a new language, you must first register the language in the system. To do this, go to the server's management section and add the new language.</li>
  <li>After registering the language, you can upload the translation files or dictionary for that language to complete the process.</li>
</ol>

### Steps to Add Words:
<ol>
  <li>Once the language is added, you can register the relevant words for that language on the server.</li>
  <li>To add words, either upload the files containing the translations for the new language or use the appropriate user interface to edit the words.</li>
  <li>Once the new words are uploaded, they will be available for use in the clients and other parts of the application.</li>
</ol>

With this process, adding new languages and words to the software can be done without writing extra code or rebuilding the application.

## Usage with Django
This server is built using **Django**, making it easy to integrate with existing Django applications. To set up the server:

<ol>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Apply migrations:
    <pre><code>python manage.py migrate</code></pre>
  </li>
  <li>Run the server:
    <pre><code>python manage.py runserver</code></pre>
  </li>
  <li>Access the API via <a href="http://localhost:5000/API/Dictionary/en?version=1" target="_blank">http://localhost:5000/API/Dictionary/en?version=1</a></li>
</ol>

---

<div dir="rtl">

# سرور آنلاین لوکالایزیشن

## معرفی
**Online Localization** یک کتابخانه برای مدیریت چندزبانه بودن نرم‌افزارها به صورت آنلاین است. این بخش سرور این کتابخانه است و کتابخانه‌های مربوط به کلاینت در مخازن دیگر همین اکانت قرار دارند.

با استفاده از این کتابخانه، می‌توانید زبان‌های جدید را به نرم‌افزار خود اضافه کرده یا به‌روزرسانی نمایید بدون نیاز به نوشتن خط کد یا **build** مجدد نرم‌افزار.

## ویژگی‌ها
<ul>
  <li>افزودن زبان‌های جدید بدون نیاز به تغییر کد و build مجدد</li>
  <li>مدیریت و ویرایش زبان‌ها از طریق سرور</li>
  <li>قابلیت سفارشی‌سازی سرور برای نیازهای مختلف</li>
  <li>هماهنگی کامل با کتابخانه‌های کلاینت</li>
</ul>

## سفارشی‌سازی
در صورت نیاز می‌توانید تغییرات مورد نیاز خود را در این سرور اعمال کرده و در کتابخانه‌های کلاینت هم این تغییرات را پیاده‌سازی نمایید.

## افزودن زبان و کلمات جدید

برای استفاده از قابلیت‌های چندزبانه، ابتدا باید زبان مورد نظر را به سیستم اضافه کنید و سپس کلمات مربوط به آن زبان را در سرور بارگذاری کنید.

### مراحل افزودن زبان:
<ol>
  <li>برای اضافه کردن یک زبان جدید، باید ابتدا زبان را در سیستم ثبت کنید. برای این کار، به قسمت مدیریت سرور رفته و زبان جدید را اضافه کنید.</li>
  <li>بعد از ثبت زبان، می‌توانید فایل‌های ترجمه یا واژه‌نامه مربوط به آن زبان را برای تکمیل فرایند اضافه کنید.</li>
</ol>

### مراحل افزودن کلمات:
<ol>
  <li>پس از افزودن زبان، می‌توانید کلمات مربوط به آن زبان را در سرور ثبت کنید.</li>
  <li>برای اضافه کردن کلمات، فایل‌هایی که شامل ترجمه‌های زبان جدید هستند را به سرور ارسال کرده یا از رابط کاربری مناسب برای ویرایش کلمات استفاده کنید.</li>
  <li>پس از بارگذاری کلمات جدید، آن‌ها برای استفاده در کلاینت‌ها و سایر بخش‌های اپلیکیشن در دسترس خواهند بود.</li>
</ol>

با این روش، فرآیند افزودن زبان‌های جدید و کلمات مربوطه به نرم‌افزار بدون نیاز به نوشتن کد اضافی یا ساخت مجدد نرم‌افزار انجام می‌شود.

## استفاده با جنگو
این سرور با **جنگو** ساخته شده است، بنابراین به‌راحتی می‌توان آن را با پروژه‌های جنگو یکپارچه کرد. برای راه‌اندازی سرور:

<ol>
  <li>نصب وابستگی‌ها:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>اعمال مهاجرت‌های پایگاه داده:
    <pre><code>python manage.py migrate</code></pre>
  </li>
  <li>اجرای سرور:
    <pre><code>python manage.py runserver</code></pre>
  </li>
  <li>دسترسی به API از طریق <a href="http://localhost:5000/API/Dictionary/en?version=1" target="_blank">http://localhost:5000/API/Dictionary/en?version=1</a></li>
</ol>

</div>
