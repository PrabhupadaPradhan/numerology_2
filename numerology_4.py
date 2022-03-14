import streamlit as st
import base64
import datetime as dt
def create_download_link(val, filename):
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'
st.title("NUMEROLOGY APP(Copyright © 2021 Prabhupada Pradhan ALL RIGHTS RESERVED)")
name_org = st.text_input("Please enter your name:- ")
date_org = st.text_input("Please enter your date of birth:- ")
a_date = st.text_input("Please enter another date of birth to check compatability:- ")
dob = [i for i in date_org.split("/")]
date_org = "-".join((date_org.split("/"))[::-1]) + " 00:00:00"
a_dob = [i for i in a_date.split("/")]
a_date = "-".join((a_date.split("/"))[::-1]) + " 00:00:00"
pdf_name = "trial_1"
import pandas as pd
from fpdf import FPDF
import os
pdf = FPDF()
df = pd.DataFrame()
df["Name"] = pd.Series([name_org])
df["Date"] = pd.Series([date_org])
compat_dict = {"A" : {1 : [4, 5, 7], 2 : [4, 6, 22], 3 : [3, 6, 8, 9], 4 : [1, 2, 7, 8], 5 : [1], 6 : [2, 3, 6, 9], 7 : [1, 4, 22], 8 : [4, 22], 9 : [3, 6, 9], 11 : [22], 22 : [2, 7, 8, 11]},
              "B" : {1 : [1, 8], 2 : [2, 3, 7, 9, 11], 3 : [2, 22], 4 : [4, 6, 22], 5 : [5, 9, 11], 6 : [4, 11], 7 : [2, 7, 11], 8 : [1, 11], 9 : [2, 5, 7, 11, 22], 11 : [2, 5, 6, 7, 8, 9, 11], 22 : [3, 4, 9, 22]},
              "C" : {1 : [2, 6, 22], 2 : [1, 5], 3 : [4, 5, 7, 11], 4 : [3, 11], 5 : [2, 3, 4, 6, 7, 22], 6 : [1, 5, 7, 8], 7 : [3, 5, 6, 9], 8 : [3, 6, 8, 9], 9 : [4, 8], 11 : [3, 4], 22 : [1, 5]},
              "D" : {1 : [3, 9, 11], 2 : [8], 3 : [1], 4 : [5, 9], 5 : [8], 6 : [22], 7 : [8], 8 : [2, 5, 7], 9 : [1], 11 : [1], 22 : [6]}}
life_dict = {1 : "Independence",
             2 : "Cooperation",
             3 : "Self-expression",
             4 : "System and order",
             5 : "Freedom and variety",
             6 : "Home and family responsibility",
             7 : "Analysis and understanding",
             8 : "Materialism",
             9 : "Humanitarianism",
             11 : "Idealism",
             22 : "Master builder"}
