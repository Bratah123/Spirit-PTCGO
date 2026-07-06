from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88ba1dc3-c4d2-58dc-b67d-a78d0c0eb106",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name",
    display_name="Appletun",
    searchable_by=["Appletun", "Stage 1", "Appletun"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Delicious Aroma",
            game_text="Once during your turn, you may flip a coin. If heads, switch 1 of your opponent's Benched Basic Pok\u00e9mon with their Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)