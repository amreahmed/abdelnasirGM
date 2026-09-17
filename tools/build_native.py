"""Generate native HTML5. Photographs and campaign creatives remain image assets."""
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
media = json.loads((ROOT/'tools/media.json').read_text(encoding='utf-8'))

def heading(arabic, english, level=2, extra=''):
    return f'''<header class="section-heading {extra}">
      <h{level} lang="ar" dir="rtl" data-outline="{escape(arabic)}">{escape(arabic)}</h{level}>
      <p>{escape(english)}</p>
    </header>'''

icons = '''<span class="post-actions" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M20 11a8 8 0 1 0-4 7l5 3-1-6a8 8 0 0 0 0-4Z"/></svg><svg class="heart" viewBox="0 0 24 24"><path d="M12 21 3 12C-3 5 6-2 12 5c6-7 15 0 9 7Z"/></svg><svg viewBox="0 0 24 24"><path d="M5 3h14v18l-7-5-7 5Z"/></svg></span>'''
posts = {
  'food': [
    ('صينية العيلة — أهل اليمن','العيلة تتجمع،\nوالصينية تكفي.\nقعدة فيها كل اللي بتحبهم،\nوصينية عليها كل اللي بتحبوه.\nصينية العيلة من أهل اليمن...\nطعم يجمع الكل.'),
    ('المعصوب الملكي — أهل اليمن','لسه فيه مكان للحلو...\nوالملكي يستاهل المكان ده.\nالمعصوب الملكي من أهل اليمن\nبطعمه ولمسته الحلوة\nاللي تخلي آخر لقمة هي أحلى لقمة.'),
    ('شواية هايل','شواية هايل\nطعم الشوي\nو ريحة تفتح النفس\nولقمة تستاهل تتكرر.'),
    ('دجاج — طعم يروق المزاج','إذا ودك بطعم يضبط المزاج\nخلك على المضمونة.\nنصف حبة بطعم طيب،\nوسفرة تستاهلها.')],
  'beauty': [
    ('Cairo Cosmo Center — رحلة العناية بالبشرة','ابدئي رحلتك في العناية بالبشرة\nمع Cairo Cosmo Center\nمن أول التشخيص لحد النتيجة اللي بتحلمي بيها،\nهنساعدك تختاري الجلسات الأنسب لبشرتك\nلأن العناية ببشرتك... رحلة تستحق البداية.'),
    ('Cairo Cosmo Center — تشخيص البشرة','مش كل عيوب البشرة... بتكون ظاهرة.\nممكن يكون تحت السطح جفاف، تصبغات، أو انسداد مسام.\nعشان كده في مركز Cairo Cosmo بنبدأ بتشخيص بشرتك،\nوبعدها بنحدد الجلسة الأنسب ليكي.'),
    ('Cairo Cosmo Center — جلسة الديرما','متخبيش نفسك...\nالحبوب وآثارها مش لازم تكون جزء من بشرتك.\nجلسة الديرما بتساعد على:\n• تقليل آثار الحبوب والندبات\n• تنعيم وتوحيد ملمس البشرة\n• تحفيز الكولاجين وتجديد خلايا البشرة'),
    ('Cairo Cosmo Center — OxyGeneo','الحل السحري لبشرتك في جلسة واحدة\nجلسة OxyGeneo\nبتساعد على تنظيف البشرة، وتجديد الخلايا، وتحفيز الكولاجين والنضارة.\nوالنتيجة من أول جلسة\nاحجزي جلستك في Cairo Cosmo Center')],
  'fashion': [
    ('Gorest winter collection','Gorest hoodies\nIs available now!'),
    ('Gorest player hoodie','Hoodie oversized\n“player”\nOrder now'),
    ('Gorest dream hoodie','Hoodie oversized\n“dream”\nOrder now'),
    ('Gorest heart break hoodie','Hoodie oversized\n“heart break”\nOrder now')]
}

