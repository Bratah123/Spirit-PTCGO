from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fee652b7-2d45-54cc-96af-0de41ccfe985",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name",
    display_name="Galarian Obstagoon",
    searchable_by=["Galarian Obstagoon", "Stage 2", "GalarianObstagoon"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    family_id=263,
    abilities=[
        Ability(
            title="Wicked Ruler",
            game_text="Once during your turn, you may have your opponent discard cards from their hand until they have 4 cards in their hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Knuckle Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)