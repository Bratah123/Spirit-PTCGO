from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76d41205-ecdd-568e-a76a-3a5c0e808f45",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcaronaV.Name",
    display_name="Volcarona V",
    searchable_by=["Volcarona V", "Basic", "V", "VolcaronaV"],
    subtypes=["Basic", "V"],
    collector_number=170,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=637,
    abilities=[
        Attack(
            title="Surging Flames",
            game_text="This attack does 20 more damage for each basic Energy card in your discard pile. Then, shuffle those Energy cards into your deck.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)