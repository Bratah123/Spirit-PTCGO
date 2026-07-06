from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1bb51612-663b-5e74-abc5-2e1d4005b13d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Rapid Strike", "Wishiwashi"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=46,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Group Power",
            game_text="If this Pok\u00e9mon has 3 or more Water Energy attached, it gets +150 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Schooling Shot",
            game_text="This attack does 30 more damage for each basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)