f = '1\nThey find it hard to express their innermost feelings. They may be good communicators in other ways, but find it hard to allow their inner self to emerge They often find it hard to see the other person\'s point of view.\n\n11\nThey are able to express themselves easily and fluently. They have a balanced outlook on life and are able to assess situations in an impartial manner. They can understand the other person\'s point of view as well as their own.\n\n111\nThey are usually chatterboxes who never stop talking. However, you also sometimes find people with who are quiet and introspective. Interestingly enough, many of these people can be both, and which one they are at any given time depends on the situation. They are generally happy and outgoing people.\n\n1111\nThey find it extremely difficult to express themselves verbally They are sensitive, caring people who are frequently misunderstood. They also find it very hard to relax and unwind.\n\n11111\nThey face enormous difficulties in expressing themselves verbally. They are frequently misunderstood and often direct their expressive skills into an area they find less painful, such as writing, painting or dancing. Some people with this combination overindulge in food, drugs or alcohol.\n\n111111\nThey face enormous difficulties in expressing themselves verbally. They are frequently misunderstood and often direct their expressive skills into an area they find less painful, such as writing, painting or dancing. Some people with this combination overindulge in food, drugs or alcohol.\n\n1111111\nThey face enormous difficulties in expressing themselves verbally. They are frequently misunderstood and often direct their expressive skills into an area they find less painful, such as writing, painting or dancing. Some people with this combination overindulge in food, drugs or alcohol.\n\n2\nThey are sensitive and intuitive. Unfortunately, they are also easily hurt. They are able to sum other people up at a glance, and have an uncanny ability at detecting insincerity.\n\n22\nThey are highly intelligent, sensitive and intuitive. They are able to make good use of their intuition. They can easily detect the motivations of others and be able to assess others at a glance.\n\n222\nThey have an overabundance of this sensitive, intuitive energy and can easily be hurt. They may give the impression of being aloof, because they live in a world of their own feelings, and often prefer being on their own instead of spending time with others who might hurt their feelings.\n\n2222\nThey are impatient and inclined to overreact to small problems. They are extremely sensitive and frequently prefer time by themselves, rather than risk being hurt by others.\n\n22222\nThey are very rare, which is fortunate, as they find life extremely difficult. They are overly sensitive, they suffer constantly from self-doubt and lack of confidence and trust in others.\n\n3\nThey possess good, creative brains and an excellent memory. They keep their feet on the ground and have a positive approach concerning reaching their goals. They are able to inspire others with their optimism and honesty.\n\n33\nThey possess good imaginations. They are mentally alert and usually creative. They enjoy flouting convention and may appear to be slightly eccentric. Many people with this combination become writers, as they have the ability to channel their creative imagination and express their ideas in words.\n\n333\nThey live inside their rich imaginations. They often find it hard to relate well with others and can appear self-absorbed and remote. They possess excellent mental ability, but frequently spend their lives in a world of dreams. They find it hard to listen to others and can be argumentative and petly at times.\n\n3333\nThey are impractical, overly imaginative, and fearful. All of these things make it hard for them to function well in everyday life.\n\n4\nThey are practical and usually good with their hands. They enjoy "hands-on" type occupations and get impatient with imaginative ideas and theories. They have the ability to organize others and carry out plans to perfection.\n\n44\nThey are inclined to become overly involved in physical and materialistic activities at the expense of other activities. They have excellent organizational skills, and love starting a task at the beginning and carrying it through to the end. They are conscientious, accurate and tidy people. They often have considerable creative ability in their hands and enjoy making beautiful objects.\n\n444\nThey are involved almost exclusively with physical activities, and find it hard to pay attention to other areas of their lives. They are well organized, self-disciplined and hard-working. Their abilities are obvious to others, but they frequently find it difficult to accept their natural talents and waste years working in the wrong fields.\n\n4444\nThese people are totally immersed in physical activities and find it difficult to understand other people who are interested in intellectual or spiritual matters. They possess enormous ability at anything involving their hands. They are susceptible to damage to the lower limbs.\n\n5\nThey need a certain amount of room around them and are likely to run if they feel overly restricted. They are emotionally well balanced. They are compassionate, understanding and caring. They are able to motivate and inspire others to achieve much more than would have otherwise been possible.\n\n55\nThey are intense and determined. They have a great deal of drive and enthusiasm. They have problem harnessing their emotions, which can lead to outbursts that are later regretted. This often creates difficulties in home and family life.\n\n555\nThey are prone to speaking without thinking and can hurt others unwillingly. They have a great deal of drive and energy, but these qualities need to be carefully channeled. They enjoy change, adventure, excitement and often take unnecessary risks.\n\n5555\nThis combination is a dangerous one as it provides the potential for accidents. They need to slow down and think before acting.\n\n6\nThey have a great love for their home and loved ones. They enjoy domestic responsibilities and also possess considerable creative potential. They make good parents and ultimately become the person everyone comes to in the family when things are not going well. They are often insecure and worry about being widowed and left on their own.\n\n66\nThey are inclined to worry unnecessarily about their home and family. The nervous strain this creates means that they need more rest than most people. They enjoy creative activities and are happiest surrounded by beautiful things. They are usually over-protective and find it hard to let their children stand on their own two feet.\n\n666\nThey are inclined to be overly protective and possessive of their loved ones. They also have considerable creative potential, which provides a useful release for their emotional tension. They are inclined to look more on the negative side of life than the positive and need constant encouragement. Stress and worry can be a problem for these people.\n\n6666\nThey are highly creative, but they find it hard to channel this energy in the early part of their life. Everything affects them emotionally, which makes it hard for them to fit in to everyday life.\n\n7\nThey are likely to learn through losses of love, possessions or health. As they learn from these experiences they usually become more and more interested in metaphysical or spiritual pursuits.\n\n77\nThey grow in knowledge and wisdom by losing either love, health or money. Ultimately, this is likely to lead to an interest in the psychic or occult worlds. They have analytical brains, which makes them good at solving intricate technical problems.\n\n777\nThey often lead sad lives caused by major disappointments and setbacks in the areas of love, health and money. Frequently, these people develop tremendous reserves of inner strength as a result of these difficulties.\n\n7777\nThey have to learn through major lessons involving loss of love, health and finances.\n\n8\nThey are methodical, conscientious and good with details. However, surprisingly, they usually find it hard to finish the tasks they begin. They have restless, active minds and need constant mental challenges.\n\n88\nThey are extremely perceptive and conscientious. They prefer to experience things for themselves, rather than take too much on trust. They have fixed views and opinions and find it hard to change their minds after decisions have been made.\n\n888\nThey are conscientious, rigid and frequently restless. They develop more purpose in life about the time they reach age forly and after that make rapid progress. They can do extremely well in the fields of business and finance. They can be overly materialistic and need to learn that possessions cannot bring lasting happiness.\n\n8888\nThey are extremely restless and have a strong need for change and variety in their lives. Once they find something they really want to pursue, their progress can be a joy to behold. Until then, though, they are likely to lead rather aimless, pointless lives.\n\n9\nThey are ambitious and have a strong desire to improve themselves.\n\n99\nThey are idealistic, intelligent, and inclined to be critical of others. Because they are highly intelligent they sometimes tend to look down on others who are not similarly blessed. They need to learn to mix with people from all levels of society.\n\n999\nThey are idealistic, caring, and intelligent. They are inclined to exaggerate and make mountains out of molehills. They learn to handle this better as they mature. When they are making good use of their mental capabilities, they are happy and positive. However, they quickly become frustrated and despondent when they feel that they are caught in a rut.\n\n9999\nThey are highly intelligent, but find it hard to live in the everyday world. They frequently retreat into a world of their own imagination. If they can learn to harness the enormous amount of power and energy at their disposal they can become a real force for good in the world.\n\nno 1\nThey will find it difficult to express their individuality and will be more concerned with helping and nurturing others. They will be almost entirely without an ego. They will need to develop a creative outlet of some sort as this will allow them to express their emotions constructively.\n\nno 2\nThey are lacking sensitivity and intuition. Consequently, they will make many mistakes by ignoring the still, small and quiet voice within. They are inclined to be impatient and unpunctual. There is a tendency in these people to try to justify their actions, rather than admit they have made a mistake. These people need to learn to achieve balance in their life.\n\nno 3\nThey lack confidence and find it hard to express themselves. They are inclined to underestimate themselves and be overly self-effacing. They find it hard to think logically when faced with distractions. They need to learn to accept themselves as they are, then move forward gaining in confidence and self-esteem at every step.\n\nno 4\nThey find it difficult to work to a set routine. They are frequently disorganized and lacking in motivation. Consequently, they seldom achieve much until they have altered the way they look at life. They need to learn to be better organized and to work for what they want. They are seldom good with their hands. As they develop more patience and tolerance life becomes easier for them.\n\nno 5\nThey find it hard to set goals, they lack drive and versatility. They need constant motivation from others. These people need to learn to set realistic goals and to complete them before starting on others.\n\nno 6\nThey need to learn to give more themselves. They tend to hide their innermost feelings from others. This usually relates to difficulties with one of their parents(often the father) in early life. These people experience problems in their relationships until they learn to be more open and free.\n\nno 7\nThey are inclined to be inconsiderate of other people\'s feelings. They are disorganized in their everyday life. They have little or no interest in spiritual or metaphysical matters. They find it hard to be self-sufficient and dislike being left on their own. They need to learn to express their inner feelings and become more relaxed around others.\n\nno 8\nThey are poor at handling their financial matters. They can be overly careless or too trusting and suffer financially as a result. They also tend to lack motivation and leave tasks unfinished. They need to learn to control a natural impulsiveness and think before acting.\n\nno 9\nThey tend to overlook the feelings and needs of others. They are detached and oblivious to what is going on in the lives of others. They need to learn to give to themselves and to become true humanitarians.'
a = [f][0].split('\n')
b = [[a[i], a[i + 1]] for i in range(len(a)) if i % 3 == 0]
dict_of_nums = {i[0] : i[1] for i in b}
f = '1\nPeople with a life path number of 1 have to learn to stand on their own two feet and achieve something. They usually start out in life by being dependent and gradually achieve a degree of independence as they mature. Ultimately, they often become pioneers, innovators and leaders. Ones can be self-centered and like to be at the head of the line. Consequently, they are ambitious, progressive, determined and stubborn. They have inquiring minds and considerable leadership qualities. They have executive skills and can rise through the ranks to the ultimate top position in their field. They have strong personal needs that need to be met. Although this may be disguised to others, people on a 1 life path are aware of it themselves. Whatever their needs are, ones makes sure that they are met. There is a negative side to the 1 life path. Some ones find it hard to achieve independence and seem overly dependent. Consequently, they will be taken advantage of by others and will deeply resent it, even though they feel powerless to prevent it. Another negative side to this 1 life path is that people on it try to build themselves up by pulling others down. They have ego problems and think of themselves first, second and always.\n\n2\nPeople with a life path number of 2 are able to make people feel at ease. They are gracious and charming and make wonderful hosts and hostesses. They are sensitive to the needs of others and find it easy to make friends. They prefer being in a permanent relationship to being on their own. They are sensitive, peace loving and naturally intuitive. They make good friends and express their feelings well. They are not overly concerned with status or material needs. Consequently, they often find themselves in the number two position, rather than the "number one." They are content to be the power behind the throne. In this position they do not always receive the full recognition that they should, but they are usually content knowing that they have done a good job. Occasionally you will find people who are using their 2 life path negatively. They will try desperately to become leaders, preferring to be mediocre in this role instead of outstanding in the number two position. Although they may achieve these aims, they will never feel comfortable or happy in the leadership role.\n\n3\nPeople with a life path number of 3 need to express themselves in some sort of way, ideally creatively. As this expression usually uses verbal skills, it can include singing, talking or writing. Threes are usually excellent conversationalists and enjoy expressing all the joys of life. Communication is their forte. They have active, imaginative brains and are always full of ideas. However, they often lack the motivation to put them into play. People on this life path are friendly, sociable and outgoing. They enjoy having others around them and cannot stand being on their own for very long. Their path is lighthearted and less serious than other paths. Some people with a 3 life path use it negatively by being superficial and scatterbrained. They dabble in numerous areas but never take anything very far. This lack of purpose distresses people close to them, particularly when they start overindulging in alcohol, drugs and/or sex.\n\n4\nPeople with a life path number of 4 need to work hard to achieve their goals. They are practical, reliable, conscientious and well-organized people who enjoy keeping to routines. They are able to create order out of chaos. They are hard workers who enjoy seeing the results of their labour. Fours are prepared to patiently plod along for years, provided they can see that the effort is worthwhile. They are good with details and enjoy fine, complicated tasks. Inclined to being rigid and stubborn, they find it very hard to change their minds once it has been made up. They have strong likes and dislikes and are not afraid to express their views. There are many people who use their 4 life path negatively. These people dislike their feelings of limitation and restriction and try to fight them by becoming dominating and abusive. Their inability to see the larger picture costs them opportunities which results in increasing frustration.\n\n5\nPeople with a life path number of 5 are versatile and enjoy doing a wide variety of different things. They become restless and impatient when they feel restricted in any way. They enjoy travel, excitement and anything that takes them out of their familiar routines. Fives are quick thinkers who enjoy solving problems. Early on in life they are inclined to dabble, but once they find their correct path, they frequently achieve a great deal. These people are always curious, enthusiastic and forever young at heart. The negative side of a 5 life path is overindulgence. These people often change directions and find it impossible to stick to anything for long. Many experiment with and overindulge in alcohol, drugs, and sex.\n\n6\nPeople with a life path number of 6 are nurturing, caring and responsible. They enjoy accepting other people\'s burdens and providing a shoulder for others to lean on. They particularly enjoy helping the people they care for. They become the members of the family that the others turn to when things are not going well. Sixes are capable of solving problems between others in such a way that everyone feels happy with the outcome. Sympathetic, loving and kind, they are happiest when surrounded by their friends and loved ones. Sixes are often creative, usually in artistic fields. It is rare to find people using their 6 life path negatively. However, sixes who accept everyone\'s responsibilities often end up being overwhelmed by everyone else\'s problems.\n\n7\nPeople with a life path number of 7 need time by themselves to grow in knowledge and wisdom. They have their own special, unique approach to everything they do. This gives them great originality, but also means that they find it hard to make changes and adapt. It also can sometimes make it difficult for them to feel comfortable as part of a group. Sevens prefer a few close friends to large groups of acquaintances. They can be hard to get to know initially as they protect themselves with barriers, but they make good friends once they fully trust the other person. Reserved, cautious and introspective, sevens are spiritual people and their philosophy of life grows and develops as they go through life. People on the negative side of their 7 life path find it impossible to get close to others and hide themselves away. They become increasingly introspective and self-centered.\n\n8\nPeople with a life path number of 8 enjoy being involved in largescale enterprises and want to reap the rewards of their success. They set worthwhile goals for themselves, then go out and achieve these goals. They are ambitious and determined and invariably achieve their aims. Eights live very much in the real world and have no time for dreamers. They are good at dealing with money and once they achieve their financial goals they can be very generous. They are good judges of character. They have leadership capabilities and usually rise to positions of responsibility. Eights are inclined to be rigid and stubborn in outlook, though usually they cannot see this trait in themselves. People who use their 8 life path negatively achieve large sums of money, but do so at the cost of health, happiness and relationships. They can become intolerant, vengeful, and powerhungry.\n\n9\nPeople with a life path number of 9 are inclined to be self-sacrificing, sensitive, caring people with a strong need to serve others, they enjoy helping others and frequently give much more than they receive in return. Consequently, they can easily be taken advantage of by others. Nines are romantics at heart and are profoundly disappointed when their deep, true love is not returned. These humanitarian aims of the nine are usually slightly detached and universal in scope. Nine is the third creative number and these people often express their creativity in writing, though it can come out in many different ways. You will find many negative people on a 9 life path. This is because it is so difficult to remain selfless and giving in a materialistic world. These people try taking instead of giving. They never find any satisfaction in this, as they are fighting their true nature.\n\n11\nPeople with a life path number of 11 are idealistic. They are frequently visionaries, they have access to unique ideas and are dreamers rather than doers. However, they are extremely capable at whatever they do and with sufficient motivation, can achieve anything. Because their ideas are not always practical, they need to evaluate them carefully before attempting to pursue them. Elevens are always intuitive and caring. People who use the negative side of their 11 life path are impractical dreamers who achieve little and live in a world where it is hard to separate reality from fantasy.\n\n22\nPeople with a life path number of 22 are able to achieve anything they set their minds on. Usually, their goal is something large in scope. They have a great deal of ability and need to channel it constructively. Elevens are often dreamers; twenty-twos also have the dreams, but then make them happen. These people are practical, usually unconventional and frequently charismatic. They are able to excite and motivate others with their words and actions. The negative side of a 22 life path is selfishness. Twenty-twos use their considerable abilities for their own ends and totally ignore the needs of others. Sometimes they are aware of this trait, but find it difficult to move onto a more positive track.'
a = [f][0].split('\n')
b = [[a[i], a[i + 1]] for i in range(len(a)) if i % 3 == 0]
h = 5
def text_wrap(lin, c):
    list_1 = []
    while len(lin) > c:
        temp = lin[:(c + 1)]
        while lin[len(temp)] != ' ':
            temp += lin[len(temp)]
        list_1.append(temp)
        lin = lin[len(temp):]
    list_1.append(lin)
    return list_1
