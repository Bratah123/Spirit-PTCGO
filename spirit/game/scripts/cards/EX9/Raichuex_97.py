"""STUB: effect not implemented — do not guess mechanics.
Raichu ex (EX9 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import power_short, rai_shield_passive

card = PokemonCardDef(
    guid="6b7f75c1-fd15-5bb7-a6ca-66ac7f24a7d3",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichuex.Name",
    display_name="Raichu ex",
    searchable_by=["Raichu ex", "Stage 1", "ex", "Raichuex"],
    subtypes=["Stage 1", "ex"],
    collector_number=97,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Rai-shield",
            game_text="Damage done to any of your Raichu ex in play by attacks from your opponent's Pok\u00e9mon-ex is reduced by 30 (after applying Weakness and Resistance). You can't use more than 1 Rai-shield Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=rai_shield_passive(),
        ),
        Attack(
            title="Power Short",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If that Pok\u00e9mon has Pok\u00e9-Powers, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
                        effect=power_short(30, 20),
        ),
        Attack(
            title="Pika Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)