from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8e900cf3-217f-544e-ac79-aad797981c06",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega", "Stage 1", "Yanmega"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Wide Wing",
            game_text="If you have more cards in your hand than your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)