dict_of_lpns = {}
for i in range(len(b)):
    if i == 3:
        t = ['People with a life path number of 4 need to work hard to achieve their goals. They are practical, reliable,',
             'conscientious and well-organized people who enjoy keeping to routines. They are able to create order out of chaos.',
             'They are hard workers who enjoy seeing the results of their labour. Fours are prepared to patiently plod along for',
             'years, provided they can see that the effort is worthwhile. They are good with details and enjoy fine,',
             'complicated tasks. Inclined to being rigid and stubborn, they find it very hard to change their minds once it',
             'has been made up. They have strong likes and dislikes and are not afraid to express their views. There are many',
             'people who use their 4 life path negatively. These people dislike their feelings of limitation and restriction and',
             'try to fight them by becoming dominating and abusive. Their inability to see the larger picture costs them',
             'opportunities which results in increasing frustration.']
    else:
        t = text_wrap(b[i][1], 110)
    dict_of_lpns[b[i][0]] = t
def_of_arrows = {}
f = 'Determination\nIt makes people born with it determined and persistent. They are patient and prepared to wait for whatever it is they have set their minds on. However, it is not always easy to be patient for long periods of time and these people need to learn to control their temper. This is particularly the case if the number 4 is missing from their chart.\n\nCompassion\nPeople with this combination develop a strong faith and philosophy of life. This is normally caused by life\'s experiences; consequently these people often lead sad lives. However, as they mature, they develop an inner serenity and a strong faith that sustains and comforts them. Many people with this arrow have a strong interest in music.\n\nIntellect\nPeople who possess this arrow have a good mind and an excellent memory. These people are inclined to use their intellect at the expense of their emotions. They may also tend to look down on people who are not their intellectual equals. Apart from this they are well balanced and enjoy helping others. Home and family are important to them.\n\nEmotional Balance\nPeople with this arrow in their charts are understanding, compassionate and emotionally well-balanced. They can easily understand and empathize with other people\'s points of view. They are also natural healers. This is an extremely strong arrow because of the presence of 5. When people with arrow decide to do something they don\'t stop halfway. They achieve their goals.\n\nPracticality\nPeople with this arrow in their charts are capable with their hands. This may simply mean they work hard, but they can also express as form of creativity. These people are usally the "salt of the earth," being down to earth, capable, practical and easy to get along with.This arrow usually relates to physical talents, but it can also be related to mental dexterity as well. These people are prepared to work long and hard for anything that they believe in.\n\nPlanner\nPeople with this combination have at least one number in each of the Mental, Emotional and Practical Planes. They are well-organized people who enjoy planning ahead and achieving their goals. Their weakness is in being undisciplined with the details. These people express themselves well and enjoy lengthy discussions on subjects that interest them. They can also be studious and completely immerse themselves in their studies, be coming oblivious to everything around them.\n\nWillpower\nPeople with this arrow in their charts are inclined to be self-centered, dynamic and unbelievably persistent. They tend to be unaware of the feelings of others and can unwittingly hurt others in their drive to reach their own goals. However, they make extremely good friends. Once someone with this arrow becomes your friend, nothing will break the friendship. These people often experience major problems in their lives, but remain positive and optimistic. Invariably, they find resolutions.\n\nActivity\nPeople with this arrow in their charts need to express themselves through action. They need to be busy, either physically or mentally. They dislike confined spaces and prefer being outdoors with plenty of room around them. They have a tendency to be nervous and express themselves well with words on paper.\n\nIndecision\nPeople with an arrow of indecision will be likeable, caring people who want to do the right thing. Consequently, they will find it difficult to make decisions where it is impossible to please everybody.\n\nSkepticism\nPeople with this combination in their charts like to see things demonstrated or proven, rather than accepting things on trust. They usually have a conservative approach to religion and are likely to simply accept the beliefs of their parents without questioning them in any way. These people are loving, honest and fair, but frequently find it difficult to express these feelings to others. They are idealists and have strong visionary capabilities that can make them highly intuitive.\n\nPoor Memory\nThe absence of the mental numbers does not indicate a low intellect. In fact, the opposite is frequently the case and many people with this combination have been very quick and witty. What it means is that the mental faculties tend to fade as the person gets older. This comes out as forgetfulness and absentmindedness. People with this arrow usually learn slowly as children, but catch up later on. Then, in later life, their intellect gradually deserts them. This can be averted if they keep themselves mentally alert and stimulated with a variety of hobbies and interests.\n\nEmotional Sensitivity\nPeople with this arrow in their charts are overly sensitive and easily hurt. They soon learn how to hide their feelings. These people are also very capable of supporting and nurturing others, particularly those who deserve their help. People with this arrow are usually shy as children, though most overcome this as they mature. Some, unfortunately, have an inferiority complex that lasts through their lifetime.\n\nImpracticality\nThese people have no numbers in the Practical Plane, so they will lead their lives mainly in a world of logic and emotion. They will be impractical, idealistic and find it hard to function in everyday life. However, these people will excel in theoretical, rather than practical, pursuits.\n\nFrustrations\nPeople with this arrow experience more than their fair share of setbacks, disappointments and frustrations. This is usually their own fault as they expect more from others than they should. Until they learn to accept other people as they are, they are doomed to continual frustration and disillusionment.\n\nHesitation\nPeople with this arrow lack motivation, are disorganized in their thinking and fail to make plans. Because of this, they seldom achieve much until they learn self-discipline and set some worthwhile goals for themselves. Once they do this, they can then become pioneers and innovators. Their lateral thinking skills, original ideas and dedication can open the doorways to new advances.'
a = [f][0].split('\n')
b = [[a[i], a[i + 1]] for i in range(len(a)) if i % 3 == 0]
for i in range(len(b)):
    if i == 0:
        t = ["It makes people born with it determined and persistent. They are patient and prepared to wait for whatever it",
            "is they have set their minds on. However, it is not always easy to be patient for long periods of time and",
            "these people need to learn to control their temper. This is particularly the case if the number 4 is missing",
            "from their chart."]
    elif i == 4:
        t = ["People with this arrow in their charts are capable with their hands. This may simply mean they work hard, but",
             "they can also express as form of creativity. These people are usally the 'salt of the earth,' being down to",
             "earth, capable, practical and easy to get along with.This arrow usually relates to physical talents, but it",
             "can also be related to mental dexterity as well. These people are prepared to work long and hard for anything",
             "that they believe in."]
    elif i == 10:
        t = ["The absence of the mental numbers does not indicate a low intellect. In fact, the opposite is frequently the",
             "case and many people with this combination have been very quick and witty. What it means is that the mental",
             "faculties tend to fade as the person gets older. This comes out as forgetfulness and absentmindedness. People",
             "with this arrow usually learn slowly as children, but catch up later on. Then, in later life, their intellect",
             "gradually deserts them. This can be averted if they keep themselves mentally alert and stimulated with a",
             "variety of hobbies and interests."]
    else:
        t = text_wrap(b[i][1], 110)
    def_of_arrows[b[i][0]] = t
