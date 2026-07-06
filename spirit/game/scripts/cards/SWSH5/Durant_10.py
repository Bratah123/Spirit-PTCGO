from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="330eda35-2701-51b9-ab21-d990bb0f6db6",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=632,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Devour",
            game_text="For each of your Durant in play, discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)