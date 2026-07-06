from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="de957e31-726c-5a09-9d74-19f7a364a5d9",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boltund.Name",
    display_name="Boltund",
    searchable_by=["Boltund", "Stage 1", "Boltund"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    family_id=835,
    abilities=[
        Attack(
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Fighting Fangs",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V or Pok\u00e9mon-GX, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)