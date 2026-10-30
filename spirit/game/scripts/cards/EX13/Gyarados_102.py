"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    all_out_blast,
    spiral_growth_attach_heads,
)

card = PokemonCardDef(guid='271411cc-1411-5451-9684-64bf6a1face7', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name', display_name='Gyarados ★ δ', searchable_by=['Gyarados ★ δ', 'Basic', 'Star', 'Gyarados'], subtypes=['Basic', 'Star'], collector_number=102, set_code='EX13', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, family_id=130, abilities=[Attack(title='Spiral Growth', game_text='Flip a coin until you get tails. For each heads, search your discard pile for a basic Energy card and attach it to Gyarados Star.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=spiral_growth_attach_heads()), Attack(title='All-out Blast', game_text='Discard cards from the top of your deck until you have 1 card left. This attack does 50 damage plus 20 more damage for each Energy card you discarded in this way.', cost={PokemonTypes.FIRE: 4}, damage=50, damage_operator='+', effect=all_out_blast(50, 20))])
