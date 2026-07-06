from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aabb4dbb-ca2d-5d66-9f48-c3dd3f7ef71a",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2", "Rapid Strike", "Inteleon"],
    subtypes=["Stage 2", "Rapid Strike"],
    collector_number=227,
    set_code="SWSH7",
    rarity=Rarities.RareSecret,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=818,
    abilities=[
        Ability(
            title="Quick Shooting",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)