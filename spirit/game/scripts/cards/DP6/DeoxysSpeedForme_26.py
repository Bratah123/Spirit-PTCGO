"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_deoxysspeedforme_26_form_change,
)
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='66ac98cc-a267-5ace-8f0e-a4f8c9e3860e', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysSpeedForme.Name', display_name='Deoxys Speed Forme', searchable_by=['Deoxys Speed Forme', 'Basic', 'DeoxysSpeedForme'], subtypes=['Basic'], collector_number=26, set_code='DP6', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=0, weakness_type=PokemonTypes.PSYCHIC, family_id=386, abilities=[Ability(title='Form Change', game_text="Once during your turn (before your attack), you may search your deck for any Deoxys and switch it with Deoxys Speed Forme. (Any cards attached to Deoxys Speed Forme, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys Speed Forme on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_deoxysspeedforme_26_form_change(), activation=Activations.ONCE_PER_TURN), Attack(title='Speed Shot', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.COLORLESS: 2}, effect=snipe_attack(30, pool='any'))])
