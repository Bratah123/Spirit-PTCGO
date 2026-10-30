"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import form_change_deoxys
from spirit.game.card_effects.ex import (
    teleportation_burst_switch,
)

card = PokemonCardDef(guid='90bf506f-ae66-57a2-9932-a4805e522b70', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name', display_name='Deoxys δ', searchable_by=['Deoxys δ', 'Basic', 'Deoxys'], subtypes=['Basic'], collector_number=6, set_code='EX13', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=386, abilities=[Ability(title='Form Change', game_text="Once during your turn (before your attack), you may search your deck for another Deoxys and switch it with Deoxys. (Any cards attached to Deoxys, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, shared_once_per_turn='Form Change', effect=form_change_deoxys()), Attack(title='Teleportation Burst', game_text='Switch Deoxys with 1 of your Benched Pokémon.', cost={PokemonTypes.LIGHTNING: 1}, damage=20, effect=teleportation_burst_switch())])
