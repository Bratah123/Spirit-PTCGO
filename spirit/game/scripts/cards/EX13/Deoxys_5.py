"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import form_change_deoxys
from spirit.game.card_effects.ex import (
    crystal_laser_lock,
)

card = PokemonCardDef(guid='a51e8a8f-2d51-5f49-a3bd-041ad6e062ef', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name', display_name='Deoxys δ', searchable_by=['Deoxys δ', 'Basic', 'Deoxys'], subtypes=['Basic'], collector_number=5, set_code='EX13', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=386, abilities=[Ability(title='Form Change', game_text="Once during your turn (before your attack), you may search your deck for another Deoxys and switch it with Deoxys. (Any cards attached to Deoxys, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, shared_once_per_turn='Form Change', effect=form_change_deoxys()), Attack(title='Crystal Laser', game_text="During your next turn, Deoxys's attacks do 40 more damage to the Defending Pokémon (before applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=crystal_laser_lock())])
