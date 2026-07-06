from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95a51d07-4ea7-5ced-8a3f-789e259f7aac",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Ghostly Cries",
            game_text="For each Pok\u00e9mon in your opponent's discard pile, put 1 damage counter on your opponent's Pok\u00e9mon in any way you like. If you placed any damage counters in this way, your opponent shuffles all Pok\u00e9mon from their discard pile into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)