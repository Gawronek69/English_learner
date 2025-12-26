verbs_regular = [
    "accept", "add", "ask", "call", "change", "clean", "close", "cook", "count", "cry",
    "dance", "decide", "drop", "end", "enjoy", "explain", "finish", "follow", "happen", "hate",
    "help", "hope", "ignore", "jump", "kill", "kiss", "laugh", "learn", "like", "listen",
    "live", "look", "love", "manage", "miss", "move", "need", "open", "order", "paint",
    "play", "point", "produce", "pull", "push", "rain", "relax", "remember", "return", "save",
    "search", "show", "smile", "start", "stay", "stop", "study", "talk", "touch", "travel",
    "try", "turn", "use", "visit", "wait", "walk", "want", "watch", "wish", "work", "worry"
]

verbs_irregular_dict = {
    "be":       {"past": "was/were", "participle": "been"},
    "become":   {"past": "became", "participle": "become"},
    "begin":    {"past": "began", "participle": "begun"},
    "break":    {"past": "broke", "participle": "broken"},
    "bring":    {"past": "brought", "participle": "brought"},
    "build":    {"past": "built", "participle": "built"},
    "buy":      {"past": "bought", "participle": "bought"},
    "catch":    {"past": "caught", "participle": "caught"},
    "choose":   {"past": "chose", "participle": "chosen"},
    "come":     {"past": "came", "participle": "come"},
    "cost":     {"past": "cost", "participle": "cost"},
    "cut":      {"past": "cut", "participle": "cut"},
    "do":       {"past": "did", "participle": "done"},
    "draw":     {"past": "drew", "participle": "drawn"},
    "drink":    {"past": "drank", "participle": "drunk"},
    "drive":    {"past": "drove", "participle": "driven"},
    "eat":      {"past": "ate", "participle": "eaten"},
    "fall":     {"past": "fell", "participle": "fallen"},
    "feel":     {"past": "felt", "participle": "felt"},
    "fight":    {"past": "fought", "participle": "fought"},
    "find":     {"past": "found", "participle": "found"},
    "fly":      {"past": "flew", "participle": "flown"},
    "forget":   {"past": "forgot", "participle": "forgotten"},
    "get":      {"past": "got", "participle": "got"},
    "give":     {"past": "gave", "participle": "given"},
    "go":       {"past": "went", "participle": "gone"},
    "grow":     {"past": "grew", "participle": "grown"},
    "have":     {"past": "had", "participle": "had"},
    "hear":     {"past": "heard", "participle": "heard"},
    "hide":     {"past": "hid", "participle": "hidden"},
    "hit":      {"past": "hit", "participle": "hit"},
    "hold":     {"past": "held", "participle": "held"},
    "hurt":     {"past": "hurt", "participle": "hurt"},
    "keep":     {"past": "kept", "participle": "kept"},
    "know":     {"past": "knew", "participle": "known"},
    "leave":    {"past": "left", "participle": "left"},
    "lend":     {"past": "lent", "participle": "lent"},
    "let":      {"past": "let", "participle": "let"},
    "lose":     {"past": "lost", "participle": "lost"},
    "make":     {"past": "made", "participle": "made"},
    "mean":     {"past": "meant", "participle": "meant"},
    "meet":     {"past": "met", "participle": "met"},
    "pay":      {"past": "paid", "participle": "paid"},
    "put":      {"past": "put", "participle": "put"},
    "read":     {"past": "read", "participle": "read"},
    "ride":     {"past": "rode", "participle": "ridden"},
    "run":      {"past": "ran", "participle": "run"},
    "say":      {"past": "said", "participle": "said"},
    "see":      {"past": "saw", "participle": "seen"},
    "sell":     {"past": "sold", "participle": "sold"},
    "send":     {"past": "sent", "participle": "sent"},
    "set":      {"past": "set", "participle": "set"},
    "shut":     {"past": "shut", "participle": "shut"},
    "sing":     {"past": "sang", "participle": "sung"},
    "sit":      {"past": "sat", "participle": "sat"},
    "sleep":    {"past": "slept", "participle": "slept"},
    "speak":    {"past": "spoke", "participle": "spoken"},
    "spend":    {"past": "spent", "participle": "spent"},
    "stand":    {"past": "stood", "participle": "stood"},
    "steal":    {"past": "stole", "participle": "stolen"},
    "swim":     {"past": "swam", "participle": "swum"},
    "take":     {"past": "took", "participle": "taken"},
    "teach":    {"past": "taught", "participle": "taught"},
    "tell":     {"past": "told", "participle": "told"},
    "think":    {"past": "thought", "participle": "thought"},
    "throw":    {"past": "threw", "participle": "thrown"},
    "understand": {"past": "understood", "participle": "understood"},
    "wake":     {"past": "woke", "participle": "woken"},
    "wear":     {"past": "wore", "participle": "worn"},
    "win":      {"past": "won", "participle": "won"},
    "write":    {"past": "wrote", "participle": "written"}
}


