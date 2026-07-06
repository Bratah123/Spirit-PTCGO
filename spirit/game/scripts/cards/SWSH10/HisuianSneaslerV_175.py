from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1f899139-84ed-585c-bedb-fb747ec1eca5",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSneaslerV.Name",
    display_name="Hisuian Sneasler V",
    searchable_by=["Hisuian Sneasler V", "Basic", "V", "HisuianSneaslerV"],
    subtypes=["Basic", "V"],
    collector_number=175,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=903,
    abilities=[
        Attack(
            title="Poison Claws",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Dire Claw",
            game_text="This attack does 80 damage for each Special Condition affecting your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)