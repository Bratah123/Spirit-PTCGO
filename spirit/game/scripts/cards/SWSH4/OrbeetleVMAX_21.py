from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b21e232b-f85b-590f-9982-adeb5cad7d25",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleVMAX.Name",
    display_name="Orbeetle VMAX",
    searchable_by=["Orbeetle VMAX", "VMAX", "OrbeetleVMAX"],
    subtypes=["VMAX"],
    collector_number=21,
    set_code="SWSH4",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleV.Name",
    family_id=826,
    abilities=[
        Ability(
            title="Eerie Beam",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Wave",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)