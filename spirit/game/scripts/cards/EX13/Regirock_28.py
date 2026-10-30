"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    clear_body_passive,
    rock_slide_bench2,
)

card = PokemonCardDef(guid='f4c32b08-d0cc-55c5-b700-29a910a6976d', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name', display_name='Regirock', searchable_by=['Regirock', 'Basic', 'Regirock'], subtypes=['Basic'], collector_number=28, set_code='EX13', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.WATER, family_id=377, abilities=[Ability(title='Clear Body', game_text="Regirock can't be affected by any Special Conditions.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=clear_body_passive()), Attack(title='Rock Slide', game_text="Does 10 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=40, effect=rock_slide_bench2(10))])
