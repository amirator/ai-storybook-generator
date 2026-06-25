"""
The Ugly Duckling - Premium Children's Picture Book
6 Landscape Pages - Complete Story Content + Design Notes
"""

PAGE_SIZE = (792, 612)  # 11" x 8.5" landscape in points

# Color Palette - Premium Warm Storybook
COLORS = {
    'title': '#1E3A3A',        # Deep teal-forest
    'body': '#2C3E50',         # Warm dark slate
    'accent': '#D35400',       # Warm burnt orange (beak feel)
    'highlight': '#F39C12',    # Golden
    'text_bg': '#FDF8F0',      # Cream parchment
    'text_bg_alt': '#F0F7F4',  # Soft mint cream
    'page_border': '#E8E0D5',  # Warm taupe
}

# Exact story text for each page (optimized for picture book pacing + read-aloud)
PAGES = {
    1: {
        "type": "cover",
        "title": "THE UGLY DUCKLING",
        "subtitle": "A Story About Courage, Kindness,\nand Becoming Who You Are Meant to Be",
        "footer": "Written for every child who has ever felt different",
        "image_prompt": """Premium children's picture book cover illustration, landscape format. A serene golden-hour pond scene with soft watercolor and digital painting style, whimsical yet elegant cartoon animals. In the foreground, a kind mother duck with warm orange beak and gentle eyes swims gracefully, surrounded by five fluffy bright yellow ducklings. Slightly behind and to the side is one larger, fluffy grey duckling with a longer neck, big curious eyes full of hope, and oversized feet. He looks a little different but endearing and sweet. Lush green reeds, water lilies in soft pink and white, dragonflies with iridescent wings, soft sunlight rays through willow branches, distant rolling hills, beautiful clouds in peach and lavender sky. Extremely high quality, emotional, heartwarming, detailed feathers with soft texture, perfect composition for title text at top, published by top children's book publisher quality like Chronicle Books or HarperCollins, no text in image, 16:9 landscape cinematic""",
    },
    2: {
        "type": "story",
        "title": "A Different Kind of Beautiful",
        "text": """In a cozy nest tucked among the reeds, Mother Duck waited patiently for her eggs to hatch.

One by one, the shells cracked. Five tiny yellow ducklings tumbled out, peeping with joy.

But the biggest egg took the longest.

When it finally opened, out wobbled a large grey duckling with a long neck and very big feet.

The yellow ducklings stared in surprise.

Mother Duck smiled warmly and gathered him close with her wing.

"You are different, little one," she whispered. "But you are mine. And you are loved." """,
        "image_prompt": """Beautiful children's book illustration, warm morning light in a cozy nest beside a calm pond. Close-up emotional scene: A loving mother duck (cream and soft brown feathers, kind eyes, gentle smile) sits in a nest of soft grass and feathers. Five adorable fluffy round yellow ducklings with tiny wings and bright eyes are gathered around her. In the center, a newly hatched larger grey duckling with fluffy down, a slightly long neck, big soulful dark eyes, and oversized webbed feet looks around curiously and a little shy. Broken eggshell pieces. Soft golden sunlight filtering through reeds, delicate wildflowers, dragonfly on a leaf, peaceful water reflections in background. Premium picture book style, soft textures, expressive faces, heartwarming and tender mood, no text, landscape composition with space at top and bottom for elegant typography""",
    },
    3: {
        "type": "story",
        "title": "The Unkind Words",
        "text": """When the family swam to the big pond, the other ducks gathered around.

"Look at that one!" squawked a proud white duck. "He's so grey and clumsy!"

"His feet are too big!" laughed another.

"His neck is too long!" said a third.

The little grey duckling tried to hide behind his mother. His heart felt heavy and sore.

Even his yellow brothers and sisters swam away to play without him.

"Why am I so ugly?" he asked the still water.

A tear rolled down his cheek and made a tiny ripple." """,
        "image_prompt": """Emotional children's book illustration at a beautiful sunny pond with water lilies and reeds. In the foreground, a group of 4-5 adult ducks and ducklings with bright yellow feathers are laughing and pointing their wings unkindly toward the center. The little grey duckling stands alone in shallow water, head lowered, big eyes sad and hurt, body language shy and small. His kind mother duck stands protectively beside him with a worried, loving expression. Other ducks have smug or mean expressions. Gorgeous detailed pond environment: sparkling water, pink water lilies, tall elegant reeds swaying, butterflies, soft blue sky with fluffy clouds. Premium quality, soft cinematic lighting, strong emotional storytelling, expressive cartoon characters with personality, no text, landscape, balanced composition leaving calm water area for text overlay""",
    },
    4: {
        "type": "story",
        "title": "The Long Winter",
        "text": """The little duckling could not bear the cruel words any longer.

One foggy morning he slipped away from the only home he knew.

He walked through golden autumn fields, then into lonely marshes where wild ducks hissed, "Go away, ugly thing!"

Winter arrived with bitter winds. Snow covered everything.

Cold and hungry, the little duckling found shelter under an old wooden bridge.

He curled into a tiny ball, listening to the howling wind, and wondered if anyone in the whole wide world would ever be kind to him.""",
        "image_prompt": """Dramatic yet gentle children's book winter landscape illustration. A small, lonely grey duckling trudges through deep snow in a vast quiet marshland at dusk. Bare twisted trees, frozen reeds and cattails covered in snow, soft falling snowflakes, cold pale blue and lavender sky with hints of warm sunset on horizon. The duckling looks tired, cold, feathers fluffed against wind, but his eyes still hold a tiny spark of hope. In the distance, an old rustic wooden bridge offers shelter. Moody but not frightening, empathetic, beautiful atmospheric perspective, premium storybook quality, soft detailed snow texture, emotional solitude, landscape format with open sky area for text, no text in art""",
    },
    5: {
        "type": "story",
        "title": "The Reflection",
        "text": """At last, the ice melted. Warm sun touched the earth again.

The little duckling, now much bigger, came to a peaceful lake.

There he saw the most magnificent birds he had ever seen — swans! Their feathers were whiter than clouds. Their necks curved like the most graceful music.

He watched them in awe, his heart aching with a strange new feeling.

Slowly he paddled closer, expecting them to chase him away too.

Then he saw his own reflection in the glassy water...

A long elegant white neck. Brilliant white wings. Eyes that sparkled like stars.

He was not an ugly duckling at all.

He was a swan.""",
        "image_prompt": """Magical, joyful transformation moment in premium children's book style. A serene beautiful lake on a perfect spring morning, golden sunlight, cherry blossoms or apple blossoms on trees, soft green new leaves. In the center, a magnificent young swan (formerly the ugly duckling) with pure white feathers, long graceful neck, and gentle wise eyes stares in wonder at his own perfect reflection in the mirror-calm water. Two or three elegant adult swans swim nearby with kind, welcoming expressions, one extending a wing. The young swan has an expression of pure awe, joy, and disbelief. Sparkling water, delicate flowers floating, dragonflies, soft morning mist, heavenly quality light. Extremely beautiful, emotional, high-end illustration, no text, landscape with excellent space for typography in sky and water""",
    },
    6: {
        "type": "ending",
        "title": "You Are Beautiful",
        "text": """The swans welcomed him with open wings.

"You are one of us," they said gently.

Children playing by the shore pointed and laughed with delight.

"Look! The most beautiful swan has joined the family!"

The young swan raised his long neck proudly and smiled.

He finally understood: He had always been beautiful. He simply needed time, patience, and the right place to grow into himself.

And so he lived happily, swimming with grace and kindness, never forgetting how it felt to be left out.

Because true beauty lives in the heart that chooses to be kind.

You, dear child, are already wonderful — exactly as you are.""",
        "image_prompt": """Heartwarming triumphant final illustration for children's book. A glorious sunny day at the pond. The beautiful young white swan (hero of the story) swims proudly in the center of a happy group of 4-5 elegant swans of all ages. On the grassy shore, 3-4 happy children (diverse, 6-9 years old) wave and smile with pure joy, one child tossing flower petals. Butterflies dance in the air, water lilies in full bloom, soft rainbow in a gentle cloud, golden sunlight everywhere. The swan has the most peaceful, confident, and kind expression. Atmosphere of complete belonging, love, and celebration. Ultra premium quality, rich yet soft colors, detailed joyful expressions, masterpiece children's book ending page, no text, landscape cinematic composition""",
    }
}

# Educational discussion questions for last page or back (optional gentle addition)
DISCUSSION_QUESTIONS = [
    "Have you ever felt different from others? What did it feel like?",
    "What could you say or do to help someone who feels left out?",
    "The duckling became a swan with time and patience. What are you growing into?"
]

MORAL = "Being different is not being less. It is often the first sign that you are something truly special."

def get_page_content(page_num):
    return PAGES[page_num]

print("Story content loaded successfully. 6 pages ready.")