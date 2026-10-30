from spirit.game.card_effects.ex import baby_evolution_ex7, detour_supporter
"""STUB: effect not implemented — do not guess mechanics.
Magby (EX7 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3ca231c4-324a-57e0-b8e2-e60951c8f83b",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Basic", "Magby"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=240,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Magmar from your hand onto Magby (this counts as evolving Magby), and remove all damage counters from Magby.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=baby_evolution_ex7("Magmar"),
        ),
        Attack(
            title="Detour",
            game_text="If you have a Supporter card in play, use the effect on that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=detour_supporter(),
        ),
    ],
)