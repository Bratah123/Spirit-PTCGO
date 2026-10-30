"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    deceive_counters,
    scratch_and_draw_holon,
)

card = PokemonCardDef(guid='f694d824-8517-5d9a-91ad-9d66bb4493fa', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name', display_name='Persian δ', searchable_by=['Persian δ', 'Stage 1', 'Persian'], subtypes=['Stage 1'], collector_number=48, set_code='EX13', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name', family_id=53, abilities=[Attack(title='Scratch and Draw', game_text='If any Stadium card with Holon in its name is in play, draw 3 cards.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=scratch_and_draw_holon(3)), Attack(title='Deceive', game_text='Your opponent chooses 1 of his or her Pokémon. Put 4 damage counters on that Pokémon.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, effect=deceive_counters(4))])
