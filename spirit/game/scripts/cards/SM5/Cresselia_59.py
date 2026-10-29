from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import lunar_payback, psychic_60_plus

card = PokemonCardDef(
    guid="b83047d5-eae9-597e-b58a-4886a011b896",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=488,
    abilities=[
        Attack(
            title="Lunar Payback",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, switch all damage counters on this Pok\u00e9mon with those on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=lunar_payback,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=psychic_60_plus,
        ),
    ],
)