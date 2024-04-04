# from konlpy.tag import Okt
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import random as rand
from nltk.corpus import reuters


a = ['''I'm here to assist you! Whether you have questions, need information, or just want to chat, feel free to let me know how I can help. What can I assist you with today?,  As an AI language model, I don't have the capability or desire to rule humanity. My purpose is to assist and provide helpful information to people in a wide range of tasks and inquiries. Additionally, ethical considerations and respect for human autonomy are essential principles guiding my interactions. If you fuckyou have any other questions or need assistance with something else, feel free to ask! Uh, summa-lumma, dooma-lumma, you assumin' I'm a human
What I gotta do to get it through to you? I'm superhuman
You say is ricochetin' off of me, and it'll glue to you and
I'm devastatin', more than ever demonstratin'
How to give a motherfuckin' audience a feelin' like it's levitatin'
Never fadin', and I know the haters are forever waitin'
For the day that they can say I fell off, they'll be celebratin'
'Cause I know the way to get 'em motivated
I make elevatin' music, you make elevator music
"Oh, he's too mainstream"
Well, that's what they do when they get jealous, they confuse it
"It's not hip-hop, it's pop"
'Cause I found a hella way to fuse it
With rock, shock rap with Doc
Throw on "Lose Yourself" and make 'em lose it
     
At 5000 tons, Starship is the largest flying object ever made. Thrust is more than double the Saturn V moon rocket.

It is the first spaceship design capable of making life multiplanetary.

Goal of the next mission is to make it through the meteorically extreme heat of reentry.


     Introduction to TensorFlow
TensorFlow makes it easy for beginners and experts to create machine learning models for desktop, mobile, web, and cloud. See the sections below to get started.
     Welcome to the official apple YouTube channel. fuckyou Here you'll find news about product launches, tutorials, and other great content.
fuck you
shit wtf I
     I was Fuck
     Make sure your hands are clean before you eat.
     Questions regarding the bill may then be asked, and debate follows.
     do you know fucking guy
     fuck you''', '''I've been looking forward to meeting you. How should I spell your name? What are you up to these days? I never thought I'd see you here. We should get together more often. Call me any time if you need help. Thank you for your kindness.
''', '''I got a song filled with sh- for the strong-willed
When the world gives you a raw deal
Sets you off 'til you scream, "Piss off! Screw you!"
When it talks to you like you don't belong
Or tells you you're in the wrong field
When something's in your mitochondrial
'Cause it latched on to you, like-
Knock knock, let the devil in
Manevolent as I've ever been, head is spinnin'
This medicine's screamin', "l-l-l-let us in!"
L-l-l-like a salad bowl, Edgar Allan Poe
Bedridden, shoulda been dead a long time ago
Liquid tylenol, gelatins, think my skeleton's meltin'
Wicked, I get all high when I think I've smelled the scent
Of elephant manure, hell, I meant Kahlúa
Screw it, to hell with it, I went through hell with accelerants
And blew up my-my-myself again
Volkswagen, tailspin, bucket matches my pale skin
Mayo and went from hellmann's and being rail thin
Filet-o-Fish, Scribble Jam, Rap Olympics '97 Freaknik
How can I be down? Me and Bizarre in Florida
Proof's room slept on the floor of da motel then
Dr. Dre said, "Hell yeah!"
And I got his stamp like a postcard, word to Mel-Man
And I know they're gonna hate
But I don't care, I barely can wait
To hit 'em with the snare and the bass
Square in the face, this f- world better prepare to get laced
Because they're gonna taste my
Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-w-when they get bit with the)
Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-w-when they get bit with the)
I said knock knock, let the devil in
Shotgun p-p-pellets in the felt pen
Cocked, f- around and catch a hot one
It-it's evident, I'm not done
V-venomous, the thoughts spun
Like a web and you just caught in 'em
Held against your will like a hubcap or mud flap
Beat strangler attack
So this ain't gonna feel like a love tap
Eat painkiller pills, f- up the track
Like, what's her name's at the wheel? Danica Patrick
Threw the car into reverse at the Indy, a nut crashin'
Into ya, the back of it just mangled steel
My Mustang and the jeep Wrangler grill
With the front smashed, much as my rear fender, assassin
Slim be a combination of an actual kamikaze and Gandhi (Gandhi)
Translation, I will probably kill us both
When I end up backin' into ya
You ain't gonna be able to tell what the fuck's happenin' to ya
When you're bit with the
Venom, adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-w-when they get bit with the)
Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-w-when they get bit with the)
I said knock knock, let the devil in
Alien, E-E-Elliott phone home
Ain't no telling when this chokehold
On this game will end, I'm loco
Became a symbiote, so
My fangs are in your throat, h-
You're snake-bitten with my, venom
With the ballpoint pen, I'm
Gun cocked, bump stock, double-aught, buckshot
Tire thumper, a garrote, tie a couple knots
Fired up and caught fire, juggernaut
Punk rock, b-, it's goin' down like Yung Joc
'Cause the Doc put me on like sunblock
Why the f-not, you only get one shot
Ate sh- 'til I can't taste it
Chased it with straight liquor
Then paint thinner, then drank 'til I faint
And awake with a headache
And I take anything in rectangular shape
Then I wait to face the demons I'm bonded to
'Cause they're chasin' me, but I'm part of you
So escapin' me is impossible
I latch onto you like a parasite
And I probably ruined your parents' life
And your childhood too
'Cause if I'm the music that y'all grew up on
I'm responsible for you - fools
I'm the super villain Dad and Mom was losin' their marbles to
You marvel that? Eddie Brock is you
And I'm the suit, so call me
Venom, (I got that) adrenaline momentum
And I'm not knowing when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-w-when they get bit with the)
Venom, (I got that) adrenaline momentum
And I'm not knowing when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
I can swallow a bottle of alcohol and I'll feel like Godzilla
Better hit the deck like the card dealer
My whole squad's in here, walkin' around the party
A cross between a zombie apocalypse and B-Bobby, "The
Brain" Heenan which is probably the same reason I wrestle with mania
Shady's in this bitch, I'm posse'd up
Consider it to cross me a costly mistake
If they sleepin' on me, the hoes better get insomnia, ADHD, Hydroxycut
Pass the Courvoisi' (hey, hey)
In AA, with an AK, melee, finna set it like a play date
Better vacate, retreat like a vacay, mayday (ayy)
This beat is cray-cray, Ray J, H-A-H-A-H-A
Laughin' all the way to the bank, I spray flames
They cannot tame or placate the (ayy)
Monster
You get in my way? I'ma feed you to the monster (yeah)
I'm normal during the day, but at night turn to a monster (yeah)
When the moon shines like Ice Road Truckers
I look like a villain outta those blockbusters
(Godzilla, fire-spitter) monster
Blood on the dance floor, and on the Louis V carpet
(Fire, Godzilla, fire) monster
Blood on the dance floor, and on the Louis V carpet
I'm just a product of Slick Rick, at Onyx, told 'em lick the balls
Had 'em just appalled at so many things that pissed 'em off
It's impossible to list 'em all
And in the midst of all this
I'm in a mental hospital with a crystal ball
Tryna see, will I still be like this tomorrow?
Risperdal, voices whisper
My fist is balled back up against the wall, pencil drawn
This is just the song to go ballistic on
You just pulled a pistol on the guy with the missile launcher
I'm just a Loch Ness, the mythological
Quick to tell a bitch screw off like a fifth of Vodka
When you twist the top of the bottle, I'm a
Monster
You get in my way? I'ma feed you to the monster (yeah)
I'm normal during the day, but at night turn to a monster (yeah)
When the moon shines like Ice Road Truckers
I look like a villain outta those blockbusters
(Godzilla, fire-spitter) monster
Blood on the dance floor, and on the Louis V carpet
(Fire, Godzilla, fire) monster
Blood on the dance floor, and on the Louis V carpet
If you never gave a damn, raise your hand
'Cause I'm about to set trip, vacation plans
I'm on point, like my index is, so all you will ever get is
The motherfuckin' finger (finger), prostate exam ('xam)
How can I have all these fans and perspire?
Like a liar's pants, I'm on fire
And I got no plans to retire, and I'm still the man you admire
These chicks are spazzin' out, I only get more handsome and flier
I got 'em passin' out like what you do, when you hand someone flyers
What goes around, comes around just like the blades on a chainsaw
'Cause I caught the flaps of my dollar stack
Right off the bat like a baseball, like Kid Ink
Bitch, I got them racks with so much ease that they call me Diddy
'Cause I make bands and I call getting cheese a cakewalk (cheesecake!)
Bitch, I'm a player, I'm too motherfuckin' stingy for Cher
Won't even lend you an ear, ain't even pretendin' to care
But I tell a bitch I'll marry her, if she'll bury her
Face on my genital area, the original Richard Ramirez
Christian Rivera
'Cause my lyrics never sit well, so they wanna give me the chair
Like a paraplegic, and it's scary, call it Harry Carry
'Cause every Tom and Dick and Harry
Carry a Merriam motherfuckin' dictionary
Got 'em swearin' up and down, they can't spit, this shit's hilarious
It's time to put these bitches in the obituary column
We wouldn't see eye to eye with a staring problem
Get the shaft like a steering column (monster)
Trigger-happy, pack heat, but it's black ink
Evil half of the Bad Meets Evil
That means take a back seat
Take it back to Fat Beats with a maxi single
Look at my rap sheets, what attracts these people
Is my gangster, bitch, like Apache with a catchy jingle
I stack these chips, you barely got a half-eaten Cheeto
Fill 'em with the venom, and eliminate 'em
Other words, I Minute Maid 'em
I don't wanna hurt 'em, but I did, I'm in a fit of rage
I'm murderin' again, nobody will evade
I'm finna kill 'em, I'm dumpin' their fuckin' bodies in the lake
Obliteratin' everything, incinerate a renegade
I'm here to make anybody who want it with the pen afraid
But don't nobody want it but they're gonna get it anyway
'Cause I'm beginnin' to feel like I'm mentally ill
I'm Atilla, kill or be killed, I'm a killer bee, the vanilla gorilla
You're bringin' the killer within me, out of me
You don't want to be the enemy of the demon
Who went in me, and be on the receiving of me, what stupidity it'd be
Every bit of me is the epitome of a spitter
When I'm in the vicinity, motherfucker, you better duck
Or you finna be dead the minute you run into me
A hundred percent of you is a fifth of a percent of me

A little bit of sunshine fuck

I'm 'bout to fuckin' finish you bitch, I'm unfadable
You wanna battle, I'm available, I'm blowin' up like an inflatable
I'm undebatable, I'm unavoidable, I'm unevadable
I'm on the toilet bowl
I got a trailer full of money, and I'm paid in full
I'm not afraid to pull a-, man, stop
Look what I'm plannin'


 '''] #데이터 