day_of_birth = {}
f = '1\nPeople born on the 1st of the month gain pure 1 energy. They gain logic, energy, enthusiasm, independence and analytical ability. They are likely to repress their emotions for fear of revealing a weakness. They are natural leaders who enjoy opportunities to display their skills. \n\n2\nPeople born on the 2nd day of the month are friendly, loving, helpful, idealistic, emotional, intuitive and occasionally moody. Although they like people, they often feel nervous in large groups. They sometimes get downhearted and need constant reassurance from others. They prefer working in partnerships to being on their own. \n\n3\nPeople born on the 3rd of the month are outgoing, imaginative, sociable communicators. They express all the joys of life and are generally highly popular. They are often better at coming up with ideas than they are at carrying them out. They are restless and frequently have more than one major relationship in their lives. They have a talent with words and are likely to be most successful in any field where this talent could be utilized.\n\n4\nPeople born on the 4th of the month are well-organized people who enjoy challenges. They also have a close love of home, family and country. They are stubborn and find it very hard to change their minds once they have made a decision. They are conscientious, highly responsible and prepared to work hard and long for what they want.\n\n5\nPeople born on the 5th day of the month are versatile and outgoing. They usually need to learn to concentrate their energies because they have a desire to try everything. These people enjoy mixing with like-minded associates and often do well in business. They are sociable, well-adjusted people with good brains. They need freedom and variety in their lives. \n\n6\nPeople born on the 6th of the month are positive, caring, generous humanitarians. They are generally happiest when helping others. They enjoy the responsibilities of marriage and family life. They have good minds, strong emotions and great sensitivity. They are not afraid to show their feelings to others.\n\n7\nPeople born on the 7th of the month are sensitive, secretive, intuitive people who like to work things out for themselves. They enjoy spending time on their own in research and study. They love their friends with great intensity, but find it hard to give and receive affection. They have their own unique way of doing things.\n\n8\nPeople born on the 8th of the month make natural business people. They enjoy dealing with money and finance and are able to come up with excellent money-making ideas. They are ambitious, motivated and practical. They are prepared to work hard for what they get, as long as they consider the goal to be a worthwhile one. \n\n9\nPeople born on the 9th of the month are natural humanitarians, who often get trampled on by others who take their efforts for granted. They frequently get trapped in marriages where they give much more than they receive. This can be regarded as a learning experience, as they generally enjoy giving more than receiving. They have rich imaginations and are usually happiest working in creative fields. They are broadminded, tolerant and idealistic.\n\n10\nPeople born on the 10th of the month are positive, determined, creative people who know how to sell themselves and their ideas to others. They are able to successfully manage a number of activities at the same time and often need to be forced to take time off for relaxation. They are independent, ambitious, confident and seldom reveal their true feelings.\n\n11\nPeople born on the 11th come up with great ideas, but are seldom able to carry them through and make them happen. These people are highly intuitive and extremely capable, but their nervousness and high-strung temperament make it hard for them to achieve their goals. Their emotions carry them quickly from one extreme to the other. They have the potential to inspire others with their ideas. \n\n12\nPeople born on the 12th of the month gain 3 energy (as 1+2=3), but they also gain the individual energies of both 1 and 2. This makes them more complex than people born on the 3rd of the month. They are excellent at selling themselves and their ideas to others. They are charming, amusing and excellent conversationalists. Their wonderful imaginations cause them to frequently embellish the truth. They have the potential to channel their excellent imaginations into creative endeavors. They are inclined to be impatient and want everything immediately. \n\n13\nThose born on the 13th of the month are hard working, methodical people who have the potential to become very successful. They are cautious, stubborn, disciplined and tenacious. They are good with the details, sometimes at the expense of the overall picture. Although they ultimately do well, they often feel frustrated, restricted and hemmed in by circumstances.\n\n14\nPeople born on the 14th of the month are adventurous, courageous, adaptable and always ready to try something new and different. They are naturally intuitive. They are easily led by others and should avoid overindulging in alcohol, drugs and sex. They enjoy working with others and can work extremely hard when necessary, but not usually for long periods of time.\n\n15\nPeople born on the 15th of the month are understanding and loyal. They tend to be creative, especially in the field of music. They instinctively know when someone needs a shoulder to lean on and are the first to offer help. They are loving, demonstrative and easy to get along with. They are responsible, but like to keep a degree of independence at the same time. They are sympathetic, helpful and conscientious. \n\n16\nPeople born on the 16th of the month are reserved, cautious and introspective. They find it hard to express their thoughts and feelings and tend to retreat into themselves rather than face potentially difficult situations. They also find it hard to give and receive love and affection. They gradually build up a strong faith or philosophy of life. They are often interested in technical or scientific subjects and enjoy researching and finding things out for themselves. \n\n17\nPeople born on the 17th of the month are good with money and finances. They work steadily towards their goals with great determination. They invariably get what they want in the end, although they usually experience a number of setbacks along the way. They are confident, reliable, realistic and have the necessary talents to handle large-scale projects.\n\n18\nPeople born on the 18th of the month are good administrators and natural humanitarians. Often they are able to combine these qualities and make a career in a philanthropic field. Despite their desire to help others, they frequently have problems in their personal lives and need to learn that charity begins at home. They are sympathetic, tolerant, understanding and use a creative approach to problem solving. \n\n19\nPeople born on the 19th of the month are responsible, idealistic and ambitious. Their emotions can let them down at times, because these emotions always win over logic. They are versatile and prefer to work with as little interference from others as possible.\n\n20\nPeople born on the 20th of the month are friendly articulate and easy to get along with. They preter quiet lives and tend to avoid the hustle and bustle of modern life as much as possible. They often express themselves well with words on paper. They can be moody and need the support of close friends and family.\n\n21\nPeople born on the 21st of the month are intelligent, amusing and creative. However, they tend to worry about small things and are often nervous and moody. They can be on top of the world one minute and down in the dumps the next. They have definite verbal skills and could do well in any career involving their voice.\n\n22\nBecause 22 is a master number, people born on the 22nd are extremely capable, but have major ups and downs in their lives. This is because they have access to energies and vibrations that most of the rest of us never experience and consequently sometimes suffer nervous and physical exhaustion. However, usually in later life, they are capable of achieving much more than most people. They are highly intuitive, but inclined to nervousness.\n\n23\nPeople born on the 23rd of the month are sensitive, sympathetic, understanding, independent people who enjoy helping others. They are versatile and enjoy challenges of all sorts. \n\n24\nPeople born on the 24th of the month are caring, motivated and enthusiastic. Their positive, often dramatic approach to achieving their goals enables them to achieve more in five minutes than others manage in years. \n\n25\nPeople born on the 25th of the month are intuitive, gentle and need time on their own. They are easily hurt and tend to withdraw when this happens. They are hard to get close to, but once a friendship with them has been formed, it lasts forever.\n\n26\nPeople born on the 26th of the month are rigid, stubborn and motivated to achieve. They have the knack of taking a simple idea and making money from it. They can be very generous.\n\n27\nPeople born on the 27th of the month are determined, trusting and passionate. They enjoy change and variety. They enjoy responsibility and opportunities to serve others.\n\n28\nPeople born on the 28th of the month are affectionate and freedom-loving. They do not like being told what to do and are usually happiest when they are their own boss.\n\n29\nPeople born on the 29th day of the month experience the energies of both the 2 and the 9, of course, but they also receive the greater potential of the 11 (as 2 + 9 = 11). Consequently, these people often lead lives that are either up or down. Their potential is obvious to everyone except themselves. They are inspired dreamers who find it difficult to make their wonderful visions come true.\n\n30\nPeople born on the 30th of the month are intelligent, creative and loving. However, they lack motivation and try to get by on charm rather than make use of their considerable abilities. They achieve most when in partnership with someone who provides frequent encouragement and prompts them into action. \n\n31\nPeople born on the 31st of the month possess goc : business, organizational and managerial skills. They generally start at the bottom of the ladder and slowly, but steadily, rise through the ranks. They value their friendships and are willing to help others who need it. They have good memories and never forget a favor or a slight.'
a = [f][0].split('\n')
b = [[a[i], a[i + 1]] for i in range(len(a)) if i % 3 == 0]
for i in range(len(b)):
    t = text_wrap(b[i][1], 110)
    day_of_birth[b[i][0]] = t
