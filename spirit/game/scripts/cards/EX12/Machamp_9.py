"""STUB: effect not implemented — do not guess mechanics.
Machamp (EX12 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import discard_special_energy_from_defender
from spirit.game.card_effects.ex import (
    swift_blow_react,
)

card = PokemonCardDef(guid='a375226b-8674-5647-ba6a-2a3438682498', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name', display_name='Machamp', searchable_by=['Machamp', 'Stage 2', 'Machamp'], subtypes=['Stage 2'], collector_number=9, set_code='EX12', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name', family_id=66, abilities=[Attack(title='Derail', game_text='Discard a Special Energy card, if any, attached to the Defending Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=discard_special_energy_from_defender()), Attack(title='Swift Blow', game_text='Does 60 damage plus 20 damage for each React Energy card attached to Machamp.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=swift_blow_react(60, 20))])
