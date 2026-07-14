from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1da3abc5-6669-50ab-bbe9-e80900566bdc",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasV.Name",
    display_name="Regigigas V",
    searchable_by=["Regigigas V", "Basic", "V", "RegigigasV"],
    subtypes=["Basic", "V"],
    collector_number=113,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Angry Whack",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon. This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)