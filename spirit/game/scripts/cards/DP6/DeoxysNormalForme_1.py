"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_deoxysnormalforme_1_energy_crush,
    dp6_deoxysnormalforme_1_form_change,
)

card = PokemonCardDef(guid='a92c2c6b-7fb8-58fb-b9a0-add9809735f5', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysNormalForme.Name', display_name='Deoxys Normal Forme', searchable_by=['Deoxys Normal Forme', 'Basic', 'DeoxysNormalForme'], subtypes=['Basic'], collector_number=1, set_code='DP6', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=386, abilities=[Ability(title='Form Change', game_text="Once during your turn (before your attack), you may search your deck for any Deoxys and switch it with Deoxys Normal Forme. (Any cards attached to Deoxys Normal Forme, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys Normal Forme on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_deoxysnormalforme_1_form_change(), activation=Activations.ONCE_PER_TURN), Attack(title='Energy Crush', game_text="Does 20 damage plus 10 more damage for each Energy attached to all of your opponent's Pokémon.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp6_deoxysnormalforme_1_energy_crush())])
