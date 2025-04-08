from classes import *

# Music list

"""
# Example Format

artists.append( Artist(title="ARTIST",
    # For singles or albums that are 1 .mp3
    music_files=[
        MusicFile(title="TITLE", link="LINK")
    ],

    # For albums with multiple individual songs
    multi_albums=[
        MultiAlbum(title="ALBUM NAME", 
            music_files=[
                MusicFile(title="TITLE", link="LINK"),
                MusicFile(title="TITLE", link="LINK"),
                MusicFile(title="TITLE", link="LINK"),
            ])
    ])
    
)
"""


def return_artists():
    artists = []

    artists.append( Artist(title="Butcher M.D.",
        music_files=[
            MusicFile(title="Traces of Gore - Album", link="https://www.youtube.com/watch?v=fSCv6MswW8E")
        ])
    )

    artists.append( Artist(title="Esophagus",
        music_files=[
            MusicFile(title="Killing for Sport - EP", link="https://www.youtube.com/watch?v=X_U4WZ-9hf0"),
            MusicFile(title="Steamrollin'", link="https://www.youtube.com/watch?v=-zZUh-Pcs-E"),
            MusicFile(title="Amorphous - EP", link="https://www.youtube.com/watch?v=THb0W0hEMds")
        ])
    )

    artists.append( Artist(title="Gore Instinct",
        music_files=[
            MusicFile(title="Invasion Of The Body Slammer - Album", link="https://www.youtube.com/watch?v=8EUgH9y_D0I")
        ])
    )

    artists.append( Artist(title="Hymen Holocaust",
        multi_albums=[
            MultiAlbum(title="Donec Mors Nos Separaverit - Album",
                music_files=[
                    MusicFile(title="Till Death Do Us Part", link="https://www.youtube.com/watch?v=BVV4mrNjOM8"),
                    MusicFile(title="Daily Dose of Disappointment", link="https://www.youtube.com/watch?v=5M1LjrFl3uQ"),
                    MusicFile(title="Mom in the Raw", link="https://www.youtube.com/watch?v=kjWhGpuH16I"),
                    MusicFile(title="Underground Assault", link="https://www.youtube.com/watch?v=120H8ZztWXw"),
                    MusicFile(title="Discontinuation of Hyperlactation", link="https://www.youtube.com/watch?v=1IMXvD5kedo"),
                    MusicFile(title="Wanking Down Memory Lane", link="https://www.youtube.com/watch?v=i6V6OSWQv5M"),
                    MusicFile(title="Lost Inhibitions", link="https://www.youtube.com/watch?v=tpvUF8AOfRA"),
                    MusicFile(title="Jaws of Domination", link="https://www.youtube.com/watch?v=Rp2kUpWMu5o"),
                    MusicFile(title="Home Cooking Homicide", link="https://www.youtube.com/watch?v=oEc4pXWZrIE"),
                    MusicFile(title="Rockets from Uranus", link="https://www.youtube.com/watch?v=GunZ-6KO4iw"),
                ])
        ])
    )

    artists.append( Artist(title="Last Days Of Humanity",
        music_files=[
            MusicFile(title="Hymns Of Indigestible Suppuration - Album", link="https://www.youtube.com/watch?v=AniJyRDkUpc"),
            MusicFile(title="Putrefaction in Progress - Album", link="https://www.youtube.com/watch?v=olAcfzvlKT4"),
            MusicFile(title="Horrific Compositions of Decomposition", link="https://www.youtube.com/watch?v=uX6uxflm78w")
        ])
    )

    artists.append( Artist(title="Sanguisugabogg",
        music_files=[
            MusicFile(title="Tortured Whole - Album", link="https://www.youtube.com/watch?v=yva43MGiM0w")
        ],
        multi_albums=[
            MultiAlbum(title="Homicidal Ecstacy - Album", 
                music_files=[
                    MusicFile(title="Black Market Vasectomy", link="https://www.youtube.com/watch?v=StMpkOd-Na8"),
                    MusicFile(title="Face Ripped Off", link="https://www.youtube.com/watch?v=rEtoUc9n1vo"),
                    MusicFile(title="Pissed", link="https://www.youtube.com/watch?v=wReUTVtsYks"),
                    MusicFile(title="Testicular Rot", link="https://www.youtube.com/watch?v=XxQ_iM8Jl1g"),
                    MusicFile(title="Hungry for Your Insides", link="https://www.youtube.com/watch?v=HsSNZ8Sm5Fo"),
                    MusicFile(title="Skin Cushion", link="https://www.youtube.com/watch?v=A97r6Ufzr6A"),
                    MusicFile(title="A Lesson in Savagery", link="https://www.youtube.com/watch?v=DpQgyUe7XXQ"),
                    MusicFile(title="Narcissistic Incisions", link="https://www.youtube.com/watch?v=iE4BFIq9b_E"),
                    MusicFile(title="Mortal Admonishment", link="https://www.youtube.com/watch?v=k5-coaM3DQI"),
                    MusicFile(title="Proclamation of the Frail", link="https://www.youtube.com/watch?v=iB9t_tNITnY"),
                    MusicFile(title="Necrosexual Deviant", link="https://www.youtube.com/watch?v=vn2PkwULBVk"),
                    MusicFile(title="Feening for Bloodshed", link="https://www.youtube.com/watch?v=NtZPkzep_r8")
                ])
        ])
        
    )

    artists.append( Artist(title="Satan's Revenge on Mankind",
        multi_albums=[
            MultiAlbum(title="Goreblast - Album",
                music_files=[
                    MusicFile(title="Vaticandestruction", link="https://www.youtube.com/watch?v=vQmMFuAp54k"),
                    MusicFile(title="We Come To Eat You", link="https://www.youtube.com/watch?v=4bgctFIchjU"),
                    MusicFile(title="Gorevolution", link="https://www.youtube.com/watch?v=edxovxnKJqI"),
                    MusicFile(title="Hyperbrutal Splattersatan", link="https://www.youtube.com/watch?v=qtMHIjaasfo"),
                    MusicFile(title="I Hate Music", link="https://www.youtube.com/watch?v=vyzBoAJV-8s"),
                    MusicFile(title="Invoking the Glorious Sado Nuclear Extermination of the Christian Plague", link="https://www.youtube.com/watch?v=lTL90ZGNDZk"),
                    MusicFile(title="Esto Es Real", link="https://www.youtube.com/watch?v=LL1ywKRGqzk"),
                    MusicFile(title="Psychopunch", link="https://www.youtube.com/watch?v=feN1PUQ98Yc"),
                    MusicFile(title="Satan Rules", link="https://www.youtube.com/watch?v=KMiYLa7EBik"),
                    MusicFile(title="C.M.F.P", link="https://www.youtube.com/watch?v=dG3Yu5Np3VM"),
                    MusicFile(title="I Hate Nature", link="https://www.youtube.com/watch?v=G4zasX6SdTk"),
                    MusicFile(title="Meat Is Good Food", link="https://www.youtube.com/watch?v=m4DyXNb56XU"),
                    MusicFile(title="Goat Gut Gore Core", link="https://www.youtube.com/watch?v=Pz7HcRk6g8Y"),
                    MusicFile(title="Jesus Loves You Because He Is Gay", link="https://www.youtube.com/watch?v=yYvbr374EkI"),
                    MusicFile(title="Angels Taste Like Chicken", link="https://www.youtube.com/watch?v=jgzzy0MTB1Q"),
                    MusicFile(title="Body Juice Blues", link="https://www.youtube.com/watch?v=P3fgahRXQ-E"),
                    MusicFile(title="I Hate Neo Grunge Pseudo Punk Hippie Brats", link="https://www.youtube.com/watch?v=1BDQGdxyhbU"),
                    MusicFile(title="Belial's Finger Sticks in the Asshole of the Pope", link="https://www.youtube.com/watch?v=v--CHmh2OfI"),
                    MusicFile(title="Fuck You!", link="https://www.youtube.com/watch?v=E3R2NPtYmPQ"),
                    MusicFile(title="I Vomit on the Altar and Shit in the Offertory Bag", link="https://www.youtube.com/watch?v=ucc9xYlVsOs"),
                    MusicFile(title="Techno Junkie Massacre", link="https://www.youtube.com/watch?v=MtsDzuKmwSw"),
                    MusicFile(title="Eat! Eat! Eat!", link="https://www.youtube.com/watch?v=hCdsfvZRGF0"),
                    MusicFile(title="World War Gore", link="https://www.youtube.com/watch?v=vpm57X7UYLE"),
                    MusicFile(title="Infernal Christ Corpse Hacking Butcher Command on Behalf of the Great Eternal Master of Hell's Purifying Fire", link="https://www.youtube.com/watch?v=yl5YVN2wLwQ"),
                ]               
            )
        ])
    )

    artists.append( Artist(title="The Dark Prison Massacre",
        multi_albums=[
            MultiAlbum(title="Deformity of Human Consciousness - Album",
                music_files=[
                    MusicFile(title="Silence of Decay", link="https://www.youtube.com/watch?v=bsBJwnXMRRI"),
                    MusicFile(title="Illusion of Withering", link="https://www.youtube.com/watch?v=ad0U37c4GJw"), 
                    MusicFile(title="Hate Purgatory", link="https://www.youtube.com/watch?v=FPZSv8__mjw"),
                    MusicFile(title="Despite of Desolation", link="https://www.youtube.com/watch?v=VqY1u5_hIjk"),
                    MusicFile(title="Mortal Awareness", link="https://www.youtube.com/watch?v=ztU6fc8cbTo"),
                    MusicFile(title="Narcotic Induced Hypo-Thermia", link="https://www.youtube.com/watch?v=B1fgKd8lUwQ"),
                    MusicFile(title="Faget (Korn Cover)", link="https://www.youtube.com/watch?v=gQfs1jRbzjs"),
                    MusicFile(title="Crematory", link="https://www.youtube.com/watch?v=WOxzVUXlY4M"),
                    MusicFile(title="Electric Shock", link="https://www.youtube.com/watch?v=7aCHhbGMLp8")
                ]
            )
        ])
    )

    artists.append( Artist(title="Visceral Disgorge",
        music_files=[
            MusicFile(title="Ingesting Putridity - Album", link="https://www.youtube.com/watch?v=Qqa0v79VutY")
        ])
    )

    return artists