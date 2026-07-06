from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3dc1dd1-a9fa-57e2-94dd-9186bf97ac4b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name",
    display_name="Orbeetle",
    searchable_by=["Orbeetle", "Stage 2", "Orbeetle"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    family_id=824,
    abilities=[
        Ability(
            title="Bug's Radar",
            game_text="Once during your turn, you may look at the top 3 cards of your opponent's deck and put them back in any order.",
            effect=unimplemented,
        ),
        Attack(
            title="Brainwave",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)