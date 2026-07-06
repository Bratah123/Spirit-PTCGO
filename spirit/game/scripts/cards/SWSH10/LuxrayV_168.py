from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce5226bb-a7da-5f95-b467-6a7b2a91de07",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayV.Name",
    display_name="Luxray V",
    searchable_by=["Luxray V", "Basic", "V", "LuxrayV"],
    subtypes=["Basic", "V"],
    collector_number=168,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=405,
    abilities=[
        Attack(
            title="Fang Snipe",
            game_text="Your opponent reveals their hand. Discard a Trainer card you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Radiating Pulse",
            game_text="Discard 2 Energy from this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)