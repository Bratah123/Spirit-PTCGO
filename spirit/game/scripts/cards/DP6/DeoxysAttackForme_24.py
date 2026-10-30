"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_deoxysattackforme_24_form_change,
    dp6_deoxysattackforme_24_psychic_boost,
)

card = PokemonCardDef(guid='93a0d9b3-f7c5-58fa-9373-42ae40a8850c', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysAttackForme.Name', display_name='Deoxys Attack Forme', searchable_by=['Deoxys Attack Forme', 'Basic', 'DeoxysAttackForme'], subtypes=['Basic'], collector_number=24, set_code='DP6', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=386, abilities=[Ability(title='Form Change', game_text="Once during your turn (before your attack), you may search your deck for any Deoxys and switch it with Deoxys Attack Forme. (Any cards attached to Deoxys Attack Forme, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys Attack Forme on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_deoxysattackforme_24_form_change(), activation=Activations.ONCE_PER_TURN), Attack(title='Psychic Boost', game_text="During your next turn, Deoxys's Psychic Boost attack's base damage is 20.", cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=80, effect=dp6_deoxysattackforme_24_psychic_boost())])
