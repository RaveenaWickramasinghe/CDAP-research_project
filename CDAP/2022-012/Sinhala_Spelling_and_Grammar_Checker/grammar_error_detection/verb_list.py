verbs = [
  ['කරනවා','කරමි', 'කළෙමි', 'කරන්නෙමි','කරන්න', 'කරයි' , 'කරනු', 'කරන්නේ','කළා','කල','කළේ','කළ','කරන','කිරීම','කිරීමට','කිරීමේ','කර','කරමින්','කරලා','කළේය','කරපු','කලේ','කරන්නට','කරගෙන','කරමු','කරන්නෙමු','කළෙමු','කෙරෙන','කරගන්න','කිරීමෙන්','කරගත්','කිරීම්','කරති','කරයි','කරන්නේය','කරන්නෙහි'],
  ['තිබෙනවා', 'තිබේ','තිබූ','තිබෙන','තිබුණා','තිබුණේ','තිබුනේ','තිබුන','තිබුණු','තිබුණි','තිබිණි','තිබෙන්නේ'],
  ['තියනවා','තියෙන්නේ','තියෙන','තියන','තියමි','තියන්නෙමි','තියමු','තියන්නෙමු','තබා','තියෙනව'],
  ['දෙන්න', 'දෙන','දුන්','දුන්න','දෙනවා','දෙමු','දෙන්නෙමු','දෙමි','දෙන්නෙමි','දෙන්නේය','දිය','දීම','දීමට'],
  ['ගිය','ගොස්','ගියේ','ගියා','ගියෙමි','ගියේය','ගියාය','ගියෙමු','ගියහ','ගියෙහි'],
  ['එන','එන්න','එනවා','එන්නෙමි','එන්නෙමු','එමි','එමු','එන්නෙය'],
  ['ලබන','ලද','ලබා','ලබනවා','ලබන්නෙමි','ලබන්නෙමු','ලැබෙන','ලැබූ','ලදී','ලැබේ','ලැබී','ලබාදෙන','ලැබුණු'],
  ['හිටපු','හිටිනවා','හිටියේ','හිටිය','හිටියා'],
  ['ගත්','ගත්තාය','ගත්තේය','ගත','ගන්න','ගැනීමට','ගැනීම','ගෙන','ගත්තේ','ගන්නා','ගත්තා','ගත්තෙමි','ගත්තෙමු','ගමු','ගමි','ගත්ත','ගන්නේ','ගැනීමේ','ගන්නවා','ගන්නට','ගනු'],
  ['වෙන','වන','විය','වූ','වෙන්න','වීම','වෙයි','වී','වෙලා','වෙන්නේ','වූයේ','වීමට','වෙනවා','වෙමි','වෙමු','වෙන්නෙමු','වෙන්නෙමි','වුණෙමි','වුණෙමු','වුනේ','වුණේ','වනවා','වුන'],
  ['සිටි','සිටී','සිටියි' ,'සිටින','සිටියේ','සිටිනවා','සිටිමි','සිටින්නෙමි','සිටින්නෙමු','සිටියෙමි','සිටියහ','සිටියා','සිටියේය','සිටින්නේ'],
  ['කියන්නේ','කියන','කියලා','කියලයි','කියල','කියන්න','කියා','කියනවා','කියමි','කියමු','කියන්නෙමි','කියන්නෙමු','කීවෙමි','කීවෙමු','කිව්වා','කී','කියයි','කිව්වෙ','කිව','කියති'],
  ['කියවන','කියවන්න'],
  ['ආදරෙයි'],
  ['නාදවෙයි'],
  ['ඉන්න','ඉන්නේ','ඉන්නවා','ඉමු'],
  ['බලන්න','බලා','බලනවා','බලමි','බලන්නෙමි','බලමු','බලන්නෙමු','බලුවෙමි','බලුවෙමු','බලුවාය','බලන','බලහු','බැලුවෙහු'],
  ['නොවේ','නොවන','නෙවෙයි','නොව','නොවෙනවා'],
  ['සිදු','වුණා','උනා','සිදුවෙනවා','උනේ'],
  ['සිදුවෙනවා','සිදුවන','සිදුවූ','සිදුකළ','සිදුකරන'],
  ['ඉදිරිපත්'],
  ['පවසනවා','පැවසුවෙමි','පවසන්නෙමි','පැවසුවෙමු','පවසන්නෙමු','පැවසූහ','පැවසුවාය','පැවසුවේ','පවසයි','පවසා','පැවසීය','පවසන්නේ'],
  ['යනු','යන්නේ','යයි','යනවා','යමි','යමු','යන්නෙමි','යන්නෙමු','යන්නෙය','යාමට','යාම','යන්නෙ','යා','යන්නීය'],
  ['පවතින','පැවති','පවතිනවා','පැවැති','පවතී','පැවැත්වෙන'],
  ['පසුගිය'],
  ['පස්සෙ'],
  ['නේ'],
  ['නෙමෙයි'],
  ['පැමිණි','පැමිණෙනවා','පැමිණ','පැමිණෙන'],
  ['ලියනවා','ලියන්න','ලියමි','ලියන්නෙමි','ලියමු','ලියන්නෙමු','ලීවෙමි','ලීවේය','ලියූහ','ලියන','ලීවෙමි','ලීවෙමු','ලියයි','ලියන්නේය'],
  ['සොයනවා','සොයා','සොයමි','සොයන්නෙමි','සෙව්වෙමි','සොයමු','සොයන්නෙමු','සෙව්වෙමු'],
  ['ඉල්ලනවා','ඉල්ලා','ඉල්ලමු','ඉල්ලන්නෙමු','ඉල්ලුවෙමු','ඉල්ලමි','ඉල්ලනෙමි','ඉල්ලුවෙමි'],
  ['උනත්'],
  ['යොදා'],
  ['දාලා'],
  ['අරන්','අරගෙන'],
  ['තීරණය'],
  ['විස්තර'],
  ['නිර්මාණය'],
  ['සංවිධානය','සකස්'],
  ['නිකුත්'],
  ['යොමු'],
  ['ඉවත්'],
  ['ඉටු'],
  ['පළ'],
  ['පිහිටි'],
  ['වනු','වු','වුවද','වුවත්'],
  ['එල්ල','එල්ලමි','එල්ලන්නෙමි','එල්ලෙමි','එල්ලෙමු','එල්ලෙන්නෙමු','එල්ලමු'],
  ['දන්නේ','දන්නවා','දනිමි','දන්නා'],
  ['හමුවේ'],
  ['දාන්න','දාගෙන'],
  ['ආපු','ආවේ'],
  ['හිතෙනවා','හිතන්නේ'],
  ['හදන'],
  ['දුන්නා','දෙමි','දෙමු','දෙන්නෙමි','දෙන්නෙමු','දෙන්නේ','දුන්නේ','දමා','දීලා'],
  ['එන්නේ'],
  ['ඇන්දේය','ඇන්දාය','ඇන්දුවෙහි','ඇන්දෙහි'],
  ['නිරත'],
  ['පදිංචි'],
  ['එක්ව'],
  ['දැක','දකින','දක්වන','දුටුවාය','දුටුවෙමි'],
  ['පෙන්වා'],
  ['පත්ව','ලක්'],
  ['බෙදා'],
  ['පාවිච්චි','භාවිත'],
  ['දෙසැ'],
  ['හිනා'],
  ['ලද්දේ','ලද්දෙහි', 'ලද්දෙහු'],
  ['කන','කමි', 'කමු', 'කන්නෙමි', 'කන්නෙමු','කෑවෝය','කනවා'],
  ['බිව්වාය','බොමි', 'බොමු', 'බිව්වේය','බොති', 'බිව්වෙමි', 'බොති', 'බිව්වෙමි', 'බිව්වෙමුබොති', 'බිව්වෙමු'],
  ['කෑ'],
  ['දරන','දරමි', 'දරන්නෙමි', 'දරනෙමි', 'දරමු', 'දරන්නෙමු', 'දරනෙමු', 'දැරුවාය'],
  ['නොකරන','නොකරමි', 'නොකරමු', 'නොකරන්නෙමි', 'නොකරන්නෙමු', 'නොකෙරුවෙමි', 'නොකෙරුවෙමු', 'නොකෙරුවාය'],
  ['අහන්න','අහනවා', 'අහමි', 'අහමු', 'අහන්නෙමි', 'අහන්නෙමු', 'අහුවෙමි', 'අහුවෙමු'],
  ['හඬයි'],
  ['කැඩුවෙමු','කැඩුවෙමි', 'කැඩුවෙහු', 'කඩන්නෙමි', 'කඩන්නෙමු', 'කැඩුවාය','කඩයි'],
  ['නටන්නීය','නටති' , 'නටමි', 'නටමු', 'නටන්නෙමු', 'නටන්නෙමි', 'නැටුවාය', 'නැටුවෙමි', 'නැටුවෙමු'],
  ['කොටති'],
  ['කැඳවයි']
]

