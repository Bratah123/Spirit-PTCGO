from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d50e350-f893-59c0-8737-1a348f784c32",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1", "Thievul"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Ability(
            title="Fumbling Hands",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may have each player shuffle their hand and put it on the bottom of their deck. If either player put any cards on the bottom of their deck in this way, each player draws 4 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)