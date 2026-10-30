"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import form_change_deoxys
from spirit.game.card_effects.ex import (
    delta_reduction_next,
)

card = PokemonCardDef(guid='bc75fa1a-fa8d-5c29-aac7-9993dbee3e92', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name', display_name='Deoxys δ', searchable_by=['Deoxys δ', 'Basic', 'Deoxys'], subtypes=['Basic'], collector_number=4, set_code='EX13', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=386, abilities=[Ability(title='Form Change', game_text="Once during your turn (before your attack), you may search your deck for another Deoxys and switch it with Deoxys. (Any cards attached to Deoxys, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, shared_once_per_turn='Form Change', effect=form_change_deoxys()), Attack(title='Delta Reduction', game_text="During your opponent's next turn, any damage done to Deoxys by attacks in reduced by 30 (before applying Weakness and Resistance).", cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=delta_reduction_next(30))])
