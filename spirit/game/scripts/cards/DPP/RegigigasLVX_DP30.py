"""STUB: effect not implemented — do not guess mechanics.
Regigigas LV.X (DP7 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    cant_attack_next_turn,
    dp7_regigigaslvx_100_sacrifice,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='234118e8-a5af-5402-8cd3-44ad73300f37', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasLVX.Name', display_name='Regigigas LV.X', searchable_by=['Regigigas LV.X', 'Level-Up', 'RegigigasLVX'], subtypes=['Level-Up'], collector_number=30, set_code='DP7', rarity=Rarities.RareHolo, hp=150, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.LEVELUP, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name', family_id=486, abilities=[Ability(title='Sacrifice', game_text="Once during your turn (before your attack), you may choose 1 of your Pokémon in play and that Pokémon is Knocked Out. Then, search your discard pile for up to 2 basic Energy cards, attach them to Regigigas, and remove 8 damage counters from Regigigas. This power can't be used if Regigigas is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_regigigaslvx_100_sacrifice(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Giga Blaster', game_text="Discard the top card from your opponent's deck. Then, choose 1 card from your opponent's hand without looking and discard it. Regigigas can't use Giga Blaster during your next turn.", cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=100, effect=cant_attack_next_turn())])
