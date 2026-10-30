"""STUB: effect not implemented — do not guess mechanics.
Unown [H] (DP4 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a6a3e6da-d562-5482-99ee-8b44fe72edb2",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownH.Name",
    display_name="Unown [H]",
    searchable_by=["Unown [H]", "Basic", "UnownH"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="DP4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="HEAL",
            game_text="Once during your turn (before your attack), if you have Unown H, Unown E, Unown A, and Unown L on your Bench, you may remove all Special Conditions from 1 of your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Discard a card from your hand. (If you can't discard a card from your hand, this attack does nothing.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)