html = ['''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#130b25">
  <meta name="description" content="Abdelnasser GM — Content Creator. Ideas, scripts, storytelling, design and video content for food, beauty, fashion and finance brands.">
  <title>Abdelnasser GM | Content Creator</title>
  <link rel="icon" href="assets/2d0b56e7e51cf11036ad8734bdb67e2d.png">
  <link rel="stylesheet" href="assets/cairo.css">
  <link rel="stylesheet" href="assets/oswald.css">
  <link rel="stylesheet" href="styles.css">
  <link rel="preload" as="image" href="assets/studio-background.png">
  <script src="script.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#about">Skip to portfolio</a>
  <main id="portfolio">
    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-type">
        <p class="hero-role">Content Creator</p>
        <h1 id="hero-title">ABDELNASSER GM</h1>
        <div class="name-echo" aria-hidden="true"><span>ABDELNASSER GM</span><span>ABDELNASSER GM</span><span>ABDELNASSER GM</span><span>ABDELNASSER GM</span><span>ABDELNASSER GM</span><span>ABDELNASSER GM</span></div>
      </div>''']
# Clip only the original photographed subject: no AI-generated portrait or face changes.
outline=[(763,190),(742,194),(723,207),(709,225),(704,248),(707,275),(712,301),(721,328),(737,352),(758,371),(766,384),(754,400),(728,413),(709,427),(688,453),(681,479),(675,509),(668,541),(665,562),(657,592),(665,619),(686,630),(678,661),(670,689),(662,721),(660,750),(654,777),(652,797),(662,822),(668,839),(666,900),(913,900),(915,864),(920,842),(930,812),(942,781),(952,750),(961,721),(968,690),(978,660),(984,636),(980,615),(991,604),(986,578),(978,549),(970,520),(963,491),(956,462),(949,440),(934,420),(913,404),(891,390),(863,379),(851,366),(841,347),(836,324),(841,304),(840,283),(835,269),(830,245),(822,223),(809,206),(790,195)]
clip=','.join(f'{(x-650)/345*100:.3f}% {(y-188)/712*100:.3f}%' for x,y in outline)
html.append(f'''<div class="hero-portrait" style="clip-path:polygon({clip})"><img src="assets/fd4eb84492676633e52dae3667c98f34.png" alt="Abdelnasser in his black T-shirt with colorful sticky notes" width="1600" height="900" fetchpriority="high"></div>''')
html += ['''    </section>
    <section class="about section-shell" id="about" aria-label="About me">
''', heading('طب أنا مين بقى؟!', 'ABOUT ME'), '''
      <div class="about-copy" lang="ar" dir="rtl">
        <p>أنا عبدالناصر، <bdi>Content Creator</bdi> بحب أكتب وأحوّل الأفكار لحاجة تتشاف وتتسمع وتفضل في الدماغ.</p>
        <p>دخلت مجال الفيديو والتصميم من سنين،<br>ومن وقتها وأنا بجرب وأتعلم وأعمل محتوى بأشكال كتير؛<br>من الـ<bdi>Reels</bdi> والـ<bdi>Social Media Content</bdi>، للـ<bdi>Storytelling</bdi> والـ<bdi>Vlogs</bdi> والمحتوى الشخصي.</p>
        <p>اشتغلت على محتوى لبراندات ومجالات مختلفة، وده خلاني أتعلم مش بس إزاي أعمل فيديو شكله حلو،<br>لكن إزاي أطلع فكرة مناسبة، أحكيها بطريقة تشد، وأحوّلها لمحتوى يخلي الناس تكمل للآخر.</p>
        <p>وده البورتفوليو بتاعي...<br>شوية من الحاجات اللي عملتها، والحاجات اللي لسه جاية.</p>
      </div>
      <div class="about-english" lang="en">
        <p>I'm Abdelnasser, a Content Creator who loves writing and turning ideas into content people remember.</p>
        <p>I've been into video and design for years, creating Reels, Social Media Content, Storytelling, Vlogs, and more.</p>
        <p>I've worked with different brands and industries, always looking for simple ideas that grab attention and tell a story.</p>
        <p>This is my portfolio — a look at what I've created and what's next.</p>
      </div>
    </section>
    <section class="skills section-shell" id="skills" aria-label="My skills">
''', heading('الحاجات اللي بعرف أعملها', 'MY SKILLS'), '<dl class="skills-list">']
skills = [
    ('Idea Generation','أفكار','بطلع أفكار وأحوّلها لحاجة قابلة للتنفيذ'),
    ('Script Writing','كتابة','بكتب اسكريبتات وحوارات وقصص للفيديو'),
    ('Directing','إخراج','بحدد شكل الفيديو واللقطات والحركة وطريقة التنفيذ'),
    ('Video Content Creation','تصوير','بصوّر فيديوهات Reels وUGC'),
    ('Graphic Design','تصميم','بعمل تصميمات للسوشيال ميديا وVisuals مختلفة'),
    ('AI Video & Content','AI','بعرف أستخدم أدوات الـAI لصناعة فيديوهات وتصميمات'),
    ('Video Editing','مونتاج','بعمل مونتاج للفيديوهات بشكل يناسب كل فكرة')]
