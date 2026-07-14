from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="80e5c7e1-2c3f-545b-9584-e7517486df62",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZorua.Name",
    display_name="Hisuian Zorua",
    searchable_by=["Hisuian Zorua", "Basic", "HisuianZorua"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=570,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={},
            effect=draw_attack(1),
        ),
        Attack(
            title="Mumble",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)