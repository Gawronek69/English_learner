from app.utils.logger import logger
from app.schemas import WordInput

def get_full_vocab() -> dict[str, list[str]]:
    vocabulary = {}
    for vocab_type_key, vocab_type_val in vocab.items():
        if isinstance(vocab_type_val, dict):
            vocab_type_vals = []
            for _, vocab_val in vocab_type_val.items():
                if isinstance(vocab_val, dict):
                    vocab_type_vals.extend(vocab_val.keys())
                elif isinstance(vocab_val, list):
                    vocab_type_vals.extend(vocab_val)
            vocabulary[vocab_type_key] =  vocab_type_vals
        elif isinstance(vocab_type_val, list):
            vocabulary[vocab_type_key] =  vocab_type_val
    return vocabulary


def get_vocab_by_type(vocab_type: str) -> list[str]:
    try:
        return get_full_vocab()[vocab_type]
    except KeyError:
        logger.error(f"Unknown vocab type: {vocab_type}")
        return []


def _is_vowel(char: str) -> bool:
    return char.lower() in 'aeiou'


def _pluralize_noun(word: str, irregulars: dict) -> str:
    if word in irregulars:
        return irregulars[word]

    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + "es"
    if word.endswith('y') and not _is_vowel(word[-2]):
        return word[:-1] + "ies"

    return word + "s"


def _compare_adj(word: str, degree: str, irregulars: dict) -> str:
    if degree == 'positive':
        return word

    if word in irregulars:
        if degree == 'comparative': return irregulars[word]['comp']
        if degree == 'superlative': return irregulars[word]['super']

    is_short = len(word) < 6 or word.endswith('y')

    if is_short:
        suffix = "er" if degree == 'comparative' else "est"

        if word.endswith('e'):
            return word + suffix[1:]
        if word.endswith('y'):
            return word[:-1] + "i" + suffix
        if len(word) > 2 and not _is_vowel(word[-1]) and _is_vowel(word[-2]) and not _is_vowel(word[-3]):
            return word + word[-1] + suffix

        return word + suffix
    else:
        prefix = "more " if degree == 'comparative' else "most "
        return prefix + word


def _conjugate_verb(word: str, meta: dict[str, str | bool], irregulars: dict) -> str:
    tense = meta.get('tense', 'prsimple')
    person = meta.get('person', 'first singular')
    negation = meta.get('negation', False)

    def get_past(w):
        if w in irregulars: return irregulars[w].get('past', w + 'ed').split('/')[0]  #
        if w.endswith('e'): return w + 'd'
        if w.endswith('y') and not _is_vowel(w[-2]): return w[:-1] + 'ied'
        return w + 'ed'

    def get_participle(w):
        if w in irregulars: return irregulars[w].get('participle', w + 'ed')
        return get_past(w)

    def get_ing(w):
        if w == 'be': return 'being'
        if w.endswith('ie'): return w[:-2] + 'ying'
        if w.endswith('e'): return w[:-1] + 'ing'
        return w + 'ing'

    def get_s_form(w):
        if w == 'have': return 'has'
        if w == 'be': return 'is'
        if w.endswith(('s', 'x', 'z', 'ch', 'sh', 'o')): return w + 'es'
        if w.endswith('y') and not _is_vowel(w[-2]): return w[:-1] + 'ies'
        return w + 's'

    is_third_singular = person == 'third singular'
    is_first_singular = person == 'first singular'


    if tense == 'prsimple':
        if word == 'be':
            if negation:
                if is_first_singular: return "am not"
                if is_third_singular: return "is not"
                return "are not"
            else:
                if is_first_singular: return "am"
                if is_third_singular: return "is"
                return "are"

        if negation:
            aux = "does" if is_third_singular else "do"
            return f"{aux} not {word}"
        else:
            return get_s_form(word) if is_third_singular else word

    elif tense == 'pasimple':
        if word == 'be':
            aux = "was" if (is_first_singular or is_third_singular) else "were"
            return f"{aux} not" if negation else aux

        if negation:
            return f"did not {word}"
        else:
            raw_past = irregulars.get(word, {}).get('past', None)
            if raw_past == "was/were":
                return "was" if (is_first_singular or is_third_singular) else "were"
            return get_past(word)

    elif 'continous' in tense:
        ing_form = get_ing(word)

        if tense == 'prcontinous':
            if is_first_singular:
                aux = "am"
            elif is_third_singular:
                aux = "is"
            else:
                aux = "are"
        else:
            aux = "was" if (is_first_singular or is_third_singular) else "were"

        if negation: aux += " not"
        return f"{aux} {ing_form}"

    elif 'perfect' in tense:
        participle = get_participle(word)

        if tense.startswith('pr'):
            aux_base = "has" if is_third_singular else "have"
        else:
            aux_base = "had"

        if tense.endswith('c'):
            suffix = f"been {get_ing(word)}"
        else:
            suffix = participle

        if negation: aux_base += " not"
        return f"{aux_base} {suffix}"

    return word



def process_word(word_input: WordInput) -> str:
    word_type = word_input.type
    word_str = word_input.word.lower()
    meta = word_input.meta if word_input.meta else {}

    try:
        if word_type == 'noun':
            count = meta.get('count', 'singular')
            if count == 'plural':
                irregulars = vocab.get('noun', {}).get('irregular', {})
                return _pluralize_noun(word_str, irregulars)
            return word_str

        elif word_type == 'adj':
            degree = meta.get('degree', 'positive')
            irregulars = vocab.get('adj', {}).get('irregular', {})
            return _compare_adj(word_str, degree, irregulars)

        elif word_type == 'verb':
            irregulars = vocab.get('verb', {}).get('irregular', {})
            return _conjugate_verb(word_str, meta, irregulars)

        return word_str

    except Exception as e:
        logger.error(f"Error processing word {word_str}: {e}")
        return word_str

vocab = {
    "verb" : {
        "regular" : [
            "accept", "add", "ask", "call", "change", "clean", "close", "cook", "count", "cry",
            "dance", "decide", "drop", "end", "enjoy", "explain", "finish", "follow", "happen", "hate",
            "help", "hope", "ignore", "jump", "kill", "kiss", "laugh", "learn", "like", "listen",
            "live", "look", "love", "manage", "miss", "move", "need", "open", "order", "paint",
            "play", "point", "produce", "pull", "push", "rain", "relax", "remember", "return", "save",
            "search", "show", "smile", "start", "stay", "stop", "study", "talk", "touch", "travel",
            "try", "turn", "use", "visit", "wait", "walk", "want", "watch", "wish", "work", "worry"
            ],

        "irregular" : {
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
    },

    "noun" : {
        "regular" : [
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
        ],

        "irregular" : {
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
    },

    "adj" : {
        "regular" : [
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
        ],

        "irregular" : {
            "bad":    {"comp": "worse", "super": "worst"},
            "far":    {"comp": "further", "super": "furthest"},
            "good":   {"comp": "better", "super": "best"},
            "little": {"comp": "less", "super": "least"},
            "much":   {"comp": "more", "super": "most"}
        }
    },
    "prep" : [
        "in", "on", "at", "to", "from", "with", "without",
        "for", "about", "by", "under", "behind", "near",
        "after", "before"
    ],

    "conj" : [
        "and", "but", "or", "so", "because", "if", "when"
    ]
}