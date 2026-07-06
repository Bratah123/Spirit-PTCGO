from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="433aa45a-eb4b-5b12-af98-0a4ac657a7e3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianArcanineV.Name",
    display_name="Hisuian Arcanine V",
    searchable_by=["Hisuian Arcanine V", "Basic", "V", "HisuianArcanineV"],
    subtypes=["Basic", "V"],
    collector_number=179,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=59,
    abilities=[
        Ability(
            title="Irresistible Force",
            game_text="As often as you like during your turn, you may move a Fighting Energy from 1 of your other Pok\u00e9mon to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Bullet",
            game_text="This attack does 30 more damage for each Fighting Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)