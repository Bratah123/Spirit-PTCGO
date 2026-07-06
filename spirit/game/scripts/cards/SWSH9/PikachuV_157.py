from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c07dc16-7be2-52f1-b87a-160772d76404",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V", "PikachuV"],
    subtypes=["Basic", "V"],
    collector_number=157,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Lightning Blast",
            game_text="You may discard all Lightning Energy from this Pok\u00e9mon. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)