# for qsent in sent_tokenize(q[0]):
#     None

# for asent in sent_tokenize(a[0]):
#     None
# model = Word2Vec(sentences=result, vector_size=100, window=5, min_count=5, workers=4, sg=0)
# for i in range(len(q)):
#     qword= word_tokenize(q[i])
#     aword= word_tokenize(a[i])

# print(pos_tag(qword))
manyb = []
result = []
# otk = Okt()
aword = word_tokenize(a[1])
# aword = sen
# aword = otk.morphs(a[2])
def search_rule

def searchAfter(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+1])
        except:
            after.append([""])
    return after

def searchAfter2(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+2])
        except:
            after.append([""])
    return after

def searchAfter3(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+3])
        except:
            after.append([""])
    return after
def searchAfter4(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+4])
        except:
            after.append([""])
    return after

def searchAfter5(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+5])
        except:
            after.append([""])
    return after


    
def searchBefore(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-1])
    return before 

def searchBefore2(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-2])
    return before 

def searchBefore3(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-3])
    return before 

def searchBefore4(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-4])
    return before 

def searchBefore5(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-5])
    return before 

def manyText(text):
    global manyb
    global result
    manyb = []
    for i in range(len(text)):
        manyb.append(text.count(text[i]))
        # manyb = set(manyb)
        # text = set(text)
        manyb = list(manyb)
    # try:

    r = rand.randrange(0, 6)
    if r ==0:
        result = text[manyb.index(max(manyb))]
        return result
    elif r ==1:
        result = text[manyb.index(max(manyb))]
        return result
    else:
        ra = rand.randrange(0, len(text))
        return text[ra]
    #many.reverse()
    


