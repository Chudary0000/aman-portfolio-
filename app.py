
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aman Imran | Portfolio</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth}
body{font-family:Arial,sans-serif;background:#080d18;color:#edf2f7;line-height:1.7}
:root{--green:#19d69b;--muted:#a5b2c5}
nav{position:sticky;top:0;background:#080d18ed;
padding:18px 8%;display:flex;justify-content:space-between;
align-items:center;border-bottom:1px solid #ffffff12;z-index:10}
.logo{font-size:23px;font-weight:bold;color:var(--green)}
nav a{color:#dce5ee;text-decoration:none;margin-left:20px;font-size:14px}
nav a:hover{color:var(--green)}
.hero{min-height:85vh;display:flex;align-items:center;padding:70px 10%;
background:radial-gradient(circle at 80% 30%,#123e3545,transparent 40%)}
.tag{color:var(--green);letter-spacing:3px;font-size:13px}
h1{font-size:clamp(42px,7vw,75px);line-height:1.1;margin:20px 0}
h1 span{color:var(--green)}
.hero p{color:var(--muted);max-width:600px;font-size:17px}
.btn{display:inline-block;margin-top:28px;background:var(--green);
color:#06140f;padding:13px 25px;border-radius:7px;
text-decoration:none;font-weight:bold}
section{padding:85px 10%}
.heading{font-size:34px;margin-bottom:12px}
.heading span{color:var(--green)}
.sub{color:var(--muted);margin-bottom:35px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
.card{background:#111b2b;border:1px solid #ffffff12;
padding:25px;border-radius:14px;transition:.3s}
.card:hover{transform:translateY(-6px);border-color:var(--green)}
.card h3{color:var(--green);margin-bottom:12px}
.card p{color:var(--muted);font-size:15px}
.skills{display:flex;flex-wrap:wrap;gap:12px}
.skills span{background:#112c29;color:#6ef0c1;padding:10px 17px;
border-radius:7px;border:1px solid #19d69b35}
.contact{background:#0d1725;text-align:center}
.contact p{color:var(--muted)}
footer{text-align:center;padding:25px;color:#8290a4;
border-top:1px solid #ffffff12}
@media(max-width:650px){
nav{padding:15px 5%;flex-wrap:wrap;gap:12px}
nav div:last-child{width:100%;display:flex;gap:14px;flex-wrap:wrap}
nav a{margin:0}
.hero{padding:65px 7%;min-height:75vh}
section{padding:65px 7%}
}
</style>
</head>
<body>

<nav>
<div class="logo">AMAN.</div>
<div>
<a href="#home">Home</a>
<a href="#about">About</a>
<a href="#education">Education</a>
<a href="#skills">Skills</a>
<a href="#projects">Projects</a>
<a href="#contact">Contact</a>
</div>
</nav>

<div class="hero" id="home">
<div>
<div class="tag">WELCOME TO MY PORTFOLIO</div>
<h1>Hi, I'm <span>Aman Imran.</span></h1>
<p>DAE Civil Engineering graduate from Pakistan.
Interested in technology, web development, AutoCAD
and building creative digital projects.</p>
<a class="btn" href="#about">Explore My Portfolio ↗</a>
</div>
</div>

<section id="about">
<div class="heading">About <span>Me</span></div>
<p class="sub">A little introduction about myself</p>
<div class="card">
<h3>Aman Imran</h3>
<p>I am from Pakistan, with an educational background
in Civil Engineering. I enjoy learning new technologies,
developing practical skills and working on creative ideas.
My interests include engineering, programming,
design and digital work.</p>
</div>
</section>

<section id="education">
<div class="heading">My <span>Education</span></div>
<p class="sub">My academic background</p>
<div class="grid">
<div class="card">
<h3>DAE Civil Engineering</h3>
<p>Kashmir Polytechnic Institute<br>
Muzaffarabad, Azad Kashmir</p>
<p>Marks: 2900 / 3600<br>Percentage: 80.56%</p>
</div>
<div class="card">
<h3>Intermediate (HSSC)</h3>
<p>Boys Inter College Khalana<br>
Mirpur Board<br>Session: 2023–2025</p>
</div>
</div>
</section>

<section id="skills">
<div class="heading">My <span>Skills</span></div>
<p class="sub">Skills I have and technologies I am learning</p>
<div class="skills">
<span>MS Word</span><span>MS Excel</span>
<span>AutoCAD</span><span>HTML</span>
<span>Python</span><span>Graphic Design</span>
<span>Customer Dealing</span><span>Communication</span>
<span>Teamwork</span><span>Sales</span>
</div>
</section>

<section id="projects">
<div class="heading">My <span>Projects</span></div>
<p class="sub">Ideas and projects I am developing</p>
<div class="grid">
<div class="card">
<h3>Personal Portfolio</h3>
<p>A responsive personal website built with Python and Flask.</p>
</div>
<div class="card">
<h3>Aman Academy</h3>
<p>An educational platform idea connecting students and tutors
through courses and study notes.</p>
</div>
<div class="card">
<h3>Explore Azad Kashmir</h3>
<p>A content creation concept focused on exploring
the beauty and culture of Azad Kashmir.</p>
</div>
</div>
</section>

<section class="contact" id="contact">
<div class="heading">Let's <span>Connect</span></div>
<p>Interested in learning, collaboration and new opportunities.</p>
<p style="margin-top:15px">Location: Pakistan</p>
<a class="btn" href="mailto:">Contact Me</a>
</section>

<footer>© 2026 Aman Imran | Personal Portfolio</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)