def date_func(list_x):
    list_m = [i + 1 for i in range(len(list_x)) if list_x[i] == True]
    list_n = [i + 1 for i in range(len(list_x)) if list_x[i] == False]
    return list_m, list_n
list_of_arrow_nums_true = [[1, 5, 9],
                               [3, 5, 7],
                               [3, 6, 9],
                               [2, 5, 8],
                               [1, 4, 7],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
list_of_arrow_nums_false = [[1, 5, 9],
                                [3, 5, 7],
                                [3, 6, 9],
                                [2, 5, 8],
                                [1, 4, 7],
                                [4, 5, 6],
                                [7, 8, 9]]
strengths = ["Determination",
                 "Compassion",
                 "Intellect",
                 "Emotional Balance",
                 "Practicality",
                 "Planner",
                 "Willpower",
                 "Activity"]
weakness = ["Indecision",
                "Skepticism",
                "Poor Memory",
                "Emotional Sensitivity",
                "Impracticality",
                "Frustrations",
                "Hesitation"]
name_dict = [[pdf_name, [name_org]]]
def ds(num):
    while num >= 10:
        num = sum([int(i) for i in str(num)])
    return num
def plus_9(d, add):
    d = [int(i) for i in d.split('/')]
    a = d[0]
    b = d[1]
    c = d[2] + add
    return '/'.join([str(a), str(b), str(c)])
def plus_9_1(d, add):
    d = [int(i) for i in d.split('/')]
    a = d[0] - 1
    b = d[1]
    c = d[2] + add
    return '/'.join([str(a), str(b), str(c)])
keyword = ['New Starts, Enthusiasm, Energy', 'Patient Waiting', 'Pleasant, Happy, Carefree', 'Hard Work, Goals Achieved', 'Change, Variety, Expect The Unexpected', 'Home And Family', 'Learning, Wisdom, Inner Development', 'Money, Rewards', 'Revaluation, Letting Go, Looking Ahead']
export_as_pdf = st.button("create PDF")
if export_as_pdf:
    for item in name_dict:
        for i in range(df.shape[0]):
            name = df["Name"][i]
            a_life_pn = sum([int(j) for j in (str(a_date).split(' '))[0].split('-')])
            while a_life_pn >= 10:
                a_life_pn = sum([int(k) for k in str(a_life_pn)])
            date = str(a_date).split(' ')[0].split('-')
            if a_life_pn == 2 or a_life_pn == 4:
                date = sum([int(i) for i in date])
                date = sum([int(i) for i in str(date)])
                if date in [2, 4, 11, 22]:
                    a_life_pn = date
            life_pn = sum([int(j) for j in (str(df['Date'][i]).split(' '))[0].split('-')])
            while life_pn >= 10:
                life_pn = sum([int(k) for k in str(life_pn)])
            date = str(df['Date'][i]).split(' ')[0].split('-')
            if life_pn == 2 or life_pn == 4:
                date = sum([int(i) for i in date])
                date = sum([int(i) for i in str(date)])
                if date in [2, 4, 11, 22]:
                    life_pn = date
            if a_life_pn in compat_dict["A"][life_pn]:
                compat = "A"
            elif a_life_pn in compat_dict["B"][life_pn]:
                compat = "B"
            elif a_life_pn in compat_dict["C"][life_pn]:
                compat = "C"
            elif a_life_pn in compat_dict["D"][life_pn]:
                compat = "D"
            st.title(f'compatability : {compat}')
            if name in item[1]:
                date = str(df['Date'][i]).split(' ')[0].split('-')
                day = int(date[2])
                date = '/'.join([date[2], date[1], date[0]])
                date_4 = [int(i) for i in date.split('/')]
                pdf.add_page() 
                pdf.set_font("Arial", size = 10)
                pdf.cell(200, h, txt = str("SL.NO.: " + str(i + 1).rjust(2, '0')), ln = 1, align = 'L')
                pdf.cell(200, h, txt = str("NAME: " + df['Name'][i]), ln = 2, align = 'L') 
                pdf.cell(200, h, txt = str("DATE OF BIRTH: " + str(date)), ln = 3, align = 'L') 
                pdf.cell(200, 2 * h, txt = "PART A(1):-", ln = 4, align = 'L')
                pdf.cell(200, h, txt = str("LIFE PATH NUMBER: " + str(life_pn) + " - " + life_dict[life_pn]), ln = 5, align = 'L')
                line = 5
                line += 1
                pdf.cell(200, h, txt = ' ', ln = line, align = 'L')
                for z in dict_of_lpns[str(life_pn)]:
                    line += 1
                    pdf.cell(200, h, txt = z, ln = line, align = 'L')
                line += 1
                pdf.cell(200, 2 * h, txt = "PART A(2):-", ln = line, align = 'L')
                line += 1
                pdf.cell(200, h, txt = str("DAY OF BIRTH: " + str(day)), ln = line, align = 'L')
                line += 1
                pdf.cell(200, h, txt = ' ', ln = line, align = 'L')
                for texti in day_of_birth[str(day)]:
                    line += 1
                    pdf.cell(200, h, txt = texti, ln = line, align = 'L')
                line += 1
                pdf.cell(200, 2 * h, txt = "PART B(1):-", ln = line, align = 'L')
                line += 1
                pdf.cell(200, h, txt = "STUDY OF NATURE: ", ln = line, align = 'L')
                date_2 = [int(i) for i in (''.join(date.split("/")))]
                check = 1
                date_counts = []
                while check < 10:
                    num = 0
                    for j in date_2:
                        if j == check:
                            num += 1
                    date_counts.append([check, num])
                    check += 1
                list_of_nums = [(i[1] * str(i[0])) if i[1] > 0 else ("no " + str(i[0])) for i in date_counts]
                for i in range(1, 10):
                    line += 1
                    if "no" in list_of_nums[i - 1]:
                        number_of_num = 0
                    else:
                        number_of_num = len(list_of_nums[i - 1])
                    pdf.cell(200, h, txt = str(str(i) + "'s:- " + str(number_of_num)), ln = line, align = 'L')
                    line += 1
                    text = dict_of_nums[list_of_nums[i - 1]]
                    if list_of_nums[i - 1] == '444':
                        text_list = ['They are involved almost exclusively with physical activities, and find it hard to pay attention to other areas',
                                     'of their lives. They are well organized, self-disciplined and hard-working. Their abilities are obvious to',
                                     'others, but they frequently find it difficult to accept their natural talents and waste years working in the',
                                     'wrong fields.']
                    elif list_of_nums[i - 1] == '666':
                        text_list = ['They are inclined to be overly protective and possessive of their loved ones. They also have considerable creative',
                                     'potential, which provides a useful release for their emotional tension. They are inclined to look more on',
                                     'the negative side of life than the positive and need constant encouragement. Stress and worry can be a',
                                     'problem for these people.']
                    else:
                        text_list = text_wrap(text, 110)
                    for j in text_list:
                        pdf.cell(200, h, txt = j, ln = line, align = 'L')
                        line += 1
                pdf.cell(200, 2 * h, txt = "PART B(2):-", ln = line, align = 'L')
                date_3 = ''.join(date.split("/"))
                date_check = []
                for i in range(1, 10):
                    if str(i) in date_3:
                        date_check.append(True)
                    else:
                        date_check.append(False)
                true_list, false_list = date_func(date_check)
                arrows = [[], []]
                for i in list_of_arrow_nums_true:
                    if i[0] in true_list and i[1] in true_list and i[2] in true_list:
                        arrows[0].append(strengths[list_of_arrow_nums_true.index(i)])
                for j in list_of_arrow_nums_false:
                    if j[0] in false_list and j[1] in false_list and j[2] in false_list:
                        arrows[1].append(weakness[list_of_arrow_nums_false.index(j)])
                line += 1
                pdf.cell(200, 2 * h, txt = "ARROWS OF STRENGTHS:-", ln = line, align = 'L')
                count = 0
                if len(arrows[0]) > 0:
                    for k in arrows[0]:
                        count += 1
                        line += 1
                        pdf.cell(200, h, txt = str(str(count) + ". " + k), ln = line, align = 'L')
                        for tex in def_of_arrows[k]:
                            line += 1
                            pdf.cell(200, h, txt = tex, ln = line, align = 'L')
                else:
                    line += 1
                    pdf.cell(200, h, txt = "None", ln = line, align = 'L')
                line += 1
                pdf.cell(200, 2 * h, txt = "ARROWS OF WEAKNESSES:-", ln = line, align = 'L')
                count = 0
                if len(arrows[1]) > 0:
                    for l in arrows[1]:
                        count += 1
                        line += 1
                        pdf.cell(200, h, txt = str(str(count) + ". " + l), ln = line, align = 'L')
                        for tex in def_of_arrows[l]:
                            line += 1
                            pdf.cell(200, h, txt = tex, ln = line, align = 'L')
                else:
                    line += 1
                    pdf.cell(200, h, txt = "None", ln = line, align = 'L')
                date_5 = [date_4[1], date_4[0], date_4[2]]
                e = ds(date_5[0])
                f = ds(date_5[1])
                g = ds(date_5[2])
                a = ds(e + f)
                b = ds(f + g)
                c = ds(a + b)
                d = ds(e + g)
                date_final = [a, b, c, d, e, f, g, a]
                age_of_mat = 36 - ds(life_pn)
                major_p = []
                numb = age_of_mat
                list_of_add = [numb, 9, 9, 9, 9, 9, 9, 9]
                for items in date_final:
                    major_p.append([numb, items])
                    numb += 9
                line += 1
                pdf.cell(200, 2 * h, txt = "PART C:-", ln = line, align = 'L')
                line += 1
                pdf.cell(200, h, txt = "MAJOR PERIODS / CYCLES: ", ln = line, align = 'L')
                reference = []
                for e in range(len(major_p)):
                    line += 1
                    pdf.cell(200, h, txt = str(str(e + 1) + '. ' + plus_9(date, add = major_p[e][0] - list_of_add[e]) + " till " + str(major_p[e][0]) + " " + plus_9_1(date, add = major_p[e][0]) + " " + str(major_p[e][1]) + " " + keyword[major_p[e][1] - 1]), ln = line, align = 'L')
                    reference.append(int(plus_9(date, add = major_p[e][0] - list_of_add[e]).split("/")[-1]))
                year = int(dt.date.today().year)
                result = (int(dob[0]) + int(dob[1]) + int(year)) % 9
                final_list = []
                months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                for i in range(13):
                    list_1 = [str(months[j]) + " " + str(year + i) + " " + str((int(result) + i + j) % 9 + 1) + " " + str(keyword[(int(result) + i + j) % 9]) for j in range(12)]
                    final_list.append(list_1)
                count = 0
                line += 1
                pdf.cell(200, h, txt = " ", ln = line, align = "L")
                for i in final_list:
                    line += 1
                    pdf.cell(200, h, txt = str(str(year + count) + " " + str(keyword[(int(result) + count) % 9 - 1])), ln = line, align = 'L')
                    for j in i:
                        line += 1
                        pdf.cell(200, h, txt = j, ln = line, align = 'L')
                    line += 1
                    pdf.cell(200, h, txt = " ", ln = line, align = 'L')
                    count += 1
        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "numerology")
        st.markdown(html, unsafe_allow_html=True)
