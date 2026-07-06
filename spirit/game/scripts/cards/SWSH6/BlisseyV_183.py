from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="431bd38a-b900-57f7-b9a5-bbb26630e66d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlisseyV.Name",
    display_name="Blissey V",
    searchable_by=["Blissey V", "Basic", "V", "BlisseyV"],
    subtypes=["Basic", "V"],
    collector_number=183,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=242,
    abilities=[
        Ability(
            title="Natural Cure",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, remove all Special Conditions from it.",
            effect=unimplemented,
        ),
        Attack(
            title="Blissful Blast",
            game_text="This attack does 30 more damage for each Energy attached to this Pok\u00e9mon. If you did any damage with this attack, you may attach up to 3 Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)