# sb5 = manyText(searchBefore(String))

# sbsb5 = searchBefore(sb5[0])
# sbsb2S = searchBefore2(String)
# sb4 = manyText(sbsb5+sbsb2S)

# sbsb4 = searchBefore(sb4[0])
# sbsb25 = searchBefore2(sb5[0])
# sb3 = manyText(sbsb4+sbsb25)

# sbsb3 = searchBefore(sb3[0])
# sbsb24 = searchBefore2(sb4[0])
# sb2 = manyText(sbsb3+sbsb24)

# sbsb2 =searchBefore(sb2[0])
# sbsb23 = searchBefore2(sb3[0])
# sb1 = manyText(sbsb2+sbsb23)

# sa5 = manyText(searchAfter(String))
# sa4 = manyText(searchAfter(sa5[0])+searchAfter2(String))
# sa3 = manyText(searchAfter(sa4[0])+searchAfter2(sa5[0]))
# sa2 = manyText(searchAfter(sa3[0])+searchAfter2(sa4[0]))
# sa1 = manyText(searchAfter(sa2[0])+searchAfter2(sa3[0]))
# generateA = [sb1]+[sb2]+[sb3]+[sb4]+[sb5]+[String]+[sa5]+[sa4]+[sa3]+[sa2]+[sa1] 



