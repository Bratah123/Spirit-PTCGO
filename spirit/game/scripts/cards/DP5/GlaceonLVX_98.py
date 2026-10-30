"""STUB: effect not implemented — do not guess mechanics.
Glaceon LV.X (DP5 #98): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a873f9b6-2e3d-515c-9f1e-24fe8a6ec500",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonLVX.Name",
    display_name="Glaceon LV.X",
    searchable_by=["Glaceon LV.X", "Level-Up", "GlaceonLVX"],
    subtypes=["Level-Up"],
    collector_number=98,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.LEVELUP,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Chilly Breath",
            game_text="As long as Glaceon is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon can't use any Pok\u00e9-Powers.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Avalanche",
            game_text="Flip a coin. If heads, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)