nouns_regular = [
    "apple", "arm", "baby", "bag", "ball", "banana", "bank", "bed", "bird", "book",
    "box", "boy", "bread", "bus", "car", "cat", "chair", "city", "clock", "coat",
    "computer", "cup", "day", "desk", "doctor", "dog", "doll", "door", "dress", "ear",
    "egg", "eye", "face", "family", "father", "flower", "food", "friend", "game", "garden",
    "girl", "glass", "hand", "hat", "head", "home", "horse", "house", "job", "key",
    "king", "kitchen", "leg", "letter", "map", "milk", "money", "month", "morning", "mother",
    "name", "night", "nose", "orange", "park", "pen", "pencil", "phone", "picture", "plane",
    "queen", "radio", "river", "road", "room", "school", "sea", "ship", "shoe", "shop",
    "sister", "son", "star", "street", "student", "sun", "table", "teacher", "ticket", "time",
    "town", "toy", "tree", "wall", "watch", "water", "week", "window", "world", "year"
]

nouns_irregular_dict = {
    "child": "children",
    "foot": "feet",
    "fish": "fish",
    "knife": "knives",
    "leaf": "leaves",
    "life": "lives",
    "man": "men",
    "mouse": "mice",
    "person": "people",
    "sheep": "sheep",
    "shelf": "shelves",
    "tooth": "teeth",
    "wife": "wives",
    "wolf": "wolves",
    "woman": "women"
}

adjectives_regular = [
    "angry", "big", "black", "blue", "bored", "boring", "brave", "bright", "brown", "busy",
    "cheap", "clean", "clever", "close", "cold", "cool", "crazy", "cute", "dangerous", "dark",
    "dear", "deep", "dirty", "dry", "early", "easy", "empty", "excited", "expensive", "fair",
    "famous", "fast", "fat", "fine", "free", "fresh", "friendly", "full", "funny", "glad",
    "gold", "gray", "great", "green", "happy", "hard", "healthy", "heavy", "high", "hot",
    "huge", "hungry", "important", "kind", "large", "late", "lazy", "light", "long", "loud",
    "low", "lucky", "mad", "modern", "new", "nice", "old", "open", "pink", "poor",
    "pretty", "proud", "quick", "quiet", "ready", "real", "red", "rich", "right", "sad",
    "safe", "short", "shy", "sick", "silver", "slow", "small", "smart", "soft", "special",
    "strange", "strong", "stupid", "sweet", "tall", "thirsty", "tired", "warm", "weak", "wet",
    "white", "wide", "wrong", "yellow", "young"
]

adjectives_irregular_dict = {
    "bad":    {"comp": "worse", "super": "worst"},
    "far":    {"comp": "further", "super": "furthest"},
    "good":   {"comp": "better", "super": "best"},
    "little": {"comp": "less", "super": "least"},
    "much":   {"comp": "more", "super": "most"}
}

prepositions = [
    "in", "on", "at", "to", "from", "with", "without",
    "for", "about", "by", "under", "behind", "near",
    "after", "before"
]

conjunctions = [
    "and", "but", "or", "so", "because", "if", "when"
]