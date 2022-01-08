import pytest
import tortitle
from torcategory import GuessCategoryUtils


@pytest.mark.parametrize("test_input, e1, e2, e3", [
    ('权力的游戏.第S01-S08.Game.Of.Thrones.S01-S08.1080p.Blu-Ray.AC3.x265.10bit-Yumi',
     'Game Of Thrones', '', 'S01-S08'),
    ('辅佐官：改变世界的人们S01-S02.Chief.of.Staff.2019.1080p.WEB-DL.x265.AC3￡cXcY@FRDS',
     'Chief of Staff', '2019', 'S01-S02'),
    ('半暖时光.The.Memory.About.You.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'The Memory About You', '2021', 'S01'),
    ('不惑之旅.To.the.Oak.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'To the Oak',
     '2021', 'S01'),
    ('不惑之旅.To.the.Oak.S01.2021.V2.2160p.WEB-DL.AAC.H265-HDSWEB', 'To the Oak',
     '2021', 'S01'),
    ('当家主母.Marvelous.Women.S01.2021.V3.2160p.WEB-DL.AAC.H265-HDSWEB',
     'Marvelous Women', '2021', 'S01'),
    ('民警老林的幸福生活.The.Happy.Life.of.People\'s.Policeman.Lao.Lin.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'The Happy Life of People\'s Policeman Lao Lin', '2021', 'S01'),
    ('千古风流人物.Qian.Gu.Feng.Liu.Ren.Wu.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'Qian Gu Feng Liu Ren Wu', '2021', 'S01'),
    ('太平间闹鬼事件 The Haunting in Connecticut 2009 Blu-ray 1080p AVC DTS-HD MA 7.1-Pete@HDSky',
     'The Haunting in Connecticut', '2009', ''),
    ('一片冰心在玉壶.Heart.of.Loyalty.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'Heart of Loyalty', '2021', 'S01'),
    ('住在我隔壁的甲方.Party.A.Who.Lives.Beside.Me.S01.2021.1080p.WEB-DL.AAC.H264-HDSWEB',
     'Party A Who Lives Beside Me', '2021', 'S01'),
    ('铸匠.The.Builders.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'The Builders',
     '2021', 'S01'),
    ('CCTV1.Yuan.Meng.Zhong.Guo.De.Yao.Zhong.Hua.20211129.HDTV.1080i.H264-HDSTV.ts',
     'Yuan Meng Zhong Guo De Yao Zhong Hua 20211129', '', ''),
    ('CCTV5+.2021.Snooker.UK.Championship.20211129.HDTV.1080i.H264-HDSTV.ts',
     '2021 Snooker UK Championship 20211129', '2021', ''),
    ('CCTV5+.2021.World.Table.Tennis.Championship.20211130.HDTV.1080i.H264-HDSTV.ts',
     '2021 World Table Tennis Championship 20211130', '2021', ''),
    ('CCTV5.Total.Soccer.20211129.HDTV.1080i.H264-HDSTV.ts',
     'Total Soccer 20211129', '', ''),
    ('CCTV9.The.Legend.Of.Film.Ep01-Ep06.HDTV.1080i.H264-HDSTV',
     'The Legend Of Film', '', 'Ep01-Ep06'),
    ('The.Boys.S02.2020.1080p.BluRay.DTS.x265-10bit-HDS', 'The Boys', '2020',
     'S02'),
    ('Doctor.X.Surgeon.Michiko.Daimon.S06.1080p.BluRay.x265.10bit.FLAC.MNHD-FRDS',
     'Doctor X Surgeon Michiko Daimon', '', 'S06'),
    ('逆世界.Upside.Down.2012.BluRay.1080p.x265.10bit.2Audio.MNHD-FRDS',
     'Upside Down', '2012', ''),
    ('野战排.Platoon.1986.BluRay.1080p.x265.10bit.2Audio.MNHD-FRDS', 'Platoon',
     '1986', ''),
    ('Stargate.Atlantis.S04.Multi.1080p.BluRay.DTS-HDMA.5.1.H.264-CELESTIS',
     'Stargate Atlantis', '', 'S04'),
    ('谍影重重1-5.The.Bourne.2002-2016.1080p.Blu-ray.x265.DTS￡cXcY@FRDS',
     'The Bourne', '2002-2016', ''),
    ('豹.1963.JPN.1080p.意大利语中字￡CMCT风潇潇', '豹', '1963', ''),
    ('过界男女.2013.国粤双语.简繁中字￡CMCT紫卿醺', '过界男女', '2013', ''),
    ('金刚狼3殊死一战.Logan.2017.BluRay.1080p.x265.10bit.MNHD-FRDS', 'Logan', '2017',
     ''),
    ('(BDMV)Anneke Gronloh - De Regenboog Serie (2009) FLAC-CD] {NL,Telstar B.V,TCD 70316-2}',
     'Anneke Gronloh - De Regenboog Serie', '2009', ''),
    ('Foundation.2021.S01.2160p.ATVP.WEB-DL.DDP5.1.DV.HEVC-CasStudio',
     'Foundation', '2021', 'S01'),
    ('我是你的眼.I\'m.Your.Eyes.2016.S01.2160p.WEB-DL.H265.AAC-LeagueWEB',
     'I\'m Your Eyes', '2016', 'S01'),
    ('Guard.Jie.Fang.Xi.2022.S03.1080p.WEB-DL.H264.AAC-TJUPT', 'Guard Jie Fang Xi', '2022', 'S03'),
    ('[不能只有我看到的-便利店追女神食谱].Fast&Delicious.2021.1080i.HDTV.H264.DD-PTerTV', 'Fast&Delicious', '2021', ''),
    ('Ms.45.1981.720p.BluRay.FLAC1.0.x264-PTer', 'Ms 45', '1981', ''),
    ('BTV.The.Forbidden.City.Ep11-Ep12.HDTV.1080i.H264-HDSTV', 'The Forbidden City', '', 'Ep11-Ep12'),
    ('HunanTV.Da.Wan.Zai.De.Ye.20211201.HDTV.1080i.H264-HDSTV.ts', 'Da Wan Zai De Ye 20211201', '', ''),
    ('2021.FIVB.VNL.CHN.vs.BRA.20210608.1080p.REPACK.WEB-DL.x264.AAC-TJUPT.mp4', '2021 FIVB VNL CHN vs BRA 20210608', '2021', ''),
    ('失落的秘符.第1季', '失落的秘符', '', 'S1'),
    ('最后的决斗.The.Last.Duel.2021.1080p.Blu-ray.x265.DTS￡cXcY@FRDS', 'The Last Duel', '2021', ''),
    ('现代爱情S02.Modern.Love.2021.1080p.WEB-DL.x265.AC3￡cXcY@FRDS', 'Modern Love', '2021', 'S02'),
    ('สิ่งเล็กเล็กที่เรียกว่า...รัก.A.Little.Thing.Called.Love.AKA.First.Love.2010.WEB-DL.1080p.x264.AAC-PTHome.mp4', 'A Little Thing Called Love', '2010', ''),
    ('Top138.英雄本色(4K修复版).A.Better.Tomorrow.1986.REMASTERED.Bluray.1080p.x265.AAC(5.1).2Audios.GREENOTEA', 'A Better Tomorrow', '1986', ''),
    ('Weathering.With.You.2019.1080p.NLD.AVC.DTS-HD.MA.5.1-NeoVision', 'Weathering With You', '2019', ''),
    ('[BDMV][Bokutachi no Remake][Vol.01-02]', 'Bokutachi no Remake', '', ''),
    ('[吸血鬼同盟][Dance In The Vampire Bund][ダンスインザヴァンパイアバンド][BDMV][1080p][DISC×2][GER]', 'Dance In The Vampire Bund', '', ''),
    ('1917 2019 V2 ULTRAHD BluRay 2160p HEVC Atmos TrueHD7.1-sGnb@CHDBits', '1917', '2019', ''),
    ('[和楽器バンド (Wagakki Band) – TOKYO SINGING [初回限定映像盤 2Blu-ray]][BDMV][1080P][MPEG-4 AVC / LPCM]', 'Wagakki Band', '', ''),
    ('[酷爱电影的庞波小姐][Eiga Daisuki Pompo-san][映画大好きポンポさん][BDRip][1920x1040][Movie][x264 Hi10P TrueHD MKV][TTGA]', 'Eiga Daisuki Pompo-san', '', ''),
    ('[柳林风声][The Wind in the Willows][BDMV][1080p][MOVIE][AVC LPCM][UK]', 'The Wind in the Willows', '', ''),
    ('[BanG Dream! Episode of Roselia][劇場版 BanG Dream! Episode of Roselia][BDRip][1920x1080][Movie 01-02 Fin+SP][H264 FLAC DTS-HDMA MKV][自壓]', 'BanG Dream! Episode of Roselia', '', ''),
    ('[持续狩猎史莱姆三百年, 不知不觉就练到LV MAX][Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita][スライム倒して300年、知らないうちにレベルMAXになってました][外挂结构][日英简]', 'Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita', '', ''),
    ('[贾希大人不气馁][The Great Jahy Will Not Be Defeated! / Jahy-sama wa Kujikenai!][ジャヒー様はくじけない!][BDMV][1080p][Vol.1]', 'The Great Jahy Will Not Be Defeated!', '', ''),
])
def test_parseTVName(test_input, e1, e2, e3):
    a1, a2, a3, a4 = tortitle.parseMovieName(test_input)
    assert a1 == e1 and a2 == e2 and a3 == e3


@pytest.mark.parametrize("test_input, e1, e2", [
    ('权力的游戏.第S01-S08.Game.Of.Thrones.S01-S08.1080p.Blu-Ray.AC3.x265.10bit-Yumi',
     'TV', 'YUMI'),
    ('辅佐官：改变世界的人们S01-S02.Chief.of.Staff.2019.1080p.WEB-DL.x265.AC3￡cXcY@FRDS',
     'TV', 'FRDS'),
    ('半暖时光.The.Memory.About.You.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'TV',
     'HDSWEB'),
    ('不惑之旅.To.the.Oak.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'TV', 'HDSWEB'),
    ('BDRemux+Hakumei+to+Mikochi+JP+7³ACG@OurBits', 'Other', 'OURBITS'),
    ('FIFA.WORLD.CUP.QUALIFIERS.ENG.VS.ALB.20211113.1080i.HDTV.H264.DD-PTerTV.ts', 'HDTV', 'PTERTV'),
    ('Babymother.1998.1080p.BluRay.REMUX.AVC.FLAC.2.0-BLURANiUM.mkv', 'MovieRemux', 'BLURANIUM'),
    ('春花秋月未了情.Breezy.1973.1080p.BluRay.x265.10bit.FLAC.MNHD-FRDS', 'MovieEncode', 'FRDS'),
    ('Michael Jackson - The Mystery Of HIStory (1997) [FLAC]', 'Music', None),
    ('New_Order-(The_Rest_Of)_New_Order-CD-FLAC-1995-WREMiX', 'Music', 'WREMIX'),
    ('VA-Kill_Bill_Vol_2-(9362-48676-2)-CD-FLAC-2004', 'Music', '2004'),
    ('The Blue Diamonds - Het Beste Van (1988) [FLAC-CD] {WG,RM,Philips,834 484-2}', 'Music', None),
    ('Commodores - Caught In The Act (1975) [FLAC] {24-192 HDTracks}', 'Music', None),
    ('BTV.The.Forbidden.City.Ep11-Ep12.HDTV.1080i.H264-HDSTV', 'HDTV', 'HDSTV'),
    ('[漫游·张靓颖沉浸式虚拟音乐会·完整版].Roaming·Jane Zhang Immersive Virtual Concert.2021.1080p.WEB-DL.AVC.AAC-QHstudIo', 'MV', 'QHSTUDIO'),
    ('OOOPS2.2020.BluRay.1080p.2Audio.TrueHD.5.1.x265.10bit-BeiTai', 'MovieEncode', 'BEITAI'),
    ('现代爱情S02.Modern.Love.2021.1080p.WEB-DL.x265.AC3￡cXcY@FRDS', 'TV', 'FRDS'),

])
def test_guessByName(test_input, e1, e2):
    a1, a2 = GuessCategoryUtils.guessByName(test_input)
    assert a1 == e1 and a2 == e2
