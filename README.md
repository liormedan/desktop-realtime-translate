
## 🧪 בדיקה

לאחר ההתקנה, הפעל את האפליקציה:

```bash
python main.py
```

* ודא שהפלט של האודיו במחשב מוגדר ל־VB-Audio Cable
* בחלון שיופיע תראה את התרגום מתעדכן בזמן אמת

---

## 🧰 ספריות בשימוש

* [Whisper](https://github.com/openai/whisper)
* [PyQt5](https://pypi.org/project/PyQt5/)
* [Sounddevice](https://pypi.org/project/sounddevice/)
* [Googletrans](https://pypi.org/project/googletrans/)
* [FFmpeg](https://ffmpeg.org/)

---

## ✅ הרצת בדיקות אוטומטיות

להתקנת כל התלויות והרצת הבדיקות השתמשו ב־`Makefile` המצורף:

```bash
make install
make test
```

---

## 📝 הערות

* מומלץ להשתמש בכרטיס קול וירטואלי כמו [VB-Audio Virtual Cable](https://vb-audio.com/Cable/) כדי ללכוד את האודיו מהמערכת.
* במידה ויש לך כרטיס מסך NVIDIA, ניתן להתקין גרסה מותאמת של Torch עם CUDA לשיפור ביצועים.

---

## 🤝 תרומות

הפרויקט פתוח להצעות, שיפורים ותרומות 🎉

```

---

רוצה שאשמור לך אותו כקובץ `README.md` בקובץ להורדה או אעבור לשלב הבא עם הקוד של `audio_capture.py`?
```