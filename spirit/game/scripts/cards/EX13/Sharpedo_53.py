"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    brush_aside_holon,
    swift_turn_fighting_res,
)

card = PokemonCardDef(guid='a8958c2c-4202-5207-8ab2-d271ed228ceb', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name', display_name='Sharpedo δ', searchable_by=['Sharpedo δ', 'Stage 1', 'Sharpedo'], subtypes=['Stage 1'], collector_number=53, set_code='EX13', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name', family_id=319, abilities=[Attack(title='Brush Aside', game_text="If Sharpedo has any Holon Energy cards attached to it, choose 1 card from your opponent's hand without looking and discard it.", cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=brush_aside_holon()), Attack(title='Swift Turn', game_text='If the Defending Pokémon has Fighting Resistance, this attack does 50 damage plus 30 more damage.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=swift_turn_fighting_res(50, 30))])
