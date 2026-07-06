from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26246f22-7dcd-5193-8746-d2170e058d70",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name",
    display_name="Tapu Bulu",
    searchable_by=["Tapu Bulu", "Basic", "TapuBulu"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=787,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Nature's Judgment",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)