"""STUB: effect not implemented — do not guess mechanics.
Porygon-Z (DPP #DP35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="cb17db16-fe78-5be0-a94d-b83c790da3b2",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=474,
    abilities=[
        Ability(
            title="Install",
            game_text="As often as you like during your turn (before your attack), move a Technical Machine card attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Porygon-Z is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Learning",
            game_text="Search your deck for a Pok\u00e9mon LV.X that levels up from 1 of your Pok\u00e9mon, and put it onto that Pok\u00e9mon. (This counts as leveling up that Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Overload",
            game_text="Does 40 damage plus 20 more damage for each Technical Machine card attached to Porygon-Z.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)