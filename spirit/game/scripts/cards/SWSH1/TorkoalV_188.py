from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="10c5b818-6abf-50d7-a391-7ad6a0d31e46",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TorkoalV.Name",
    display_name="Torkoal V",
    searchable_by=["Torkoal V", "Basic", "V", "TorkoalV"],
    subtypes=["Basic", "V"],
    collector_number=188,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Combustion Pillar",
            game_text="Discard the top card of your deck. If that card is a Fire Energy card, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Steam Crush",
            game_text="Discard 2 Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)