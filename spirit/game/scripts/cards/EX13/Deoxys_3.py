"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import form_change_deoxys
from spirit.game.card_effects.ex import (
    energy_loop_return,
)

card = PokemonCardDef(guid='942216f5-140c-5beb-9818-104f6e6ac5ce', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name', display_name='Deoxys δ', searchable_by=['Deoxys δ', 'Basic', 'Deoxys'], subtypes=['Basic'], collector_number=3, set_code='EX13', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=386, abilities=[Ability(title='Form Change', game_text="Once during your turn (before your attack), you may search your deck for another Deoxys and switch it with Deoxys. (Any cards attached to Deoxys, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, shared_once_per_turn='Form Change', effect=form_change_deoxys()), Attack(title='Energy Loop', game_text='Return 2 Energy attached to Deoxys to your hand.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=energy_loop_return(2))])
