from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="838c5f94-c1cb-5151-bcac-84e437e151c0",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegidragoV.Name",
    display_name="Regidrago V",
    searchable_by=["Regidrago V", "Basic", "V", "RegidragoV"],
    subtypes=["Basic", "V"],
    collector_number=184,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=895,
    abilities=[
        Attack(
            title="Celestial Roar",
            game_text="Discard the top 3 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Laser",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.FIRE: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)