"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    aqua_flower_no_weakness,
    fellowship_oddish_line_passive,
)

card = PokemonCardDef(guid='8a856339-f48d-5731-93b5-4d05a9e1c26d', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name', display_name='Bellossom δ', searchable_by=['Bellossom δ', 'Stage 2', 'Bellossom'], subtypes=['Stage 2'], collector_number=19, set_code='EX13', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name', family_id=182, abilities=[Ability(title='Fellowship', game_text='Bellossom can use the attacks of all Oddish, Gloom, Vileplume, Vileplume ex, or other Bellossom you have in play as its own. (You still need the necessary Energy to use each attack.)', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=fellowship_oddish_line_passive()), Attack(title='Aqua Flower', game_text="During your opponent's next turn, Bellossom has no Weakness.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=aqua_flower_no_weakness())])
