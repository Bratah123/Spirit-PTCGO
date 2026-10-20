from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="351931d6-2241-54b2-883d-fc9805e20570",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyuremEX.Name",
    display_name="White Kyurem-EX",
    searchable_by=["White Kyurem-EX", "Basic", "EX", "WhiteKyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=63,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=646,
    abilities=[
        Attack(
            title="Dragon Stream",
            game_text="Flip a coin. If heads, attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Ice Burn",
            game_text="Discard 2 Fire Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)