for english,arabic,description in skills:
    html.append(f'<div class="skill-row"><dt>{escape(english)}</dt><dd lang="ar" dir="rtl"><strong>{escape(arabic)} :</strong><p>{escape(description)}</p></dd></div>')
html.append('</dl></section>')

for group_index, group in enumerate(['food','beauty','fashion','finance']):
    entry = next(s for s in media if s[0]==group)
    english,arabic = entry[1].split(' / ')
    html.append(f'<section class="work-section section-shell" id="{group}" aria-label="{escape(english)}">')
    if group_index==0:
        html.append(heading('المحتوى اللي اشتغلت عليه','SELECTED WORK',extra='work-title'))
    html.append(heading(arabic,english,3,'category-heading'))
    html.append('<div class="video-grid">')
    for n,(video,poster,*_) in enumerate(entry[4],1):
        label=f'{english} — video {n}'
        html.append(f'''<article class="video-card">
          <video muted loop playsinline preload="none" poster="assets/{poster}.jpg" data-src="assets/{video}.mp4" aria-label="{escape(label)}"></video>
          <button class="watch-video" type="button" data-title="{escape(label)}" aria-label="Play {escape(label)} with sound"><span aria-hidden="true">▶</span></button>
          <noscript><a class="video-fallback" href="assets/{video}.mp4">Watch video {n}</a></noscript>
        </article>''')
    html.append('</div>')
    if group in posts:
        source = next(s for s in media if s[0]==group+'-posts')[2]
        # CSS clips the exact original campaign images. Frames and captions are HTML/CSS.
        xs, y, size, total = ([212,616,1014,1417],174,318,1920) if group=='beauty' else ([176,513,845,1181],145,265,1600)
        html.append(f'<div class="post-grid" aria-label="{escape(english)} social media designs">')
        for n,(label,caption) in enumerate(posts[group]):
            direction='ltr' if group=='fashion' else 'rtl'
            lang='en' if group=='fashion' else 'ar'
            html.append(f'''<article class="post-card">
              <figure class="social-frame">
                <div class="post-top" aria-hidden="true"><span>•••</span><span class="post-plus">+</span></div>
                <div class="campaign-photo"><img src="assets/{source}.png" alt="{escape(label)}" loading="lazy" decoding="async" style="width:{total/size*100:.5f}%;left:{-xs[n]/size*100:.5f}%;top:{-y/size*100:.5f}%"></div>
                {icons}
              </figure>
              <div class="caption-note" lang="{lang}" dir="{direction}"><span class="paper-clips" aria-hidden="true"></span><p>{escape(caption).replace(chr(10),'<br>')}</p></div>
            </article>''')
        html.append('</div>')
    html.append('</section>')

html.append('''  </main>
  <button class="back-to-top" type="button" aria-label="Back to top" hidden>↑</button>
  <dialog class="viewer" aria-labelledby="viewer-title">
    <div class="viewer-bar"><h2 id="viewer-title"></h2><button class="close-viewer" type="button" aria-label="Close video">✕</button></div>
    <div class="viewer-content"></div>
  </dialog>
</body>
</html>
''')
(ROOT/'index.html').write_text('\n'.join(html),encoding='utf-8')
print('Built native HTML: selectable text, 7 flowing sections, 16 videos, 12 individual social cards.')
