from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9a4964e-aed4-5b33-80e0-5f7545517600",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCursolaV.Name",
    display_name="Galarian Cursola V",
    searchable_by=["Galarian Cursola V", "Basic", "V", "GalarianCursolaV"],
    subtypes=["Basic", "V"],
    collector_number=71,
    set_code="SWSH35",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=864,
    abilities=[
        Ability(
            title="Gnawing Aura",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever your opponent attaches an Energy card from their hand to 1 of their Pok\u00e9mon, put 3 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hollow Missile",
            game_text="Put 3 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)