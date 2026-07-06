from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7752b7b3-69e9-52ab-932f-c48d09aedd76",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cramorant.Name",
    display_name="Cramorant",
    searchable_by=["Cramorant", "Basic", "Cramorant"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=845,
    abilities=[
        Attack(
            title="Continuous Gulp Missile",
            game_text="Discard any number of Arrokuda from your Bench. This attack does 60 damage for each Arrokuda you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)