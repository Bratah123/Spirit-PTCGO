from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce380d56-f682-5267-b661-6afc1d22ea1a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=198,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=776,
    abilities=[
        Attack(
            title="Shell Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)