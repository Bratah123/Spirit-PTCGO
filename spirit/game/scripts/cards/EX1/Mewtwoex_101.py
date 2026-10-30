from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard


card = PokemonCardDef(
    guid="df9111d0-e6db-58f3-83c0-925ced43cc33",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name",
    display_name="Mewtwo ex",
    searchable_by=["Mewtwo ex", "Basic", "ex", "Mewtwoex"],
    subtypes=["Basic", "ex"],
    collector_number=101,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Absorption",
            game_text="Attach up to 2 Energy cards from your discard pile to Mewtwo ex.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=attach_from_discard(count=2, minimum=0, target="self"),
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