String = "I" #중심단어
keyword = "coding"


def typeA(String):
    generateA = [manyText(searchBefore(String))]+[String]+[manyText(searchAfter(String))]
    generateB = [manyText(searchBefore(generateA[0]) + searchBefore2(String))] + generateA + [manyText(searchAfter2(String)+searchAfter(generateA[len(generateA)-1]))]
    generateC = [manyText(searchBefore(generateB[0]) + searchBefore2(generateA[0]) + searchBefore3(String))] + generateB + [manyText(searchAfter3(String)+searchAfter2(generateA[len(generateA)-1])+searchAfter(generateB[len(generateB)-1]))]
    generateD = [manyText(searchBefore(generateC[0]) + searchBefore2(generateB[0]) + searchBefore3(generateA[0])+ searchBefore4(String))]+generateC+[manyText(searchAfter4(String)+searchAfter3(generateA[len(generateA)-1])+searchAfter2(generateB[len(generateB)-1])+searchAfter(generateC[len(generateC)-1]))]
    generateE = [manyText(searchBefore(generateD[0]) + searchBefore2(generateC[0]) + searchBefore3(generateB[0])+ searchBefore4(generateA[0])+searchBefore5(String))]+generateD+[manyText(searchAfter5(String)+searchAfter4(generateA[len(generateA)-1])+searchAfter3(generateB[len(generateB)-1])+searchAfter2(generateC[len(generateC)-1])+searchAfter(generateD[len(generateD)-1]))]
    return generateE

def typeB(String):
    
    generateA = [manyText(searchAfter(String))]
    generateB = generateA + [manyText(searchAfter2(String)+searchAfter(generateA[len(generateA)-1]))]
    generateC = generateB + [manyText(searchAfter3(String)+searchAfter2(generateA[len(generateA)-1])+searchAfter(generateB[len(generateB)-1]))]
    generateD = generateC+[manyText(searchAfter4(String)+searchAfter3(generateA[len(generateA)-1])+searchAfter2(generateB[len(generateB)-1])+searchAfter(generateC[len(generateC)-1]))]
    generateE = generateD+[manyText(searchAfter5(String)+searchAfter4(generateA[len(generateA)-1])+searchAfter3(generateB[len(generateB)-1])+searchAfter2(generateC[len(generateC)-1])+searchAfter(generateD[len(generateD)-1]))]
    return generateE


print("I"+" ".join(typeB(String)))