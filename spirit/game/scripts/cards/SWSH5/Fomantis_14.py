from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d782dd7-cc22-5314-8bc8-bd96952809f6",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    display_name="Fomantis",
    searchable_by=["Fomantis", "Basic", "Fomantis"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=753,
    abilities=[
        Attack(
            title="Continuous Slash",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)