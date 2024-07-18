from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0),
    author = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_ref = models.CharField(max_length=250)

class Pattern(Post):
    instructions = models.CharField(max_length=1000)

class Yarn(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete= models.CASCADE)
    WEIGHT_CHOICES = [
    ('lace', 'Lace'),
    ('super_fine', 'Super Fine / Fingering / Sock'),
    ('fine', 'Fine / Sport / Baby'),
    ('light', 'Light / DK (Double Knitting) / Light Worsted'),
    ('medium', 'Medium / Worsted / Aran / Afghan'),
    ('bulky', 'Bulky / Chunky'),
    ('super_bulky', 'Super Bulky'),
    ('jumbo', 'Jumbo')
]
    weight = models.CharField(
        max_length=50, 
        choices=WEIGHT_CHOICES, 
    )
    YARN_CHOICES = [
    ('wool', 'Wool'),
    ('cotton', 'Cotton'),
    ('silk', 'Silk'),
    ('linen', 'Linen'),
    ('alpaca', 'Alpaca'),
    ('cashmere', 'Cashmere'),
    ('acrylic', 'Acrylic'),
    ('nylon', 'Nylon'),
    ('polyester', 'Polyester'),
    ('rayon', 'Rayon'),
    ('hand_dyed', 'Hand-Dyed'),
    ('self_stripling', 'Self-Striping'),
    ('variegated', 'Variegated'),
    ('gradient', 'Gradient'),
    ('metallic', 'Metallic'),
    ('boucle', 'Bouclé'),
    ('chenille', 'Chenille'),
    ('ribbon', 'Ribbon')
    ]
    yarn_type = models.CharField(
        max_length=50,
        choices=YARN_CHOICES,)
    COLOR_CHOICES = [
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('purple', 'Purple'),
    ('pink', 'Pink'),
    ('brown', 'Brown'),
    ('black', 'Black'),
    ('white', 'White'),
    ('gray', 'Gray'),
    ('beige', 'Beige')
]
    color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,)

class Tool(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    TOOL_CHOICES = [
        ('crochet_hook', 'Crochet Hook'),
        ('stitch_marker', 'Stitch Marker'),
        ('scissors', 'Scissors'),
        ('measuring_tape', 'Measuring Tape'),
        ('tapestry_needle', 'Tapestry Needle'),
        ('blocking_board', 'Blocking Board')
    ]
    tool = models.CharField(
        max_length=40, 
        choices=TOOL_CHOICES, 
    )


class Inspiration(Post):
    insp_link = models.CharField(max_length=250, blank=True)
    seeking_pattern = models.BooleanField(default=False)
